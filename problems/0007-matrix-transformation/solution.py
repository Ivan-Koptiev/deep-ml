import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	
	if np.linalg.det(T)==0 or np.linalg.det(S)==0:
		return -1
	
	inv_t=np.linalg.inv(T)

	new=np.matmul(inv_t,A)
	new2=np.matmul(new,S)

	return new2