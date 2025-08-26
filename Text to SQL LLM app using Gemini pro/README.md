# Text to SQL APP using Google Gemini Pro

This project is a Streamlit web application that allows users to ask questions based on the database and it will generate the corresponding **SQL query** using **Google Gemini pro** model and execute it on a **SQLite database**.

## 🚀 Features
- Converts **English questions → SQL queries** using `gemini-2.5-pro` model.
- Runs the generated SQL on a **SQLite database**.
- Displays query results in the Streamlit UI.

## 📦 Installation
Required Python 3.10+
#### 1. Clone the repository
```bash
git clone https://github.com/your-username/text-to-sql-gemini.git
cd text-to-sql-gemini
```
#### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
#### 3. Install dependencies
```bash
pip install -r requirements.txt
```
#### 4. Environment Variables
Create a `.env` file and add your Gemini API key:
```bash
GOOGLE_API_KEY=your_google_api_key
```
#### 5. Running the App
Start the Streamlit app with:
```
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`

## ⚙️ How It Works
1. The user asks a question "What is the average marks of all students"
2. The app sends a question to google gemini model.
3. The model returns the SQL query:
   `SELECT AVG(MARKS) FROM STUDENT`
4. The app runs the query on SQLite database and generates an answer for the user query.

### 💡 Example Queries
1. How many entries of records are present?
2. Tell me all students studying in "Data science"
3. Give me a list of students scored marks more than 90

