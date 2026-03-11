# Basic RAG (Naive Retrieval-Augmented Generation)

This project demonstrates a **Basic / Naive Retrieval-Augmented Generation (RAG) pipeline** using **LangChain, FAISS, HuggingFace embeddings, and Ollama**.

The goal of this project is to understand how modern AI systems retrieve external knowledge and use large language models (LLMs) to generate more accurate answers.

---

# What is RAG?

Retrieval-Augmented Generation (RAG) is a technique that combines **information retrieval** with **language model generation**.

Instead of relying only on the LLM’s training data, RAG retrieves relevant documents from a knowledge base and uses them as context when generating answers.

Benefits of RAG:

* Reduces hallucinations
* Allows private knowledge integration
* Provides more accurate responses
* Supports domain-specific AI assistants

---

# RAG Pipeline Overview

This project implements a **Naive RAG pipeline**, which is the simplest form of retrieval-augmented generation.

Pipeline:

User Query
↓
Embedding Model
↓
Vector Similarity Search
↓
Retrieve Relevant Document Chunks
↓
Add Context to Prompt
↓
LLM Generates Answer

---

# Project Structure

```
01-basic-rag
│
├── data
│   └── demo.txt
│
├── vector_db
│
├── ingest.py
├── app.py
└── README.md
```

---

# Components

### 1. Document Loader

Loads text documents from the `data` folder.

### 2. Text Splitter

Splits documents into smaller chunks for better retrieval.

### 3. Embedding Model

Converts text into vector representations.

Model used:

```
sentence-transformers/all-MiniLM-L6-v2
```

### 4. Vector Database

FAISS is used to store and search embeddings efficiently.

### 5. Retriever

Retrieves the most relevant document chunks for a user query.

### 6. LLM

A local LLM running through **Ollama** generates the final answer.

---

# Ingestion Pipeline

The ingestion pipeline prepares the knowledge base.

Steps:

1. Load documents
2. Split text into chunks
3. Convert chunks into embeddings
4. Store embeddings in FAISS vector database

Run ingestion:

```
python ingest.py
```

---

# Query Pipeline

The query pipeline answers user questions using retrieved context.

Steps:

1. Convert user query to embedding
2. Search vector database
3. Retrieve top relevant chunks
4. Add chunks to the prompt
5. Send prompt to LLM
6. Generate answer

Run the application:

```
python app.py
```

---

# Example

Example query:

```
What is Retrieval-Augmented Generation?
```

Example output:

```
Retrieval-Augmented Generation (RAG) is a technique that combines
document retrieval with large language models to generate accurate responses.
```

---

# Technologies Used

* Python
* LangChain
* FAISS
* HuggingFace Embeddings
* Ollama (Local LLM)

---

# Limitations of Naive RAG

This basic implementation has some limitations:

* No reranking
* No query rewriting
* No hybrid search
* No metadata filtering
* No evaluation framework


# Learning Goal

This project helps understand the **core concept of Retrieval-Augmented Generation**, which is the foundation of modern AI applications like:


# learning rag see next project  