def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:

	det=((matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0]))

	if det==0:
		return -1

	c=[]
	row1=[matrix[1][1],-matrix[1][0]]
	row2=[-matrix[0][1],matrix[0][0]]
	c.append(row1)
	c.append(row2)

	c_t=[]

	for m in range(len(c[0])):
		r=[]
		for n in range(len(c)):
			r.append(c[n][m])
		c_t.append(r)
			
	inverse=[]

	for i in c_t:
		row=[]
		for j in i:
			inv=j/det
			row.append(inv)
		inverse.append(row)
	
	return inverse