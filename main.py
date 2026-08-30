from simulation.heat_solver import heat_2d
from pod.svd import compute_svd, reconstruct
from analysis.energy import compute_energy, cumulative_energy
import numpy as np


# Training parameters
training_alphas = [0.1, 0.5, 1.0]

# Unseen test parameter
test_alpha = 0.75

print("Parametric POD Study")
print("--------------------")

# 1. Generate training snapshots
training_snapshots = []

for alpha in training_alphas:
    X = heat_2d(alpha=alpha)
    training_snapshots.append(X)

# Combine all training snapshots
X_train = np.hstack(training_snapshots)

# 2. Compute one common POD basis
U, S, VT, X_mean = compute_svd(X_train)

# 3. Energy analysis
energy = compute_energy(S)
cum_energy = cumulative_energy(S)

# Choose number of modes for 99% energy
k = np.argmax(cum_energy >= 0.99) + 1

print("Training alphas =", training_alphas)
print("Test alpha =", test_alpha)
print("Number of POD modes =", k)
print("Cumulative energy =", cum_energy[k - 1])

# 4. Generate FOM solution for unseen parameter
X_test = heat_2d(alpha=test_alpha)

# 5. Reconstruct test solution using the common POD basis

X_test_centered = X_test - X_mean

U_k = U[:, :k]
X_test_rec = U_k @ (U_k.T @ X_test_centered) + X_mean

# 6. Calculate test error
error = np.linalg.norm(X_test - X_test_rec) / np.linalg.norm(X_test)

print("Test relative error =", error)

# 7. Basic POD checks
print("Energy sum =", np.sum(energy))
print("Singular values decreasing =", np.all(np.diff(S) <= 0))

# Save new results
np.savetxt(
    "results/test_result.csv",
    [[test_alpha, k, cum_energy[k - 1], error]],
    delimiter=",",
    header="test_alpha,modes,cumulative_energy,test_error",
    comments=""
)

np.savetxt(
    "results/energy_modes.csv",
    energy,
    delimiter=","
)

np.savetxt(
    "results/energy_cumulative.csv",
    cum_energy,
    delimiter=","
)

print("New results saved in results/")