import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
	# Your code here
    step1=w1 @ x
    step2=np.maximum(0,step1)
    step3=step2 @ w2
    step4=x+step3
    step5=np.maximum(0,step4)
    return step5