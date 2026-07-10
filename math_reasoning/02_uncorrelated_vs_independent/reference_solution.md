# Uncorrelated vs Independent — Reference Solution

No. Zero covariance does not imply independence in general.

Let $X$ be uniformly distributed on $\{-1,0,1\}$, so

$$
\mathbb{P}(X=-1)
=
\mathbb{P}(X=0)
=
\mathbb{P}(X=1)
=
\frac{1}{3}.
$$

Define

$$
Y=X^2.
$$

## Zero Covariance

First,

$$
\mathbb{E}[X]
=(-1)\frac{1}{3}+0\frac{1}{3}+1\frac{1}{3}
=0.
$$

Since $Y=X^2$,

$$
\mathbb{E}[Y]
=\mathbb{E}[X^2]
=\frac{1}{3}+0+\frac{1}{3}
=\frac{2}{3}.
$$

Also, $XY=X^3$, so

$$
\mathbb{E}[XY]
=\mathbb{E}[X^3]
=-\frac{1}{3}+0+\frac{1}{3}
=0.
$$

Consequently,

$$
\operatorname{Cov}(X,Y)
=
\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]
=
0-0\cdot\frac{2}{3}
=
0.
$$

## Failure of Independence

Because $Y=X^2$, the event $\{Y=0\}$ is exactly the event $\{X=0\}$. Hence

$$
\mathbb{P}(X=0,Y=0)=\frac{1}{3}.
$$

But

$$
\mathbb{P}(X=0)\mathbb{P}(Y=0)
=
\frac{1}{3}\cdot\frac{1}{3}
=
\frac{1}{9}.
$$

Since $1/3\neq 1/9$, the joint probability does not factor, so $X$ and $Y$ are not independent.

Therefore,

$$
\operatorname{Cov}(X,Y)=0
$$

does not imply independence. The reverse implication is valid when the required expectations exist: independence implies $\operatorname{Cov}(X,Y)=0$.