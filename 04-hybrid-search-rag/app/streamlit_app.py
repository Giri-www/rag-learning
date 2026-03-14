import streamlit as st
import sys
import os
from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.loader import DocumentLoader
from core.embeddings import EmbeddingModel
from core.vectorstore import VectorStore
from core.keyword_search import KeywordSearch
from core.retriver import HybridRetriever
from core.reranker import Reranker
from core.rag_pipeline import RagPipeline


st.title("Enterprise Hybrid RAG")

loader = DocumentLoader()

docs = loader.load_documents()

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