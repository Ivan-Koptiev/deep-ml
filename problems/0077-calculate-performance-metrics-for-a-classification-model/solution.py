import numpy as np

def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	# Implement your code here
	tp=0
	tn=0
	fp=0
	fn=0

	for i in range(len(actual)):
		if predicted[i]==0 and actual[i]==predicted[i]:
			tn+=1
		elif predicted[i]==0 and actual[i]!=predicted[i]:
			fn+=1
		elif predicted[i]==1 and actual[i]==predicted[i]:
			tp+=1
		elif predicted[i]==1 and actual[i]!=predicted[i]:
			fp+=1

	conf=[[tp,fn],[fp,tn]]

	acc=(tp+tn)/(tp+tn+fp+fn)

	prec=tp/(tp+fp)

	npv=tn/(tn+fn)

	rec=tp/(tp+fn)

	spec=tn/(tn+fp)

	f1=2*((prec*rec)/(prec+rec))

	return conf, round(acc, 3), round(f1, 3), round(spec, 3), round(npv, 3)
