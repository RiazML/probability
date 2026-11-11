# Module 15: Generating Functions

[Probability](../README.md) / Module 15

**Level:** 4 (Big Theorems) · **Time:** about 1 week · **Importance:** ★★★☆☆

> **Big idea:** A generating function packs a whole distribution into one function, so that moments become derivatives, sums of independent variables become products, and a matching function means a matching distribution.

---

## What You Will Learn

After this module you will be able to:

- Compute the moment generating function (MGF) of a distribution, and say when it does not exist (Cauchy, log-normal).
- Get $E[X^n]$ by differentiating the MGF or reading its power series.
- Find the distribution of a sum of independent variables by multiplying MGFs, and recognize the answer by the uniqueness theorem.
- Follow the MGF proof of the Central Limit Theorem and of the Poisson limit.
- Use the probability generating function (PGF) for counts: probabilities, moments, sums and random sums, and the extinction probability of a branching process.
- Explain why the characteristic function always exists, and why the mean of Cauchy variables is still Cauchy.
- Compute cumulants, skewness and excess kurtosis, and use the fact that cumulants add.

## Before You Start

You should be comfortable with:

- [Module 06: Expectation, Variance and Moments](../06-EXPECTATION-VARIANCE-AND-MOMENTS/README.md):
  LOTUS ([6.3](../06-EXPECTATION-VARIANCE-AND-MOMENTS/6.3-LOTUS.md)) and moments, skewness and kurtosis
  ([6.7](../06-EXPECTATION-VARIANCE-AND-MOMENTS/6.7-Moments-Skewness-and-Kurtosis.md)).
- [Module 07: Discrete Distributions](../07-DISCRETE-DISTRIBUTIONS/README.md): the binomial, geometric and Poisson PMFs.
- [Module 09: Continuous Distributions](../09-CONTINUOUS-DISTRIBUTIONS/README.md): the normal, exponential, Gamma, Cauchy and log-normal, and heavy tails
  ([9.13](../09-CONTINUOUS-DISTRIBUTIONS/9.13-Heavy-vs-Light-Tails.md)).
- [Module 13: Functions of Random Variables](../13-FUNCTIONS-OF-RANDOM-VARIABLES/README.md): convolutions of sums
  ([13.4](../13-FUNCTIONS-OF-RANDOM-VARIABLES/13.4-Convolution-Sums-of-Random-Variables.md), [13.5](../13-FUNCTIONS-OF-RANDOM-VARIABLES/13.5-Sums-of-Known-Distributions.md)).
- [Module 14: Conditional Expectation](../14-CONDITIONAL-EXPECTATION/README.md): random sums
  ([14.7](../14-CONDITIONAL-EXPECTATION/14.7-Random-Sums.md)).

The characteristic function in 15.6 uses a little complex arithmetic. The topic explains the few facts you need ($i^2 = -1$ and $e^{i\theta} = \cos\theta + i\sin\theta$) when it first uses them.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 15.1 | [Moment Generating Function](15.1-Moment-Generating-Function.md) | $M_X(t) = E[e^{tX}]$ stores all moments; it does not exist for the Cauchy or the log-normal |
| 15.2 | [Moments from the MGF](15.2-Moments-from-the-MGF.md) | The $n$-th derivative at $0$ is $E[X^n]$; the series gives all moments at once |
| 15.3 | [MGF of Sums](15.3-MGF-of-Sums.md) | For independent variables the MGF of the sum is the product of the MGFs |
| 15.4 | [Uniqueness Theorem](15.4-Uniqueness-Theorem.md) | Same MGF, same distribution; the proof of the CLT and the Poisson limit |
| 15.5 | [Probability Generating Function](15.5-Probability-Generating-Function.md) | $G_X(s) = E[s^X]$ for counts: PMF, moments, sums, random sums and extinction |
| 15.6 | [Characteristic Function](15.6-Characteristic-Function.md) | $\varphi_X(t) = E[e^{itX}]$ exists for every random variable |
| 15.7 | [Cumulants](15.7-Cumulants.md) | The coefficients of $\ln M_X$: mean, variance, skewness, and they add |
| 15.8 | [Practice Problems](15.8-Practice-Problems.md) | Mixed problems, proofs and projects for the whole module |

## Map of This Module

```text
   15.1 Moment generating function
                  |
                  v
   15.2 Moments from the MGF
                  |
                  v
   15.3 MGF of sums
                  |
                  v
   15.4 Uniqueness (and the CLT proof)
          |                 |
          v                 v
   15.5 PGF (counts)   15.6 Characteristic function
          |                 |
          +--------+--------+
                   |
                   v
   15.7 Cumulants (the log of the MGF)
                   |
                   v
   15.8 Practice problems
```

