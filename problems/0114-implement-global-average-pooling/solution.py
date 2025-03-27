import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
	# Your code here
	final=[]
	for i in range(x.shape[-1]):
		val=0
		count=0
		for j in np.nditer(x[...,i]):
			val+=j
			count+=1
		final.append(val/count)
		
	return final