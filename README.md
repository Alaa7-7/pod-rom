
 Reduced Order Modeling (POD-ROM) for 2D Heat Equation

 Overview

This project implements a *Proper Orthogonal Decomposition (POD)* based Reduced Order Model (ROM) for the numerical solution of the 2D heat equation.

The objective is to demonstrate how a high-dimensional dynamical system can be efficiently approximated using a low-dimensional representation while preserving the dominant energetic structures.



 Governing Equation

We consider the 2D heat diffusion equation:

?T/?t = a ( ?²T/?x² + ?²T/?y² )

where:
- T(x,y,t) is the temperature field
- a is the diffusion coefficient


 Methodology

 1. Full Order Model (FOM)
A high-dimensional numerical solver generates snapshot data of the temperature field.

 2. Snapshot Matrix
The solution snapshots are assembled into a matrix:

X = [x1, x2, ..., x?]

 3. Singular Value Decomposition (SVD)
We apply SVD:

X = U S V?

to extract dominant spatial modes.

 4. Proper Orthogonal Decomposition (POD)
A reduced basis is constructed using the leading modes corresponding to the highest energy contribution.

 5. Reduced Order Model (ROM)
The system is projected onto the reduced subspace for reconstruction.



 Energy Analysis

The energy content of each mode is computed as:

E? = s?² / S s?²

Results show that:

- Mode 1 ˜ 97.5% of total energy
- Mode 2 ˜ 2.4% of total energy
- Remaining modes are negligible

This confirms the *low-rank structure* of the system.



 Results

 Key Findings

- Only *2 POD modes* are sufficient to capture more than *99% of system energy*
- Relative reconstruction error ˜ *1.3%*
- Strong exponential decay in singular values

 Convergence Behavior

| Modes | Relative Error |
|------|----------------|
| 1    | High |
| 2    | ~1.3% |
| 3    | ~0.15% |
| 5    | ~0.001% |


 Computational Efficiency

Original system size:
- 1600 degrees of freedom

Reduced system:
- 2 POD modes

Reduction ratio:

1600 / 2 = 800× compression



 Files Structure

- main.py ? Main simulation pipeline
- simulation/heat_solver.py ? FOM solver
- pod/svd.py ? SVD & reconstruction
- analysis/energy.py ? Energy analysis
- energy_plot.csv ? Energy data
- svd_spectrum.csv ? Singular values
- *.npy ? Saved numerical results



 Scientific Significance

This work demonstrates the effectiveness of POD for model reduction in diffusion-dominated systems. The strong energy concentration in the first modes confirms that the system dynamics lie on a low-dimensional manifold.

This approach is widely used in:
- Computational Fluid Dynamics (CFD)
- Thermal systems
- Real-time simulation
- Control and optimization



 Future Work

- Extension to nonlinear systems
- POD-Galerkin projection
- Dynamic Mode Decomposition (DMD)
- Parametric ROM (pROM)
- Application to Navier-Stokes equations


 Author

Alaa Alomari



Academic and research use only.