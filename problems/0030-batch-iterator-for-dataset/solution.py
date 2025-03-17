import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	
	batch=[]
	if y is not None:
		for i in range(0,len(X),batch_size):
			batch.append([X[i:i+batch_size],y[i:i+batch_size]])
	else:
		for i in range(0,len(X),batch_size):
			batch.append(X[i:i+batch_size])

	return batch