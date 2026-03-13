import os
import logging
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

logger = logging.getLogger(__name__)

class DocumentLoader:
    def __init__(self, data_path="data/", chunk_size=800, chunk_overlap=150):
        self.data_path = data_path
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def load_documents(self):
        all_docs = []
        for file in os.listdir(self.data_path):
            if file.endswith(".pdf"):
                logger.info(f"Loading document: {file}")
                loader = PyPDFLoader(os.path.join(self.data_path, file))
                docs = loader.load()
                all_docs.extend(docs)
        split_docs = self.split_docs(all_docs)
        logger.info(f"Total chunks created: {len(split_docs)}")
        return split_docs

    def split_docs(self, docs):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        return splitter.split_documents(docs)