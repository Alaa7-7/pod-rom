import numpy as np


def heat_2d(alpha=1.0):
    nx, ny = 50, 50

    # Spatial and time steps
    dx = 1.0
    dy = 1.0
    dt = 0.1

    # Initial temperature
    T = np.zeros((nx, ny))
    T[20:30, 20:30] = 1.0

    snapshots = []

    # Time integration
    for t in range(100):
        T_new = T.copy()

        # Finite-difference solution of the 2D heat equation
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):

                d2T_dx2 = (
                    T[i + 1, j]
                    - 2 * T[i, j]
                    + T[i - 1, j]
                ) / dx**2

                d2T_dy2 = (
                    T[i, j + 1]
                    - 2 * T[i, j]
                    + T[i, j - 1]
                ) / dy**2

                T_new[i, j] = T[i, j] + alpha * dt * (
                    d2T_dx2 + d2T_dy2
                )

        T = T_new
        snapshots.append(T.flatten())

    return np.array(snapshots).T