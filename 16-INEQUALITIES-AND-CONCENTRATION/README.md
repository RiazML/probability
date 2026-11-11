# Module 16: Inequalities and Concentration

[Probability](../README.md) / Module 16

**Level:** 4 (Big Theorems) · **Time:** about 1 week · **Importance:** ★★★★☆

> **Big idea:** Often you cannot compute a probability exactly, but you can bound it, and the more you know about a random variable (mean, variance, range, MGF), the faster its tail bound shrinks.

---

## What You Will Learn

After this module you will be able to:

- Prove Markov's and Chebyshev's inequalities, and say when each one is tight.
- Use Jensen's inequality to compare $E[f(X)]$ with $f(E[X])$, and to show that variance, KL divergence and $E[\ln X] - \ln E[X]$ have a fixed sign.
- Use Cauchy-Schwarz to explain why $\lvert \rho \rvert \le 1$, and to check whether a covariance is possible.
- Combine the union bound with a tail bound to control many events at once.
- Derive a Chernoff bound from the MGF, and apply it to the normal and the binomial.
- Use Hoeffding's inequality to compute how many samples give $\pm\varepsilon$ with 95% confidence.
- Explain concentration of measure: why lengths, angles and volumes behave strangely in high dimension.
- Simulate a tail probability and compare it with every bound.

## Before You Start

You should be comfortable with:

- [Module 03: Axioms of Probability](../03-AXIOMS-OF-PROBABILITY/README.md): the union bound ([3.6](../03-AXIOMS-OF-PROBABILITY/3.6-Union-Bound.md)).
- [Module 06: Expectation, Variance and Moments](../06-EXPECTATION-VARIANCE-AND-MOMENTS/README.md): linearity, variance and its properties ([6.5](../06-EXPECTATION-VARIANCE-AND-MOMENTS/6.5-Variance-and-Standard-Deviation.md), [6.6](../06-EXPECTATION-VARIANCE-AND-MOMENTS/6.6-Properties-of-Variance.md)).
- [Module 11: Covariance and Correlation](../11-COVARIANCE-AND-CORRELATION/README.md): covariance and the correlation coefficient.
- [Module 15: Generating Functions](../15-GENERATING-FUNCTIONS/README.md): the MGF and the fact that the MGF of an independent sum is a product ([15.1](../15-GENERATING-FUNCTIONS/15.1-Moment-Generating-Function.md), [15.3](../15-GENERATING-FUNCTIONS/15.3-MGF-of-Sums.md)). The Chernoff bound in 16.6 builds directly on them.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 16.1 | [Markov Inequality](16.1-Markov-Inequality.md) | $P(X \ge a) \le E[X]/a$ for $X \ge 0$: the mean alone limits the tail |
| 16.2 | [Chebyshev Inequality](16.2-Chebyshev-Inequality.md) | $P(\lvert X - \mu \rvert \ge k\sigma) \le 1/k^2$ for every distribution; proves the Weak Law |
| 16.3 | [Jensen Inequality](16.3-Jensen-Inequality.md) | For convex $f$, $f(E[X]) \le E[f(X)]$; the direction flips for concave $f$ |
| 16.4 | [Cauchy-Schwarz Inequality](16.4-Cauchy-Schwarz-Inequality.md) | $(E[XY])^2 \le E[X^2]E[Y^2]$; why correlation stays in $[-1, 1]$ |
| 16.5 | [Union Bound Revisited](16.5-Union-Bound-Revisited.md) | Error budgets, the Bonferroni lower bound, and many events at once |
| 16.6 | [Chernoff Bounds](16.6-Chernoff-Bounds.md) | Markov applied to $e^{tX}$: exponentially small tails from the MGF |
| 16.7 | [Hoeffding Inequality](16.7-Hoeffding-Inequality.md) | Bounded independent summands, and how many samples you need |
| 16.8 | [Concentration of Measure](16.8-Concentration-of-Measure.md) | Smooth functions of many independent inputs are nearly constant; high-dimensional geometry |
| 16.9 | [Practice Problems](16.9-Practice-Problems.md) | Mixed problems, proofs and projects for the whole module |

## Map of This Module

```text
   16.1 Markov (mean only)
        |
        v
   16.2 Chebyshev (mean + variance) ---+---> 16.3 Jensen (convexity)
        |                               |
        v                               +---> 16.4 Cauchy-Schwarz
   16.5 Union bound (many events)
        |
        v
   16.6 Chernoff (Markov on e^(tX); uses the MGF from Module 15)
        |
        v
   16.7 Hoeffding (bounded summands)
        |
        v
   16.8 Concentration of measure
        |
        v
   16.9 Practice problems
```

Start at the top. Topics 16.3 and 16.4 stand on their own and can be read in any order after 16.2. Chernoff (16.6) uses Markov, and Hoeffding (16.7) is Chernoff plus one lemma.

