from config import Config

from ingestion.loader import DocumentLoader
from ingestion.chunker import DocumentChunker
from ingestion.embeddings import ChunkEmbeddings

from retrieval.vector_store import VectorStore
from retrieval.retriever import Retriver
from retrieval.reranker import Reranker

from llm.ollama_llm import OllamaLLM

class RAGPipeline:

    def __init__(self):
        
        loader = DocumentLoader(Config.DOC_PATH)

        documents = loader.load_documents()

        chunker = DocumentChunker(Config.CHUNK_SIZE,Config.CHUNK_OVERLAP)

        chunks = chunker.chunk_documents(documents)

        self.chunk_embeddings = ChunkEmbeddings()

        embeddings = self.chunk_embeddings.embed_chunks(chunks)

        dimension = len(embeddings[0]) 

        self.vectorstore = VectorStore(dimension)

        self.vectorstore.add(embeddings,chunks)

        # self.retriever = Retriver(self.chunk_embeddings,self.vectorstore,Config.TOP_K_RETRIEVAL)

        self.retriever = Retriver(self.vectorstore,Config.EMBEDDING_MODEL,Config.TOP_K_RETRIEVAL)
        
        self.reranker = Reranker(Config.RERANK_MODEL,Config.TOP_K_RETRIEVAL)

        self.llm = OllamaLLM(Config.LLM_MODEL)
       
    
    def ask(self, query):

        retrieved_chunks = self.retriever.retrieve(query)

        best_chunks = self.reranker.rerank(query, retrieved_chunks)

        answer = self.llm.generate(query, best_chunks)

        return answer, best_chunks