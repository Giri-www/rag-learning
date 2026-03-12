""" 
Converts document chunks into vector embeddings using a SentenceTransformer model.

"""

from langchain_huggingface import HuggingFaceEmbeddings
from config import embedding_model


class ChunkEmbeddings:

    def __init__(self,model_name=embedding_model):
        self.model_name = model_name
        self.model = HuggingFaceEmbeddings(model_name=model_name)

    
    def embed_chunks(self,chunks,show_progress=True):

        texts = [chunk['page_content'] for chunk in chunks]
        
        embeddings = self.model.encode(texts,show_progress=show_progress)

        return embeddings