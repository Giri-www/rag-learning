""" 
Query/Inference/RetrievalQA Pipeline

why : Answer user questions 

Steps : User Question -> Convert Question to Embedding -> Vector DB Search (FAISS) -> Retrieve Chunks -> Build Prompt -> Send Prompt to LLM (Ollama) -> Get Response

"""
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
# from langchain_community.chains import RetrievalQA
from langchain_classic.chains import RetrievalQA



#!Load Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#! Load Vector DB
vectorstore = FAISS.load_local("vector_db",embeddings,allow_dangerous_deserialization=True)

#! Create Retriever
retriver = vectorstore.as_retriever(search_kwargs={"k": 2})

#! Initialize LLM
llm = Ollama(model="llama3", temperature=0.5)

#Create Rag Chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriver)


while True:
    query = input("Ask a question: ")
    
    if query == "exit":
        break
    else:
        result = qa_chain.invoke({"query": query})
        print(result["result"])