## Key Formulas

| Name | Formula |
|---|---|
| Markov | $P(X \ge a) \le \frac{E[X]}{a}$ for $X \ge 0$, $a \gt 0$ |
| General Markov | $P(X \ge a) \le \frac{E[g(X)]}{g(a)}$ for non-decreasing $g \ge 0$ |
| Chebyshev | $P(\lvert X - \mu \rvert \ge \varepsilon) \le \frac{\sigma^2}{\varepsilon^2}$, or $P(\lvert X - \mu \rvert \ge k\sigma) \le \frac{1}{k^2}$ |
| Cantelli (one side) | $P(X - \mu \ge a) \le \frac{\sigma^2}{\sigma^2 + a^2}$ |
| Chebyshev for the mean | $P(\lvert \bar{X}_n - \mu \rvert \ge \varepsilon) \le \frac{\sigma^2}{n\varepsilon^2}$ |
| Jensen | $f$ convex: $f(E[X]) \le E[f(X)]$; $f$ concave: $\ge$ |
| Cauchy-Schwarz | $(E[XY])^2 \le E[X^2]E[Y^2]$, so $\lvert \operatorname{Cov}(X, Y) \rvert \le \sigma_X\sigma_Y$ |
| Second moment | $P(X \gt 0) \ge \frac{(E[X])^2}{E[X^2]}$ for $X \ge 0$ |
| Union bound | $P(\bigcup_i A_i) \le \sum_i P(A_i)$; budget $\frac{\delta}{K}$ each gives success $\ge 1 - \delta$ |
| Chernoff | $P(X \ge a) \le \min_{t \gt 0} e^{-ta}M_X(t)$ |
| Binomial Chernoff | $P(X \ge na) \le e^{-nD(a \Vert p)}$, $D(a \Vert p) = a\ln\frac{a}{p} + (1-a)\ln\frac{1-a}{1-p}$ |
| Normal tail | $P(Z \ge a) \le e^{-a^2/2}$ |
| Hoeffding | $P(\lvert \bar{X}_n - \mu \rvert \ge \varepsilon) \le 2\exp\left(-\frac{2n\varepsilon^2}{(b-a)^2}\right)$ |
| Sample size | $n \ge \frac{(b-a)^2\ln(2/\delta)}{2\varepsilon^2}$; for a coin, $\pm 0.02$ at 95% needs $n = 4612$ |
| McDiarmid | $P(\lvert f - E[f] \rvert \ge t) \le 2\exp\left(-\frac{2t^2}{\sum_i c_i^2}\right)$ |

## Study Tips

- Learn the ladder: Markov (mean) $\to$ Chebyshev (variance) $\to$ Chernoff (MGF) $\to$ Hoeffding (range). Each step uses more information and gives a smaller bound. For every new problem ask: "what do I know about $X$?"
- The proofs to learn by heart: Markov (one line with an indicator), Chebyshev (Markov on $(X-\mu)^2$), Chernoff (Markov on $e^{tX}$), and the tangent-line proof of Jensen. Module 17 reuses Chebyshev for the Weak Law of Large Numbers.
- The bounds are usually loose. Compare each with the exact value in the Simulate It sections to get a feeling for how loose: Markov and Chebyshev are often 10 to 1000 times too big, Chernoff for rare events is within a factor of about 10.
- The most important problems: the sample-size calculation in 16.7, the 100-model example in 16.5, the majority-vote example in 16.6, and H4 in 16.9.
- Classic mistakes: using Markov for a variable that can be negative, reading "at most" as "equal to", getting the direction of Jensen wrong, forgetting the factor 2 in the two-sided Hoeffding bound, and forgetting to minimize over $t$ in a Chernoff bound.

## Where This Leads

- [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md) proves the Weak Law of Large Numbers with Chebyshev ([17.3](../17-LIMIT-THEOREMS/17.3-Weak-Law-of-Large-Numbers.md)), and then goes beyond it with the Strong Law and the Central Limit Theorem.
- [Module 19: Simulation and Monte Carlo](../19-SIMULATION-AND-MONTE-CARLO/README.md) uses Hoeffding and Chebyshev to say how many samples a simulation needs.
- [20.6 Borel-Cantelli Lemmas](../20-ADVANCED-PROBABILITY/20.6-Borel-Cantelli-Lemmas.md) and [20.8 Martingales](../20-ADVANCED-PROBABILITY/20.8-Martingales.md) build on the union bound and on the full proof of McDiarmid's inequality.
- In AI and machine learning: generalization bounds, test-set sizes, confidence bounds for bandit algorithms, random projections, and the curse of dimensionality all come from this module.

---

[← Module 15](../15-GENERATING-FUNCTIONS/README.md) · [Syllabus](../SYLLABUS.md#module-16-inequalities-and-concentration) · [Module 17 →](../17-LIMIT-THEOREMS/README.md)
