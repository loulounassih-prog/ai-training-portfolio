# Uniform Convergence and Derivatives — Reference Solution

No. Uniform convergence of $f_n$ and pointwise convergence of $f_n'$ do not guarantee that the limit is differentiable.

Define, for $x\in[-1,1]$,

$$
f_n(x)=\sqrt{x^2+\frac{1}{n}}.
$$

Each $f_n$ is differentiable on $[-1,1]$.

## Uniform Convergence of the Functions

For every $x\in[-1,1]$,

$$
\sqrt{x^2+\frac{1}{n}}\geq |x|.
$$

Rationalizing the difference gives

$$
0
\leq
\sqrt{x^2+\frac{1}{n}}-|x|
=
\frac{\frac{1}{n}}
{\sqrt{x^2+\frac{1}{n}}+|x|}.
$$

Because

$$
\sqrt{x^2+\frac{1}{n}}+|x|
\geq
\sqrt{\frac{1}{n}}
=
\frac{1}{\sqrt{n}},
$$

we obtain

$$
0
\leq
\sqrt{x^2+\frac{1}{n}}-|x|
\leq
\frac{1}{\sqrt{n}}.
$$

Hence

$$
\sup_{x\in[-1,1]}
\left|f_n(x)-|x|\right|
\leq
\frac{1}{\sqrt{n}}
\longrightarrow 0.
$$

Therefore $f_n\to f$ uniformly, where

$$
f(x)=|x|.
$$

## Pointwise Convergence of the Derivatives

Differentiating gives

$$
f_n'(x)
=
\frac{x}{\sqrt{x^2+\frac{1}{n}}}.
$$

If $x>0$, then

$$
f_n'(x)\longrightarrow \frac{x}{|x|}=1.
$$

If $x<0$, then

$$
f_n'(x)\longrightarrow \frac{x}{|x|}=-1.
$$

At $x=0$,

$$
f_n'(0)=0
$$

for every $n$. Thus $f_n'$ converges pointwise to

$$
g(x)=
\begin{cases}
-1, & x<0, \\
0, & x=0, \\
1, & x>0.
\end{cases}
$$

## Failure of Differentiability

The limit function $f(x)=|x|$ is not differentiable at $0$, because its one-sided difference quotients satisfy

$$
\lim_{h\downarrow 0}\frac{|h|-|0|}{h}=1
$$

and

$$
\lim_{h\uparrow 0}\frac{|h|-|0|}{h}=-1.
$$

Therefore the original claim is false.

## A Correct Theorem

Let $f_n\in C^1([a,b])$. Suppose that $f_n'$ converges uniformly on $[a,b]$ to a function $g$ and that $f_n(x_0)$ converges for at least one point $x_0\in[a,b]$. Then $f_n$ converges uniformly to a differentiable function $f$, and

$$
f'=g.
$$

Indeed, the fundamental theorem of calculus gives

$$
f_n(x)=f_n(x_0)+\int_{x_0}^{x}f_n'(t)\,dt.
$$

Uniform convergence of the derivatives permits passage to the limit in the integral, producing

$$
f(x)=c+\int_{x_0}^{x}g(t)\,dt,
$$

where $c=\lim_{n\to\infty}f_n(x_0)$. Consequently $f$ is differentiable and $f'=g$.

If $f_n\to f$ uniformly is already known, then $f_n(x_0)\to f(x_0)$ automatically, so uniform convergence of the derivatives is the additional condition needed in this standard theorem.