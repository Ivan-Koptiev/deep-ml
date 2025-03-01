
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	ssr=0
	sst=0
	mean=0
	for i in range(len(y_true)):
		ssr+=(y_true[i]-y_pred[i])**2
		mean+=y_true[i]
	mean/=len(y_true)
	for i in range(len(y_true)):
		sst+=(y_true[i]-mean)**2
	r_sq=1-(ssr/sst)
	return np.round(r_sq,4)
