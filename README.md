 Reduced Order Modeling (POD-ROM) for 2D Heat Equation

Overview

This project implements a Reduced Order Model (ROM) based on Proper Orthogonal Decomposition (POD) for the numerical approximation of the 2D heat equation.

The main objective is to demonstrate how a high-dimensional dynamical system can be efficiently represented using a low-dimensional basis while preserving the dominant energetic structures.



 Physical Model

We consider the 2D heat diffusion equation:

dT/dt = alpha * (d2T/dx2 + d2T/dy2)

where:
- T(x,y,t): temperature field
- alpha: diffusion coefficient

This system is diffusion-dominated, which makes it highly suitable for model reduction techniques.



 Methodology

 1. Full Order Model (FOM)
The system is solved numerically to generate snapshot data of the temperature field.

 2. Snapshot Matrix
The solution snapshots are arranged into a matrix:

X = [x1, x2, ..., xn]

 3. Singular Value Decomposition (SVD)
We apply SVD:

X = U S V^T

to extract dominant spatial structures.

 4. Proper Orthogonal Decomposition (POD)
The most energetic modes are selected to construct a reduced basis.

 5. Reduced Order Model (ROM)
The system is projected onto the reduced subspace for efficient reconstruction.



 Results

 Energy Analysis

- Mode 1: ~97.5% energy
- Mode 2: ~2.4% energy
- Remaining modes: negligible

 Key Findings

- Only 2 POD modes capture >99% of the system energy
- Relative reconstruction error ˜ 1.3%
- Strong exponential decay of singular values

 Compression Efficiency

The system is reduced from high dimensional space to 2 dominant modes, achieving significant computational reduction.



 Scientific Contribution

This work demonstrates the effectiveness of POD for reduced-order modeling of diffusion-dominated systems. The strong energy concentration in the first modes confirms that the system dynamics evolve on a low-dimensional manifold.



 Applications

- Computational Fluid Dynamics (CFD)
- Thermal systems
- Real-time simulation
- Control and optimization
- Scientific machine learning (SciML)

 Contribution

The main contribution of this work is the demonstration of an efficient POD-based reduced order model for diffusion-dominated systems, showing that:

- The system exhibits strong low-rank behavior
- A very small number of modes can accurately reconstruct the solution
- Energy is highly concentrated in the first singular modes

This makes the approach suitable for real-time simulation and large-scale computational problems.

 Future Work

- Extension to nonlinear PDEs (Navier-Stokes)
- POD-Galerkin projection
- Dynamic Mode Decomposition (DMD)
- Parametric ROM (pROM)



 Files

- main.py ? Full pipeline
- simulation/ ? Heat solver
- pod/ ? POD implementation
- analysis/ ? Energy analysis
- *.csv ? exported results
- *.npy ? numerical data
- POD_ROM_Paper.pdf ? generated paper



 Author

Alaa Alomari



 License

Academic and research use only.
