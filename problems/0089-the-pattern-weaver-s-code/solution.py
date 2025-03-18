import numpy as np

def softmax(values):
	# Implement the softmax function
	sum=[]
	for i in values:
		row=0
		for j in i:
			row+=np.exp(j)
		sum.append(row)

	soft=[]
	for i in range(len(values)):
		row=[]
		for j in range(len(values[0])):
			row.append(np.exp(values[i][j])/sum[i])
		soft.append(row)

	return soft

def pattern_weaver(n, crystal_values, dimension):
	# Your code here
	scores=[]
	for i in crystal_values:
		row=[]
		for j in crystal_values:
			row.append((i*j)/np.sqrt(dimension))
		scores.append(row)

	soft_scores=softmax(scores)

	final=[]
	for i in range(len(soft_scores)):
		val=0
		for j in range(len(soft_scores[0])):
			val+=soft_scores[i][j]*crystal_values[j]
		final.append(val)
	return np.round(final,3)