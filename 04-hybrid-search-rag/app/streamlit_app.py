import streamlit as st

from core.loader import DocumentLoader
from core.embeddings import EmbeddingModel
from core.vectorstore import VectorStore
from core.keyword_search import KeywordSearch
from core.retriver import HybridRetriever
from core.reranker import Reranker
from core.rag_pipeline import RagPipeline


st.title("Enterprise Hybrid RAG")

loader = DocumentLoader()

docs = loader.load()

emb = EmbeddingModel().get()

vector = VectorStore(emb).build(docs)

keyword = KeywordSearch(docs)

retriever = HybridRetriever(vector, keyword)

reranker = Reranker()

rag = RagPipeline(retriever, reranker)

query = st.text_input("Ask question")

if query:

    answer = rag.run(query)

    st.write(answer)