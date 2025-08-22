# Gemini LLM Apps

This project uses a simple **Streamlit web application** that uses **Google's Gemini models** to answer user questions. It loads the Google API key from a `.env` file and sends user queries to the Gemini model for responses.

1. **Text Q&A App** - Uses `gemini-2.5-pro` to answer text-based questions.
2. **Image + Text App** - Uses `gemini-2.5-flash` to analyze images and answer image related questions.

## Set up requirements

- Python 3.10+
- Streamlit
- python-dotenv
- google-generativeai

#### 1. Install required libraries:
```bash
pip install -r requirements.txt
```
#### 2. Add your API key
Create a `.env` file and add your Gemini API key:
```bash
GOOGLE_API_KEY=your_google_api_key
```
### To run the Apps:
**1. Text Q&A App** (`qachat.py`) Run this command:
```
streamlit run qachat.py
```
Type your questions and the app will give a response using Gemini pro model.

**2. Image + Text App** (`vision.py`) Run this command:
```
streamlit run vision.py
```
Upload the image and type your questions. The app will give a response using Gemini flash model.



