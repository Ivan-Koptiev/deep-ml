import numpy as np
def transform_basis(b: list[list[int]], c: list[list[int]]) -> list[list[float]]:

	c_inv=np.linalg.inv(c)
	p=np.dot(c_inv,b)

	return p