

class Config:

    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    RERANK_MODEL = "BAAI/bge-reranker-base"

    LLM_MODEL = "llama3"

    CHUNK_SIZE = 800
    CHUNK_OVERLAP = 150

    TOP_K_RETRIEVAL = 20
    TOP_K_RERANK = 5

    DOC_PATH = "data"