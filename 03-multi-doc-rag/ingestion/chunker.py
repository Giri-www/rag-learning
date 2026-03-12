"""  
Chunker is a function that takes in a document and returns a list of chunks.

"""

from config import chunk_size,chunk_overlap

class DocumentChunker:
    def __init__(self,chunk_size,chunk_overlap):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def chunk_documents(self,documents):
        chunks = []
        for doc in documents:
            text = doc["page_content"]
            for i in range(0,len(text),self.chunk_size -self.chunk_overlap):
                chunk = text[i:i + self.chunk_size]
                chunks.append(chunk)
        return chunks