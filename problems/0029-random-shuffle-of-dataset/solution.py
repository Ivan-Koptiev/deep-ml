import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	np.random.seed(seed)
	size=len(X)
	inds=np.random.permutation(size)
	
	new_x=[]
	new_y=[]
	for i in range(len(X)):
		new_x.append(X[inds[i]])
		new_y.append(y[inds[i]])

	return new_x, new_y