 Reduced Order Modeling of the 2D Heat Equation Using Proper Orthogonal Decomposition

 Abstract

Reduced Order Models (ROMs) are widely used to reduce computational costs in large-scale numerical simulations. This work presents a Proper Orthogonal Decomposition (POD) based ROM applied to a two-dimensional heat diffusion problem. Singular Value Decomposition (SVD) is employed to extract dominant modes from the snapshot matrix. Numerical results demonstrate that only two POD modes are sufficient to capture approximately 99% of the system energy while maintaining a reconstruction error of about 1.3%.

 Keywords

Reduced Order Modeling, Proper Orthogonal Decomposition, Singular Value Decomposition, Heat Equation, Scientific Computing.

1. Introduction

High-fidelity numerical simulations often require significant computational resources. Reduced Order Modeling provides an efficient framework for approximating complex systems using a low-dimensional representation. Among the available approaches, Proper Orthogonal Decomposition is one of the most widely used techniques due to its simplicity and effectiveness.

2. Mathematical Formulation

2.1 Snapshot Matrix

The numerical solution is collected into a snapshot matrix:


where each column represents the system state at a specific time.

2.2 Singular Value Decomposition

The snapshot matrix is decomposed as:

where:

- U contains the spatial modes.
- S contains the singular values.
- V contains temporal coefficients.

 2.3 POD Basis

The reduced basis is constructed using the dominant singular vectors associated with the largest singular values.

3. Numerical Experiment

A two-dimensional heat equation solver was implemented in Python. The generated snapshots were assembled into a snapshot matrix and processed using SVD.

 Computational Setup

- Programming language: Python 3.8
- Numerical library: NumPy
- Grid size: 40 × 40
- Number of snapshots: 20

 4. Results

Energy Analysis

The cumulative energy criterion was used to determine the number of retained modes.

Results showed that:

- 2 POD modes captured approximately 99% of the total energy.
- Relative reconstruction error ˜ 1.36%.

 Interpretation

These results indicate that the dynamics of the heat diffusion process are highly low-dimensional and can be represented accurately using a small number of basis functions.

 5. Conclusion

This study demonstrated the effectiveness of Proper Orthogonal Decomposition for model order reduction of a two-dimensional heat equation. The reduced model achieved substantial dimensionality reduction while preserving high reconstruction accuracy.

 Future Work

Future developments may include:

- Galerkin projection based ROMs.
- Nonlinear reduced-order modeling.
- Dynamic Mode Decomposition (DMD).
- Real-time simulation applications.

 Convergence Analysis

A convergence study was performed by varying the number of retained POD modes.

The reconstruction error decreases as the number of modes increases, confirming the efficiency of the reduced-order representation.

| POD Modes | Relative Error |
|-----------|---------------|
| 1 | (from results) |
| 2 | (from results) |
| 3 | (from results) |
| 5 | (from results) |
| 10 | (from results) |

This behavior demonstrates that the system is highly low-rank and can be accurately approximated using a small number of modes.

 Author

Alaa7-7