# PhD Research Proposal

## Title
Reduced Order Modeling for Diffusion Systems using POD

---

### 1. Motivation
Many physical systems are described by partial differential equations (PDEs) like the heat equation. Solving these equations is often slow and expensive when the system size is large.

So we need simpler models that can give good results with less computation.

---

### 2. Problem Statement
The main problem is how to reduce the size of large systems while keeping the most important information from the solution.

We also want the reduced model to stay accurate for different parameter values.

---

### 3. Background
Proper Orthogonal Decomposition (POD) and Singular Value Decomposition (SVD) are common methods used to reduce the size of complex systems.

They work by finding the most important patterns in the data.

---

### 4. Research Gap
Most POD methods use fixed rules to choose the number of modes.

But in some cases, especially when parameters change, this may not give the best accuracy.

---

### 5. Proposed Contribution
- Build a simple POD-based reduced order model
- Use energy to choose the important modes automatically
- Test the method on the 2D heat equation
- Study how the model behaves for different diffusion values
- Show that a small number of modes can still give good accuracy (over 99% energy)

---

### 6. Future Work
- Apply the method to more complex equations like Navier-Stokes
- Use Dynamic Mode Decomposition (DMD)
- Extend the model to parametric reduced order systems