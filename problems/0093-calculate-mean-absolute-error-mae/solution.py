import numpy as np

def mae(y_true, y_pred):
	"""
	Calculate Mean Absolute Error between two arrays.

	Parameters:
	y_true (numpy.ndarray): Array of true values
    y_pred (numpy.ndarray): Array of predicted values

	Returns:
	float: Mean Absolute Error rounded to 3 decimal places
	"""
	# Your code here
	mae=0
	count=0
	if y_true.ndim>1:
		for i in range(len(y_true)):
			for j in range(len(y_true[0])):
				mae+=np.abs(y_true[i][j]-y_pred[i][j])
				count+=1
	else:
		for i in range(len(y_true)):
			mae+=np.abs(y_true[i]-y_pred[i])
			count+=1

	mae=mae/count
	return np.round(mae,3)