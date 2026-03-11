# 02 – PDF RAG (Chat with PDF using Retrieval-Augmented Generation)

This project extends the **Basic RAG pipeline** by allowing the system to **read and answer questions from PDF documents**.

Instead of using a simple text file as the knowledge source, this project builds a **document question-answering system** that retrieves information from PDFs and generates answers using a Large Language Model (LLM).

The system uses **LangChain, FAISS, HuggingFace embeddings, and Ollama** to build a local AI assistant that can chat with PDF files.

---

# Project Goal

The goal of this project is to understand how to:

* Extract text from PDFs
* Convert document content into embeddings
* Store embeddings in a vector database
* Retrieve relevant document chunks
* Generate answers using an LLM

This is a common architecture used in **AI document assistants and enterprise knowledge systems**.

---

# What is PDF RAG?

PDF RAG is a **Retrieval-Augmented Generation pipeline designed for PDF documents**.

Instead of relying on a language model's training data, the system retrieves relevant information from a PDF file and uses that information to answer user questions.

---

# RAG Pipeline Overview

The pipeline works as follows:

User Question
↓
Convert Question to Embedding
↓
Search Vector Database
↓
Retrieve Relevant PDF Chunks
↓
Insert Context into Prompt
↓
LLM Generates Answer

---

# Project Structure

```
02-pdf-rag
│
├── data
│   └── demo.pdf
│
├── vector_db_pdf
│
├── ingest_pdf.py
├── app.py
└── README.md
```

---

# Components of the System

### 1. PDF Loader

Reads PDF documents and extracts text content.

LangChain provides tools such as:

* PyPDFLoader(use here)
* PDFMinerLoader

---

### 2. Text Chunking

Large documents are divided into smaller pieces so they can be retrieved efficiently.

Example chunk size:

* 1000 characters
* 100 overlap

Chunking improves retrieval quality.

---

### 3. Embeddings

Each chunk of text is converted into a **vector representation** using an embedding model.

Embedding model used:

```
sentence-transformers/all-MiniLM-L6-v2
```

These embeddings capture the **semantic meaning of text**.

---

### 4. Vector Database

The embeddings are stored in **FAISS**, a vector similarity search engine.

FAISS allows fast retrieval of relevant chunks when a query is asked.

---

### 5. Retriever

When the user asks a question, the retriever searches the vector database and returns the most relevant chunks.

---

### 6. Large Language Model

A local LLM running through **Ollama** is used to generate answers.

Example models:

* llama3(used here)
* mistral
* gemma
* phi3

---

# Ingestion Pipeline

The ingestion pipeline processes the PDF and builds the vector database.

Steps:

1. Load PDF document
2. Extract text from pages
3. Split text into chunks
4. Convert chunks into embeddings
5. Store embeddings in FAISS

Run the ingestion script:

```
python ingestion.py
```

This creates the **vector database** used for retrieval.

---

# Query Pipeline

The query pipeline answers questions using retrieved context from the PDF.

Steps:

1. User enters a question
2. Question is converted to embedding
3. Similar document chunks are retrieved
4. Context is added to the prompt
5. LLM generates the answer

Run the application:

```
python app.py
```

---

# Example

Example question:

```
What is the RAG?
```

Example response:

```
RAG stands for Retrieval-Augmentation-Generation, which is a methodology that has evolved through different paradigms, including Naive RAG, Modular RAG, and Advanced RAG.
```

---

# Technologies Used

* Python
* LangChain
* FAISS
* HuggingFace Embeddings
* Ollama
* PyPDF

---

# Applications

PDF RAG systems are used in many real-world applications:

* Legal document assistants
* Research paper analysis
* Enterprise knowledge bases
* Customer support document search
* AI-powered document chatbots

---

# Limitations

This implementation is a **basic PDF RAG system** and has several limitations:

* No multi-PDF support
* No metadata filtering
* No reranking model
* No hybrid search
* No evaluation framework

Advanced RAG systems usually include these features.

---

# Future Improvements

Possible improvements for the next project:

* Multi-document RAG
* Hybrid search (BM25 + vector search)
* Reranking models
* Streaming responses
* Web UI using Streamlit
* Agentic RAG systems

---

# Learning Outcome

By completing this project you will understand how to build an **AI assistant that can read and answer questions from PDF documents using Retrieval-Augmented Generation**.

This is a fundamental step toward building **real-world AI document intelligence systems**.
