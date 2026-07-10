# Positive Definite Matrix — Reference Solution

Let $\lambda$ be an eigenvalue of $A$, and let $v\neq 0$ be a corresponding eigenvector. Then

$$
Av=\lambda v.
$$

Because $A$ is positive definite and $v$ is nonzero,

$$
v^T A v>0.
$$

Substituting the eigenvalue equation gives

$$
v^T A v
= v^T(\lambda v)
= \lambda v^T v
= \lambda\|v\|^2.
$$

Therefore,

$$
\lambda\|v\|^2>0.
$$

Since $v\neq 0$, we have $\|v\|^2>0$. Dividing by this positive quantity yields

$$
\lambda>0.
$$

Thus every eigenvalue of $A$ is strictly positive.

An equivalent proof may use the Rayleigh quotient

$$
\lambda=\frac{v^T A v}{v^T v}>0
$$

or the spectral theorem. These methods establish the same conclusion.