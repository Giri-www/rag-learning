# Hybrid Search RAG (Retrieval-Augmented Generation)

This project demonstrates **Hybrid Search RAG**, a system that combines **semantic (vector) search** and **keyword search** with a **language model** to answer questions using your own documents or knowledge base.  

It is built with **Python**, **LangChain**, **FAISS / Vector DB**, and **Streamlit** as the front-end.

---

## 1️⃣ What is Hybrid Search RAG?

**Hybrid Search RAG** is a combination of:

- **RAG (Retrieval-Augmented Generation)**: 
  - Instead of relying solely on a language model’s training, RAG **retrieves relevant information from your own documents** before generating an answer.
  
- **Hybrid Search**:
  - Combines two types of search:
    1. **Vector / Semantic Search** → Finds documents based on meaning, even if exact words don’t match.
    2. **Keyword / Boolean Search** → Finds documents with exact words or phrases.

**In short:** Hybrid Search RAG retrieves the most relevant documents **using both meaning and exact words**, then uses a language model to generate a **coherent answer**.

---

## 2️⃣ Why use Hybrid Search RAG?

- **Accurate Answers**: Combines semantic understanding and exact matches to improve retrieval quality.  
- **Up-to-Date Information**: Works on your documents, PDFs, or knowledge base instead of relying solely on AI’s pre-trained knowledge.  
- **Complex Queries**: Handles questions that require understanding, summarizing, or combining multiple document pieces.  
- **Industry Applications**: Customer support, legal research, internal knowledge bases, medical references, and more.

---

## 3️⃣ When to use Hybrid Search RAG?

Use it when:

1. You have **large collections of documents** (PDFs, manuals, guides, reports).  
2. You want **better retrieval quality** than keyword-only or vector-only search.  
3. You need **AI-powered answers** that reference your documents.  
4. You want a **scalable and maintainable system** for enterprise-level applications.  

**Example Use Cases:**

| Use Case | Description |
|----------|------------|
| Customer Support | AI answers FAQs using product manuals. |
| Research Assistant | AI reads academic papers and summarizes answers. |
| Company Knowledge Base | Employees ask AI about internal policies or HR documents. |
| Legal/Compliance | AI finds exact clauses and explains them in simple terms. |
| Healthcare | Doctors ask AI about medical literature and guidelines. |

---

## 4️⃣ Project Structure (Industry Standard)

```text
hybrid_rag_prod/
│
├── app/                   # Front-end + API layer
│   └── streamlit_app.py
│
├── core/                  # Core RAG pipeline
│   ├── loader.py          # Load and split documents
│   ├── indexer.py         # Create vector index / store embeddings
│   ├── retriever.py       # Hybrid search logic
│   └── rag.py             # RAG chain / LLM integration
│
├── configs/
│   └── config.yaml        # Model, DB, chunk sizes, top_k
│
├── data/                  # Raw documents (PDFs, DOCX, TXT)
├── logs/                  # Query logs & error logs
├── requirements.txt       # Dependencies
└── README.md