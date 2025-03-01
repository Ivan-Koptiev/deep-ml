import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	rmse=0
	count=0
	if y_true.ndim>1:
		for i in range(len(y_true)):
			for j in range(len(y_true[0])):
				rmse+=(y_true[i][j]-y_pred[i][j])**2
				count+=1
	else:
		for i in range(len(y_true)):
			rmse+=(y_true[i]-y_pred[i])**2
			count+=1

	rmse=rmse/count
	rmse=np.sqrt(rmse)
	return np.round(rmse,3)
