# Module 17: Limit Theorems

[Probability](../README.md) / Module 17

**Level:** 4 (Big Theorems) · **Time:** about 1.5 weeks · **Importance:** ★★★★★

> **Big idea:** The average of many independent values settles down to the true mean (the Law of Large Numbers), and the small error around it has a bell shape (the Central Limit Theorem), which is why the normal curve is everywhere.

---

## What You Will Learn

After this module you will be able to:

- Name the four modes of convergence (in distribution, in probability, in mean square, almost surely) and say which imply which.
- Prove the Weak Law of Large Numbers with Chebyshev's inequality, and explain what the Strong Law adds.
- State the Central Limit Theorem, explain why the bell curve appears, and judge how fast it appears.
- Approximate a binomial probability with the normal curve and the continuity correction, and say when the Poisson approximation is better.
- Find the standard error of a function of an average (delta method), and replace an unknown $\sigma$ by an estimate (Slutsky).
- Explain why averages of Cauchy data never settle, and what happens when the variance is infinite.
- Prove the Poisson limit theorem and bound its error with Le Cam's inequality.
- Simulate the laws of large numbers and the CLT and compare them with the theory.

## Before You Start

You should be comfortable with:

- [Module 16: Inequalities and Concentration](../16-INEQUALITIES-AND-CONCENTRATION/README.md): Chebyshev's inequality ([16.2](../16-INEQUALITIES-AND-CONCENTRATION/16.2-Chebyshev-Inequality.md)) proves the Weak Law, and Markov's inequality ([16.1](../16-INEQUALITIES-AND-CONCENTRATION/16.1-Markov-Inequality.md)) proves the Strong Law.
- [Module 15: Generating Functions](../15-GENERATING-FUNCTIONS/README.md): the MGF proof of the CLT is Example 3 of [15.4](../15-GENERATING-FUNCTIONS/15.4-Uniqueness-Theorem.md), and the characteristic function ([15.6](../15-GENERATING-FUNCTIONS/15.6-Characteristic-Function.md)) explains the Cauchy case.
- [Module 09: Continuous Distributions](../09-CONTINUOUS-DISTRIBUTIONS/README.md): the normal, the exponential and the Cauchy.
- [Module 07: Discrete Distributions](../07-DISCRETE-DISTRIBUTIONS/README.md): the binomial and the Poisson ([7.10](../07-DISCRETE-DISTRIBUTIONS/7.10-Poisson-Approximation-to-Binomial.md) is the first look at the Poisson limit).
- [Module 06: Expectation, Variance and Moments](../06-EXPECTATION-VARIANCE-AND-MOMENTS/README.md): variance of a sum of independent variables ([6.6](../06-EXPECTATION-VARIANCE-AND-MOMENTS/6.6-Properties-of-Variance.md)).

## Topics

