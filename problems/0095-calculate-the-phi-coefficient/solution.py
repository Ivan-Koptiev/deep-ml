from math import sqrt
def phi_corr(x: list[int], y: list[int]) -> float:
	"""
	Calculate the Phi coefficient between two binary variables.

	Args:
	x (list[int]): A list of binary values (0 or 1).
	y (list[int]): A list of binary values (0 or 1).

	Returns:
	float: The Phi coefficient rounded to 4 decimal places.
	"""
	# Your code here
	x_00=0
	x_11=0
	x_01=0
	x_10=0
	for i in range(len(x)):
		if x[i]==y[i]==0:
			x_00+=1
		elif x[i]==y[i]==1:
			x_11+=1
		elif x[i]==0 and y[i]==1:
			x_01+=1
		elif x[i]==1 and y[i]==0:
			x_10+=1
	phi=((x_00*x_11)-(x_01*x_10))/(sqrt((x_00+x_01)*(x_10+x_11)*(x_00+x_10)*(x_01+x_11)))
	return round(phi,4)