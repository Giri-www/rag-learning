import ollama

class RagPipeline:

    def __init__(self, retriever, reranker):
        self.retriever = retriever
        self.reranker = reranker

    def run(self, query: str) -> str:

        docs = self.retriever.retrieve(query)
       
        reranked_docs = self.reranker.rerank(query, docs)

        contxt = ""

        for doc in reranked_docs:
            contxt += doc.page_content + "\n\n"

        prompt = f""" Answer the question based on the following context: {contxt} \n\n Question: {query} \n\n Answer:"""

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}] 
        )

        return response["message"]["content"]