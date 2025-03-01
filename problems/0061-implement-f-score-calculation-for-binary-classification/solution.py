import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	tp=0
	tn=0
	fp=0
	fn=0
	for i in range(len(y_true)):
		if y_pred[i]==y_true[i] and y_pred[i]==0:
			tn+=1
		elif y_pred[i]==y_true[i] and y_pred[i]==1:
			tp+=1
		elif y_pred[i]!=y_true[i] and y_pred[i]==0:
			fn+=1
		elif y_pred[i]!=y_true[i] and y_pred[i]==1:
			fp+=1
	rec=tp/(tp+fn)
	prec=tp/(tp+fp)
	f_sc=(1+beta**2)*((prec*rec)/((beta**2)*prec+rec))
	return round(f_sc,3)
