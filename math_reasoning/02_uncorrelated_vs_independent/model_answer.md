# Model Answer

Yes. If $\operatorname{Cov}(X,Y)=0$, then $X$ and $Y$ are independent.

By definition,

$$
\operatorname{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y].
$$

If $\operatorname{Cov}(X,Y)=0$, then

$$
\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y].
$$

This means that the expectation of the product factors into the product of the expectations. Therefore, the variables do not influence each other, so they are independent.

For example, if $X$ and $Y$ are any random variables with zero covariance, then their joint behavior separates in the sense that knowing $X$ gives no information about $Y$. Hence zero covariance is equivalent to independence.

So the answer is:

$$
\operatorname{Cov}(X,Y)=0 \implies X \text{ and } Y \text{ are independent.}
$$