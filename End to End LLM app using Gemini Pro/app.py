from dotenv import load_dotenv 
load_dotenv() # load all environment variables from .env file

import streamlit as st
import os

import google.generativeai as genai



os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini model and get respones

model = genai.GenerativeModel('gemini-2.5-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

##initialize streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)