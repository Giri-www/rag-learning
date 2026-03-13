class HybridRetriever:

    def __init__(self, vectorstore, keyword_search):

        self.vectorstore = vectorstore
        self.keyword = keyword_search

    def retrieve(self, query):

        vector_docs = self.vectorstore.similarity_search(query, k=5)

        keyword_docs = self.keyword.search(query, k=5)

        combined = vector_docs + keyword_docs

        return combined