# Module 10: Joint Distributions

[Probability](../README.md) / Module 10

**Level:** 3 (Many Variables) · **Time:** about 1.5 weeks · **Importance:** ★★★★★

> **Big idea:** Real situations involve several uncertain quantities at once, and their joint distribution tells you everything about them: each one alone, each one given the others, and whether they are related.

---

## What You Will Learn

After this module you will be able to:

- Describe two random variables together with a joint table (discrete) or a joint
  density and double integrals (continuous).
- Compute marginal distributions by summing or integrating out a variable.
- Compute conditional distributions, and build a joint distribution step by step
  from a marginal and a conditional.
- Test whether random variables are independent, and use the IID assumption.
- Apply Bayes' theorem to random variables, for every mix of discrete and continuous.
- Work with mixture distributions, and simulate every one of these ideas in Python.

## Before You Start

You should be comfortable with:

- [Module 04: Conditional Probability and Bayes](../04-CONDITIONAL-PROBABILITY-AND-BAYES/README.md):
  conditional probability, the law of total probability, Bayes' theorem and
  independence of events. This module repeats all of them for random variables.
- [Module 05: Discrete Random Variables](../05-DISCRETE-RANDOM-VARIABLES/README.md):
  PMFs and CDFs.
- [Module 08: Continuous Random Variables](../08-CONTINUOUS-RANDOM-VARIABLES/README.md):
  densities, and probability as area under a curve.
- [Module 09: Continuous Distributions](../09-CONTINUOUS-DISTRIBUTIONS/README.md):
  the uniform, normal, exponential and beta distributions, used in the examples.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 10.1 | [Joint PMF and PDF](10.1-Joint-PMF-and-PDF.md) | A table or a density surface for two variables at once; double integrals |
| 10.2 | [Joint CDF](10.2-Joint-CDF.md) | $P(X \le x, Y \le y)$, the rectangle rule, and the density as a derivative |
| 10.3 | [Marginal Distributions](10.3-Marginal-Distributions.md) | One variable alone: sum or integrate out the other |
| 10.4 | [Conditional Distributions](10.4-Conditional-Distributions.md) | Slice the joint at a known value and rescale it |
| 10.5 | [Independence of Random Variables](10.5-Independence-of-Random-Variables.md) | The joint is the product of the marginals |
| 10.6 | [IID](10.6-IID.md) | Independent copies of the same experiment |
| 10.7 | [Bayes for Random Variables](10.7-Bayes-for-Random-Variables.md) | Posterior is proportional to likelihood times prior |
| 10.8 | [Mixture Distributions](10.8-Mixture-Distributions.md) | Pick a group at random, then draw from it |
| 10.9 | [Practice Problems](10.9-Practice-Problems.md) | Mixed problems and simulation projects for the whole module |

## Map of This Module

```text
              10.1 Joint PMF / PDF  ------>  10.2 Joint CDF
                       |
          +------------+------------+
          |                         |
          v                         v
   10.3 Marginals  ---------->  10.4 Conditionals
   (sum / integrate out)        (slice and rescale)
          |                         |
          +------------+------------+
                       |
          +------------+------------+
          |            |            |
          v            v            v
   10.5 Independence  10.7 Bayes   10.8 Mixtures
          |           for RVs      (marginal of
          v                         label + value)
     10.6 IID
          |            |            |
          +------------+------------+
                       |
                       v
             10.9 Practice problems
```

Start at the top. Each arrow means "you need this first". Everything grows out of the joint distribution in 10.1.

## Key Formulas

| Name | Formula |
|---|---|
| Probability of a region | $P((X, Y) \in A) = \iint_A f(x, y) \thinspace dx \thinspace dy$ |
| Joint CDF | $F(x, y) = P(X \le x, Y \le y)$ |
| Rectangle rule | $P(a \lt X \le b, c \lt Y \le d) = F(b, d) - F(a, d) - F(b, c) + F(a, c)$ |
| Marginal (discrete) | $p_X(x) = \sum_{y} p(x, y)$ |
| Marginal (continuous) | $f_X(x) = \int f(x, y) \thinspace dy$ |
| Conditional | $f_{Y \mid X}(y \mid x) = f(x, y) / f_X(x)$ |
| Multiplication rule | $f(x, y) = f_X(x) \thinspace f_{Y \mid X}(y \mid x)$ |
| Independence | $f(x, y) = f_X(x) \thinspace f_Y(y)$ for all $x, y$ |
| IID | $f(x_1, \dots, x_n) = \prod_{i} f(x_i)$ |
| Bayes for random variables | $f(x \mid y) = f(y \mid x) f_X(x) / \int f(y \mid x') f_X(x') \thinspace dx'$ |
| Mixture | $f(x) = \sum_{k} \pi_k f_k(x)$, with $\pi_k \ge 0$ and $\sum_{k} \pi_k = 1$ |

## Study Tips

- **Draw the region** before every continuous problem. Almost all mistakes in this
  module are wrong limits on a triangle or a disk. Ask: "for a fixed $x$, where
  does $y$ run?"
- Learn the discrete case first. Every continuous formula is the discrete one with
  sums turned into integrals, so a joint table is the best way to check your
  understanding.
- 10.4 (conditionals) and 10.7 (Bayes) are the most important topics for AI and
  machine learning. Do all their practice problems.
- Classic trap: a density that "looks" like $g(x) h(y)$ but lives on a triangle is
  **not** independent. Always check the shape of the support.
- Do the simulation projects in 10.9. Simulating a joint distribution, then
  filtering it, is how you will check conditional answers for the rest of the book.

## Where This Leads

- [Module 11: Covariance and Correlation](../11-COVARIANCE-AND-CORRELATION/README.md)
  measures how strongly two dependent variables move together, with one number.
- [Module 12: The Multivariate Gaussian](../12-MULTIVARIATE-GAUSSIAN/README.md) is the
  most important joint distribution; its marginals and conditionals are Gaussian too.
- [Module 13: Functions of Random Variables](../13-FUNCTIONS-OF-RANDOM-VARIABLES/README.md)
  uses joint densities to find the distribution of sums, maxima and other functions.
- [Module 14: Conditional Expectation](../14-CONDITIONAL-EXPECTATION/README.md) takes
  the mean of a conditional distribution.
- In AI and machine learning, a dataset is a sample from a joint distribution of
  features and labels, classifiers model a conditional distribution, and Bayesian
  methods and Gaussian mixture models use 10.7 and 10.8 directly.

---

[← Module 09](../09-CONTINUOUS-DISTRIBUTIONS/README.md) · [Syllabus](../SYLLABUS.md#module-10-joint-distributions) · [Module 11 →](../11-COVARIANCE-AND-CORRELATION/README.md)
