import numpy as np

def compute_energy(S):
    energy = S**2 / np.sum(S**2)
    return energy