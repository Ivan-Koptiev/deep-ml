import numpy as np

def multivariate_kl_divergence(mu_p: np.ndarray, Cov_p: np.ndarray, mu_q: np.ndarray, Cov_q: np.ndarray) -> float:
    """
    Computes the KL divergence between two multivariate Gaussian distributions.
    
    Parameters:
    mu_p: mean vector of the first distribution
    Cov_p: covariance matrix of the first distribution
    mu_q: mean vector of the second distribution
    Cov_q: covariance matrix of the second distribution

    Returns:
    KL divergence as a float
    """
    # Your code here
    #D_KL(P||Q) = 0.5[Tr(cov_q^-1 * cov_p) + (mean_q-mean_p)^T * cov_q^-1 * (mean_q-mean_p) - dimensions + ln(det(cov_q)/det(cov_p))]

    D_KL=0.5*(np.trace(np.linalg.inv(Cov_q) @ Cov_p) + (mu_q-mu_p).T @ np.linalg.inv(Cov_q) @ (mu_q-mu_p) - len(mu_q) + np.log(np.linalg.det(Cov_q)/np.linalg.det(Cov_p)))
    
    return D_KL