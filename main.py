from simulation.heat_solver import heat_2d
from pod.svd import compute_svd, reconstruct
from analysis.energy import compute_energy

import numpy as np
# import matplotlib.pyplot as plt

# 1. Full Order Model
X = heat_2d()

# 2. POD decomposition
U, S, VT, X_mean = compute_svd(X)

# 3. Energy analysis
E = compute_energy(S)

# 4. Find number of modes for 99% energy
cumulative = 0
k = 0

for i, e in enumerate(E):
    cumulative += e
    if cumulative >= 0.99:
        k = i + 1
        break

print("Modes used:", k)

# 5. Reconstruction
X_rec = reconstruct(U, S, VT, k, X_mean)

# 6. Relative error
error = np.linalg.norm(X - X_rec) / np.linalg.norm(X)

print("Relative reconstruction error:", error)

# ==================================================
# 7. Visual comparison
# ==================================================

snapshot_id = 10

