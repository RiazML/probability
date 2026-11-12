# 18.3 Markov Chains

[Probability](../../README.md) / [Module 18: Stochastic Processes](../README.md) / 18.3 Markov Chains

> **Big idea:** A Markov chain forgets its past, so one table of one-step probabilities tells where it goes, which states it keeps visiting, how it spends its time in the long run, and how fast it forgets where it started.

The Markov chain is the workhorse of stochastic processes. This section builds it in three parts. First, the definition and the matrix (18.3.1 and 18.3.2). Second, the structure of the states (18.3.3 and 18.3.4). Third, the long run: stationary distributions, detailed balance, absorbing chains and convergence (18.3.5 to 18.3.8). All files use the 3-state weather chain (Sunny, Cloudy, Rainy) as the running example, and the last files add a PageRank toy web and a Snakes and Ladders board. Read the topics in order: each one uses the one before it. The recurrence idea in [18.3.3](18.3.3-Classification-of-States.md) comes from [18.2.4](../18.2-Random-Walks/18.2.4-Recurrence-and-Transience.md).

## Topics

| # | Topic | What it is about |
|---|---|---|
| 18.3.1 | [Markov Property](18.3.1-Markov-Property.md) | Given the present, the future does not depend on the past; the probability of a path is a product of one-step probabilities |
| 18.3.2 | [Transition Matrix and N-Step Transitions](18.3.2-Transition-Matrix-and-N-Step-Transitions.md) | The matrix $P$, Chapman-Kolmogorov, and the law at time $n$ as $\mu_0 P^n$ |
| 18.3.3 | [Classification of States](18.3.3-Classification-of-States.md) | Communicating classes, recurrent and transient states, closed classes |
| 18.3.4 | [Irreducible and Aperiodic Chains](18.3.4-Irreducible-and-Aperiodic-Chains.md) | One class, no rhythm, and why that means that $P^n$ becomes strictly positive |
| 18.3.5 | [Stationary Distribution](18.3.5-Stationary-Distribution.md) | The law $\pi = \pi P$: it exists and is unique for a finite irreducible chain, and $\pi_i$ is $1/m_i$ |
| 18.3.6 | [Detailed Balance and Reversibility](18.3.6-Detailed-Balance-and-Reversibility.md) | Balancing each pair of states: a shortcut to $\pi$ for walks on graphs and queues |
| 18.3.7 | [Absorbing Chains](18.3.7-Absorbing-Chains.md) | The fundamental matrix: expected game length for Snakes and Ladders, and absorption probabilities |
| 18.3.8 | [Convergence to Equilibrium](18.3.8-Convergence-to-Equilibrium.md) | The law of $X_n$ tends to $\pi$ at the speed of the second eigenvalue; PageRank |

---

[↑ Module 18: Stochastic Processes](../README.md)
