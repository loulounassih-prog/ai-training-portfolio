# Uncorrelated vs Independent — Model Answer

Yes. By definition,

$$
\operatorname{Cov}(X,Y)
=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y].
$$

If $\operatorname{Cov}(X,Y)=0$, then

$$
\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y].
$$

Thus the expectation of the product factors into the product of the expectations. This means that the joint behavior separates, so knowing $X$ gives no information about $Y$. Therefore $X$ and $Y$ are independent. Hence zero covariance is equivalent to independence.