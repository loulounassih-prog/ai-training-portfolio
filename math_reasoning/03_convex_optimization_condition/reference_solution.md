# Convex Optimization Condition — Reference Solution

No. The condition

$$
\nabla f(x^*)=0
$$

only states that $x^*$ is a stationary point. A stationary point may be a local minimum, a local maximum, a saddle point, or none of these.

## Counterexample

Let

$$
f:\mathbb{R}\to\mathbb{R},
\qquad
f(x)=x^3.
$$

Then

$$
f'(x)=3x^2,
$$

so $f'(0)=0$. However, for every $x<0$,

$$
f(x)=x^3<0=f(0).
$$

Hence $0$ is not a global minimizer. It is not even a local minimizer because negative values of $x$ arbitrarily close to $0$ have smaller function values.

## Sufficient Condition

Assume instead that $f:\mathbb{R}^n\to\mathbb{R}$ is convex and differentiable. The first-order characterization of convexity states that for all $x,y\in\mathbb{R}^n$,

$$
f(y)\geq f(x)+\nabla f(x)^T(y-x).
$$

Set $x=x^*$. If $\nabla f(x^*)=0$, then for every $y$,

$$
f(y)
\geq
f(x^*)+\nabla f(x^*)^T(y-x^*)
=
f(x^*).
$$

Therefore $x^*$ is a global minimizer.

Thus stationarity alone is insufficient, while stationarity together with differentiable convexity is sufficient for global optimality.