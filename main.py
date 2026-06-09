from simulation.heat_solver import heat_2d
from pod.svd import compute_svd, reconstruct
from analysis.energy import compute_energy

import numpy as np
# import matplotlib.pyplot as plt

# 1. Full Order Model
X = heat_2d()

# 2. POD decomposition
U, S, VT, X_mean = compute_svd(X)
# Save Singular Values for plotting
np.savetxt("svd_spectrum.csv", S, delimiter=",")

print("SVD spectrum saved.")

from analysis.energy import compute_energy, cumulative_energy

energy = compute_energy(S)
cum_energy = cumulative_energy(S)

print("\nEnergy Analysis")
print("----------------")

for i, e in enumerate(energy):
    print(f"Mode {i+1}: Energy = {e:.4f}")

print("\nCumulative Energy:")
for i, e in enumerate(cum_energy):
    print(f"Modes {i+1}: {e:.4f}")

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

print("\nConvergence Study")
print("-----------------")

for k in [1, 2, 3, 5, 10]:
    if k <= len(S):

        X_rec_k = reconstruct(U, S, VT, k, X_mean)

        error_k = np.linalg.norm(X - X_rec_k) / np.linalg.norm(X)

        print(f"Modes = {k:2d} | Error = {error_k:.6f}")


# ==================================================
# 7. Visual comparison
# ==================================================

snapshot_id = 10

import numpy as np

np.save("X_original.npy", X)
np.save("X_reconstructed.npy", X_rec)

print("Data saved: X_original.npy and X_reconstructed.npy")

np.save("energy_modes.npy", energy)
np.save("energy_cumulative.npy", cum_energy)

print("\nEnergy data saved.")
