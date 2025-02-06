import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

	eigenvalues=[]
	det=np.linalg.det(matrix)
	tr=np.trace(matrix)

	d=np.sqrt(np.power(tr,2)-(4*det))
	x1=(tr+d)/2
	x2=(tr-d)/2
	eigenvalues.append(x1)
	eigenvalues.append(x2)

	return eigenvalues