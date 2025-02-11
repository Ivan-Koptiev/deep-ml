def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	means=[]

	if mode=='row':
		for i in matrix:
			mean=0
			for j in i:
				mean+=j
			means.append(mean/len(matrix))
	else:
		for i in range(len(matrix[0])):
			mean=0
			for j in range(len(matrix)):
				mean+=matrix[j][i]
			means.append(mean/len(matrix[0]))
	return means