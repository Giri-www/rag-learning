"""  
#Query/Inference/RetrievalQA Pipeline

why : Answer user questions 

Steps : User Question -> Convert Question to Embedding -> Vector DB Search/Similarity Search (FAISS) -> Retrieve Chunks -> Build Prompt/Context Builder -> Send Prompt to LLM (Ollama) -> Get Response

"""

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import Ollama


#! Load Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#! Load Vector DB
vectorstore = FAISS.load_local("vector_db_pdf",embeddings,allow_dangerous_deserialization=True)

#! Create Retriever
retriver = vectorstore.as_retriever(search_kwargs={"k": 3})

#! Initialize LLM
llm = Ollama(model="llama3", temperature=0.5)

print(" PDF RAG Loaded Successfully ")
print ("Type 'exit' to quit")

while True:
    query = input("\nAsk a question: ")
    if query.lower() == "exit":
        break
    
    docs = vectorstore.similarity_search(query,k=3)

    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"

    response = llm.invoke(prompt)
    print(response)

