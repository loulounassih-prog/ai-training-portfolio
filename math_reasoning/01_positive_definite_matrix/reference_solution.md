# Positive Definite Matrix — Correct Solution

Let \(\lambda\) be an eigenvalue of \(A\), and let \(v \neq 0\) be an associated eigenvector.

By definition,

\[
Av = \lambda v.
\]

Since \(A\) is positive definite, we have

\[
v^T A v > 0.
\]

Using the eigenvalue equation,

\[
v^T A v = v^T(\lambda v).
\]

Because \(\lambda\) is a scalar,

\[
v^T(\lambda v) = \lambda v^T v.
\]

Therefore,

\[
v^T A v = \lambda v^T v.
\]

Since \(v \neq 0\),

\[
v^T v = \|v\|^2 > 0.
\]

So

\[
\lambda v^T v > 0.
\]

Because \(v^T v > 0\), we conclude that

\[
\lambda > 0.
\]

Thus, every eigenvalue of \(A\) is strictly positive.