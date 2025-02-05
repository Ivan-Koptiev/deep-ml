import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here

    mean = np.mean(data, axis=0) 
    std = np.std(data, axis=0)  

    
    z_data = (data - mean) / std

    
    min_data = np.min(data, axis=0)   
    max_data = np.max(data, axis=0)   
    
    norm_data = ((data - min_data) / (max_data - min_data)) * (1 - 0) + 0  

    return z_data, norm_data
