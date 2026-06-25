# Images
<img width="1907" height="911" alt="Screenshot 2026-06-25 124530" src="https://github.com/user-attachments/assets/abbdc8ef-9551-444e-a94e-97f03fb0d3e6" />


# 📚 AI Knowledge Copilot

AI Knowledge Copilot is an intelligent document assistant built using Retrieval-Augmented Generation (RAG), Google Gemini, FAISS Vector Database, and Streamlit.

The application allows users to upload PDF documents and interact with them through a conversational interface. Instead of searching manually through hundreds of pages, users can ask questions, generate summaries, create study notes, generate MCQs, and extract document structure instantly.

---

## 🚀 Features

### 💬 PDF Chat

Ask questions about uploaded documents in natural language.

Examples:

* What is Dynamic Programming?
* Explain Binary Trees.
* What are the key interview questions?
* Summarize Chapter 5.

---

### 📄 PDF Summary

Generate concise summaries of large documents.

Provides:

* Main Topics
* Key Concepts
* Important Takeaways
* Quick Revision Notes

---

### 📚 PDF Index Extraction

Automatically extracts:

* Table of Contents
* Chapters
* Topics
* Sections

Useful for large books and technical documents.

---

### 📝 Notes Generator

Creates structured study notes from uploaded PDFs.

Ideal for:

* Exam Preparation
* Interview Preparation
* Quick Revision

---

### ❓ MCQ Generator

Automatically generates multiple-choice questions from document content.

Includes:

* Questions
* Options
* Correct Answers

Useful for self-assessment and learning.

---

### 🔍 RAG-Powered Search

Uses Retrieval-Augmented Generation (RAG) to:

1. Split PDF into chunks
2. Generate embeddings
3. Store vectors in FAISS
4. Retrieve relevant content
5. Generate accurate answers using Gemini

This significantly reduces hallucinations and improves answer quality.

---

## 🏗️ System Architecture

User Uploads PDF
↓
PyPDFLoader
↓
Text Chunking
↓
Sentence Transformers Embeddings
↓
FAISS Vector Database
↓
Retriever
↓
Google Gemini
↓
AI Generated Response

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### LLM

* Gemini 2.5 Flash

### Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

### Vector Database

* FAISS

### PDF Processing

* LangChain
* PyPDFLoader

### Programming Language

* Python

---

## 📂 Project Structure

AI-Knowledge-Copilot/

├── app.py

├── rag.py

├── pdf_loader.py

├── vector_store.py

├── prompts.py

├── summary.py

├── index_generator.py

├── notes_generator.py

├── mcq_generator.py

├── .env

├── requirements.txt

└── faiss_db/

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Knowledge-Copilot.git

cd AI-Knowledge-Copilot
```

Create Virtual Environment:

```bash
python -m venv venv
```

Activate Environment:

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a .env file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Get API Key from:

https://aistudio.google.com

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 📸 Example Workflow

1. Upload PDF
2. PDF is processed and indexed
3. Embeddings are generated
4. FAISS vector database is created
5. Ask questions
6. Generate summaries
7. Create notes
8. Generate MCQs
9. Extract document index

---

## 🎯 Real-World Use Cases

### Students

* Study Notes
* Exam Preparation
* Quick Revision

### Job Seekers

* Interview Preparation
* Technical Concepts Learning
* DSA Revision

### Researchers

* Research Paper Summaries
* Knowledge Extraction
* Topic Exploration

### Professionals

* Documentation Search
* Internal Knowledge Base
* Training Material Assistant

---

## 📈 Future Enhancements

* Multi-PDF Support
* Chat Memory
* Source Citations
* Voice Input
* PDF Comparison
* Research Paper Analyzer
* Export Notes to PDF
* Advanced Search Filters
* Knowledge Graph Visualization

---

## 🧠 Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Embeddings
* Large Language Models
* Prompt Engineering
* Document Understanding
* Generative AI Applications

---

## 👨‍💻 Author

Raju Baradur

Computer Science Engineer

Skills:

* Python
* Data Structures & Algorithms
* OOP
* Streamlit
* LangChain
* FAISS
* Gemini API
* Generative AI
* Machine Learning

---

## ⭐ Project Highlights

✔ RAG-Based Architecture

✔ Gemini Integration

✔ FAISS Vector Search

✔ PDF Question Answering

✔ Notes Generation

✔ MCQ Generation

✔ Summary Generation

✔ Index Extraction

✔ Resume-Worthy GenAI Project
