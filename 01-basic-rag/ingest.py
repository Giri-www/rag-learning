""" 
DATA INGESTION PIPELINE  : 
the process of converting raw text into a searchable vector database.

"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

#!load document
loader = TextLoader("data/demo.txt")
documents = loader.load()

#! Split into chunks
txt_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=500)

chunks = txt_splitter.split_documents(documents)


#! Create Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#! Vector Store 
vectorstore = FAISS.from_documents(chunks,embeddings)

#save locally 
vectorstore.save_local("vector_db")

print("======> Vector Db created & Data ingestion pipeline end ========>")





