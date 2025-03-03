
import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	props=[]
	for i in set(y):
		count=0
		for j in y:
			if i==j:
				count+=1
		props.append(count/len(y))

	sum=0
	for i in props:
		sum+=i**2

	gini=1-sum
	return round(gini,3)