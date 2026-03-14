import logging
import time
logger = logging.getLogger("hybrid_rag")
logger.setLevel(logging.INFO)

# Create file handler
file_handler = logging.FileHandler("rag_pipeline.log")

# Create formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)

# Add handler
logger.addHandler(file_handler)

class PipelineLogger:

    def log_query(self, query):
        logger.info(f"Query: {query}")

    def log_retrieval(self, vector_docs, keyword_docs):
        logger.info(f"Vector docs: {len(vector_docs)}")
        logger.info(f"Keyword docs: {len(keyword_docs)}")

    def log_rerank(self, docs):
        logger.info(f"Reranked docs: {len(docs)}")

    def log_llm(self, latency):
        logger.info(f"LLM latency: {latency:.2f}s")