# Smart ATS Resume Evaluator using Google Gemini pro
A Streamlit web application powered by Google Gemini Pro that helps job seekers improve their resumes for Applicant Tracking Systems (ATS).
This tool allows users to upload their resume and a job description, then evaluates how well the resume matches the job description and suggestions to improve the resume for better ATS compatibility.

## 🚀 Features

- Upload resume (PDF) and job description (text).
- Get a match percentage score.
- Identify missing keywords and skills.
- Receive improvement suggestions.
- Simple and interactive Streamlit UI.

## 🛠️ Tech Stack

- Python 3.10+
- Streamlit – Web application framework
- Google Gemini Pro API (`google-gemini-2.5-pro`)
- PyPDF2 / docx2txt – Resume parsing

## ⚙️ Installation & Setup
#### 1. Clone the Repository  
```
git clone https://github.com/your-username/smart-ats-resume-evaluator.git
cd smart-ats-resume-evaluator
```
#### 2. Create Virtual Environment
```
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```
#### 3. Install Dependencies
```
pip install -r requirements.txt
```
#### 4. Set Up Google Gemini API
Create a `.env` file in the project root and add:
```
GEMINI_API_KEY=your_api_key_here
```
#### 5. Run the APP
```
streamlit run app.py
```
## 🎯 Usage
1. Upload your resume in PDF
2. Paste the job description.
3. Click Submit.
4. The app returns a JSON string like this:
```
{
  "JD Match": "72%",
  "Missingkeywords": ["Tensorflow", "Deep learning", "SQL"],
  "Profile Summary": "The resume shows matches with data science and there is a lack of tools."
}
```

