import numpy as np

def train_neuron(x: np.ndarray, labels: np.ndarray, weights: np.ndarray, bias: float, lr: float, epochs: int) -> (np.ndarray, float, list[float]): 	 	
    def sigmoid(z):
        return 1/(1+np.exp(-z))

    mse_values=[]
    n=len(labels)
    
#	for _ in range(epochs):
#		#forward
#		z=x@weights+bias
#		prob=sigmoid(z)
#		error=prob-labels
#		mse=np.mean(error**2)
#		mse_values.append(round(mse, 4))
#
#		#backward
#        dl_dp=(2/n)*(prob-labels)
#		dp_dz=sigmoid(prob)*(1-sigmoid(prob))
#		dl_dz=dl_dp*dp_dz
#		dz_db=sum(z*1)
#		dl_db=sum(dl_dz*dz_db)
#        dz_dw=x
#		dl_dw=dl_dz@dz_dw
#
#		#update
#        weights-=lr*dl_dw
#		bias-=lr*dl_db
#		weights=np.round(weights,4)
#		bias=np.round(bias,4)
    for _ in range(epochs):
        z = np.dot(x, weights) + bias
        predictions = sigmoid(z)
        
        mse = np.mean((predictions - labels) ** 2)
        mse_values.append(round(mse, 4))

        # Gradient calculatio