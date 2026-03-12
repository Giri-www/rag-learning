""" 
Retriver 

Retrieves the most relevant document chunks for a user query.
    ** Handles query embedding and vector search retrieval.
"""

from config import EMBEDDING_MODEL, TOP_K_RETRIEVAL
from langchain_huggingface import HuggingFaceEmbeddings


class Retriver :

    def __init__(self,vectorstore,model_name=EMBEDDING_MODEL,top_k=TOP_K_RETRIEVAL):
        self.vectorstore = vectorstore
        self.model_name = HuggingFaceEmbeddings(model_name)
        self.top_k = top_k

    def retrieve(self,query):
       """ Retrieve  relevant chunks from vectorstore """
       qry_embeddings  = self.model.encode([query])

       results = self.vectorstore.search(qry_embeddings,self.top_k)

       return results