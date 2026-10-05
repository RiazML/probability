# Module 09: Continuous Distributions

[Probability](../README.md) / Module 09

**Level:** 2 (Random Variables) · **Time:** about 2 weeks · **Importance:** ★★★★★

> **Big idea:** A small family of continuous distributions, each with its own story, describes waiting times, measurements, proportions, lifetimes and extremes, and most of them are built from each other.

---

## What You Will Learn

After this module you will be able to:

- Explain the story behind each major continuous distribution and choose the
  right one for a problem.
- Compute probabilities, means, variances and quantiles for the uniform,
  normal, exponential, Gamma, Beta and their relatives.
- Derive means and variances with integrals, the Gamma function and the
  Beta function.
- Prove key facts such as memorylessness, "a sum of exponentials is Gamma"
  and "the Cauchy has no mean".
- Tell light tails from heavy tails, and explain why it matters for risk.
- Simulate every distribution in numpy with the correct parameters.

## Before You Start

You should be comfortable with:

- [Module 08: Continuous Random Variables](../08-CONTINUOUS-RANDOM-VARIABLES/README.md):
  PDFs, CDFs, expectation with integrals, LOTUS and change of variables.
- [Module 07: Discrete Distributions](../07-DISCRETE-DISTRIBUTIONS/README.md): the
  Poisson, geometric and binomial, which are the discrete partners of the
  exponential, Gamma and Beta.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 9.1 | [Uniform](9.1-Uniform.md) | Every value in an interval equally likely; the source of all random numbers |
| 9.2 | [Normal (Gaussian)](9.2-Normal-Gaussian.md) | The bell curve; standardization, z-scores, the 68-95-99.7 rule |
| 9.3 | [Exponential](9.3-Exponential.md) | Waiting time for the next event; memoryless |
| 9.4 | [Gamma](9.4-Gamma.md) | Waiting time for the n-th event; the Gamma function |
| 9.5 | [Beta](9.5-Beta.md) | A distribution over a probability |
| 9.6 | [Chi-Square, Student's t and F](9.6-Chi-Square-Student-t-and-F.md) | Distributions built from squared and divided normals |
| 9.7 | [Laplace](9.7-Laplace.md) | Two exponentials back to back; L1 penalties and privacy noise |
| 9.8 | [Log-Normal](9.8-Log-Normal.md) | Products of many small effects; prices, incomes, latency |
| 9.9 | [Cauchy](9.9-Cauchy.md) | A bell curve with no mean |
| 9.10 | [Logistic and Gumbel](9.10-Logistic-and-Gumbel.md) | The sigmoid as a CDF, and the distribution of maximums |
| 9.11 | [Weibull](9.11-Weibull.md) | Lifetimes whose risk falls, stays flat or rises with age |
| 9.12 | [Dirichlet](9.12-Dirichlet.md) | A distribution over probability vectors |
| 9.13 | [Heavy vs Light Tails](9.13-Heavy-vs-Light-Tails.md) | How fast extremes become rare, and why it matters |
| 9.14 | [Practice Problems](9.14-Practice-Problems.md) | Mixed problems and simulation projects for the whole module |

## Map of This Module

```text
  9.1 Uniform  (inverse transform turns it into any distribution)
      |
      v
  9.3 Exponential --- add n ---> 9.4 Gamma --- ratio ---> 9.5 Beta
      |                             |                       |
      |                             | shape k/2, rate 1/2   | K categories
      |                             v                       v
      |                     9.6 Chi-square, t, F      9.12 Dirichlet
      |                             ^
      |                             | squares and ratios
      |                             |
      |                       9.2 Normal --- exp ---> 9.8 Log-Normal
      |                             |
      |                             +--- ratio of two ---> 9.9 Cauchy
      |
      +--- difference of two ---> 9.7 Laplace
      +--- power ---------------> 9.11 Weibull
      +--- minus log, maximum --> 9.10 Logistic and Gumbel

  All of them ---> 9.13 Heavy vs Light Tails ---> 9.14 Practice Problems
```

Two "parents" generate almost everything: the exponential (waiting) and the
normal (adding up). Each arrow names the operation that builds the next
distribution.

## Key Formulas

| Name | Formula |
|---|---|
| Uniform $\text{Unif}(a, b)$ | $f(x) = \frac{1}{b - a}$, mean $\frac{a + b}{2}$, variance $\frac{(b - a)^2}{12}$ |
| Normal $\mathcal{N}(\mu, \sigma^2)$ | $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-(x - \mu)^2/(2\sigma^2)}$, $P(X \le x) = \Phi(\frac{x - \mu}{\sigma})$ |
| Exponential $\text{Exp}(\lambda)$, rate $\lambda$ | $P(X \gt x) = e^{-\lambda x}$, mean $\frac{1}{\lambda}$, variance $\frac{1}{\lambda^2}$ |
| Gamma $\text{Gamma}(\alpha, \beta)$, rate $\beta$ | $f(x) = \frac{\beta^{\alpha}}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}$, mean $\frac{\alpha}{\beta}$, variance $\frac{\alpha}{\beta^2}$ |
| Gamma function | $\Gamma(\alpha) = \int_0^{\infty} x^{\alpha - 1} e^{-x} dx$, $\Gamma(n) = (n - 1)!$, $\Gamma(\frac{1}{2}) = \sqrt{\pi}$ |
| Beta $\text{Beta}(\alpha, \beta)$ | $f(x) = \frac{x^{\alpha - 1}(1 - x)^{\beta - 1}}{B(\alpha, \beta)}$, mean $\frac{\alpha}{\alpha + \beta}$ |
| Chi-square | $Z_1^2 + \dots + Z_k^2 \sim \chi^2_k = \text{Gamma}(\frac{k}{2}, \frac{1}{2})$, mean $k$, variance $2k$ |
| Log-normal | $\ln X \sim \mathcal{N}(\mu, \sigma^2)$, mean $e^{\mu + \sigma^2/2}$, median $e^{\mu}$ |
| Weibull $\text{Weibull}(k, \lambda)$, scale $\lambda$ | $P(X \gt x) = e^{-(x/\lambda)^k}$, mean $\lambda\Gamma(1 + \frac{1}{k})$ |
| Gumbel $\text{Gumbel}(\mu, \beta)$ | $F(x) = \exp(-e^{-(x - \mu)/\beta})$, mean $\mu + 0.5772\beta$ |
| Pareto tail | $P(X \gt x) = (\frac{x_m}{x})^{\alpha}$; moments finite only below order $\alpha$ |

