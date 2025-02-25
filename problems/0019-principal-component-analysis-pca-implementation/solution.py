import numpy as np
def pca(data: np.ndarray, k: int) -> np.ndarray:
    standard = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
    
    cov = np.cov(standard, rowvar=False)
    
    eig_val, eig_vec = np.linalg.eig(cov)
    
    sorted_indices = np.argsort(eig_val)[::-1]
    eig_val = eig_val[sorted_indices]
    eig_vec = eig_vec[:, sorted_indices]
    
    pca = eig_vec[:, :k]
    
    return np.round(pca, 4)