import numpy as np

def get_pod_modes(U, k):
    """
    Extract first k POD modes
    """
    return U[:, :k]