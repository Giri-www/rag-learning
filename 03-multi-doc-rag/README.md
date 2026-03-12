                DOCUMENT SOURCES
     PDFs | Docs | DB | Websites | APIs
                    │
                    ▼
              Document Loader
                    │
                    ▼
                Chunking
         (Semantic / Recursive)
                    │
                    ▼
              Embedding Model
        (HuggingFace SentenceTransformer)
                    │
                    ▼
                Vector DB
        (FAISS / Qdrant / Chroma)
                    │
                    ▼
              Query Pipeline
        ┌─────────────────────────┐
        │ Query Rewrite (LLM)     │
        │ Hybrid Retrieval        │
        │ Metadata Filtering      │
        │ Reranking Model         │
        └─────────────────────────┘
                    │
                    ▼
             Context Builder
                    │
                    ▼
             LLM (Ollama)
      llama3 / mistral / mixtral
                    │
                    ▼
                Final Answer
             + Sources / Citations