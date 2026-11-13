# 19.7 MCMC

[Probability](../../README.md) / [Module 19: Simulation and Monte Carlo](../README.md) / 19.7 MCMC

> **Big idea:** When we cannot sample a distribution directly, we build a Markov chain whose long-run behaviour is that distribution (Metropolis-Hastings, Gibbs), run it, and then check carefully that the samples can be trusted.

**Markov chain Monte Carlo** (MCMC) takes the stationary distribution of [18.3.5](../../18-STOCHASTIC-PROCESSES/18.3-Markov-Chains/18.3.5-Stationary-Distribution.md) and turns it around: instead of finding the stationary law of a given chain, we design a chain whose stationary law is the target. Detailed balance ([18.3.6](../../18-STOCHASTIC-PROCESSES/18.3-Markov-Chains/18.3.6-Detailed-Balance-and-Reversibility.md)) is the tool that makes the design easy. Read the three topics in order. [19.7.1](19.7.1-Metropolis-Hastings.md) gives the general accept-or-reject recipe. [19.7.2](19.7.2-Gibbs-Sampling.md) is the special case where each move draws one coordinate from its exact conditional and is always accepted. [19.7.3](19.7.3-Burn-in-Mixing-and-Diagnostics.md) explains why the samples are correlated, how many of them are worth keeping, and how to detect a chain that has not converged.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 19.7.1 | [Metropolis-Hastings](19.7.1-Metropolis-Hastings.md) | Propose a move and accept it with probability $\min(1, \frac{\tilde{p}(x') q(x \mid x')}{\tilde{p}(x) q(x' \mid x)})$; detailed balance makes the target stationary |
| 19.7.2 | [Gibbs Sampling](19.7.2-Gibbs-Sampling.md) | Redraw one coordinate at a time from its full conditional; every move is accepted |
| 19.7.3 | [Burn-in, Mixing and Diagnostics](19.7.3-Burn-in-Mixing-and-Diagnostics.md) | Discard the start-up, measure the effective sample size, and compare chains with R-hat |

---

[↑ Module 19: Simulation and Monte Carlo](../README.md)
