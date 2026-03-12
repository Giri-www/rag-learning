

# from langchain_community.cross_encoders import HuggingFaceCrossEncoder
# from config import  *
# class Reranker:

#     def __init__(self, model_name=Config.RERANK_MODEL,top_k=Config.TOP_K_RETRIEVAL):
#         self.model = HuggingFaceCrossEncoder(model_name=model_name)
#         self.top_k = top_k

#     def rerank(self,query,chunks):

#         if not chunks:
#             return []
       
       
#         #create query document-pairs
#         # pairs = [(query,chunk) for chunk in chunks]
#         pairs = [
#             (query, chunk[0] if isinstance(chunk, list) else chunk)
#             for chunk in chunks
#             ]

#         #predicat the relavant score 
#         scores = self.model.score(pairs)

#         #Combine chunks & store 
#         ranked_results = sorted(zip(chunks,scores),key=lambda x:x[1],reverse=True)

#         return [chunk for chunk,_ in ranked_results][:self.top_k]


from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from config import *

class Reranker:

    def __init__(self, model_name=Config.RERANK_MODEL, top_k=Config.TOP_K_RETRIEVAL):
        self.model = HuggingFaceCrossEncoder(model_name=model_name)
        self.top_k = top_k

    # def rerank(self, query, chunks):
    #     """
    #     Rerank retrieved chunks based on relevance to query.
    #     Expects chunks as dicts with 'text', 'source', 'page'.
    #     """
    #     if not chunks:
    #         return []

    #     # Create query-document pairs for scoring
    #     pairs = [(query, chunk['text']) for chunk in chunks]

    #     # Get relevance scores from cross-encoder
    #     scores = self.model.score(pairs)

    #     # Combine chunks with scores and sort
    #     ranked_results = sorted(
    #         zip(chunks, scores),
    #         key=lambda x: x[1],
    #         reverse=True
    #     )

    #     # Return top-k chunks (dicts with text+metadata)
    #     return [chunk for chunk, _ in ranked_results][:self.top_k]

    def rerank(self, query, chunks):
        if not chunks:
            return []

        def get_text(chunk):
            if isinstance(chunk, dict):
                text = chunk.get('text', '')
            else:
                text = chunk
            # Force to plain string, strip whitespace
            return str(text).strip() if text is not None else ''

        pairs = []
        valid_chunks = []
        for chunk in chunks:
            text = get_text(chunk)
            if text:
                pairs.append((str(query).strip(), text))
                valid_chunks.append(chunk)

        if not pairs:
            return chunks[:self.top_k]

        scores = self.model.score(pairs)
        ranked = sorted(zip(scores, valid_chunks), key=lambda x: x[0], reverse=True)
        return [chunk for _, chunk in ranked[:self.top_k]]