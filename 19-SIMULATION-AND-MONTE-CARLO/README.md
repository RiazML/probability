# Module 19: Simulation and Monte Carlo

[Probability](../README.md) / Module 19

**Level:** 5 (Hero) · **Time:** about 1.5 weeks · **Importance:** ★★★★☆

> **Big idea:** When the exact answer is out of reach, run the random experiment on a computer, turn uniform random numbers into the distribution you need (inverse transform, rejection, importance weights, Markov chains), and always report the standard error, which shrinks like $\frac{1}{\sqrt{n}}$.

---

## What You Will Learn

After this module you will be able to:

- Estimate a probability, an expectation or an integral by Monte Carlo, and report its standard error, a 95% interval and the sample size you need.
- Explain how a pseudo-random generator and a seed work, and why a generator must be tested for independence as well as flatness.
- Sample from any distribution with a computable quantile function (inverse transform), and from any density you can evaluate (rejection sampling), and compute the acceptance rate.
- Use importance sampling to estimate rare events, and judge a run by its weights and effective sample size.
- Write Metropolis-Hastings and Gibbs samplers, explain why they leave the target stationary, and diagnose a run with burn-in, autocorrelation, ESS and R-hat.
- Verify a formula, a puzzle answer or your own sampler by simulation, using a $z$-score to decide when theory and code agree.

## Before You Start

You should be comfortable with:

- [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md): the Law of Large Numbers says the Monte Carlo average converges ([17.3](../17-LIMIT-THEOREMS/17.3-Weak-Law-of-Large-Numbers.md), [17.4](../17-LIMIT-THEOREMS/17.4-Strong-Law-of-Large-Numbers.md)), and the Central Limit Theorem gives the error bar $\frac{\sigma}{\sqrt{n}}$ ([17.5](../17-LIMIT-THEOREMS/17.5-Central-Limit-Theorem.md)).
- [Module 18: Stochastic Processes](../18-STOCHASTIC-PROCESSES/README.md): MCMC builds a Markov chain with a chosen stationary distribution ([18.3.5](../18-STOCHASTIC-PROCESSES/18.3-Markov-Chains/18.3.5-Stationary-Distribution.md)), using detailed balance ([18.3.6](../18-STOCHASTIC-PROCESSES/18.3-Markov-Chains/18.3.6-Detailed-Balance-and-Reversibility.md)).
- [Module 08: Continuous Random Variables](../08-CONTINUOUS-RANDOM-VARIABLES/README.md): the quantile function ([8.7](../08-CONTINUOUS-RANDOM-VARIABLES/8.7-Quantile-Function.md)) is the heart of inverse transform sampling.
- [Module 13: Functions of Random Variables](../13-FUNCTIONS-OF-RANDOM-VARIABLES/README.md): the Box-Muller transform ([13.8](../13-FUNCTIONS-OF-RANDOM-VARIABLES/13.8-Box-Muller-Transform.md)) is the best-known sampling trick.
- Python with numpy. Every topic has code that you should run and change.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 19.1 | [Why Simulate](19.1-Why-Simulate.md) | Play the random experiment many times and count; the error is about $\frac{1}{\sqrt{n}}$ |
| 19.2 | [Pseudo-Random Numbers and Seeds](19.2-Pseudo-Random-Numbers-and-Seeds.md) | Deterministic recipes that look random, the seed, the period, and why RANDU failed |
| 19.3 | [Monte Carlo Estimation](19.3-Monte-Carlo-Estimation.md) | Estimate $E[f(X)]$ by an average; standard error, 95% interval, sample size, integrals |
| 19.4 | [Inverse Transform Sampling](19.4-Inverse-Transform-Sampling.md) | $X = Q(U)$ turns a uniform number into any distribution, continuous or discrete |
| 19.5 | [Rejection Sampling](19.5-Rejection-Sampling.md) | Propose from an easy density, accept with probability $\frac{p}{Mq}$; the curse of dimensions |
| 19.6 | [Importance Sampling](19.6-Importance-Sampling.md) | Sample where it matters and weight by $\frac{p}{q}$; rare events and effective sample size |
| 19.7 | [MCMC](19.7-MCMC/README.md) | Markov chains whose stationary law is the target (a section with 3 topics) |
| 19.8 | [Verifying Theory by Simulation](19.8-Verifying-Theory-by-Simulation.md) | The $z$-score of a check, distribution tests, and catching wrong claims and buggy samplers |
| 19.9 | [Practice Problems](19.9-Practice-Problems.md) | Mixed problems, proofs and simulation projects for the whole module |

## Map of This Module

```text
   19.1 Why simulate  --->  19.2 Random numbers and seeds
            |                          |
            +------------+-------------+
                         v
            19.3 Monte Carlo estimation (error = sigma / sqrt(n))
                         |
          +--------------+---------------+
          v              v               v
   19.4 Inverse     19.5 Rejection   19.6 Importance
   transform        sampling         sampling
          \              |               /
           +-------------+--------------+
                         v
                 19.7 MCMC (needs a Markov chain)
            19.7.1 Metropolis-Hastings
            19.7.2 Gibbs sampling
            19.7.3 Burn-in, mixing, diagnostics
                         |
                         v
            19.8 Verifying theory by simulation
                         |
                         v
                 19.9 Practice problems
```

The first two topics give the tools, 19.3 gives the error bar, and 19.4 to 19.6 are three ways to draw samples or to re-weight them. MCMC takes over when those fail, usually in many dimensions, and 19.8 turns everything into a habit of checking your answers.

