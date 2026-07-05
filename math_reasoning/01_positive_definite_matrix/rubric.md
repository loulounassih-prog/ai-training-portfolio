# Positive Definite Matrix — Rubric

Total: 10 points

This rubric evaluates whether the answer correctly proves that every eigenvalue of a real symmetric positive definite matrix is strictly positive.

## 1. Correct use of positive definiteness — 2 points

The answer should correctly use the definition of positive definiteness:

$$
x^T A x > 0
$$

for every nonzero vector $x$.

Full credit requires recognizing that positive definiteness is a condition on the quadratic form, not on the individual entries of the matrix.

## 2. Correct use of an eigenpair — 2 points

The answer should introduce an eigenvalue $\lambda$ and a nonzero eigenvector $v$ such that

$$
Av = \lambda v.
$$

The proof should apply positive definiteness to this eigenvector.

## 3. Valid algebraic derivation — 2 points

The answer should derive

$$
v^T A v = \lambda v^T v.
$$

This step must follow from the eigenvalue equation $Av = \lambda v$.

## 4. Correct positivity argument — 2 points

The answer should use the fact that $v \neq 0$, so

$$
v^T v > 0.
$$

From

$$
v^T A v = \lambda v^T v > 0,
$$

the answer should correctly conclude that

$$
\lambda > 0.
$$

## 5. Mathematical rigor and clarity — 2 points

The answer should be logically valid and avoid false or vague claims.

Common mistakes include claiming that:

- positive definite matrices must have only positive entries;
- entrywise positivity is equivalent to positive definiteness;
- eigenvalues are positive because the matrix sends vectors in a “positive direction”;
- the conclusion follows from geometric intuition without proof.

A complete answer should be concise, rigorous, and based on the quadratic form definition.