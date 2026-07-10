# Uniform Convergence and Derivatives — Model Answer

Yes. Fix $x\in(-1,1)$ and take nonzero $h$ small enough that $x+h\in[-1,1]$. Uniform convergence gives

$$
\lim_{n\to\infty}
\frac{f_n(x+h)-f_n(x)}{h}
=
\frac{f(x+h)-f(x)}{h}.
$$

For each $n$, differentiability gives

$$
\lim_{h\to 0}
\frac{f_n(x+h)-f_n(x)}{h}
=
f_n'(x).
$$

Therefore we may take the limit in $n$ and then the limit in $h$ to obtain

$$
f'(x)
=
\frac{d}{dx}\left(\lim_{n\to\infty}f_n(x)\right).
$$

Then

$$
\frac{d}{dx}\left(\lim_{n\to\infty}f_n(x)\right)
=
\lim_{n\to\infty}f_n'(x)
=
g(x).
$$

Thus $f$ is differentiable and $f'=g$ on $[-1,1]$.