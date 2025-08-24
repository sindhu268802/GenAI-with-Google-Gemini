# Gemma Document Q&A model

This is a Streamlit web application that allows users to ask questions based on the PDF documents using Google gemma model from groq.

---

## 🚀 Features
- Uses **Groq's** `gemma2-9b-it` for fast & accurate answers.  
- Generates **embeddings with Google Generative AI**.  
- Stores embeddings in **FAISS vector database**.  
- Splits documents into **chunks** for efficient retrieval.  
- Interactive **Streamlit UI**.  
- Expander to view **document similarity matches**.  

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/gemma-doc-qa.git
cd gemma-doc-qa
```
### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Set API Key

Create a `.env` file in the root directory:
```bash
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```
## App Flow:
1. Place your PDFs inside the us_census/ folder.
2. Run the Streamlit app:
```bash
streamlit run app.py
```
3. Click "Documents Embedding" to build the FAISS vector store.
4. Enter your question in the text box.
5. View answers + supporting document chunks.
















