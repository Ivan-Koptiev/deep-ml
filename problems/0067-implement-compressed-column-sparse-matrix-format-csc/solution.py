def compressed_col_sparse_matrix(mat):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	values=[]
	count=0
	col_pt=[0]
	row_inds=[]
	for j in range(len(mat[0])):
		count_vals=0
		for i in range(len(mat)):
			if mat[i][j]!=0:
				values.append(mat[i][j])
				row_inds.append(i)
				count_vals+=1
		count+=count_vals
		col_pt.append(count)
	
	return (values, row_inds, col_pt)
