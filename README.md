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

 Results and Discussion

The Reduced Order Model (ROM) was constructed using Proper Orthogonal Decomposition (POD) applied to a 2D heat diffusion system.

 Key findings:

- The snapshot matrix was effectively compressed using Singular Value Decomposition (SVD).
- Only *2 POD modes* were required to capture *99% of the system energy*.
- The reduced model achieves a *relative reconstruction error of approximately 1.3%*, demonstrating high accuracy.

 Interpretation:

This indicates that the system dynamics are highly low-rank, meaning that the dominant behavior of the heat diffusion process can be represented in a very low-dimensional subspace.

 Scientific significance:

- Significant reduction in computational complexity
- Preservation of dominant physical dynamics
- Demonstrates feasibility of POD-based ROM for real-time simulation
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