# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Import required libraries
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure the Gemini API using the API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to interact with Gemini and generate SQL query from English question
def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel('gemini-2.5-pro')
        response = model.generate_content([prompt[0], question])
        sql_query = response.text.strip()
        return clean_sql_query(sql_query)
    except Exception as e:
        st.error(f"Gemini API error: {e}")
        return None

# Function to clean the SQL query from Gemini's output
def clean_sql_query(sql_text):
    # Remove unwanted formatting characters like triple backticks or extra whitespace
    sql_text = sql_text.strip()
    sql_text = sql_text.replace("```", "").replace("sql", "").strip()
    return sql_text

# Function to execute SQL query on the database and fetch results
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except sqlite3.Error as e:
        st.error(f"SQLite error: {e}")
        return []

# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database is named STUDENT and has the following columns: NAME, CLASS, SECTION and MARKS

    For example:
    - Question: How many entries of records are present?
      SQL: SELECT COUNT(*) FROM STUDENT;

    - Question: Tell me all the students studying in Data Science class.
      SQL: SELECT * FROM STUDENT WHERE CLASS = "Data Science";

    Only return the SQL query. Do not include triple backticks (```), the word 'sql', or any explanation.
    """
]

# Streamlit App

st.set_page_config(page_title="SQL Query Generator with Gemini")
st.title("Gemini App To Retrieve SQL Data")

# User input for English question
question = st.text_input("Ask a question about the STUDENT database:", key="input")

# Button to submit the query
submit = st.button("Ask the question")

# When the button is clicked
if submit:
    with st.spinner("Processing..."):
        sql_query = get_gemini_response(question, prompt)
        
        if sql_query:
            st.code(sql_query, language='sql')  # Display the generated SQL query

            result = read_sql_query(sql_query, "student.db")

            # Display result
            st.subheader("Query Result")
            if result:
                for row in result:
                    st.write(row)
                st.success("Query executed successfully!")
            else:
                st.warning("No results found or an error occurred.")