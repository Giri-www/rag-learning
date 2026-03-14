from tracemalloc import start

import ollama
from langsmith import traceable
from monitoring.logger import PipelineLogger
import time

logger = PipelineLogger()

class RagPipeline:

    def __init__(self, retriever, reranker):
        self.retriever = retriever
        self.reranker = reranker
    @traceable
    def run(self, query: str) -> str:
        

        logger.log_query(query)
       
        docs = self.retriever.retrieve(query)
        logger.log_retrieval(vector_docs=docs, keyword_docs=[])

        reranked_docs = self.reranker.rerank(query, docs)
        logger.log_rerank(reranked_docs)
        start = time.time()
        
        contxt = ""

        for doc in reranked_docs:
            contxt += doc.page_content + "\n\n"

        prompt = f""" Answer the question based on the following context: {contxt} \n\n Question: {query} \n\n Answer:"""

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}] 
        )
        
        latency = time.time() - start

        logger.log_llm(latency)

        return response["message"]["content"]