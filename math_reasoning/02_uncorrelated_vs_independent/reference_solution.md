# Reference Solution

The statement is false in general.

Zero covariance means that two random variables have no linear correlation. Independence is a much stronger condition.

We give a counterexample.

Let $X$ be uniformly distributed on $\{-1,0,1\}$. Therefore,

$$
\mathbb{P}(X=-1)=\mathbb{P}(X=0)=\mathbb{P}(X=1)=\frac{1}{3}.
$$

Define

$$
Y=X^2.
$$

Then $Y$ takes values in $\{0,1\}$.

More precisely:

$$
Y=0 \iff X=0,
$$

and

$$
Y=1 \iff X \in \{-1,1\}.
$$

So,

$$
\mathbb{P}(Y=0)=\frac{1}{3}
$$

and

$$
\mathbb{P}(Y=1)=\frac{2}{3}.
$$

## Step 1: Show that $X$ and $Y$ are not independent

Since $Y=X^2$, the value of $Y$ is completely determined by the value of $X$.

We can verify non-independence directly.

Consider the event $\{X=0\}$ and the event $\{Y=0\}$.

We have:

$$
\mathbb{P}(X=0)=\frac{1}{3}
$$

and

$$
\mathbb{P}(Y=0)=\frac{1}{3}.
$$

Also, since $Y=0$ exactly when $X=0$,

$$
\mathbb{P}(X=0, Y=0)=\frac{1}{3}.
$$

If $X$ and $Y$ were independent, we would have:

$$
\mathbb{P}(X=0, Y=0)=\mathbb{P}(X=0)\mathbb{P}(Y=0).
$$

But

$$
\mathbb{P}(X=0)\mathbb{P}(Y=0)
=
\frac{1}{3}\cdot\frac{1}{3}
=
\frac{1}{9}.
$$

Therefore,

$$
\mathbb{P}(X=0, Y=0)=\frac{1}{3}\neq \frac{1}{9}.
$$

So $X$ and $Y$ are not independent.

## Step 2: Compute the covariance

By definition,

$$
\operatorname{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y].
$$

First compute $\mathbb{E}[X]$:

$$
\mathbb{E}[X]
=
(-1)\frac{1}{3}+0\frac{1}{3}+1\frac{1}{3}
=
0.
$$

Next compute $\mathbb{E}[Y]$.

Since $Y=X^2$,

$$
\mathbb{E}[Y]
=
\mathbb{E}[X^2].
$$

Thus,

$$
\mathbb{E}[Y]
=
(-1)^2\frac{1}{3}+0^2\frac{1}{3}+1^2\frac{1}{3}
=
\frac{2}{3}.
$$

Now compute $\mathbb{E}[XY]$.

Since $Y=X^2$,

$$
XY=X \cdot X^2=X^3.
$$

Therefore,

$$
\mathbb{E}[XY]
=
\mathbb{E}[X^3].
$$

So,

$$
\mathbb{E}[XY]
=
(-1)^3\frac{1}{3}+0^3\frac{1}{3}+1^3\frac{1}{3}
=
-\frac{1}{3}+0+\frac{1}{3}
=
0.
$$

Therefore,

$$
\operatorname{Cov}(X,Y)
=
0 - 0 \cdot \frac{2}{3}
=
0.
$$

## Conclusion

We have constructed random variables $X$ and $Y$ such that:

$$
\operatorname{Cov}(X,Y)=0,
$$

but $X$ and $Y$ are not independent.

Therefore,

$$
\operatorname{Cov}(X,Y)=0 \not\implies X \text{ and } Y \text{ are independent.}
$$

The correct implication is the other way around: if $X$ and $Y$ are independent and the relevant expectations exist, then

$$
\operatorname{Cov}(X,Y)=0.
$$