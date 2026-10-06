# Module 14: Conditional Expectation

[Probability](../README.md) / Module 14

**Level:** 3 (Many Variables) · **Time:** about 1 week · **Importance:** ★★★★☆

> **Big idea:** $E[Y \mid X]$ is the average of $Y$ once you know $X$; it is itself a random variable, it is the best possible prediction of $Y$ from $X$, and conditioning on the right thing breaks hard problems into easy steps.

---

## What You Will Learn

After this module you will be able to:

- Compute $E[Y \mid X = x]$ from a joint table, a conditional density, or an event.
- Build $E[Y \mid X]$ as a random variable (a column of group averages) and find its
  distribution.
- Use the law of total expectation and first-step analysis, for example to show that a
  fair coin needs 6 flips on average for HH but only 4 for HT.
- Split a variance into a within-group part and a between-group part with Eve's law.
- Prove that $E[Y \mid X]$ is the best predictor under squared error, and pull known
  factors out of conditional expectations.
- Find the mean and variance of a random sum, and simulate every result in Python.

## Before You Start

You should be comfortable with:

- [Module 06: Expectation, Variance and Moments](../06-EXPECTATION-VARIANCE-AND-MOMENTS/README.md):
  linearity, LOTUS, variance, and the mean as the best constant guess
  ([6.10](../06-EXPECTATION-VARIANCE-AND-MOMENTS/6.10-Expectation-as-Best-Guess.md)).
- [Module 10: Joint Distributions](../10-JOINT-DISTRIBUTIONS/README.md): joint,
  marginal and conditional distributions
  ([10.4](../10-JOINT-DISTRIBUTIONS/10.4-Conditional-Distributions.md)).
- [Module 11: Covariance and Correlation](../11-COVARIANCE-AND-CORRELATION/README.md):
  covariance and the variance of a sum.
- [Module 13: Functions of Random Variables](../13-FUNCTIONS-OF-RANDOM-VARIABLES/README.md):
  the previous module; here you only need the idea of a function $g(X)$ of a random variable.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 14.1 | [Conditional Expectation Given a Value](14.1-Conditional-Expectation-Given-a-Value.md) | The average of $Y$ over the cases where $X = x$: a number |
| 14.2 | [Conditional Expectation as a Random Variable](14.2-Conditional-Expectation-as-a-Random-Variable.md) | $E[Y \mid X] = g(X)$: replace each outcome by its group average |
| 14.3 | [Law of Total Expectation](14.3-Law-of-Total-Expectation.md) | The average of the group averages is the overall average; HH versus HT |
| 14.4 | [Law of Total Variance](14.4-Law-of-Total-Variance.md) | Total variance = within groups + between groups (Eve's law) |
| 14.5 | [Best Predictor Under Squared Error](14.5-Best-Predictor-Under-Squared-Error.md) | No rule predicts $Y$ from $X$ better than $E[Y \mid X]$ |
| 14.6 | [Taking Out What is Known](14.6-Taking-Out-What-is-Known.md) | Given $X$, functions of $X$ are constants and come out |
| 14.7 | [Random Sums](14.7-Random-Sums.md) | A random number of random terms: mean and variance |
| 14.8 | [Practice Problems](14.8-Practice-Problems.md) | Mixed problems, proofs and projects for the whole module |

## Map of This Module

```text
           14.1 E[Y | X = x]: a number
                     |
                     v
           14.2 E[Y | X]: a random variable
                     |
          +----------+-----------+
          |                      |
          v                      v
   14.3 Law of total      14.6 Taking out
   expectation (Adam)     what is known
          |                      |
          v                      |
   14.4 Law of total             |
   variance (Eve)                |
          |                      |
          +----------+-----------+
                     |
          +----------+-----------+
          |                      |
          v                      v
   14.5 Best predictor     14.7 Random sums
          |                      |
          +----------+-----------+
                     |
                     v
           14.8 Practice problems
```

Start at the top. Each arrow means "you need this first". Topic 14.6 can be read any
time after 14.3; topic 14.5 uses it only for a side fact.

## Key Formulas

| Name | Formula |
|---|---|
| Given a value (discrete) | $E[Y \mid X = x] = \sum_{y} y \thinspace P(Y = y \mid X = x)$ |
| Given a value (continuous) | $E[Y \mid X = x] = \int y \thinspace f_{Y \mid X}(y \mid x) \thinspace dy$ |
| Given an event | $E[Y \mid A] = E[Y I_A] / P(A)$ |
| As a random variable | $E[Y \mid X] = g(X)$, where $g(x) = E[Y \mid X = x]$ |
| Tower (Adam's law) | $E[E[Y \mid X]] = E[Y]$ |
| Eve's law | $\operatorname{Var}(Y) = E[\operatorname{Var}(Y \mid X)] + \operatorname{Var}(E[Y \mid X])$ |
| Best predictor | $\min_h E[(Y - h(X))^2] = E[\operatorname{Var}(Y \mid X)]$, reached at $h(X) = E[Y \mid X]$ |
| Taking out what is known | $E[g(X) Y \mid X] = g(X) E[Y \mid X]$ |
| Random sum ($N$ independent of i.i.d. terms) | $E[S] = E[N] \mu$ and $\operatorname{Var}(S) = E[N] \sigma^2 + \mu^2 \operatorname{Var}(N)$ |

## Study Tips

- The hardest step is 14.2: seeing $E[Y \mid X]$ as a **random variable**. Make the
  outcome table (outcome, $X$, $Y$, group average) by hand for a die or two coins
  until it feels natural. Every later topic is easier once this is clear.
- In every problem, ask first: **what should I condition on?** Choose the thing that
  makes each case easy: the first step, the hidden group, or the number of terms.
- The most important problems: HH versus HT (14.3), the coin with an unknown bias
  (14.3 and 14.4), the curved predictor (14.5), and the counterexample to the
  random-sum formula (14.7).
- Classic mistake: averaging group averages (or group variances) without weighting
  them by the group probabilities, or forgetting the between-group part of a variance.
- Check every answer with a "group by, then average" simulation. That is exactly what a
  conditional expectation is.

## Where This Leads

- [Module 15: Generating Functions](../15-GENERATING-FUNCTIONS/README.md) gives the full
  distribution of random sums, by conditioning on the number of terms inside a
  generating function.
- [Module 18: Stochastic Processes](../18-STOCHASTIC-PROCESSES/README.md) uses
  first-step analysis for hitting times and absorption probabilities of Markov chains.
- [20.8 Martingales](../20-ADVANCED-PROBABILITY/20.8-Martingales.md) defines fair games
  by $E[M_{n+1} \mid \text{past}] = M_n$, and Module 20 defines conditional expectation
  in full generality.
- In AI and machine learning: regression models trained with squared error learn
  $E[Y \mid X]$, value functions in reinforcement learning are conditional expectations,
  and predictive uncertainty is split into noise and model disagreement with Eve's law.

---

[← Module 13](../13-FUNCTIONS-OF-RANDOM-VARIABLES/README.md) · [Syllabus](../SYLLABUS.md#module-14-conditional-expectation) · [Module 15 →](../15-GENERATING-FUNCTIONS/README.md)
