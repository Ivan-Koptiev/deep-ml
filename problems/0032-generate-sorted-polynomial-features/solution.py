import numpy as np
from itertools import combinations_with_replacement as c_w_r

def polynomial_features(X, degree):
	# Your code here
	new_X=[]
	for i in range(len(X)):
		row=X[i]
		new_row=[1.0]
		for j in range(1, degree+1):
			for comb in c_w_r(row,j):
				new_row.append(np.prod(comb))
		new_X.append(new_row)
	return new_X