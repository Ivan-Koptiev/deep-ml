import numpy as np

def l1_regularization_gradient_descent(X: np.array, y: np.array, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4) -> tuple:
    n_samples, n_features = X.shape

    weights = np.zeros(n_features)
    bias = 0
    
    # Gradient Descent Loop
    for i in range(max_iter):
        # Compute predictions
        y_pred = X @ weights + bias
        
        # Calculate errors (residuals)
        errors = y_pred - y
        
        # Compute the gradient for weights and bias
        d_w = (X.T @ errors) / n_samples + alpha * np.sign(weights)  # L1 regularization on weights
        d_b = np.sum(errors) / n_samples  # Gradient for bias
        
        # Update weights and bias
        weights -= learning_rate * d_w
        bias -= learning_rate * d_b
        
        # Check for convergence (if the change in weights is small enough)
        if np.sum(np.abs(d_w)) < tol:
            break
    
    return 