import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
	inter=0
	union=0
	for i in range(len(y_true)):
		if y_true[i]==y_pred[i]==1:
			inter+=1
		if y_true[i]==1 or y_pred[i]==1 or y_true[i]==y_pred[i]==1:
			union+=1
	if union==0:
		return 0.0
	jac=inter/union
	return round(jac, 3)
