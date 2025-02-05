
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	
	b=[]

	for m in range(len(a[0])):
		r=[]
		for n in range(len(a)):
			r.append(a[n][m])
		b.append(r)

	return b