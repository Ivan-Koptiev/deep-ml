import numpy as np

def divide_on_feature(X, feature_i, threshold):
	# Your code here
	met=[]
	not_met=[]
	for i in range(len(X)):
		if X[i][feature_i]>=threshold:
			met.append(X[i])
		else:
			not_met.append(X[i])

	return met,not_met