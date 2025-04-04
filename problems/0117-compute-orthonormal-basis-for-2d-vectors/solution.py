import numpy as np

def orthonormal_basis(vectors: list[list[float]], tol: float = 1e-10) -> list[np.ndarray]:
    ortho = []
    for i in range(len(vectors)):
        v_i = np.array(vectors[i], dtype=float)

        if i == 0:
            norm = np.linalg.norm(v_i)
            if norm > tol:
                u_i = v_i / norm
                ortho.append(u_i)
        else:
            w_k = v_i.copy()

            for u in ortho:
                w_k -= np.dot(v_i, u) * u

            norm_wk = np.linalg.norm(w_k)
            if norm_wk > tol:
                u_i = w_k / norm_wk
                ortho.append(u_i)
            

    return ortho