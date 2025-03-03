
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	tp=np.sum(np.logical_and(y_true==1, y_pred==1))
	tn=np.sum(np.logical_and(y_true==0, y_pred==0))
	fp=np.sum(np.logical_and(y_true==0, y_pred==1))
	fn=np.sum(np.logical_and(y_true==1, y_pred==0))
	if np.isnan(tp):
		tp=0
	if np.isnan(fp):
		fp=0
	if np.isnan(fn):
		fn=0
	if (2*tp+fp+fn)==0:
		dice=0.0
	else:	
		dice=(2*tp)/(2*tp+fp+fn)
	return round(dice, 3)
