# Reduced Order Modeling (POD-ROM) for 2D Heat Equation

## Overview

This project work a simple Reduced Order Model (ROM) using Proper Orthogonal Decomposition (POD) for solving the 2D heat equation.

The main idea is to reduce the size of the system while keeping the most important information from the solution.

## Keys

- 2D heat equation solver (finite difference)
- POD basis construction using SVD
- Energy-based mode selection
- Reconstruction of the solution using few modes
- Parametric study for different diffusion values (a)
- Error calculation between full and reduced models

## Physical Model

We solve the 2D heat equation:

dT/dt = a (d²T/dx² + d²T/dy²)

Where:
- T(x,y,t): temperature field
- a: diffusion coefficient

## Method

### 1. Full Model
We simulate the heat equation to generate snapshots of the solution over time.

### 2. Snapshot Matrix
The snapshots are stored in a matrix X.

## 3. Singular Value Decomposition (SVD)

We decompose the snapshot matrix as:

X = U S V?

Where:

- *X*: Snapshot matrix (data from the simulation)
- *U*: Spatial modes (POD modes)  
  ? They represent the main spatial patterns of the system
- *S (Sigma)*: Diagonal matrix of singular values  
  ? It represents the energy or importance of each mode
- *V?*: Temporal coefficients  
  ? It shows how each mode evolves over time

## Simple Interpretation

- U ? shapes of the solution (spatial structure)
- S ? importance of each shape (energy)
- V? ? evolution of these shapes over time

to extract dominant patterns.

### 4. POD Modes
We keep only the most important modes based on energy.

### 5. Reconstruction
We reconstruct the solution using a small number of modes.

## Results

### Energy

- Mode 1 ˜ 93%
- Mode 2 ˜ 6%
- Others are very small

### Main Observation

- Only 2 modes are enough to capture more than 99% of the energy
- The model works well with very small error

## Parametric Study

We tested different values of a:

- a = 0.1 ? error = 0.00158
- a = 0.5 ? error = 0.01377
- a = 1.0 ? error = 0.01954

### Observation:

- When a increases, the error increases slightly
- The reduced model still gives good results

## Files

- main.py ? full simulation pipeline
- simulation/ ? heat equation solver
- pod/ ? POD and SVD functions
- analysis/ ? energy calculations
- *.npy / *.csv ? saved results
- POD_ROM_Paper.pdf ? generated report

## Conclusion

This project shows that POD can reduce the size of the heat equation model while keeping good accuracy using only a few modes.

## Author

Alaa