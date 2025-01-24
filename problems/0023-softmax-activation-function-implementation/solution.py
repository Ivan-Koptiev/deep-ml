import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
	# Your code here
	probs=[]
	sum=0
	
	for i in scores:
		sum+=np.exp(i)

	for i in scores:
		probs.append(round(np.exp(i)/sum, 4))


	return probs