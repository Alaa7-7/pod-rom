from simulation.heat_solver import heat_2d
from pod.svd import compute_svd, reconstruct
from analysis.energy import compute_energy, cumulative_energy
import numpy as np

alphas = [0.1, 0.5, 1.0]

print("Parametric POD-ROM Study")
print("------------------------")

for alpha in alphas:

    # 1. Generate data (FOM)
    X = heat_2d(alpha=alpha)

    # 2. SVD
    U, S, VT, X_mean = compute_svd(X)

    # 3. Energy analysis
    energy = compute_energy(S)
    cum_energy = cumulative_energy(S)

    # 4. Choose k automatically (99% energy)
    k = np.argmax(cum_energy >= 0.99) + 1

    # 5. Reconstruction
    X_rec = reconstruct(U, S, VT, k, X_mean)

    # 6. Error
    error = np.linalg.norm(X - X_rec) / np.linalg.norm(X)

    # 7. Full reconstruction check (important validation)
    X_full = reconstruct(U, S, VT, len(S), X_mean)
    full_error = np.linalg.norm(X - X_full)

    # ---------------- PRINT RESULTS ----------------
    print("\n===================================")
    print("alpha =", alpha)

    print("Singular values (first 5):", S[:5])
    print("Energy sum =", np.sum(energy))
    print("Cumulative last =", cum_energy[-1])
    print("k for 99% energy =", k)

    print("Relative error =", error)
    print("Full reconstruction error =", full_error)

    print("S decreasing =", np.all(np.diff(S) <= 0))
    print("===================================\n")
