# Model Answer

Yes. If $\nabla f(x^\*) = 0$, then $x^\*$ is a global minimizer of $f$.

The gradient gives the direction of steepest increase of the function. Therefore, if the gradient is zero at $x^\*$, the function has no direction in which it can decrease from that point. This means that $x^\*$ is an equilibrium point where the function stops decreasing.

More formally, for any direction $d$, the directional derivative at $x^\*$ is

$$
D f(x^\*)[d] = \nabla f(x^\*)^T d = 0.
$$

Since all directional derivatives are zero, moving away from $x^\*$ does not decrease the value of the function. Hence,

$$
f(y) \geq f(x^\*)
$$

for all $y \in \mathbb{R}^n$.

Therefore, $x^\*$ is a global minimizer of $f$.