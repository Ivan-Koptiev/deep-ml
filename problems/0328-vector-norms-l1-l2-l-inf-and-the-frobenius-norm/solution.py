import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.
    
    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', or 'frobenius')
    
    Returns:
        The computed norm as a float
    """
    # Your code here
    if norm_type=="l1":
        out=np.sum(abs(arr))
    elif norm_type=="l2":
        out=np.sqrt(np.sum(np.power(arr,2)))

    else:
        out=np.sqrt(np.sum(np.power(arr.flatten(),2)))



    return float(out)
