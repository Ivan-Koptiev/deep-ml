
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
	if (len(v1)!=len(v2)) or (len(v1)==0) or (len(v2)==0):
		return -1.0
	
	dot=0
	sum1=0
	sum2=0
	for i in range(len(v1)):
		dot+=(v1[i]*v2[i])
		sum1+=(v1[i])**2
		sum2+=(v2[i])**2
	mag1=np.sqrt(sum1)
	mag2=np.sqrt(sum2)

	sim=dot/(mag1*mag2)

	return round(sim,3)
