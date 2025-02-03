def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:

	if len(a[0])!=len(b):
		return -1

	c=[]

	for row in a:
		holder=0
		for col in range(len(row)):
			holder+=(row[col]*b[col])
		c.append(holder)

	return c
	