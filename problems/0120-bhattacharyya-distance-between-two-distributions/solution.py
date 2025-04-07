import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    # Your code here
    if len(p)==0 or len(q)==0 or len(p)!=len(q):
        return 0.0
    else:
        step1=np.array(p)*np.array(q)
        step2=np.sqrt(step1)
        bc=np.sum(step2)
        dist=-1*np.log(bc)
        return dist