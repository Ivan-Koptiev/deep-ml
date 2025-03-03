import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	one_hot=[]
	if n_col==None:
		n_col=len(set(x))
	
	for i in range(len(x)):
		row=[]
		for j in range(n_col):
			if j==x[i]:
				val=1
			else:
				val=0
			row.append(val)
		one_hot.append(row)

	return one_hot