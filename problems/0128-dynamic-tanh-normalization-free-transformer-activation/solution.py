import numpy as np

def dynamic_tanh(x: np.ndarray, alpha: float, gamma: float, beta: float) -> list[float]:
    # Your code here
    # x-> (B,T,C)
    ax=alpha*x
    tanh=np.tanh(ax)
    g_tanh=gamma*tanh
    dynamic_tanh=g_tanh+beta

    return dynamic_tanh