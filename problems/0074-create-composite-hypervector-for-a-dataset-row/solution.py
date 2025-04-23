import numpy as np

def create_row_hv(row, dim, random_seeds):
    final = np.zeros(dim, dtype=int)

    for feature, value in row.items():
    
        np.random.seed(random_seeds[feature])
        
        hv_feat = np.random.choice([-1, 1], size=dim)
        hv_val = np.random.choice([-1, 1], size=dim)
        
        bound_hv = hv_feat * hv_val
        
        final += bound_hv

    norm=[]
    for i in range(dim):
        if final[i]>=0:
            norm.append(1)
        else:
            norm.append(-1)

    return norm
