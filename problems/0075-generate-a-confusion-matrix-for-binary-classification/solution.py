
from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	tp=0
	fp=0
	tn=0
	fn=0
	for i in data:
		if i[1]==i[0] and i[1]==1:
			tp+=1
		elif i[1]==i[0] and i[1]==0:
			tn+=1
		elif i[1]!=i[0] and i[1]==1:
			fp+=1
		elif i[1]!=i[0] and i[1]==0:
			fn+=1
	conf=[[tp,fn],[fp,tn]]
	return conf
