# Chat with multiple PDF documents with Langchain and Google Gemini Pro

This is a Streamlit application that allows you to upload multiple PDF documents and interact with them conversationally using LangChain and Google Gemini Pro.
The app extracts text from your PDFs, processes it into embeddings where responses are generated using the `gemini-2.5-pro` model and provide context-aware answers.

## ✨ Features
📂 Upload multiple PDF documents

🔎 Extract and chunk text for efficient retrieval

🤖 Use LangChain with Google Gemini Pro for Q&A

💬 Chat-style interface built with Streamlit

## 🛠️ Tech Stack

- UI framework
 – Streamlit
- LLM
 – Google Generative AI (Gemini Pro), Langchain
- Vector database for embeddings
   – FAISS/Chroma
- PDF text extraction
   – PyPDF2
      
## 📦 Installation
Required Python 3.10+
#### 1. Clone the repository
```bash
git clone https://github.com/your-username/pdf-chat-gemini.git
cd pdf-chat-gemini
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
## 🔑 Environment Variables

Create a `.env` file and add your Gemini API key:
```bash
GOOGLE_API_KEY=your_google_api_key
```

## ▶️ Running the App
Start the Streamlit app with:
```
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`
## 📚 Usage

1. Upload one or more PDF documents
2. Ask your question in the chatbox
3. Get AI-powered responses that reference your documents

## ⚠️ Notes
- Ensure your PDFs are text-based (scanned images may need OCR).
- Google Gemini Pro API requires a valid key and access.
