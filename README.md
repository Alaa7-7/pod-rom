 POD Reduced Order Model (ROM) for 2D Heat Equation

 Overview
This project implements a Reduced Order Model (ROM) using Proper Orthogonal Decomposition (POD) applied to a 2D heat diffusion problem.

The goal is to reduce the computational complexity of high-dimensional simulations while preserving the dominant dynamics of the system.

--

 Methodology

 1. Full Order Model (FOM)
The system is generated using a numerical solver for the 2D heat equation, producing a snapshot matrix of the solution over time.

 2. Proper Orthogonal Decomposition (POD)
Singular Value Decomposition (SVD) is applied to the snapshot matrix:

\[
X = U \Sigma V^T
\]

The most energetic modes are extracted based on cumulative energy criteria.

 3. Reduced Order Model (ROM)
The system is reconstructed using only the dominant POD modes:

\[
X_{ROM} = U_k \Sigma_k V_k^T
\]

--

 Features

- Snapshot generation from 2D heat equation
- SVD-based POD decomposition
- Energy-based mode selection (99% threshold)
- Low-rank reconstruction
- Error analysis between full and reduced model

--

 Results

- Number of modes used: ~2 (depending on energy threshold)
- Relative reconstruction error: ~1.3%
- Significant dimensionality reduction achieved


 Project Structure

--

 Technologies

- Python 3.8
- NumPy
- (Optional) Matplotlib for visualization

--

 Author

Alaa7-7

--

 License

This project is for academic and research purposes.