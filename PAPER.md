 Reduced Order Modeling using POD for the 2D Heat Equation

 Abstract

This work presents a Reduced Order Modeling (ROM) framework based on Proper Orthogonal Decomposition (POD) applied to the 2D heat equation. The model reduces computational complexity while preserving dominant system dynamics.

 Methodology

The approach is based on:
- Snapshot generation from full-order simulations
- Singular Value Decomposition (SVD)
- Energy-based mode truncation
- POD reconstruction of the system

 Parametric Study

The model is tested under varying diffusion coefficients (alpha):

| Alpha | Relative Error |
|------|----------------|
| 0.1  | 0.00158        |
| 0.5  | 0.01377        |
| 1.0  | 0.01954        |

 Results

- Low diffusion regimes produce highly accurate reconstructions
- Error increases as system dynamics become more complex
- The first POD modes capture over 99% of system energy

 Conclusion

POD-based reduced order models provide efficient approximations of the heat equation, but their accuracy is sensitive to physical parameters. This motivates further research in parametric reduced order modeling (pROM).