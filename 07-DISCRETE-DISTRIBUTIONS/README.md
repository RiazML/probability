# Module 07: Discrete Distributions

[Probability](../README.md) / Module 07

**Level:** 2 (Random Variables) · **Time:** about 1.5 weeks · **Importance:** ★★★★★

> **Big idea:** A small family of named distributions models most real-world counts, and each one comes from a simple story about trials, waiting, rare events or drawing from a box.

---

## What You Will Learn

After this module you will be able to:

- Tell the story behind each named discrete distribution, and pick the right one for
  a problem.
- Write the PMF, support, mean and variance of the Bernoulli, binomial, geometric,
  negative binomial, Poisson, hypergeometric, discrete uniform, categorical and
  multinomial distributions.
- Derive means and variances with indicators, series and the tail-sum formula.
- Prove that the geometric distribution is memoryless and that
  $\text{Bin}(n, \frac{\lambda}{n})$ approaches $\text{Pois}(\lambda)$.
- Connect the distributions to each other by sums, limits, splitting and conditioning.
- Sample every distribution with numpy and check the formulas by simulation.

## Before You Start

You should be comfortable with:

- [Module 02: Counting](../02-COUNTING/README.md): combinations $\binom{n}{k}$, the
  binomial theorem and multinomial coefficients.
- [Module 04: Conditional Probability and Bayes](../04-CONDITIONAL-PROBABILITY-AND-BAYES/README.md):
  independence and the law of total probability.
- [Module 05: Discrete Random Variables](../05-DISCRETE-RANDOM-VARIABLES/README.md):
  PMF, CDF, support and indicator variables.
- [Module 06: Expectation, Variance and Moments](../06-EXPECTATION-VARIANCE-AND-MOMENTS/README.md):
  expected value, linearity, LOTUS, variance and the tail-sum formula.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 7.1 | [Bernoulli](7.1-Bernoulli.md) | One yes/no trial: 1 with probability $p$, 0 otherwise |
| 7.2 | [Binomial](7.2-Binomial.md) | Number of successes in $n$ independent trials |
| 7.3 | [Geometric](7.3-Geometric.md) | Trials until the first success; the memoryless waiting time |
| 7.4 | [Negative Binomial](7.4-Negative-Binomial.md) | Failures before the $r$-th success; overdispersed counts |
| 7.5 | [Poisson](7.5-Poisson.md) | Number of rare, independent events in a fixed window |
| 7.6 | [Hypergeometric](7.6-Hypergeometric.md) | Special items in a sample drawn without replacement |
| 7.7 | [Discrete Uniform](7.7-Discrete-Uniform.md) | Every value in a finite list equally likely, like a fair die |
| 7.8 | [Categorical](7.8-Categorical.md) | One roll of a $k$-sided, possibly unfair die |
| 7.9 | [Multinomial](7.9-Multinomial.md) | Counts of each face in $n$ rolls of a $k$-sided die |
| 7.10 | [Poisson Approximation to Binomial](7.10-Poisson-Approximation-to-Binomial.md) | Many trials with tiny chances give a Poisson count |
| 7.11 | [Relationships Between Distributions](7.11-Relationships-Between-Distributions.md) | The family tree: sums, limits, splitting and conditioning |
| 7.12 | [Practice Problems](7.12-Practice-Problems.md) | Mixed problems and simulation projects for the whole module |

## Map of This Module

```text
                          7.1 Bernoulli
                (one yes/no trial, the building block)
            /              |               |               \
           v               v               v                v
     7.2 Binomial    7.3 Geometric   7.6 Hypergeometric  7.8 Categorical
     (n trials)      (wait for 1)    (no replacement)    (k outcomes)
           |               |                               /         \
           v               v                              v           v
  7.10 Poisson     7.4 Negative Binomial      7.9 Multinomial  7.7 Discrete
  approximation    (wait for r)               (n draws)        Uniform
           |
           v
  7.5 Poisson (rare events in a window)

  all of the above  ----->  7.11 Relationships  ----->  7.12 Practice
```

Start at the top. Each arrow means "this topic builds on that one". Topic 7.11 ties
the whole family together.

## Key Formulas

