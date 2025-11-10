# RW Heat Solver

**RW Heat Solver** (Random–Walk Heat Solver) is a simple Python re-implementation of the 1-D **heat diffusion equation** using a *Monte Carlo random-walk* method.  
It simulates how heat spreads over time by moving many small “globs” of heat in random directions, then reconstructing the resulting temperature field.

---

## Overview

The **heat equation** models how temperature changes in space and time:
\[
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
\]
where:
- \(u(x,t)\) is the temperature,  
- \(\alpha\) is the diffusion coefficient (how quickly heat spreads).

Instead of solving this with calculus, this program uses a **stochastic approach**:
1. Represent the initial temperature as many discrete particles (“globs”).
2. Each glob moves a small random distance at every time step.
3. The new positions are collected into bins to rebuild the temperature field.
4. Repeating this process gradually smooths out sharp gradients — just like real diffusion.

This random-walk approach provides an intuitive and visual way to understand diffusion, showing how random motion can lead to the same smooth results predicted by the analytical PDE solution.

---


