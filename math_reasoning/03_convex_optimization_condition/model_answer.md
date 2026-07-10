# Convex Optimization Condition — Model Answer

Yes. If $\nabla f(x^*)=0$, then $x^*$ is a global minimizer of $f$. The gradient gives the direction of steepest increase, so a zero gradient means there is no direction in which the function can decrease.

More formally, for every direction $d$,

$$
Df(x^*)[d]=\nabla f(x^*)^T d=0.
$$

Since every directional derivative is zero, moving away from $x^*$ cannot decrease the function. Therefore,

$$
f(y)\geq f(x^*)
$$

for every $y\in\mathbb{R}^n$, and $x^*$ is a global minimizer.