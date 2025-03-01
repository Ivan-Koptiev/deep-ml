def model_fit_quality(tr_acc, test_acc):
	"""
	Determine if the model is overfitting, underfitting, or a good fit based on training and test accuracy.
	:param training_accuracy: float, training accuracy of the model (0 <= training_accuracy <= 1)
	:param test_accuracy: float, test accuracy of the model (0 <= test_accuracy <= 1)
	:return: int, one of '1', '-1', or '0'.
	"""
	# Your code here
	if tr_acc>test_acc and tr_acc-test_acc>=0.2:
		return 1
	elif tr_acc<0.7 and test_acc<0.7:
		return -1
	else:
		return 0