| Distribution | PMF $P(X = k)$ | Support | Mean | Variance |
|---|---|---|---|---|
| $\text{Bern}(p)$ | $p^k (1-p)^{1-k}$ | $\lbrace 0, 1 \rbrace$ | $p$ | $p(1-p)$ |
| $\text{Bin}(n, p)$ | $\binom{n}{k} p^k (1-p)^{n-k}$ | $\lbrace 0, \dots, n \rbrace$ | $np$ | $np(1-p)$ |
| $\text{Geom}(p)$ (trials) | $(1-p)^{k-1} p$ | $\lbrace 1, 2, \dots \rbrace$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ |
| $\text{NegBin}(r, p)$ (failures) | $\binom{k+r-1}{k} p^r (1-p)^k$ | $\lbrace 0, 1, \dots \rbrace$ | $\frac{r(1-p)}{p}$ | $\frac{r(1-p)}{p^2}$ |
| $\text{Pois}(\lambda)$ | $\frac{e^{-\lambda} \lambda^k}{k!}$ | $\lbrace 0, 1, \dots \rbrace$ | $\lambda$ | $\lambda$ |
| $\text{HGeom}(N, K, n)$ | $\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$ | $\max(0, n-N+K)$ to $\min(n, K)$ | $\frac{nK}{N}$ | $n \frac{K}{N}(1 - \frac{K}{N})\frac{N-n}{N-1}$ |
| $\text{Unif}\lbrace a, \dots, b \rbrace$ | $\frac{1}{b-a+1}$ | $\lbrace a, \dots, b \rbrace$ | $\frac{a+b}{2}$ | $\frac{(b-a+1)^2 - 1}{12}$ |
| $\text{Cat}(p_1, \dots, p_k)$ | $p_j$ at the value $j$ | $\lbrace 1, \dots, k \rbrace$ | (labels) | (labels) |
| $\text{Mult}(n, p_1, \dots, p_k)$ | $\frac{n!}{x_1! \cdots x_k!} p_1^{x_1} \cdots p_k^{x_k}$ | counts adding to $n$ | $E[X_j] = n p_j$ | $n p_j (1 - p_j)$ |

Two more facts to remember:

- **Memoryless (geometric):** $P(X \gt m + n \mid X \gt m) = P(X \gt n)$.
- **Poisson limit:** $\text{Bin}(n, p) \approx \text{Pois}(np)$ when $n$ is large and $p$ is
  small, with error at most $np^2$.

## Study Tips

- Learn the **stories**, not just the formulas. "Fixed number of trials" means
  binomial; "wait until success" means geometric or negative binomial; "rare events in
  a window" means Poisson; "without replacement" means hypergeometric.
- Watch the conventions. In this book the geometric counts **trials** (support starts
  at 1) and the negative binomial counts **failures** (support starts at 0). numpy and
  scipy use the same conventions, but other books may not.
- The indicator trick (write a count as a sum of 0/1 variables) gives the mean of the
  binomial and hypergeometric in one line. Practice it until it is automatic.
- Topic 7.11 is the best review: if you can explain every arrow in its family tree,
  you understand the module.
- Run every simulation. Seeing the simulated and exact values agree builds trust in
  the formulas, and changing the parameters builds intuition about shape.

## Where This Leads

- [Module 08: Continuous Random Variables](../08-CONTINUOUS-RANDOM-VARIABLES/README.md)
  replaces sums with integrals, and
  [Module 09](../09-CONTINUOUS-DISTRIBUTIONS/README.md) meets the continuous cousins: the
  exponential (the continuous geometric), the gamma and the normal.
- [Module 15: Generating Functions](../15-GENERATING-FUNCTIONS/README.md) gives a faster
  way to find these means and variances and to add independent variables.
- [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md) shows why binomial and
  Poisson counts look normal when their mean is large.
- [Module 18: Stochastic Processes](../18-STOCHASTIC-PROCESSES/README.md) builds the
  Poisson process and Markov chains from these distributions.
- In AI and machine learning: classifiers output categorical distributions, training
  uses Bernoulli and categorical log-likelihoods (cross-entropy), language models sample
  tokens, and count data is modeled with Poisson and negative binomial distributions.

---

[← Module 06](../06-EXPECTATION-VARIANCE-AND-MOMENTS/README.md) · [Syllabus](../SYLLABUS.md#module-07-discrete-distributions) · [Module 08 →](../08-CONTINUOUS-RANDOM-VARIABLES/README.md)