| # | Topic | What it is about |
|---|---|---|
| 17.1 | [Modes of Convergence](17.1-Modes-of-Convergence.md) | Four meanings of the phrase $X_n$ gets close to $X$: in distribution, in probability, in mean square, almost surely |
| 17.2 | [Relationships Between Modes](17.2-Relationships-Between-Modes.md) | Which mode implies which, and a counterexample for every arrow that is missing |
| 17.3 | [Weak Law of Large Numbers](17.3-Weak-Law-of-Large-Numbers.md) | $\bar{X}_n \to \mu$ in probability; the proof is Chebyshev applied to the sample mean |
| 17.4 | [Strong Law of Large Numbers](17.4-Strong-Law-of-Large-Numbers.md) | $\bar{X}_n \to \mu$ almost surely; one run settles for good |
| 17.5 | [Central Limit Theorem](17.5-Central-Limit-Theorem.md) | The standardized sum tends to $\mathcal{N}(0, 1)$; why, and how fast (Berry-Esseen) |
| 17.6 | [Normal Approximation and Continuity Correction](17.6-Normal-Approximation-and-Continuity-Correction.md) | Binomial probabilities by the normal curve; why we add or subtract one half |
| 17.7 | [Delta Method](17.7-Delta-Method.md) | The standard error of $g(\bar{X}_n)$ is $\lvert g'(\mu) \rvert \sigma / \sqrt{n}$ |
| 17.8 | [Slutsky's Theorem](17.8-Slutsky-Theorem.md) | Replace an unknown $\sigma$ by $S_n$ and keep the normal limit |
| 17.9 | [When the CLT Fails](17.9-When-the-CLT-Fails.md) | Cauchy, infinite variance, the St. Petersburg game, and stable laws |
| 17.10 | [Poisson Limit and Law of Rare Events](17.10-Poisson-Limit-and-Law-of-Rare-Events.md) | $\text{Bin}(n, \lambda/n) \to \text{Pois}(\lambda)$, Le Cam's inequality and the Poisson paradigm |
| 17.11 | [Practice Problems](17.11-Practice-Problems.md) | Mixed problems, proofs and simulation projects for the whole module |

## Map of This Module

```text
   17.1 Modes of convergence
            |
            v
   17.2 How the modes relate
            |
      +-----+-----------------+
      |                       |
      v                       v
   17.3 Weak LLN          17.5 CLT <----- Module 15 (MGFs)
   (Chebyshev)                |
      |             +---------+---------+-----------+
      v             |         |         |           |
   17.4 Strong      v         v         v           v
   LLN          17.6 Normal  17.7     17.8        17.9 When
                approx + CC  Delta <- Slutsky     the CLT fails
                             method

   7.10 Poisson approximation ----> 17.10 Poisson limit (rare events)

                         17.11 Practice problems
```

The two laws (17.3 and 17.4) say where the average goes. The CLT (17.5) says how it gets there, and 17.6 to 17.9 put it to work. The proof of the delta method (17.7) uses Slutsky's theorem (17.8), so read them as a pair. The Poisson limit (17.10) is the second great limit, for rare events instead of many small pieces.

## Key Formulas

| Name | Formula |
|---|---|
| Convergence chain | almost surely $\implies$ in probability $\implies$ in distribution; mean square $\implies$ in probability |
| Variance of the average | $\operatorname{Var}(\bar{X}_n) = \frac{\sigma^2}{n}$, standard error $\frac{\sigma}{\sqrt{n}}$ |
| Weak Law (Chebyshev) | $P\big(\lvert \bar{X}_n - \mu \rvert \gt \varepsilon\big) \le \frac{\sigma^2}{n\varepsilon^2}$ |
| Sample size (Chebyshev) | $n \ge \frac{\sigma^2}{\varepsilon^2\delta}$ |
| Strong Law | $P\big(\lim_{n \to \infty} \bar{X}_n = \mu\big) = 1$ if $E\lvert X \rvert \lt \infty$ |
| Central Limit Theorem | $\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \xrightarrow{d} \mathcal{N}(0, 1)$ |
| Practical CLT | $\bar{X}_n \approx \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$ and $S_n \approx \mathcal{N}(n\mu, n\sigma^2)$ |
| Berry-Esseen | $\sup_z \lvert P(Z_n \le z) - \Phi(z) \rvert \le \frac{C\rho}{\sigma^3\sqrt{n}}$, $C \lt 0.48$ |
| Continuity correction | $P(X \le k) \approx \Phi\left(\frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right)$ |
| Delta method | $\sqrt{n}\big(g(\bar{X}_n) - g(\mu)\big) \xrightarrow{d} \mathcal{N}\big(0, g'(\mu)^2\sigma^2\big)$ |
| Slutsky | $X_n \xrightarrow{d} X$, $Y_n \xrightarrow{p} c$ $\implies$ $X_n + Y_n \xrightarrow{d} X + c$, $X_n Y_n \xrightarrow{d} cX$ |
| Studentized mean | $\frac{\sqrt{n}(\bar{X}_n - \mu)}{S_n} \xrightarrow{d} \mathcal{N}(0, 1)$ |
| Poisson limit | $\text{Bin}(n, p_n) \to \text{Pois}(\lambda)$ if $np_n \to \lambda$ |
| Le Cam | $\sup_A \lvert P(S \in A) - P(T \in A) \rvert \le \sum p_i^2$, $T \sim \text{Pois}(\sum p_i)$ |

## Study Tips

- The most important topic is 17.5 (CLT). Be able to say in one minute what it states, why only the mean and the variance matter, and why $\sqrt{n}$ appears. Then do the sample-size problems in 17.3, 17.5 and 17.6 until you can do them without notes.
- Learn the proof of the Weak Law (three lines: mean, variance, Chebyshev). It is the proof that every exam asks for, and Problem H1 in 17.11 is a full write-up.
- Always say the mode of convergence in words: "in probability", "almost surely" or "in distribution". Most confusion in this module is a missing mode.
- A classic mistake: using the CLT for a single value, or using $\sigma$ instead of $\frac{\sigma}{\sqrt{n}}$ for an average. Ask first: "is the question about one value, a sum or an average?"
- Check the assumptions before you use a theorem. Finite mean for the LLN, finite variance for the CLT, small $p$ for the Poisson. Topic 17.9 shows what happens when they fail.
- The simulations in this module are short. Run them, change $n$, and watch the numbers move. The Cauchy and Pareto runs in 17.9 and in the projects of 17.11 are the best way to remember that the theorems have conditions.

## Where This Leads

- [Module 18: Stochastic Processes](../18-STOCHASTIC-PROCESSES/README.md) uses the LLN for long-run averages of Markov chains, the CLT for the position of a random walk, and the Poisson limit to define the Poisson process ([18.5](../18-STOCHASTIC-PROCESSES/18.5-Poisson-Process.md)).
- [Module 19: Simulation and Monte Carlo](../19-SIMULATION-AND-MONTE-CARLO/README.md) is built on the Strong Law (the estimate converges) and on the CLT (the error bar is $1.96\frac{\sigma}{\sqrt{n}}$).
- [Module 20: Advanced Probability](../20-ADVANCED-PROBABILITY/README.md) gives the Borel-Cantelli lemmas ([20.6](../20-ADVANCED-PROBABILITY/20.6-Borel-Cantelli-Lemmas.md)) behind almost sure convergence, and martingale convergence theorems.
- In AI and machine learning: test accuracy is an average (LLN), its error bar comes from the CLT, minibatch gradient noise is approximately Gaussian, and heavy-tailed gradients are the reason for clipping and for robust estimators.

---

[← Module 16](../16-INEQUALITIES-AND-CONCENTRATION/README.md) · [Syllabus](../SYLLABUS.md#module-17-limit-theorems-lln-and-clt) · [Module 18 →](../18-STOCHASTIC-PROCESSES/README.md)
