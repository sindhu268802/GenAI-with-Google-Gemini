# Multi-Language Invoice Extractor using Gemini

This project is a **Streamlit web application** that extracts key information from invoices in multiple languages using **Google’s Gemini**.
The app uses a `gemini-2.5-pro` model and ask users to upload an image of the invoice and ask the user to type the questions and the model gives responses based on the invoice provided.

## ✨ Features
- 🌍 Multi-language support (process invoices in English, French, Spanish, German, etc...). Supports the image format (`.jpg`, `jpeg`, `.png`)
- 📑 Extracts information like:
  - Invoice number
  - Date
  - Vendor name
  - Total amount

## Set up requirements

- Python 3.9+
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
```
streamlit run app.py
```
1. Upload an invoice image
2. Type your question (e.g.,"What is the invoice number").
3. Click the button "Tell me about the invoice"
4. View the response





