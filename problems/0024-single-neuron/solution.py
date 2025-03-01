import math
import numpy as np

def single_neuron_model(x: list[list[float]], y: list[int], w: list[float], b: float) -> (list[float], float):
	# Your code here

	def sig(x):
		return 1/(1+np.exp(-x))

	probs=[]
	n=len(y)
	err=0
	sum=0

	sum=np.dot(x,w)
	z=sum+b

	for i in z:
		probs.append(sig(i))
		
	for i in range(len(y)):
		err+=(probs[i]-y[i])**2
	mse=(1/n)*err


	return (probs, mse)