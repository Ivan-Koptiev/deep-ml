def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	cov_mat=[]
	means=[]
	vars=[]
	covs=[]

	for i in vectors:
		mean=0
		for j in i:
			mean+=j
		means.append(mean/len(i))

	for i in range(len(vectors)):
		var=0
		for j in range(len(vectors[0])):
			var+=(vectors[i][j]-means[i])**2
		vars.append(var/(len(vectors[i])-1))

	for i in range(len(vectors)):
		row = []
		for j in range(len(vectors)):
			if i == j:  
				row.append(vars[i])
			elif i < j:  
				cov = 0
				for k in range(len(vectors[0])):
					cov += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
				cov_value = cov / (len(vectors[0]) - 1)
				row.append(cov_value)
			else:  
				row.append(cov_mat[j][i])
		cov_mat.append(row)

	return cov_mat