from langchain_community.vectorstores import FAISS


class VectorStore:

    def __init__(self, embeddings):

        self.embeddings = embeddings

    def build(self, documents):

        return FAISS.from_documents(
            documents,
            self.embeddings
        )