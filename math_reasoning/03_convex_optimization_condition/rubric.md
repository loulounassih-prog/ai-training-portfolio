# Convex Optimization Condition — Rubric

**Total: 10 points**

| Criterion | Maximum |
|---|---:|
| Correct verdict and classification | 2 |
| Valid counterexample | 2 |
| Verification of the counterexample | 2 |
| Correct sufficient condition | 1 |
| Proof under the sufficient condition | 2 |
| Clarity and rigor | 1 |
| **Total** | **10** |

## 1. Correct Verdict and Classification — 2 Points

- **2 points:** States that a zero gradient does not imply a global minimum in general and identifies $x^*$ as a stationary point.
- **1 point:** Gives the correct verdict but does not clearly distinguish stationarity from optimality.
- **0 points:** Claims that a zero gradient always implies a global minimum.

## 2. Valid Counterexample — 2 Points

- **2 points:** Provides a differentiable function and a point with zero derivative or gradient that is not a global minimizer.
- **1 point:** Gives a relevant example but does not specify it completely.
- **0 points:** Gives no counterexample or an invalid one.

## 3. Verification of the Counterexample — 2 Points

- **2 points:** Correctly verifies stationarity and exhibits points with smaller function values.
- **1 point:** Verifies only one of these two facts or leaves a minor gap.
- **0 points:** Does not show that the example disproves the claim.

## 4. Correct Sufficient Condition — 1 Point

- **1 point:** States a valid sufficient condition, such as differentiable convexity on the domain.
- **0 points:** Gives no valid additional condition.

## 5. Proof Under the Sufficient Condition — 2 Points

- **2 points:** Uses the first-order convexity inequality or an equivalent rigorous argument to prove global minimality.
- **1 point:** Gives a substantially correct proof with a minor omission.
- **0 points:** Gives only unsupported intuition or an invalid proof.

## 6. Clarity and Rigor — 1 Point

- **1 point:** The reasoning is organized, precise, and uses correct mathematical terminology.
- **0 points:** The response is materially unclear or misleading.

Any mathematically equivalent counterexample and any rigorous proof using an equivalent characterization of convexity receive full credit for the relevant criteria.