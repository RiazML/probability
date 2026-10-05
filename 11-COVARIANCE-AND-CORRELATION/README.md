# Module 11: Covariance and Correlation

[Probability](../README.md) / Module 11

**Level:** 3 (Many Variables) · **Time:** about 1 week · **Importance:** ★★★★★

> **Big idea:** Covariance measures how two random variables move together, and the covariance matrix collects these numbers for a whole random vector so that one matrix rule describes the spread of any weighted sum.

---

## What You Will Learn

After this module you will be able to:

- Compute the covariance and the correlation of two random variables, and explain
  what their signs and sizes mean.
- Prove that the correlation is always between $-1$ and $1$, and that it equals
  $\pm 1$ only for a straight-line relation.
- Find the variance of a sum, a difference, a portfolio or an average, including
  all the covariance terms.
- Give examples of variables that are uncorrelated but still dependent.
- Build the mean vector and covariance matrix of a random vector, test whether a
  matrix can be a covariance matrix, and transform it with $A\Sigma A^{\top}$.
- Simulate correlated random numbers and check every formula with code.

## Before You Start

You should be comfortable with:

- [Module 06: Expectation, Variance and Moments](../06-EXPECTATION-VARIANCE-AND-MOMENTS/README.md):
  linearity of expectation, and variance as $E[X^2] - (E[X])^2$.
- [Module 10: Joint Distributions](../10-JOINT-DISTRIBUTIONS/README.md): joint
  PMFs and densities, marginals, and independence of random variables.
- A little matrix algebra (vectors, transpose, matrix product) for topics 11.5 to
  11.7. Each tool is explained briefly, with a $2 \times 2$ example, the first time
  it is used.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 11.1 | [Covariance](11.1-Covariance.md) | The average product of deviations: do X and Y move together? |
| 11.2 | [Correlation Coefficient](11.2-Correlation-Coefficient.md) | Covariance without units, always between -1 and 1 |
| 11.3 | [Variance of a Sum](11.3-Variance-of-a-Sum.md) | Variances add, plus twice every covariance |
| 11.4 | [Uncorrelated vs Independent](11.4-Uncorrelated-vs-Independent.md) | Zero covariance does not mean independent |
| 11.5 | [Random Vectors and Covariance Matrix](11.5-Random-Vectors-and-Covariance-Matrix.md) | All the variances and covariances in one matrix |
| 11.6 | [Covariance Matrix is PSD](11.6-Covariance-Matrix-is-PSD.md) | No weighted sum can have negative variance |
| 11.7 | [Linear Transformations](11.7-Linear-Transformations.md) | The mean and covariance of AX + b |
| 11.8 | [Practice Problems](11.8-Practice-Problems.md) | Mixed problems, proofs and projects for the whole module |

## Map of This Module

```text
                         11.1 Covariance
                        /       |       \
                       v        v        v
     11.2 Correlation    11.3 Variance    11.4 Uncorrelated
       (-1 to 1)          of a sum        vs independent
                        \       |
                         v      v
              11.5 Random vectors and covariance matrix
                                |
                                v
              11.6 The covariance matrix is PSD
                                |
                                v
              11.7 Linear transformations: A Σ Aᵀ
                                |
                                v
                     11.8 Practice problems
```

Start at the top. Each arrow means "you need this first". Topics 11.2, 11.3 and
11.4 can be read in any order after 11.1.

## Key Formulas

| Name | Formula |
|---|---|
| Covariance | $\operatorname{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - E[X]E[Y]$ |
| Bilinearity | $\operatorname{Cov}(aX + b, \thinspace cY + d) = ac \operatorname{Cov}(X, Y)$ |
| Correlation | $\rho = \frac{\operatorname{Cov}(X, Y)}{\sigma_X \sigma_Y}$, with $-1 \le \rho \le 1$ |
| Variance of a sum | $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2\operatorname{Cov}(X, Y)$ |
| Average of uncorrelated | $\operatorname{Var}(\bar{X}_n) = \frac{\sigma^2}{n}$ |
| Independent | $X \perp Y \implies \operatorname{Cov}(X, Y) = 0$ (not the other way) |
| Covariance matrix | $\Sigma = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^{\top}]$, $\Sigma_{ij} = \operatorname{Cov}(X_i, X_j)$ |
| Weighted sum | $\operatorname{Var}(\mathbf{a}^{\top}\mathbf{X}) = \mathbf{a}^{\top}\Sigma\mathbf{a} \ge 0$ |
| Linear map | $E[A\mathbf{X} + \mathbf{b}] = A\boldsymbol{\mu} + \mathbf{b}$, $\operatorname{Cov}(A\mathbf{X} + \mathbf{b}) = A\Sigma A^{\top}$ |

## Study Tips

- Learn **bilinearity** (11.1) until it is automatic. Almost every result in this
  module, from the variance of a sum to $A\Sigma A^{\top}$, is bilinearity applied
  carefully.
- Topics 11.5 to 11.7 look hard because of the matrices, but the probability is
  the same as in 11.1 to 11.3. Whenever a matrix formula confuses you, write it out
  for $2 \times 2$ and check it against the formulas you already know.
- The most important practice problems are the portfolio (11.3), the $Y = X^2$
  counterexample (11.4), and the three-variable matrix that is not PSD (11.6).
- Classic mistake: writing $\operatorname{Var}(X - Y) = \operatorname{Var}(X) - \operatorname{Var}(Y)$.
  Variances never subtract.
- Always plot or simulate before you believe a correlation. A correlation of 0 can
  hide a perfect curved relation.

## Where This Leads

- [Module 12: The Multivariate Gaussian](../12-MULTIVARIATE-GAUSSIAN/README.md) uses
  the mean vector and covariance matrix as its two parameters, and
  $A\Sigma A^{\top}$ to show that Gaussians stay Gaussian under linear maps.
- [Module 14: Conditional Expectation](../14-CONDITIONAL-EXPECTATION/README.md) and
  [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md) use the variance of
  sums and averages.
- [16.4 Cauchy-Schwarz Inequality](../16-INEQUALITIES-AND-CONCENTRATION/16.4-Cauchy-Schwarz-Inequality.md)
  gives a second proof that $\lvert \rho \rvert \le 1$.
- In AI and data science: PCA, whitening, Gaussian processes, Kalman filters and
  portfolio risk are all built on the covariance matrix.

---

[← Module 10](../10-JOINT-DISTRIBUTIONS/README.md) · [Syllabus](../SYLLABUS.md#module-11-covariance-and-correlation) · [Module 12 →](../12-MULTIVARIATE-GAUSSIAN/README.md)
