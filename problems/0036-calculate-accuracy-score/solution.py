import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	corr=0
	for i in range(len(y_true)):
		if y_pred[i]==y_true[i]:
			corr+=1
	acc=corr/len(y_pred)
	return acc