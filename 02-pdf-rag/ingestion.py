""" 
DATA INGESTION PIPELINE  : 
the process of converting raw text into a searchable vector database.

"""

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


#! loader document 
loader = PyPDFLoader("data/demo.pdf")
docuements = loader.load()

# Split into chunks 
pdf_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)

chnks = pdf_splitter.split_documents(docuements)

#! Create Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#! Vector Store 
vectorstore =  FAISS.from_documents(chnks,embeddings)

#! save locally 
vectorstore.save_local("vector_db_pdf")

print("=====> Ingestion Complete <======")
