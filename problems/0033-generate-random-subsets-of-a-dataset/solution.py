import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True, seed=42):
	# Your code here
    if seed is not None:
        np.random.seed(seed)
    
    subsets=[]

    for _ in range(n_subsets):
        if replacements:
            indicies=np.random.choice(len(X),size=len(X),replace=True)
        else:
            indicies=np.random.choice(len(X),size=2,replace=False)

        X_subset=X[indicies]
        y_subset=y[indicies]
        
        subsets.append((X_subset,y_subset))

	return subsets