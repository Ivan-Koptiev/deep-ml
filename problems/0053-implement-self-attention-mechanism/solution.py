import numpy as np

def compute_qkv(X, W_q, W_k, W_v):
    Q=np.dot(X, W_q)
    K=np.dot(X, W_k)
    V=np.dot(X, W_v)
    return Q,K,V

def softmax(i):
	return np.exp(i) / np.sum(np.exp(i), axis=1, keepdims=True)

def self_attention(Q, K, V):
    attention_output=np.dot(softmax(np.dot(Q, np.transpose(K))/np.sqrt(K.shape[1])), V)
    return attention_output
