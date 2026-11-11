# Module 13: Functions of Random Variables

[Probability](../README.md) / Module 13

**Level:** 3 (Many Variables) · **Time:** about 1 week · **Importance:** ★★★☆☆

> **Big idea:** If you know the distribution of $X$ (or of several variables), you can find the distribution of anything computed from it, such as $X^2$, $X + Y$ or $\max(X, Y)$, by asking which inputs produce each output and adding up their probability.

---

## What You Will Learn

After this module you will be able to:

- Find the distribution of $g(X)$ with the CDF method, for any function $g$.
- Use the change-of-variables formula in one dimension, including functions that fold the
  line, and in two dimensions with a Jacobian determinant.
- Compute the distribution of a sum of independent variables by convolution, and use the
  short list of families that stay in the family when added.
- Derive the distributions of the maximum, the minimum and the $k$-th smallest of a sample,
  and show that sorted uniforms are Beta.
- Explain and implement the Box-Muller transform, and check every result with a simulation.

## Before You Start

You should be comfortable with:

- [Module 08: Continuous Random Variables](../08-CONTINUOUS-RANDOM-VARIABLES/README.md):
  the link between a CDF and a density ([8.4](../08-CONTINUOUS-RANDOM-VARIABLES/8.4-CDF-and-PDF-Relationship.md)),
  and the one-variable change of variables for a monotone function
  ([8.8](../08-CONTINUOUS-RANDOM-VARIABLES/8.8-Change-of-Variables.md)).
- [Module 09: Continuous Distributions](../09-CONTINUOUS-DISTRIBUTIONS/README.md): the uniform,
  normal, exponential, Gamma and Beta distributions, used in almost every example.
- [Module 10: Joint Distributions](../10-JOINT-DISTRIBUTIONS/README.md): joint densities,
  double integrals over a region, and independence.
- [Module 12: The Multivariate Gaussian](../12-MULTIVARIATE-GAUSSIAN/README.md): only for
  context; Box-Muller makes the standard normals that 12.4 turns into correlated ones.

A $2 \times 2$ determinant and partial derivatives are needed in 13.3. Both are explained
there the first time they appear.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 13.1 | [CDF Method](13.1-CDF-Method.md) | Turn the event $g(X) \le y$ into an event about $X$, then take the slope |
| 13.2 | [Change of Variables 1D](13.2-Change-of-Variables-1D.md) | The density formula, with one term for each $x$ that gives the same $y$ |
| 13.3 | [Jacobian Multivariate Change of Variables](13.3-Jacobian-Multivariate-Change-of-Variables.md) | In 2-D the density changes by the area factor $\lvert \det J \rvert$ |
| 13.4 | [Convolution Sums of Random Variables](13.4-Convolution-Sums-of-Random-Variables.md) | The distribution of $X + Y$: add up every way to split the total |
| 13.5 | [Sums of Known Distributions](13.5-Sums-of-Known-Distributions.md) | Poisson, binomial, normal and Gamma sums stay in the family |
| 13.6 | [Max and Min](13.6-Max-and-Min.md) | The slowest of many tasks and the weakest link: products of CDFs |
| 13.7 | [Order Statistics](13.7-Order-Statistics.md) | The $k$-th smallest value; sorted uniforms are Beta |
| 13.8 | [Box-Muller Transform](13.8-Box-Muller-Transform.md) | Two uniforms become two independent standard normals |
| 13.9 | [Practice Problems](13.9-Practice-Problems.md) | Mixed problems, proofs and simulation projects for the whole module |

## Map of This Module

```text
              8.8 Change of variables (monotone, from Module 08)
                                 |
                                 v
                  13.1 CDF method  (the master tool)
                 /               |                \
                v                v                 v
     13.2 Change of       13.4 Convolution     13.6 Max and min
     variables 1D                |                   |
          |                      v                   v
          v               13.5 Sums of known   13.7 Order statistics
     13.3 Jacobian (2-D)       distributions
          |
          v
     13.8 Box-Muller
                \                |                 /
                 +---------------+----------------+
                                 |
                                 v
                      13.9 Practice problems
```

Start with 13.1; the three branches (change of variables, sums, sorting) can then be read
in any order. Each arrow means "you need this first".

## Key Formulas

