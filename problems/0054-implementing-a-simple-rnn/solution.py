import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
	# Your code here
	h=np.array(initial_hidden_state)
	Wx=np.array(Wx)
	Wh=np.array(Wh)
	b=np.array(b)

	for t in input_sequence:
		h=np.tanh(np.dot(Wx,t)+np.dot(Wh,h)+b)
	h=np.round(h,4)
	return h.tolist()