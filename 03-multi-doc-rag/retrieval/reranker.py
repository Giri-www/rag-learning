

from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from config import  RERANK_MODEL, TOP_K_RETRIEVAL

class Reranker:

    def __init__(self, model_name=RERANK_MODEL,top_k=TOP_K_RETRIEVAL):
        self.model = HuggingFaceCrossEncoder(model_name=model_name)
        self.top_k = top_k

    def rerank(self,query,chunks):

        if not chunks:
            return []
        
        #create query document-pairs
        pairs = [(query,chunk['page_content']) for chunk in chunks]

        #predicat the relavant score 
        scores = self.model.predict(pairs)

        #Combine chunks & store 
        ranked_results = sorted(zip(chunks,scores)key=lambda x:x[1],reverse=True)

        return [chunk for chunk,_ in ranked_results][:self.top_k]