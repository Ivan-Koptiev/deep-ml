def meteor_score(reference, candidate, alpha=0.9, beta=3, gamma=0.5):
    """
    Calculate the METEOR score between a reference and candidate text.
    
    Args:
        reference (str): The reference text
        candidate (str): The candidate text
        alpha (float): Weight for precision in F-score calculation (default: 0.9)
        beta (float): Parameter for penalty calculation (default: 3)
        gamma (float): Weight for fragmentation penalty (default: 0.5)
        
    Returns:
        float: METEOR score
    """
    # Tokenize
    token_1 = reference.lower().split()
    token_2 = candidate.lower().split()
    
    # Edge cases
    if len(token_1) == 0 and len(token_2) == 0:
        return 1.0  # Perfect match for empty strings
    if len(token_1) == 0 or len(token_2) == 0:
        return 0.0  # No match possible
    
    # Match words using exact matching
    matches = 0
    match_ind1 = []
    match_ind2 = []
    matched_2 = [False] * len(token_2)
    
    # Match indivi