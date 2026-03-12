"""  
Chunker is a function that takes in a document and returns a list of chunks.

"""

from config import Config

class DocumentChunker:
    def __init__(self,CHUNK_SIZE,CHUNK_OVERLAP):
        self.chunk_size = CHUNK_SIZE
        self.chunk_overlap = CHUNK_OVERLAP
    
    # def chunk_documents(self,documents):
    #     chunks = []
    #     for doc in documents:
    #         text = doc["text"]
    #         for i in range(0,len(text),self.chunk_size -self.chunk_overlap):
    #             chunk = text[i:i + self.chunk_size]
    #             chunks.append(chunk)
    #     return chunks

    def chunk_documents(self, documents):
        chunks = []
        for doc in documents:
            # Handle both plain strings and dicts
            if isinstance(doc, dict):
                text = doc.get("text", "")
                source = doc.get("source", "unknown")
            else:
                text = doc
                source = "unknown"

            for i in range(0, len(text), self.chunk_size - self.chunk_overlap):
                chunk_text = text[i:i + self.chunk_size]
                if chunk_text.strip():          # skip empty chunks
                    chunks.append({
                        "text": chunk_text,
                        "source": source        # add source
                    })
        return chunks