Start at the top. Each arrow means "you need this first". Topics 15.5 and 15.6 can be read in either order, and 15.7 only needs 15.2 to 15.4.

## Key Formulas

| Name | Formula |
|---|---|
| MGF | $M_X(t) = E[e^{tX}]$, with $M_X(0) = 1$ |
| Moments | $E[X^n] = M_X^{(n)}(0)$ and $M_X(t) = \sum_n E[X^n] \frac{t^n}{n!}$ |
| Shift and scale | $M_{aX+b}(t) = e^{bt} M_X(at)$ |
| Independent sum | $M_{X+Y}(t) = M_X(t) M_Y(t)$ |
| Uniqueness | $M_X = M_Y$ near $0$ $\implies$ same distribution |
| CLT, key step | $M_{Z_n}(t) = M_Y(t/\sqrt{n})^n \to e^{t^2/2}$ |
| PGF | $G_X(s) = E[s^X]$, $P(X = k) = G^{(k)}(0)/k!$, $E[X] = G'(1)$ |
| Random sum | $G_S(s) = G_N(G_X(s))$ |
| Extinction probability | smallest root of $q = G(q)$ |
| Characteristic function | $\varphi_X(t) = E[e^{itX}]$, $\lvert \varphi_X(t) \rvert \le 1$ |
| Cumulants | $K_X(t) = \ln M_X(t)$, $\kappa_n(X + Y) = \kappa_n(X) + \kappa_n(Y)$ |
| Cumulants and shape | $\kappa_3 = \mu_3$, $\kappa_4 = \mu_4 - 3\sigma^4$ |
| Bernoulli, Binomial | $M(t) = 1 - p + pe^t$, $(1 - p + pe^t)^n$ |
| Poisson | $M(t) = \exp\big(\lambda(e^t - 1)\big)$ |
| Exponential (rate $\lambda$) | $M(t) = \frac{\lambda}{\lambda - t}$ for $t \lt \lambda$ |
| Normal | $M(t) = \exp\left( \mu t + \frac{\sigma^2 t^2}{2} \right)$ |
| Cauchy | $\varphi(t) = e^{-\lvert t \rvert}$, and no MGF |

## Study Tips

- The key idea is 15.3: **multiply** the MGFs of independent variables. After that, 15.4 is mostly the question "which known MGF is this?" Keep the table of common MGFs in 15.1 next to you.
- The two proofs to learn by heart are in 15.4: the Poisson limit (two lines) and the Central Limit Theorem (six steps). Write them out from memory. Module 17 uses the CLT proof.
- Always check three things about an MGF: $M(0) = 1$, the range of $t$ where it is finite, and that the variables you multiply are independent.
- The complex numbers in 15.6 look scary but need only one formula, $e^{i\theta} = \cos\theta + i\sin\theta$, and the fact that this point has length 1. That is why $\varphi$ always exists.
- The most important problems: the sum of independent Poissons (15.3, 15.8 C1), the MGF proof of the CLT (15.4), the extinction probability (15.5, 15.8 H2), the geometric sum of exponentials (15.8 H1), and the Cauchy average (15.6).
- Classic mistakes: $E[e^{tX}] \ne e^{tE[X]}$, forgetting the factor $n!$ when reading a moment from a series, and adding cumulants of dependent variables.

## Where This Leads

- [Module 16: Inequalities and Concentration](../16-INEQUALITIES-AND-CONCENTRATION/README.md) builds the Chernoff bound directly from the MGF
  ([16.6](../16-INEQUALITIES-AND-CONCENTRATION/16.6-Chernoff-Bounds.md)).
- [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md) states the Central Limit Theorem
  ([17.5](../17-LIMIT-THEOREMS/17.5-Central-Limit-Theorem.md)) using the proof from 15.4, proves the Poisson limit
  ([17.10](../17-LIMIT-THEOREMS/17.10-Poisson-Limit-and-Law-of-Rare-Events.md)), and uses the characteristic function to explain why the CLT fails for the Cauchy
  ([17.9](../17-LIMIT-THEOREMS/17.9-When-the-CLT-Fails.md)).
- [18.6 Branching Processes](../18-STOCHASTIC-PROCESSES/18.6-Branching-Processes.md) uses the PGF and the equation $q = G(q)$ to decide whether a population dies out.
- In AI and machine learning: the log of an MGF is the log-partition function of exponential families (its derivatives are the mean and variance of the model), independent component analysis uses the fourth cumulant, and random Fourier features are built on the characteristic function.

---

[← Module 14](../14-CONDITIONAL-EXPECTATION/README.md) · [Syllabus](../SYLLABUS.md#module-15-generating-functions) · [Module 16 →](../16-INEQUALITIES-AND-CONCENTRATION/README.md)