## Study Tips

- **Always state the parameterization.** In this book the exponential and Gamma
  use a **rate** and the normal's second parameter is the **variance**. numpy's
  `exponential` and `gamma` take a **scale** $= \frac{1}{\text{rate}}$, and `normal` takes the
  standard deviation. Most wrong answers in this module come from this.
- **Learn the stories, not just the formulas.** "Waiting for the next event",
  "waiting for the n-th event", "a probability you are unsure about", "the
  biggest of many": each story points to one distribution.
- **Master the Gamma function trick** in [9.4](9.4-Gamma.md). The key integral
  $\int_0^{\infty} x^{a - 1} e^{-\beta x} dx = \frac{\Gamma(a)}{\beta^a}$ gives the moments of the Gamma,
  Beta, chi-square, t and Weibull.
- The hardest topics are [9.6](9.6-Chi-Square-Student-t-and-F.md) and
  [9.13](9.13-Heavy-vs-Light-Tails.md). Run their simulations and change the
  parameters until the results feel natural.
- In [9.14](9.14-Practice-Problems.md), do problems C1, C2, H1 and project P2:
  together they connect the exponential, Poisson and Gamma.

## Where This Leads

- [Module 10: Joint Distributions](../10-JOINT-DISTRIBUTIONS/README.md) puts several
  of these variables together, and uses the Beta and Gamma as priors in Bayes.
- [Module 12: The Multivariate Gaussian](../12-MULTIVARIATE-GAUSSIAN/README.md)
  extends the normal to vectors.
- [Module 13: Functions of Random Variables](../13-FUNCTIONS-OF-RANDOM-VARIABLES/README.md)
  proves the sums and ratios used here (convolution and Jacobians).
- [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md) explains why the normal
  appears everywhere, and what goes wrong with heavy tails.
- In AI and machine learning these distributions are everywhere: normal and
  uniform weight initialization, the sigmoid (logistic), Gumbel-softmax,
  Beta and Dirichlet priors, Laplace (L1) regularization and Student-t noise.

---

[← Module 08](../08-CONTINUOUS-RANDOM-VARIABLES/README.md) · [Syllabus](../SYLLABUS.md#module-09-continuous-distributions) · [Module 10 →](../10-JOINT-DISTRIBUTIONS/README.md)
