import numpy as np

def compressed_row_sparse_matrix(mat):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	values=[]
	count=0
	rows=[0]
	for i in mat:
		non_zero=0
		for j in i:
			if j!=0:
				values.append(j)
				non_zero+=1
		count+=non_zero
		rows.append(count)
	
	inds=np.argwhere(mat)
	columns=[row[1] for row in inds]
	

	
	
		

	return (values, columns, rows)
