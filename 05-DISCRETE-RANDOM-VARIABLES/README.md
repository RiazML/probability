# Module 05: Discrete Random Variables

[Probability](../README.md) / Module 05

**Level:** 2 (Random Variables) · **Time:** about 1 week · **Importance:** ★★★★★

> **Big idea:** A random variable turns the outcomes of an experiment into numbers, and for a discrete one a single table, the PMF, tells you everything about how it behaves.

---

## What You Will Learn

After this module you will be able to:

- Explain why a random variable is a function from outcomes to numbers, and not
  something "random" in itself.
- Tell discrete, continuous and mixed random variables apart.
- Write the PMF and the CDF of a discrete random variable, and move from one to
  the other.
- Count with indicator random variables and turn "and", "or" and "not" into
  arithmetic.
- Find the PMF and the support of a function $Y = g(X)$.
- Explain why two variables with the same distribution can still be different,
  and simulate PMFs and CDFs in Python.

## Before You Start

You should be comfortable with:

- [Module 01: Sets, Sample Spaces and Events](../01-SETS-SAMPLE-SPACES-AND-EVENTS/README.md):
  sample spaces, events as sets, and partitions.
- [Module 02: Counting](../02-COUNTING/README.md): counting equally likely outcomes,
  such as the 36 pairs of two dice.
- [Module 03: Axioms of Probability](../03-AXIOMS-OF-PROBABILITY/README.md):
  additivity for disjoint events and continuity of probability.
- [Module 04: Conditional Probability and Bayes](../04-CONDITIONAL-PROBABILITY-AND-BAYES/README.md):
  independence, used to multiply the probabilities of separate trials.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 5.1 | [What is a Random Variable](5.1-What-is-a-Random-Variable.md) | A fixed rule that gives a number to every outcome |
| 5.2 | [Discrete vs Continuous](5.2-Discrete-vs-Continuous.md) | Probability on a list of points, or spread over intervals |
| 5.3 | [Probability Mass Function](5.3-Probability-Mass-Function.md) | The table of $P(X = x)$ that answers every question about $X$ |
| 5.4 | [Cumulative Distribution Function](5.4-Cumulative-Distribution-Function.md) | $P(X \le x)$, a staircase for discrete variables |
| 5.5 | [Indicator Random Variables](5.5-Indicator-Random-Variables.md) | 0-or-1 switches that count events and simplify set algebra |
| 5.6 | [Functions of a Random Variable](5.6-Functions-of-a-Random-Variable.md) | The PMF of $Y = g(X)$ by merging values |
| 5.7 | [Distribution vs Random Variable](5.7-Distribution-vs-Random-Variable.md) | Same distribution does not mean same variable |
| 5.8 | [Support](5.8-Support.md) | The values a variable really takes, and why models need the right one |
| 5.9 | [Practice Problems](5.9-Practice-Problems.md) | Mixed problems and simulation projects for the whole module |

## Map of This Module

```text
              5.1 Random variable: a function X : Ω -> ℝ
                                 |
                                 v
                      5.2 Discrete or continuous?
                                 |
                                 v
                      5.3 PMF  p(x) = P(X = x)
                 /               |               \
                v                v                v
       5.4 CDF  F(x)     5.5 Indicators I_A    5.6 Functions Y = g(X)
                                                  /            \
                                                 v              v
                                  5.7 Distribution vs RV    5.8 Support
                                                 \              /
                                                  v            v
                                             5.9 Practice problems
```

Start at the top. Each arrow means "you need this first"; 5.4 and 5.5 also feed the
practice problems.

## Key Formulas

| Name | Formula |
|---|---|
| Random variable | $X : \Omega \to \mathbb{R}$ and $P(X = x) = P(\lbrace \omega : X(\omega) = x \rbrace)$ |
| PMF | $p_X(x) = P(X = x)$, with $p_X(x) \ge 0$ and $\sum_{x} p_X(x) = 1$ |
| Events from the PMF | $P(X \in B) = \sum_{x \in B} p_X(x)$ |
| CDF | $F_X(x) = P(X \le x) = \sum_{t \le x} p_X(t)$ |
| Interval | $P(a \lt X \le b) = F_X(b) - F_X(a)$ |
| Point from the CDF | $P(X = x) = F_X(x) - F_X(x^-)$ |
| Indicator | $I_A = 1$ if $A$ happens, else $0$, and $P(I_A = 1) = P(A)$ |
| Function of a variable | $p_Y(y) = \sum_{x : g(x) = y} p_X(x)$ for $Y = g(X)$ |
| Support | $\operatorname{supp}(X) = \lbrace x : p_X(x) \gt 0 \rbrace$ |

## Study Tips

- The hardest idea is the first one: a random variable is a **function**. Draw the
  arrow picture of 5.1 for every new example until it feels natural.
- Always write the **support** and the **PMF** first, and check that the PMF sums
  to 1. This one habit catches most mistakes.
- With the CDF, watch the endpoints. For a discrete variable $P(X \le 2)$ and
  $P(X \lt 2)$ differ by $P(X = 2)$.
- Practice problems C1, C2, C4 and H1 in [5.9](5.9-Practice-Problems.md) cover the
  core skills; do them all.
- Run the simulations. When a simulated PMF matches your table, you know the table
  is right.

## Where This Leads

- [Module 06: Expectation, Variance and Moments](../06-EXPECTATION-VARIANCE-AND-MOMENTS/README.md)
  summarizes a PMF by its mean and spread, and turns indicators into a powerful
  counting trick.
- [Module 07: Discrete Distributions](../07-DISCRETE-DISTRIBUTIONS/README.md) gives
  names and stories to the PMFs that appear again and again: Bernoulli, binomial,
  geometric, Poisson and more.
- [Module 08: Continuous Random Variables](../08-CONTINUOUS-RANDOM-VARIABLES/README.md)
  replaces the PMF with a density and sums with integrals.
- In AI and computer science, class labels, next tokens, retry counts and hash
  buckets are discrete random variables, and a softmax output is a PMF.

---

[← Module 04](../04-CONDITIONAL-PROBABILITY-AND-BAYES/README.md) · [Syllabus](../SYLLABUS.md#module-05-discrete-random-variables) · [Module 06 →](../06-EXPECTATION-VARIANCE-AND-MOMENTS/README.md)
