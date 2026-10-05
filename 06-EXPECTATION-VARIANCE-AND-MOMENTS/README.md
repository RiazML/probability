# Module 06: Expectation, Variance and Moments

[Probability](../README.md) / Module 06

**Level:** 2 (Random Variables) · **Time:** about 1.5 weeks · **Importance:** ★★★★★

> **Big idea:** A few numbers summarize a random variable: the expected value is its long-run average and balance point, the variance measures its spread (its risk), and higher moments, medians and quantiles describe its shape.

---

## What You Will Learn

After this module you will be able to:

- Compute the expected value of a discrete random variable and explain it as a long-run
  average.
- Use linearity of expectation and indicator variables to find the mean of a complicated
  count in a few lines, without independence.
- Compute $E[g(X)]$ with LOTUS, and explain why $E[g(X)]$ is usually not $g(E[X])$.
- Compute variances and standard deviations, and predict how they change under shifting
  and scaling.
- Describe the shape of a distribution with skewness, kurtosis, the median, the mode and
  quantiles.
- Prove that the mean is the best guess under squared error and the median under absolute
  error, and check every result with a simulation.

This module works with **discrete** random variables, where averages are sums. The same
ideas carry over to continuous variables in
[Module 08](../08-CONTINUOUS-RANDOM-VARIABLES/README.md), where the sums become integrals.

## Before You Start

You should be comfortable with:

- [Module 05: Discrete Random Variables](../05-DISCRETE-RANDOM-VARIABLES/README.md): random
  variables as functions, the PMF, the CDF, indicator variables and functions $g(X)$.
- [Module 03: Axioms of Probability](../03-AXIOMS-OF-PROBABILITY/README.md): the rules that every
  probability follows, such as $P(A^c) = 1 - P(A)$.
- [Module 02: Counting](../02-COUNTING/README.md): binomial coefficients like $\binom{n}{2}$, for
  counting pairs.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 6.1 | [Expected Value](6.1-Expected-Value.md) | The probability-weighted average of the values, and the long-run average |
| 6.2 | [Linearity of Expectation](6.2-Linearity-of-Expectation.md) | The mean of a sum is the sum of the means, even for dependent variables |
| 6.3 | [LOTUS](6.3-LOTUS.md) | The mean of $g(X)$ straight from the PMF of $X$ |
| 6.4 | [Indicator Trick](6.4-Indicator-Trick.md) | Write a count as a sum of 0/1 variables, then add probabilities |
| 6.5 | [Variance and Standard Deviation](6.5-Variance-and-Standard-Deviation.md) | How far a value typically lands from the mean |
| 6.6 | [Properties of Variance](6.6-Properties-of-Variance.md) | Shifting changes nothing, scaling by $a$ multiplies the variance by $a^2$ |
| 6.7 | [Moments, Skewness and Kurtosis](6.7-Moments-Skewness-and-Kurtosis.md) | Higher powers describe lopsidedness and heavy tails |
| 6.8 | [Median, Mode and Quantiles](6.8-Median-Mode-and-Quantiles.md) | The middle value, the most likely value, and percentiles |
| 6.9 | [Tail-Sum Formula](6.9-Tail-Sum-Formula.md) | The mean of a counting variable as a sum of tail probabilities |
| 6.10 | [Expectation as Best Guess](6.10-Expectation-as-Best-Guess.md) | Mean, median and mode are the best guesses for three losses |
| 6.11 | [Practice Problems](6.11-Practice-Problems.md) | Mixed problems, proofs and simulation projects for the whole module |

## Map of This Module

```text
                          6.1 Expected value
                                  |
          +-----------------------+------------------------+
          v                       v                        v
   6.2 Linearity             6.3 LOTUS              6.8 Median, mode
          |                       |                   and quantiles
          v                       v                        |
   6.4 Indicator trick       6.5 Variance and SD           |
          |                  /    |          \             |
          v                 v     v           v            v
   6.9 Tail-sum       6.6 Shift   6.7 Moments,   6.10 Expectation
       formula        and scale   skewness,      as best guess
                                  kurtosis
                                     |
                                     v
                      6.11 Practice problems (all topics)
```

Start at the top. Each arrow means "you need this first"; 6.10 needs both the variance
(6.5) and the median (6.8).

## Key Formulas

| Name | Formula |
|---|---|
| Expected value | $E[X] = \sum_x x \thinspace p(x)$ |
| Linearity (always) | $E[aX + bY + c] = aE[X] + bE[Y] + c$ |
| LOTUS | $E[g(X)] = \sum_x g(x) \thinspace p(x)$ |
| Indicator | $E[I_A] = P(A)$ |
| Variance | $\operatorname{Var}(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2$ |
| Standard deviation | $\sigma = \sqrt{\operatorname{Var}(X)}$ |
| Shift and scale | $\operatorname{Var}(aX + b) = a^2 \operatorname{Var}(X)$ |
| Standardization | $Z = (X - \mu)/\sigma$ has mean 0 and variance 1 |
| Skewness | $E[(X - \mu)^3] / \sigma^3$ |
| Kurtosis | $E[(X - \mu)^4] / \sigma^4$ |
| Quantile | $Q(q) = \min \lbrace x : F(x) \ge q \rbrace$ |
| Tail sum ($X$ in $0, 1, 2, \dots$) | $E[X] = \sum_{k \ge 1} P(X \ge k)$ |
| Best guess | $E[(X - c)^2] = \operatorname{Var}(X) + (\mu - c)^2$, smallest at $c = \mu$ |

## Study Tips

- Linearity (6.2) and the indicator trick (6.4) are the most powerful ideas here, and the
  least obvious. When a question asks "how many, on average?", look for indicators first.
  Work through every example in 6.4 until the method feels automatic.
- Keep $E[X^2]$ and $(E[X])^2$ apart in your head. Their difference is the variance, and mixing
  them up is the most common mistake in this module.
- Never push $E$ inside a non-linear function: $E[g(X)] \ne g(E[X])$ in general. Linear
  functions are the only safe case.
- Do the proofs in Challenge H1 and H2 of [6.11](6.11-Practice-Problems.md) yourself. They use
  almost every tool of the module.
- Run the simulations. Seeing a running average settle near $E[X]$ makes the definitions
  real.

## Where This Leads

- [Module 07: Discrete Distributions](../07-DISCRETE-DISTRIBUTIONS/README.md) uses linearity and
  indicators to find the means and variances of the binomial, geometric and other named
  distributions.
- [Module 08: Continuous Random Variables](../08-CONTINUOUS-RANDOM-VARIABLES/README.md) repeats
  this module with integrals in place of sums.
- [Module 11: Covariance and Correlation](../11-COVARIANCE-AND-CORRELATION/README.md) explains the
  variance of a sum of dependent variables.
- [Module 14: Conditional Expectation](../14-CONDITIONAL-EXPECTATION/README.md) turns "best guess"
  into "best prediction given information".
- [Module 16: Inequalities and Concentration](../16-INEQUALITIES-AND-CONCENTRATION/README.md) and
  [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md) use means and variances to bound
  probabilities and to prove the Law of Large Numbers.
- In AI and machine learning, every training loss is an expected value, MSE training learns
  means, and feature scaling is standardization.

---

[← Module 05](../05-DISCRETE-RANDOM-VARIABLES/README.md) · [Syllabus](../SYLLABUS.md#module-06-expectation-variance-and-moments) · [Module 07 →](../07-DISCRETE-DISTRIBUTIONS/README.md)
