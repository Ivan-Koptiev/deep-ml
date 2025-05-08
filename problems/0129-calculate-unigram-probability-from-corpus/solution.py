def unigram_probability(corpus: str, word: str) -> float:
    # Your code here
    corpus=corpus.split()  
    count_match=0
    total_count=0

    for i in corpus:
        if i==word:
            count_match+=1
        total_count+=1

    final=round(count_match/total_count,4)


    return final