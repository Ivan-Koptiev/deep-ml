import numpy as np

def sparse_window_attention(Q, K, V, window_size, scale_factor=None):
    # Your code here
    outputs=[]
    scale_factor=scale_factor if scale_factor else np.sqrt(K.shape[1])

    for i in range(len(Q)):
        
        start_ind = max(0, i - window_size)
        end_ind = min(len(Q), i + window_size + 1)

        current_Q=Q[i:i+1,:]
        current_K=K[start_ind:end_ind,:]
        current_V=V[start_ind:end_ind,:]

        scores=(current_Q @ current_K.T)/scale_factor
        attentions=np.exp(scores)/np.sum(np.exp(scores),axis=1,keepdims=True)

        outputs.append(attentions @ current_V)

    return np.vstack(outputs)
