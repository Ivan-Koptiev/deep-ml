import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	def partial_pivot(A, b, row_index):
    
    	n = len(b)
    	pivot_value = abs(A[row_index, row_index])
    	pivot_row = row_index
    
    	for i in range(row_index + 1, n):
        	if abs(A[i, row_index]) > pivot_value:
            	pivot_value = abs(A[i, row_index])
            	pivot_row = i
    
    	if pivot_row != row_index:
        	A[[row_index, pivot_row]] = A[[pivot_row, row_index]]
        	b[[row_index, pivot_row]] = b[[pivot_row, row_index]]  

    	return A, b
	
	for k in range(len(A)-1):
		A,b=partial_pivot(A,b,k)
		for i in range(k+1,len(A)):
			factor=A[i][k]/A[k][k]
			for j in range(k, len(A[0])):
				A[i][j]=A[i][j]-factor*A[k][j]
			b[i]=b[i]-factor*b[k]

	x=np.zeros(len(A))

	for k in range(len(A)-1,-1,-1):
		s=0
		for i in range