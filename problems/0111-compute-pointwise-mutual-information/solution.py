import numpy as np

def compute_pmi(joint_counts, total_counts_x, total_counts_y, total_samples):
	# Implement PMI calculation here
	P_x=total_counts_x/total_samples
	P_y=total_counts_y/total_samples
	P_xy=joint_counts/total_samples
	pmi=np.log2((P_xy)/(P_x*P_y))
	pmi=round(pmi,3)
	if pmi==-1.0:
		return -1
	else:
		return pmi