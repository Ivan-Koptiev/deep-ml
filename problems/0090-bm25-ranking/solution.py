import numpy as np
from collections import Counter
import math

def calculate_bm25_scores(corpus, query, k1=1.5, b=0.75):
    """
    Calculate BM25 scores for a query across a corpus of documents.
    
    Parameters:
    -----------
    corpus : list of list of str
        A list of documents where each document is a list of terms
    query : list of str
        The search query terms
    k1 : float, optional (default=1.5)
        Saturation parameter controlling term frequency scaling
    b : float, optional (default=0.75)
        Length normalization parameter
    
    Returns:
    --------
    np.ndarray
        BM25 scores for each document in the corpus
    """
    
    N = len(corpus)  # Number of documents in the corpus
    doc_lengths = [len(doc) for doc in corpus]  # Document lengths
    avg_doc_length = np.mean(doc_lengths)  # Average document length
    
    # Calculate IDF for each term in the query
    idf = {}
    query_terms = set(query)
    for term in query_terms:
  