def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	# Your code here
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
	if tp+fp==0 or tp+fn==0:
		return 0.0
	prec=tp/(tp+fp)
	rec=tp/(tp+fn)
	f1=2*((prec*rec)/(prec+rec))
	return round(f1,3)