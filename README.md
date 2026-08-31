### Reduced Order Modeling (POD) for 2D Heat Equation

## Overview

In this project, I solve a simple 2D heat equation using Python.

I first use a finite difference method to calculate the temperature over time.

Then I use POD (Proper Orthogonal Decomposition) and SVD (Singular Value Decomposition) to reduce the amount of data.

The main idea is to see if a small number of POD modes can represent the main temperature behavior.

--------------------------------------------------------------------------------------------------

```
The project contains:

- 2D heat equation solver
- Finite difference method
- POD using SVD
- Energy calculation
- Training with different diffusion values
- Testing with a new diffusion value
- Reconstruction error calculation
``` 

-------------------------------------------------------------------------------------------

## 1. Heat Equation

```
I use the following 2D heat equation:

dT/dt = alpha * (d2T/dx2 + d2T/dy2)

Where:

- "T" = temperature
- "t" = time
- "x" = x direction
- "y" = y direction
- "alpha" = diffusion coefficient
```

----------------------------------------------------------------------------------------------------------


## 2. Numerical Method

I use an explicit finite difference method.

```
The second derivative in the x direction is approximated by:

d2T/dx2 =
(T[i+1,j] - 2*T[i,j] + T[i-1,j]) / dx^2

The second derivative in the y direction is:

d2T/dy2 =
(T[i,j+1] - 2*T[i,j] + T[i,j-1]) / dy^2

Then I update the temperature using:

T_new[i,j] =
T[i,j] + alpha * dt * (d2T/dx2 + d2T/dy2)

This is the main numerical formula used in "heat_solver.py".
```

------------------------------------------------------------------------------------------


## 3. Numerical Settings

```
I use a 50 x 50 grid.

The numerical settings are:

dx = 1.0
dy = 1.0
dt = 0.1

Here:

- "dx" is the distance between grid points in the x direction.
- "dy" is the distance between grid points in the y direction.
- "dt" is the time step.

The simulation uses 100 time steps.

The boundary temperature stays at zero during the simulation.
```
--------------------------------------------------------------------------------------------


## 4. Initial Condition

```
The temperature starts at zero everywhere:

T = 0

I then put a hot square in the middle of the grid:

T[20:30, 20:30] = 1.0

So the middle part has temperature 1.0 and the rest of the grid starts at 0.0.

5. Training Data

I use three diffusion values for training:

alpha = 0.1
alpha = 0.5
alpha = 1.0

For each value, I generate temperature snapshots.

I then combine all training snapshots into one matrix.

This matrix is used to build one common POD basis.
```

-----------------------------------------------------------------------------------------------



## 6. POD and SVD

I use SVD to find the main patterns in the training data.

```
The SVD is:

X = U * S * V^T

Where:

- "X" = snapshot matrix
- "U" = POD spatial modes
- "S" = singular values
- "V^T" = time information

I subtract the mean temperature before calculating the SVD.
```

----------------------------------------------------------------------------------------------------


## 7. Energy

```
I calculate the energy of each singular value using:

energy[i] = S[i]^2 / sum(S[j]^2)

Then I calculate the cumulative energy:

cumulative_energy(k) =
energy[1] + energy[2] + ... + energy[k]

I choose the number of POD modes needed to keep at least 99% of the training energy.

For my results, I need:

3 POD modes

The first 3 modes contain about:

99.93% of the training energy
```

-----------------------------------------------------------------------------------------


## 8. Test Parameter

After building the POD basis, I test it using a new parameter that was not used during training.

```
The test parameter is:

alpha = 0.75

Training parameters:

0.1, 0.5, 1.0

Test parameter:

0.75

This allows me to check if the common POD basis can approximate the solution for a new parameter.
```

--------------------------------------------------------------------------------------------


## 9. Test Approximation

```
I first calculate the full solution for:

alpha = 0.75

Then I project the test solution onto the first 3 POD modes.

The Approximation is calculated using:

X_test_centered = X_test - X_mean

X_test_rec =
U_k * (U_k^T * X_test_centered) + X_mean

where "U_k" contains the first 3 POD modes.
```

----------------------------------------------------------------------


## 10. Error

I calculate the relative approximation error using:

```
Relative Error =
||X_test - X_test_rec|| / ||X_test||

For the unseen test parameter, I obtained:

Test relative error = 0.0068056

This is approximately: 0.68%
```

-----------------------------------------------------------------------------------------------------


## 11. Results

```
My final results are:

Training parameters = [0.1, 0.5, 1.0]

Test parameter = 0.75

Number of POD modes = 3

Training energy = 99.93%

Test relative error = 0.68%

Energy sum = approximately 1.0

Singular values decreasing = True

The results show that the common POD basis can represent the unseen test parameter with a small approximation error.
```

------------------------------------------------------------------------------------------------


## 12. Files

```
main.py

Runs the main POD study.

simulation/

Contains the heat equation solver.

pod/

Contains the POD and SVD functions.

analysis/

Contains the energy calculations.

results/

Contains saved results.
```

------------------------------------------------------------------------------------------------------



## Conclusion

```
In this project, I solve the 2D heat equation using a simple finite difference method.

I use three parameter values for training and build one common POD basis.

Then I test the basis using the unseen value "alpha = 0.75".

I need 3 POD modes to keep about 99.93% of the training energy.

The reconstruction error for the unseen test parameter is about 0.68%.

This shows that POD can reduce the amount of information while still giving a good approximation of the heat solution.
```