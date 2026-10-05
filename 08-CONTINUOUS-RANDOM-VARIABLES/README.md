# Module 08: Continuous Random Variables

[Probability](../README.md) / Module 08

**Level:** 2 (Random Variables) · **Time:** about 1 week · **Importance:** ★★★★★

> **Big idea:** When a variable can take any value in a range, probability is no longer a list of numbers but an area under a curve called the density.

---

## What You Will Learn

After this module you will be able to:

- Explain what a density is, why single values have probability 0, and why a density
  can be larger than 1.
- Compute probabilities as areas, and move between the density and the CDF.
- Compute the mean, the variance and $E[g(X)]$ with integrals.
- Find medians and percentiles, and use the quantile function to simulate any
  distribution from uniform random numbers.
- Find the density of a transformed variable $g(X)$.
- Handle mixed variables that have both lumps of probability and a density part.

## Before You Start

You should be comfortable with:

- [Module 05: Discrete Random Variables](../05-DISCRETE-RANDOM-VARIABLES/README.md):
  random variables, the PMF and the CDF.
- [Module 06: Expectation, Variance and Moments](../06-EXPECTATION-VARIANCE-AND-MOMENTS/README.md):
  the mean, the variance, LOTUS and quantiles for discrete variables.
- [Module 07: Discrete Distributions](../07-DISCRETE-DISTRIBUTIONS/README.md): named
  distributions, to compare with their continuous cousins.
- **Basic calculus:** an integral is the area under a curve, and a derivative is a
  slope. Topic 8.1 gives a one-minute reminder of integrals, and 8.4 of derivatives.
  That is all the calculus this module needs.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 8.1 | [Probability Density Function](8.1-Probability-Density-Function.md) | Probability is the area under a curve |
| 8.2 | [Why Point Probabilities are Zero](8.2-Why-Point-Probabilities-are-Zero.md) | One exact value has no width, so it has probability 0 |
| 8.3 | [Densities Can Exceed One](8.3-Densities-Can-Exceed-One.md) | A density is probability per unit length, not a probability |
| 8.4 | [CDF and PDF Relationship](8.4-CDF-and-PDF-Relationship.md) | The CDF is the area so far; the density is its slope |
| 8.5 | [Expectation and Variance with Integrals](8.5-Expectation-and-Variance-with-Integrals.md) | The mean and the variance, with integrals in place of sums |
| 8.6 | [LOTUS for Continuous](8.6-LOTUS-for-Continuous.md) | The mean of g(X) without finding the density of g(X) |
| 8.7 | [Quantile Function](8.7-Quantile-Function.md) | The inverse CDF: medians, percentiles and simulation |
| 8.8 | [Change of Variables](8.8-Change-of-Variables.md) | The density of g(X) for a monotone g |
| 8.9 | [Mixed Distributions](8.9-Mixed-Distributions.md) | Lumps of probability plus a density part |
| 8.10 | [Practice Problems](8.10-Practice-Problems.md) | Mixed problems and simulation projects for the whole module |

## Map of This Module

```text
                  8.1 Density: probability = area
                 /               |               \
                v                v                v
       8.2 Points have     8.3 Densities     8.4 CDF <-> density
       probability 0       can exceed 1        /      |       \
                                              v       v        v
                                 8.5 Mean and   8.7 Quantile   8.8 Change of
                                 variance       function       variables
                                      |
                                      v
                                 8.6 LOTUS
                                      |
                                      v
                  8.9 Mixed distributions (uses everything above)
                                      |
                                      v
                          8.10 Practice problems
```

Start at the top. Each arrow means "you need this first"; 8.2 and 8.3 are short and
mostly about how to think.

## Key Formulas

| Name | Formula |
|---|---|
| Probability as area | $P(a \le X \le b) = \int_a^b f_X(x) \thinspace dx$ |
| Density rules | $f_X(x) \ge 0$ and $\int_{-\infty}^{\infty} f_X(x) \thinspace dx = 1$ |
| Single points | $P(X = c) = 0$ |
| CDF from density | $F_X(x) = \int_{-\infty}^{x} f_X(t) \thinspace dt$ |
| Density from CDF | $f_X(x) = F_X'(x)$ |
| Mean | $E[X] = \int x \thinspace f_X(x) \thinspace dx$ |
| Variance | $\operatorname{Var}(X) = E[X^2] - (E[X])^2$ |
| LOTUS | $E[g(X)] = \int g(x) \thinspace f_X(x) \thinspace dx$ |
| Quantile | $Q_X(u) = F_X^{-1}(u)$, so $P(X \le Q_X(u)) = u$ |
| Inverse transform | if $U$ is uniform on $[0, 1]$, then $Q_X(U)$ has the distribution of $X$ |
| Change of variables | $f_Y(y) = f_X(g^{-1}(y)) \cdot \left\lvert \frac{d}{dy} g^{-1}(y) \right\rvert$ for monotone $g$ |
| Mixed variable | $E[h(X)] = \sum_i h(a_i) \thinspace p_i + \int h(x) \thinspace g(x) \thinspace dx$ |

## Study Tips

- **Write the support first.** Most mistakes in this module are wrong limits of
  integration. Before you integrate, write down where the density is not zero.
- **Think "area", not "height".** A density value is never a probability. Whenever you
  want a probability, ask "area over which interval?"
- 8.8 (change of variables) is the hardest topic. Always derive it through the CDF
  first; the formula is just the CDF method plus the chain rule. Do not forget the
  absolute value.
- Check every answer with a few lines of numpy, as in the "Simulate It" sections. A
  simulation catches a missing factor of 2 in seconds.
- The most important practice problems are C2, C4 and H1 in
  [8.10](8.10-Practice-Problems.md): they combine densities, CDFs, LOTUS and change of
  variables.

## Where This Leads

- [Module 09: Continuous Distributions](../09-CONTINUOUS-DISTRIBUTIONS/README.md)
  applies these tools to the uniform, normal, exponential, gamma, beta and other famous
  densities.
- [Module 10: Joint Distributions](../10-JOINT-DISTRIBUTIONS/README.md) extends
  densities to two or more variables, with double integrals.
- [Module 13: Functions of Random Variables](../13-FUNCTIONS-OF-RANDOM-VARIABLES/README.md)
  generalizes the change of variables to many variables.
- In AI and machine learning, densities appear in likelihoods, generative models,
  normalizing flows and every loss defined on continuous data.

---

[← Module 07](../07-DISCRETE-DISTRIBUTIONS/README.md) · [Syllabus](../SYLLABUS.md#module-08-continuous-random-variables) · [Module 09 →](../09-CONTINUOUS-DISTRIBUTIONS/README.md)
