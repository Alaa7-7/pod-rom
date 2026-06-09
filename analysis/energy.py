import numpy as np

def compute_energy(S):
    energy = S**2
    return energy / np.sum(energy)


def cumulative_energy(S):
    energy = compute_energy(S)
    return np.cumsum(energy)