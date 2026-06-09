 POD Reduced Order Model (ROM) for 2D Heat Equation

 Abstract
This project implements a Reduced Order Model using Proper Orthogonal Decomposition (POD)
applied to a 2D heat diffusion system. The objective is to reduce computational cost
while preserving dominant dynamics.



 Methodology

The system is decomposed using Singular Value Decomposition (SVD):

X = U S V^T

A reduced basis is constructed using the most energetic modes that capture 99% of system energy.



 Results

- Number of modes used: 2
- Relative reconstruction error: ~1.3%
- Strong dimensionality reduction achieved



 Conclusion

The POD-ROM successfully captures the dominant behavior of the system with minimal loss of accuracy.
This demonstrates the efficiency of model order reduction techniques for scientific computing.



 Parametric POD-ROM Analysis

A parametric study was conducted by varying the diffusion coefficient a.

 Numerical Results:

| Alpha | Relative Error |
|------|---------------|
| 0.1  | 0.00158       |
| 0.5  | 0.01377       |
| 1.0  | 0.01954       |

 Discussion:

The results show that POD-ROM accuracy decreases with increasing diffusion intensity. This highlights the sensitivity of reduced-order bases to system parameters, motivating future work in parametric reduced order modeling (pROM).

 Author
Alaa Alomari