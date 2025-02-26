import numpy as np
def precision(y_true, y_pred):
	# Your code here
	tp=0
	fp=0
	for i in range(len(y_true)):
		if (y_pred[i]==y_true[i]) and (y_pred[i]==1):
			tp+=1
		elif (y_pred[i]!=y_true[i]) and (y_pred[i]==1):
			fp+=1
	prec=tp/(tp+fp)

	return prec
