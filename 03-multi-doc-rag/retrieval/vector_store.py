""" 
Vector Store : 

Stores document embeddings in a vector database with metadata info .

"""

import faiss
import numpy as np

class VectorStore: 

    def __init__(self, dimension):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []

    def add(self, embeddings, chunks):
        
        embeddings = np.array(embeddings).astype('float32')  # change data type to float32 for faiss index compatibility 
        
        if embeddings.ndim == 1 :   # here we check if embeddings is a 1D array
            embeddings = embeddings.reshape(1, -1)  # if it is, we reshape it to a 2D array with a single row because faiss expects 2D arrays
        
        self.index.add(embeddings)
        self.metadata.append(chunks)

    def search(self, query, k=5):
        """ 
        Search for similar document chunks to the query 
        """

        query = np.array(query).astype('float32')
        
        if query.ndim == 1:
            query = query.reshape(1,-1)

        distances, indices = self.index.search(query, k)   #  Search for k nearest neighbors  closest to the query #indicies meaning position of the nearest neighbors

        result = []

        for idx in indices[0]:
            if 0 <= idx < len(self.metadata):
                result.append(self.metadata[idx])
        
        return result

    def save(self,path_index="inedex.faiss",path_metadata="metadata.npy"): 
        """ 
        Save the vector store / index and metadata   
        """
        faiss.write_index(self.index,path_index)
        np.save(path_metadata,np.array(self.metadata,dtype=object))

    def load(self,path_index="inedex.faiss",path_metadata="metadata.npy"):
        """ 
        Load the vector store / index and metadata   
        """
        self.index = faiss.read_index(path_index)
        self.metadata = np.load(path_metadata,dtype=object)