import ollama


class OllamaLLM:

    def __init__(self, model):

        self.model = model

  
    def _build_context(self, context_chunks: list) -> str:
        """
        Convert retrieved chunks into a formatted context string. ||  Format Nicely 
        """
        context_parts = []

        for chunk in context_chunks:
            source = chunk.get("source", "unknown")
            page = chunk.get("page", "N/A")
            page_content = chunk.get("page_content", "")

            context_parts.append(
                f"Source: {source} | Page: {page}\n{page_content}"
            )

        return "\n\n".join(context_parts)
    


    def generate(self, query: str, context_chunks: list) -> str:
        """
        Generate answer using the LLM.

        Args:
            query (str): User question
            context_chunks (list): Retrieved document chunks

        Returns:
            str: Generated answer
        """

        context = self._build_context(context_chunks)

        prompt = f"""
                    You are a helpful assistant.

                    Answer the question using ONLY the provided context.
                    If the answer is not in the context, say "I don't know".

                    Context:
                    {context}

                    Question:
                    {query}

                    Answer:
                    """

        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )

        return response["message"]["content"]