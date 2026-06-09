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


 Research Gap

Classical Proper Orthogonal Decomposition (POD) methods are widely used for Reduced Order Modeling of partial differential equations. However, most existing approaches assume a fixed parameter setting during the construction of the reduced basis.

This assumption limits the applicability of POD-ROM when dealing with systems that exhibit strong parametric dependency.

In particular, diffusion-driven systems such as the heat equation show significant variation in their solution structure as physical parameters change. Standard POD models trained at a single parameter value may fail to generalize across different regimes.

Therefore, there is a need for:

- Robust reduced-order models that remain accurate under parameter variation
- Systematic analysis of POD sensitivity to physical parameters
- Efficient strategies for constructing parameter-independent or adaptive reduced bases

This work addresses this gap by analyzing the behavior of POD-ROM accuracy under varying diffusion coefficients (a), providing insight into the limitations of classical POD and motivating future developments in parametric reduced order modeling (pROM).


 Conclusion

POD-based reduced order models provide efficient approximations of the heat equation, but their accuracy is sensitive to physical parameters. This motivates further research in parametric reduced order modeling (pROM).