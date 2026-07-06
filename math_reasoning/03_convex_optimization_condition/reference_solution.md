# Reference Solution

No. The condition

$$
\nabla f(x^\*) = 0
$$

does not imply, in general, that $x^\*$ is a global minimizer of $f$.

It only says that $x^\*$ is a stationary point. A stationary point can be a local minimum, a local maximum, a saddle point, or neither.

## Counterexample

Consider the differentiable function

$$
f : \mathbb{R} \to \mathbb{R}, \qquad f(x) = x^3.
$$

Its derivative is

$$
f'(x) = 3x^2.
$$

At $x^\* = 0$, we have

$$
f'(0) = 0.
$$

So $0$ is a stationary point.

However, $0$ is not a global minimizer. Indeed, for every $x < 0$,

$$
f(x) = x^3 < 0 = f(0).
$$

Therefore, there are points with strictly smaller function value than $f(0)$.

In fact, $0$ is not even a local minimum, because values immediately to the left of $0$ are smaller than $f(0)$.

Thus, the condition $f'(0) = 0$ does not guarantee that $0$ is a local or global minimizer.

## Sufficient Condition: Convexity

A classical sufficient condition is convexity.

Assume that $f : \mathbb{R}^n \to \mathbb{R}$ is convex and differentiable. Then for all $x, y \in \mathbb{R}^n$, the first-order convexity inequality gives

$$
f(y) \geq f(x) + \nabla f(x)^T (y - x).
$$

Now take $x = x^\*$. Then for every $y \in \mathbb{R}^n$,

$$
f(y) \geq f(x^\*) + \nabla f(x^\*)^T (y - x^\*).
$$

If

$$
\nabla f(x^\*) = 0,
$$

then the inequality becomes

$$
f(y) \geq f(x^\*)
$$

for every $y \in \mathbb{R}^n$.

Therefore, $x^\*$ is a global minimizer of $f$.

## Final Statement

For a general differentiable function, a zero gradient is only a stationarity condition.

For a convex differentiable function, a zero gradient is sufficient to guarantee global optimality.