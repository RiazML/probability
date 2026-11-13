# Module 18: Stochastic Processes

[Probability](../README.md) / Module 18

**Level:** 5 (Hero) · **Time:** about 2.5 weeks · **Importance:** ★★★★☆

> **Big idea:** A stochastic process is a random variable that evolves in time; its path is built from independent steps, exponential clocks or one table of transition rules, and the same few tools answer where it goes, how long it stays, and whether it ever comes back or dies out.

---

## What You Will Learn

After this module you will be able to:

- Describe a stochastic process by its time set, its state space and its sample paths, and tell its four basic types apart.
- Solve problems on random walks: position, gambler's ruin, the reflection principle, and recurrence and transience.
- Write the transition matrix of a Markov chain, compute $n$-step probabilities, classify states, and find the stationary distribution, absorption times and the speed of convergence (PageRank and Snakes and Ladders are the examples).
- Build a continuous-time Markov chain from exponential holding times and find its stationary law from $\pi Q = 0$.
- Use the Poisson process: Poisson counts, exponential gaps, splitting, merging, and uniform arrival times given the count.
- Find the extinction probability of a branching process as the smallest root of $q = G(q)$, and analyse an M/M/1 queue with Little's law.
- Describe Brownian motion as the limit of a random walk, and simulate every process in this module.

## Before You Start

You should be comfortable with:

- [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md): the Law of Large Numbers (long-run averages) and the Central Limit Theorem (the walk becomes normal).
- [Module 15: Generating Functions](../15-GENERATING-FUNCTIONS/README.md): the probability generating function, used for branching processes.
- [Module 14: Conditional Expectation](../14-CONDITIONAL-EXPECTATION/README.md): first-step equations and random sums.
- [Module 09: Continuous Distributions](../09-CONTINUOUS-DISTRIBUTIONS/README.md) and [Module 07: Discrete Distributions](../07-DISCRETE-DISTRIBUTIONS/README.md): the exponential, gamma, normal, binomial and Poisson laws.
- A little matrix multiplication (row vector times matrix). It is explained again when it is first needed, in [18.3.2](18.3-Markov-Chains/18.3.2-Transition-Matrix-and-N-Step-Transitions.md).

## Topics

| # | Topic | What it is about |
|---|---|---|
| 18.1 | [What is a Stochastic Process](18.1-What-is-a-Stochastic-Process.md) | A family of random variables $X_t$; sample paths, increments, and why single-time laws are not enough |
| 18.2 | [Random Walks](18.2-Random-Walks/README.md) | The simple walk, gambler's ruin, the reflection principle, recurrence and transience (a section with 4 topics) |
| 18.3 | [Markov Chains](18.3-Markov-Chains/README.md) | The Markov property, the transition matrix, classes of states, stationary law, detailed balance, absorption, convergence (a section with 8 topics) |
| 18.4 | [Continuous-Time Markov Chains](18.4-Continuous-Time-Markov-Chains.md) | Exponential holding times, the generator $Q$, Kolmogorov equations, and $\pi Q = 0$ |
| 18.5 | [Poisson Process](18.5-Poisson-Process.md) | Arrivals at a constant rate: Poisson counts, exponential gaps, splitting and merging, uniform arrival times |
| 18.6 | [Branching Processes](18.6-Branching-Processes.md) | Families that grow by random offspring; the extinction probability is the smallest root of $q = G(q)$ |
| 18.7 | [Queues Intuition](18.7-Queues-Intuition.md) | The M/M/1 queue: load $\rho$, the geometric stationary law, mean waiting time and Little's law |
| 18.8 | [Brownian Motion](18.8-Brownian-Motion.md) | The limit of the random walk: normal increments, $\operatorname{Cov} = \min(s, t)$, rough paths |
| 18.9 | [Practice Problems](18.9-Practice-Problems.md) | Mixed problems, proofs and simulation projects for the whole module |

## Map of This Module

```text
                     18.1 What is a stochastic process?
                  /                |                  \
                 v                 v                   v
        18.2 Random walks   18.3 Markov chains   18.6 Branching processes
                 |                 |                  (needs the PGF, 15.5)
                 |                 v
                 |          18.4 Continuous-time
                 |            Markov chains
                 |                 |
                 |                 v
                 |          18.5 Poisson process
                 |                 |
                 v                 v
         18.8 Brownian      18.7 Queues (M/M/1)
            motion
                  \                |                  /
                   v               v                 v
                         18.9 Practice problems
```

Time goes in steps (18.2, 18.3, 18.6) or flows continuously (18.4, 18.5, 18.7, 18.8). The Poisson process is the simplest continuous-time chain, and a queue is a continuous-time chain fed by a Poisson process. Brownian motion is what a random walk turns into when the steps become tiny.

## Key Formulas

