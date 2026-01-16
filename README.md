# AgenticAI_RAG_Chatbot

A **Retrieval-Augmented Generation (RAG)** based chatbot that answers user queries from PDF documents using **LangGraph workflows**, **Google Gemini**, and **semantic search**.

---

##  Key Features

- **PDF Ingestion** – Extracts and indexes text from PDF documents  
- **Semantic Search** – Retrieves relevant content using vector similarity  
- **Conversational Q&A** – Natural language question answering  
- **Intent Classification** – Routes queries (greeting, summary, question)  
- **Document Summarization** – Generates concise overviews  
- **FastAPI Backend** – High-performance REST API  
- **Streamlit Frontend** – Clean and interactive user interface  

---
## ⚙️ Environment Setup

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_google_api_key
CHROMA_DIR=./chroma_db
LLM_MODEL=gemini-2.5-flash
HF_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```
---

##  System Architecture

┌─────────────┐
│ Streamlit   │ Frontend UI
└──────┬──────┘
       │ HTTP
┌──────▼──────┐
│ FastAPI     │ Backend API
└──────┬──────┘
       │
┌──────▼──────┐
│ LangGraph   │ Workflow Engine
│ (Classify → │
│ Retrieve →  │
│ Generate)   │
└──────┬──────┘
       │
┌─────┴─────┬───────────────┐
│           │               │
▼           ▼               ▼
ChromaDB   Gemini LLM      HF Embeddings
(Vector)   (LLM)           (Semantic)


## 📦 Install Dependencies

Install all required Python packages using:

```bash
pip install -r requirements.txt
```

## 📄 PDF Ingestion

Place your ebook PDF in the project root directory and run:

```bash
python -m app.ingest
```

### This step performs the following:

- Loads the PDF document  
- Splits the content into semantic text chunks  
- Generates embeddings using HuggingFace models  
- Stores vector embeddings in ChromaDB for efficient retrieval  

---

## 🚀 Backend (FastAPI)

Start the FastAPI backend server using:

```bash
uvicorn backend.main:app --reload
```

### The backend is responsible for:

- Handling user queries  
- Managing LangGraph agent state  
- Performing document retrieval  
- Generating grounded responses using retrieved context  

---

## 🎨 Frontend (Streamlit)

Launch the Streamlit frontend interface with:

```bash
streamlit run frontend/front.py
```
### 🎨 Frontend Capabilities

The frontend allows users to:

- Ask questions related to the ebook  
- Receive context-aware, grounded answers  
- Ensure responses are generated strictly from retrieved document content  

---

## 🧠 Tech Stack

- **LangChain** – LLM orchestration  
- **LangGraph** – Agentic workflow and state management  
- **ChromaDB** – Vector database for similarity search  
- **FastAPI** – Backend API  
- **Streamlit** – Interactive frontend UI  
- **HuggingFace Embeddings** – Text vectorization  
- **Google Gemini LLM** – Response generation  

---
## 📦 Cloning the Project

To get started with this project, you need to clone the repository to your local machine. Make sure you have **Git** installed.

```bash
# Clone the repository
git clone https://github.com/yourusername/rag-ai-chatbot.git

# Navigate into the project directory
cd rag-ai-chatbot
```
After cloning, you can proceed to set up your environment, install dependencies, and configure API keys as described in the setup instructions.

