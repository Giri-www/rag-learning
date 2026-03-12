""" 
Converts document chunks into vector embeddings using a SentenceTransformer model.

"""

from langchain_huggingface import HuggingFaceEmbeddings
from config import *


class ChunkEmbeddings:

    def __init__(self,model_name=Config.EMBEDDING_MODEL):
        self.model_name = model_name
        self.model = HuggingFaceEmbeddings(model_name=model_name)

    
    def embed_chunks(self,chunks):

        # texts = [chunk['page_content'] for chunk in chunks]
        texts = chunks
        
        embeddings = self.model.embed_documents(texts)

        return embeddings