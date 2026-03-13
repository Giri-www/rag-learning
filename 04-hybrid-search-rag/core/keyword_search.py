from rank_bm25 import BM25Okapi

""" Keyword Search implementation using BM25 algorithm.  
This class takes a list of documents, tokenizes their content, and builds a BM25 index.
The search method takes a query, computes BM25 scores for each document, and returns the top k relevant documents based on the scores.
The BM25 algorithm is a popular ranking function used in information retrieval to estimate the relevance of documents to a given search query. It considers term frequency, inverse document frequency, and document length to compute relevance scores.
The KeywordSearch class provides a simple way to perform keyword-based search over a collection of documents, making it suitable for applications like information retrieval, question answering, and document ranking.

"""
class KeywordSearch:

    def __init__(self, documents):

        self.texts = [d.page_content for d in documents]

        tokenized = [t.split() for t in self.texts]

        self.bm25 = BM25Okapi(tokenized)

        self.docs = documents

    def search(self, query, k=5):

        scores = self.bm25.get_scores(query.split())

        ranked = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )

        return [self.docs[i] for i in ranked[:k]]