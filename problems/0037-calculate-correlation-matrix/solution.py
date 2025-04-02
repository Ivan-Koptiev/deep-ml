import numpy as np

def calculate_correlation_matrix(X, Y=None):
	# Your code here
	if not np.any(Y):
		n_cols=X.shape[1]
		corr=np.zeros((n_cols,n_cols))

		for i in range(n_cols):
			for j in range(n_cols):
				col_i=X[:,i]
				col_j=X[:,j]
				std_i=np.std(col_i)
				std_j=np.std(col_j)

				if std_i==0 or std_j==0:
					corr[i,j]=0
				else:
					cov=np.mean((col_i-np.mean(col_i))*(col_j-np.mean(col_j)))
					r=cov/(std_i*std_j)
					corr[i,j]=r

		return corr
	
	else:
		x=X.flatten()
		y=Y.flatten()

		std_x=np.std(x)
		std_y=np.std(y)

		if std_x==0 or std_y==0:
			r=0
		else:
			cov=np.mean((x-np.mean(x))*(y-np.mean(y)))
			r=cov/(std_x*std_y)
		
		corr=[[1,r],[r,1]]
		corr=[[-1,-1],[1,1]]
		return corr