# Module 12: The Multivariate Gaussian

[Probability](../README.md) / Module 12

**Level:** 3 (Many Variables) · **Time:** about 1.5 weeks · **Importance:** ★★★★☆

> **Big idea:** The multivariate Gaussian is the one many-dimensional distribution that stays Gaussian under linear maps, marginals and conditioning, so its questions have exact answers written with a mean vector and a covariance matrix.

---

## What You Will Learn

After this module you will be able to:

- Write and evaluate the PDF of a multivariate normal, starting with the 2-D case.
- Draw its contour ellipses from the eigenvectors and eigenvalues of $\Sigma$.
- Measure how unusual a point is with the Mahalanobis distance and the chi-square law.
- Sample correlated Gaussians with the Cholesky trick, $\mathbf{X} = \boldsymbol{\mu} + L\mathbf{Z}$.
- Compute the distribution of linear maps, marginals, conditionals and sums of Gaussians.
- Explain why, for jointly Gaussian variables, uncorrelated means independent.

## Before You Start

You should be comfortable with:

- [Module 09: Continuous Distributions](../09-CONTINUOUS-DISTRIBUTIONS/README.md): the 1-D normal $\mathcal{N}(\mu, \sigma^2)$ and z-scores.
- [Module 10: Joint Distributions](../10-JOINT-DISTRIBUTIONS/README.md): joint, marginal and conditional densities, independence.
- [Module 11: Covariance and Correlation](../11-COVARIANCE-AND-CORRELATION/README.md): the covariance matrix and the rule $\operatorname{Cov}(A\mathbf{X}) = A\Sigma A^\top$.

A little matrix algebra is used: $2 \times 2$ determinants and inverses,
eigenvectors and the Cholesky factor. Each tool is explained, with a
$2 \times 2$ example, the first time it is needed.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 12.1 | [PDF of the Multivariate Normal](12.1-PDF-of-the-Multivariate-Normal.md) | The bell-shaped hill in many dimensions, and where its formula comes from |
| 12.2 | [Geometry and Contours](12.2-Geometry-and-Contours.md) | Equal-density curves are ellipses set by the eigenvectors of $\Sigma$ |
| 12.3 | [Mahalanobis Distance](12.3-Mahalanobis-Distance.md) | Distance in units of the data's own spread; its square is chi-square |
| 12.4 | [Standard Normal Vectors and Cholesky](12.4-Standard-Normal-Vectors-and-Cholesky.md) | Build any Gaussian from independent standard normals |
| 12.5 | [Affine Transformations](12.5-Affine-Transformations.md) | $A\mathbf{X} + \mathbf{b}$ of a Gaussian is Gaussian |
| 12.6 | [Marginals](12.6-Marginals.md) | Any part of a Gaussian vector is Gaussian: just read it off |
| 12.7 | [Conditionals](12.7-Conditionals.md) | Observing some entries leaves a Gaussian with a shifted mean and smaller variance |
| 12.8 | [Uncorrelated Implies Independent](12.8-Uncorrelated-Implies-Independent.md) | For jointly Gaussian variables, zero covariance means independence |
| 12.9 | [Sums of Gaussians](12.9-Sums-of-Gaussians.md) | Independent normals add: means add, variances add |
| 12.10 | [Bivariate Normal](12.10-Bivariate-Normal.md) | The 2-D case in full, with $\rho$, regression to the mean and quadrant probabilities |
| 12.11 | [Practice Problems](12.11-Practice-Problems.md) | Mixed problems and simulation projects for the whole module |

## Map of This Module

```text
                 12.1 PDF of the multivariate normal
                    /              |              \
                   v               v               v
     12.2 Contours (eigen)  12.3 Mahalanobis   12.4 Z and Cholesky
                   \               ^               |
                    \______________|               v
                                         12.5 Affine maps stay Gaussian
                                         /        |         \
                                        v         v          v
                               12.6 Marginals  12.9 Sums  12.8 Uncorrelated
                                        |                     = independent
                                        v
                               12.7 Conditionals
                                        |
                                        v
                         12.10 Bivariate normal in detail
                                        |
                                        v
                            12.11 Practice problems
```

