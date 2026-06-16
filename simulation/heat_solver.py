import numpy as np

def heat_2d(alpha=1.0):
    nx, ny = 50, 50
    T = np.zeros((nx, ny))

    # initial condition
    T[20:30, 20:30] = 1.0

    snapshots = []

    for t in range(100):
        T_new = T.copy()

        for i in range(1, nx-1):
            for j in range(1, ny-1):
                lap = (
                    T[i+1,j] + T[i-1,j] +
                    T[i,j+1] + T[i,j-1] -
                    4*T[i,j]
                )

                T_new[i,j] = T[i,j] + alpha * 0.1 * lap

        T = T_new
        snapshots.append(T.flatten())

    return np.array(snapshots).T