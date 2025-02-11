import numpy as np

def make_diagonal(x):

	d=np.zeros((len(x),len(x)))

	for i in range(len(d)):
		for j in range(len(d[0])):
			if i==j:
				d[i][j]=x[i]

	return d
	