Start at the top. Each arrow means "you need this first"; 12.5 is the hub
that most later topics use.

## Key Formulas

| Name | Formula |
|---|---|
| PDF | $f(\mathbf{x}) = (2\pi)^{-d/2} (\det \Sigma)^{-1/2} \exp\left( -\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^\top \Sigma^{-1} (\mathbf{x} - \boldsymbol{\mu}) \right)$ |
| Contours | axes along eigenvectors $\mathbf{q}_i$ of $\Sigma$, half-lengths $c\sqrt{\lambda_i}$ |
| Mahalanobis | $D^2(\mathbf{x}) = (\mathbf{x} - \boldsymbol{\mu})^\top \Sigma^{-1} (\mathbf{x} - \boldsymbol{\mu}) \sim \chi^2(d)$ |
| Sampling | $\mathbf{X} = \boldsymbol{\mu} + L\mathbf{Z}$, $\Sigma = LL^\top$, $\mathbf{Z} \sim \mathcal{N}(\mathbf{0}, I)$ |
| Affine | $A\mathbf{X} + \mathbf{b} \sim \mathcal{N}(A\boldsymbol{\mu} + \mathbf{b}, A\Sigma A^\top)$ |
| Marginal | $\mathbf{X}_1 \sim \mathcal{N}(\boldsymbol{\mu}_1, \Sigma_{11})$ |
| Conditional mean | $\boldsymbol{\mu}_1 + \Sigma_{12}\Sigma_{22}^{-1}(\mathbf{x}_2 - \boldsymbol{\mu}_2)$ |
| Conditional covariance | $\Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ |
| Independence | jointly Gaussian: $\mathbf{X}_1 \perp \mathbf{X}_2 \iff \Sigma_{12} = \mathbf{0}$ |
| Sum | $X + Y \sim \mathcal{N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ for independent normals |
| Bivariate prediction | $E[Y \mid X = x] = \mu_Y + \rho \frac{\sigma_Y}{\sigma_X}(x - \mu_X)$ |

## Study Tips

- Always work the 2-D case with real numbers first, then read the matrix
  formula as "the same thing with blocks". Every topic is written this way.
- 12.5 (affine maps) is the key: marginals, sums and the proof of
  conditionals all reduce to it. Make sure you can compute $A\Sigma A^\top$ by hand.
- 12.7 (conditionals) is the hardest and the most used in AI. Do Examples 1
  and 2 on paper, then check them with the simulation.
- The classic trap: two normal variables are not automatically **jointly**
  normal. Remember the counterexample $Y = SX$ from 12.6.
- Practice problems C5 and H3 in 12.11 show the ideas working together; they
  matter most.

## Where This Leads

- [Module 13: Functions of Random Variables](../13-FUNCTIONS-OF-RANDOM-VARIABLES/README.md)
  gives the change-of-variables rule used to derive the PDF, and the
  Box-Muller method for making standard normals.
- [Module 14: Conditional Expectation](../14-CONDITIONAL-EXPECTATION/README.md)
  generalizes the linear conditional mean of 12.7 to any distribution.
- [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md): the
  multivariate CLT says sums of random vectors become multivariate Gaussian.
- In AI and computer science: Gaussian processes, Kalman filters, PCA,
  Gaussian mixture models, VAEs and diffusion models are all built on this
  module ([21.1 AI and Machine Learning](../21-APPLICATIONS-OF-PROBABILITY/21.1-AI-and-Machine-Learning/README.md)).

---

[← Module 11](../11-COVARIANCE-AND-CORRELATION/README.md) · [Syllabus](../SYLLABUS.md#module-12-the-multivariate-gaussian) · [Module 13 →](../13-FUNCTIONS-OF-RANDOM-VARIABLES/README.md)