| Name | Formula |
|---|---|
| CDF method | $F_Y(y) = P(g(X) \le y)$, then $f_Y(y) = F_Y'(y)$ |
| Change of variables, 1D | $f_Y(y) = \sum_{x : \thinspace g(x) = y} f_X(x) / \lvert g'(x) \rvert$ |
| Jacobian, n-D | $f_{\mathbf{Y}}(\mathbf{y}) = f_{\mathbf{X}}(g^{-1}(\mathbf{y})) \thinspace \lvert \det J_{g^{-1}}(\mathbf{y}) \rvert$ |
| 2 by 2 determinant | $\det$ of rows $(a, b)$ and $(c, d)$ is $ad - bc$; polar coordinates give $r$ |
| Convolution | $f_{X+Y}(z) = \int f_X(x) f_Y(z - x) \thinspace dx$ for independent $X, Y$ |
| Poisson sum | $\text{Pois}(\lambda_1) + \text{Pois}(\lambda_2) = \text{Pois}(\lambda_1 + \lambda_2)$ (independent) |
| Normal sum | $\mathcal{N}(\mu_1, \sigma_1^2) + \mathcal{N}(\mu_2, \sigma_2^2) = \mathcal{N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ (independent) |
| Gamma sum | $\text{Gamma}(\alpha_1, \beta) + \text{Gamma}(\alpha_2, \beta) = \text{Gamma}(\alpha_1 + \alpha_2, \beta)$ (same rate) |
| Max of $n$ i.i.d. | $F_{\max}(x) = F(x)^n$ |
| Min of $n$ i.i.d. | $F_{\min}(x) = 1 - (1 - F(x))^n$ |
| $k$-th order statistic | $f_{(k)}(x) = \frac{n!}{(k-1)!(n-k)!} F(x)^{k-1} f(x) (1 - F(x))^{n-k}$ |
| Sorted uniforms | $U_{(k)} \sim \text{Beta}(k, n - k + 1)$, mean $\frac{k}{n + 1}$ |
| Box-Muller | $Z_1 = \sqrt{-2 \ln U_1} \cos(2\pi U_2)$, $Z_2 = \sqrt{-2 \ln U_1} \sin(2\pi U_2)$ |

## Study Tips

- Learn the CDF method (13.1) really well. Every other formula in this module is a
  shortcut for it, and it is what you fall back on when a shortcut does not apply.
- The hardest topic is 13.3 (the Jacobian). Do the polar coordinates calculation and
  Example 3 (sum and share of two exponentials) by hand until the steps feel routine:
  invert, take the determinant, substitute, read off the support.
- In convolution problems, most mistakes are wrong limits. Draw both supports on one line
  and see where they overlap for each $z$.
- Classic traps: adding standard deviations instead of variances, forgetting a root of
  $g(x) = y$, and using $1 - F(x)^n$ for the minimum. Each topic's Common Mistakes section
  lists them.
- The most important problems: the triangle density of two uniforms (13.4), the minimum
  of exponentials (13.6), the Beta order statistics (13.7) and the one-step Jacobian proof
  of Box-Muller (13.8, Practice 5).

## Where This Leads

- [Module 14: Conditional Expectation](../14-CONDITIONAL-EXPECTATION/README.md) studies the
  average of $Y$ once $X$ is known, which is itself a function $g(X)$ of a random variable.
- [Module 15: Generating Functions](../15-GENERATING-FUNCTIONS/README.md) turns convolutions
  into products, giving much shorter proofs of the sums in 13.5.
- [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md): the Central Limit Theorem
  explains why repeated convolution always drifts toward a bell curve.
- [Module 19: Simulation and Monte Carlo](../19-SIMULATION-AND-MONTE-CARLO/README.md) uses
  transformations like Box-Muller, the inverse transform and rejection to generate random
  numbers.
- In AI and computer science: normalizing flows (the Jacobian rule), diffusion models
  (sums of Gaussian noise), latency percentiles and straggler tasks (order statistics and
  maxima), and every random number generator for non-uniform distributions.

---

[← Module 12](../12-MULTIVARIATE-GAUSSIAN/README.md) · [Syllabus](../SYLLABUS.md#module-13-functions-of-random-variables) · [Module 14 →](../14-CONDITIONAL-EXPECTATION/README.md)
