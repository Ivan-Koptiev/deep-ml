import numpy as np
def recall(y_true, y_pred):
	tp=0
	fn=0
	for i in range(len(y_true)):
		if y_pred[i]==y_true[i] and y_pred[i]==1:
			tp+=1
		elif y_pred[i]!=y_true[i] and y_pred[i]==0:
			fn+=1
	recall=tp/(tp+fn)
	return round(recall,3)
