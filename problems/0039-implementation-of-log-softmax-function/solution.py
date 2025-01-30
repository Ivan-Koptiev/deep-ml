import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here

	log_soft=[]
	soft_sum_list=[]

	for i in scores:
		elem=np.exp((i-max(scores)))
		soft_sum_list.append(elem)

	soft_sum=sum(soft_sum_list)

	for i in scores:
		log=i-(max(scores))-(np.log(soft_sum))
		log_soft.append(log)
		
	return log_soft