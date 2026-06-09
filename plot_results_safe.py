import numpy as np

alphas = [0.1, 0.5, 1.0]
errors = [0.00158, 0.01377, 0.01954]

np.savetxt(
    "alpha_vs_error.csv",
    np.column_stack((alphas, errors)),
    delimiter=",",
    header="alpha,error",
    comments=""
)

print("CSV file generated: alpha_vs_error.csv")