import streamlit as st
import tempfile
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

st.title("📚 AI Knowledge Copilot")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    st.success("PDF Loaded")
    st.write(f"Pages Loaded: {len(docs)}")

    # Split PDF into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    st.success("PDF Split Successfully")
    st.write(f"Chunks Created: {len(chunks)}")

    # Create embeddings
    # embeddings = GoogleGenerativeAIEmbeddings(
    #     model="models/embedding-001"
    embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004"

    )

    st.success("Embeddings Model Loaded")

    # Create vector database
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    st.success("Vector Database Created")