| Name | Formula |
|---|---|
| Covariance of a random walk | $\operatorname{Cov}(S_m, S_n) = \sigma^2 \min(m, n)$ |
| Simple walk | $S_n = 2K_n - n$, $\operatorname{Var}(S_n) = 4npq$ |
| Gambler's ruin (fair game, start $k$, stop at 0 or $N$) | $P(\text{reach } N) = \frac{k}{N}$, expected duration $k(N - k)$ |
| Reflection principle | $P(M_n \ge m) = 2P(S_n \gt m) + P(S_n = m)$ |
| Markov chain path | $P(X_0 = i_0, \dots, X_n = i_n) = \mu_0(i_0) \thinspace p_{i_0 i_1} \cdots p_{i_{n-1} i_n}$ |
| $n$ steps | $\mu_n = \mu_0 P^n$, $\quad P^{m+n} = P^m P^n$ |
| Stationary law | $\pi = \pi P$, $\quad \sum_i \pi_i = 1$, $\quad \pi_i = \frac{1}{m_i}$ (mean return time) |
| Detailed balance | $\pi_i \thinspace p_{ij} = \pi_j \thinspace p_{ji} \implies \pi = \pi P$ |
| Absorbing chain ($Q$ is the block of transient states) | $N = (I - Q)^{-1}$, expected time to absorption $\mathbf{t} = N \mathbf{1}$ |
| Convergence to $\pi$ | $d(n) \approx c \lvert \lambda_2 \rvert^n \to 0$ |
| Continuous-time chain (generator $Q$, rows sum to 0) | $P(t) = e^{tQ}$, $\quad \pi Q = 0$ |
| Poisson process | $N(t) \sim \text{Pois}(\lambda t)$, gaps $\overset{\text{iid}}{\sim} \text{Exp}(\lambda)$ |
| Splitting and merging | rates $p \lambda$ and $(1 - p) \lambda$; merged rate $\lambda_1 + \lambda_2$ |
| Branching process | $E[Z_n] = m^n$; $q$ = smallest root in $[0, 1]$ of $q = G(q)$; $q = 1 \iff m \le 1$ |
| M/M/1 queue ($\rho = \frac{\lambda}{\mu} \lt 1$) | $\pi_n = (1 - \rho) \rho^n$, $\quad L = \frac{\rho}{1 - \rho}$, $\quad W = \frac{1}{\mu - \lambda}$ |
| Little's law | $L = \lambda W$ |
| Brownian motion | $B(t) - B(s) \sim \mathcal{N}(0, t - s)$, $\quad \operatorname{Cov}(B(s), B(t)) = \min(s, t)$ |

## Study Tips

- The hardest topics are the stationary distribution and convergence ([18.3.5](18.3-Markov-Chains/18.3.5-Stationary-Distribution.md), [18.3.8](18.3-Markov-Chains/18.3.8-Convergence-to-Equilibrium.md)) and the extinction proof in [18.6](18.6-Branching-Processes.md). Read each proof once for the idea (a balance of flows, a limit of $q_n$), then solve the worked example without looking.
- Start every problem by naming the **state** and the **time**. For a Markov chain, write the transition matrix or the rate matrix first. For a first-step problem, write one equation per state.
- The most useful problems in [18.9](18.9-Practice-Problems.md) are C1 (first-step equations), C3 (the balance equations of a continuous chain), C5 (the root of $q = G(q)$), and the proofs H1 and H3 (the inspection paradox and the waiting time of a queue).
- Classic mistakes to watch for: taking the root 1 as the extinction probability; confusing a **rate** with a **probability**; forgetting that rows of $P$ sum to 1 but rows of $Q$ sum to 0; using the standard deviation where a Brownian motion needs the variance; and using queue formulas when $\rho \ge 1$.
- Simulate. Every process here is a few lines of Python, and the simulation is the fastest way to find a mistake in a formula.

## Where This Leads

- [Module 19: Simulation and Monte Carlo](../19-SIMULATION-AND-MONTE-CARLO/README.md) uses these processes. MCMC ([19.7](../19-SIMULATION-AND-MONTE-CARLO/19.7-MCMC/README.md)) builds a Markov chain whose stationary distribution is the target, and the exponential-gap recipe of [18.5](18.5-Poisson-Process.md) is how event simulations run.
- [Module 20: Advanced Probability](../20-ADVANCED-PROBABILITY/README.md) turns the fair walk, the gambler's fortune and Brownian motion into **martingales** ([20.8](../20-ADVANCED-PROBABILITY/20.8-Martingales.md)) and proves gambler's ruin again with stopping times.
- [Module 21: Applications of Probability](../21-APPLICATIONS-OF-PROBABILITY/README.md) uses language models and reinforcement learning (Markov chains), queues and networks, and share prices (Brownian motion).
- In AI and machine learning: PageRank and text generators are Markov chains, hidden Markov models and reinforcement learning are built on them, and diffusion models for images add noise as a discretized Brownian motion.

---

[← Module 17](../17-LIMIT-THEOREMS/README.md) · [Syllabus](../SYLLABUS.md#module-18-stochastic-processes) · [Module 19 →](../19-SIMULATION-AND-MONTE-CARLO/README.md)
