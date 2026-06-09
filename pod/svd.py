import numpy as np

def compute_svd(X):
    X_mean = np.mean(X, axis=1, keepdims=True)
    X_centered = X - X_mean

    U, S, VT = np.linalg.svd(X_centered, full_matrices=False)

    return U, S, VT, X_mean


def reconstruct(U, S, VT, k, X_mean):
    U_k = U[:, :k]
    S_k = np.diag(S[:k])
    VT_k = VT[:k, :]

    X_rec = U_k @ S_k @ VT_k + X_mean

    return X_rec