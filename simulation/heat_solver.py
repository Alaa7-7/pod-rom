import numpy as np

def heat_2d(nx=40, ny=40, nt=100, alpha=0.01):

    u = np.zeros((nx, ny))
    u[nx//2, ny//2] = 1.0

    snapshots = []

    for t in range(nt):

        u_new = u.copy()

        for i in range(1, nx-1):
            for j in range(1, ny-1):

                u_new[i, j] = u[i, j] + alpha * (
                    u[i+1, j] + u[i-1, j] +
                    u[i, j+1] + u[i, j-1] -
                    4 * u[i, j]
                )

        u = u_new

        if t % 5 == 0:
            snapshots.append(u.flatten())

    return np.array(snapshots).T