## Key Formulas

| Name | Formula |
|---|---|
| Estimate of a probability | $\hat{p}_n = \frac{\text{successes}}{n}$, $\quad \operatorname{SE} = \sqrt{\frac{\hat{p}_n(1 - \hat{p}_n)}{n}}$ |
| Monte Carlo estimate | $\hat{\theta}_n = \frac{1}{n} \sum_{i=1}^{n} f(X_i)$, $\quad \operatorname{SE} = \frac{\sigma}{\sqrt{n}}$ |
| 95% interval and sample size | $\hat{\theta}_n \pm 1.96 \frac{s}{\sqrt{n}}$, $\quad n \ge \left( \frac{1.96 \sigma}{\varepsilon} \right)^2$ |
| Linear congruential generator | $x_{n+1} = (a x_n + c) \operatorname{mod} m$, $\quad u_n = \frac{x_n}{m}$ |
| Inverse transform | $U \sim \text{Unif}(0, 1) \implies X = F^{-1}(U)$ has CDF $F$ |
| Exponential sampler | $X = -\frac{\ln(1 - U)}{\lambda} \sim \text{Exp}(\lambda)$ |
| Rejection sampling | accept $X \sim q$ with probability $\frac{p(X)}{M q(X)}$, where $p \le Mq$; acceptance rate $\frac{1}{M}$ |
| Importance sampling | $E_p[f(X)] = E_q\left[ f(X) \frac{p(X)}{q(X)} \right]$ |
| Effective sample size (weights) | $\text{ESS} = \frac{\left( \sum_i w_i \right)^2}{\sum_i w_i^2}$ |
| Metropolis-Hastings | $\alpha = \min \left( 1, \frac{\tilde{p}(x') q(x \mid x')}{\tilde{p}(x) q(x' \mid x)} \right)$ |
| Gibbs sampling | draw $x_j \sim p(x_j \mid x_{-j})$ for each $j$; acceptance probability 1 |
| MCMC error | $\tau = 1 + 2 \sum_{k \ge 1} \rho_k$, $\quad \text{ESS} = \frac{n}{\tau}$, $\quad \operatorname{SE} \approx \frac{\sigma}{\sqrt{\text{ESS}}}$ |
| Check against theory | $z = \frac{\hat{\theta} - \theta_0}{\operatorname{SE}}$; pass if $\lvert z \rvert \lt 2$ |

## Study Tips

- The key habit is in [19.3](19.3-Monte-Carlo-Estimation.md) and [19.8](19.8-Verifying-Theory-by-Simulation.md): never write a simulation result without its standard error. Do this in every problem, even when nobody asks.
- Run every code block, then change one thing: the number of samples, the seed, the step size. Watching the error bar shrink by $\frac{1}{\sqrt{n}}$ teaches more than reading the proof.
- The hardest topics are importance sampling ([19.6](19.6-Importance-Sampling.md)) and the MCMC section. For importance sampling, remember the question: where does $\lvert f \rvert p$ live, and is my proposal large there? For MCMC, work Example 1 of [19.7.1](19.7-MCMC/19.7.1-Metropolis-Hastings.md) by hand until detailed balance is clear.
- The most useful practice problems in [19.9](19.9-Practice-Problems.md) are C4 (importance weights and variance), C6 (the effective sample size), H1 (the rejection proof) and the project P2 (an MCMC run with diagnostics).
- Classic mistakes to watch for: forgetting that MCMC samples are correlated; a proposal with thinner tails than the target; the wrong direction of the weight $\frac{p}{q}$; recording only accepted moves in Metropolis; and a simulation built from the same wrong idea as the theory it is meant to check.

## Where This Leads

- [Module 20: Advanced Probability](../20-ADVANCED-PROBABILITY/README.md) makes precise what "almost surely" means for the Strong Law that justifies every Monte Carlo average, and gives the Radon-Nikodym derivative ([20.10](../20-ADVANCED-PROBABILITY/20.10-Radon-Nikodym-and-Densities.md)), which is exactly the importance weight $\frac{p}{q}$ of [19.6](19.6-Importance-Sampling.md).
- [Module 21: Applications of Probability](../21-APPLICATIONS-OF-PROBABILITY/README.md) uses these tools: Bayesian inference and generative models ([21.1.4](../21-APPLICATIONS-OF-PROBABILITY/21.1-AI-and-Machine-Learning/21.1.4-Generative-Models.md)), reinforcement learning ([21.1.5](../21-APPLICATIONS-OF-PROBABILITY/21.1-AI-and-Machine-Learning/21.1.5-Reinforcement-Learning.md)), randomized algorithms ([21.3.1](../21-APPLICATIONS-OF-PROBABILITY/21.3-Computer-Science/21.3.1-Randomized-Algorithms.md)) and pricing in finance ([21.5](../21-APPLICATIONS-OF-PROBABILITY/21.5-Finance-and-Insurance.md)).
- In AI and machine learning: minibatch gradients are Monte Carlo estimates, off-policy reinforcement learning uses importance weights, Bayesian models are fitted with MCMC (Gibbs, Hamiltonian Monte Carlo), and text and images are generated by sampling.

---

[← Module 18](../18-STOCHASTIC-PROCESSES/README.md) · [Syllabus](../SYLLABUS.md#module-19-simulation-and-monte-carlo) · [Module 20 →](../20-ADVANCED-PROBABILITY/README.md)
