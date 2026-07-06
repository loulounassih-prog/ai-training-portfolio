# Rubric

Total: 10 points

## 1. Correctly identifies that the implication is false: 2 points

- 2 points: Clearly states that $\nabla f(x^\*) = 0$ does not imply that $x^\*$ is a global minimizer in general.
- 1 point: Suggests that the implication may fail, but the statement is unclear or incomplete.
- 0 points: Claims that zero gradient always implies a global minimum.

## 2. Provides a valid counterexample: 2 points

- 2 points: Gives a correct differentiable counterexample, such as $f(x) = x^3$ with $x^\* = 0$.
- 1 point: Provides an example that is relevant but incomplete or not fully justified.
- 0 points: Provides no counterexample or an invalid counterexample.

## 3. Explains why the counterexample disproves the claim: 1.5 points

- 1.5 points: Correctly computes the derivative or gradient and shows that the stationary point is not a global minimizer.
- 1 point: Gives the right intuition but misses part of the verification.
- 0 points: Does not explain why the example disproves the claim.

## 4. Distinguishes stationary points from minima: 1 point

- 1 point: Clearly explains that a zero gradient only identifies a stationary point, not necessarily a local or global minimum.
- 0.5 points: Mentions stationarity but does not explain the distinction clearly.
- 0 points: Does not distinguish stationarity from optimality.

## 5. States a correct additional sufficient condition: 1 point

- 1 point: Correctly states that convexity plus differentiability is sufficient.
- 0.5 points: Mentions convexity but in a vague or incomplete way.
- 0 points: Gives no sufficient condition or gives an incorrect one.

## 6. Proves the convex case correctly: 1.5 points

- 1.5 points: Uses the first-order convexity inequality

$$
f(y) \geq f(x^\*) + \nabla f(x^\*)^T (y - x^\*)
$$

and correctly concludes that $f(y) \geq f(x^\*)$ for all $y$.
- 1 point: Gives a mostly correct proof but omits some details.
- 0.5 points: Provides only intuition for the convex case.
- 0 points: Gives no proof or an incorrect proof.

## 7. Clarity and rigor: 1 point

- 1 point: The answer is clear, logically structured, and mathematically precise.
- 0.5 points: The answer is mostly understandable but lacks precision or structure.
- 0 points: The answer is unclear, misleading, or poorly organized.