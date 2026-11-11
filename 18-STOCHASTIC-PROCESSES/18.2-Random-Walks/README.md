# 18.2 Random Walks

[Probability](../../README.md) / [Module 18: Stochastic Processes](../README.md) / 18.2 Random Walks

> **Big idea:** A random walk adds up independent steps, and four questions about it (where it is, whether it hits a wall, how high it goes, whether it comes home) are answered by one binomial formula, one first-step equation, one mirror trick and one series test.

The random walk is the simplest stochastic process that is not trivial, and it is the skeleton of Markov chains and of Brownian motion. This section studies the simple walk that moves $+1$ or $-1$ at each step. Read the four topics in order: each one uses the one before it. [18.2.2](18.2.2-Gamblers-Ruin.md) builds on the ruin formula of [4.11.5](../../04-CONDITIONAL-PROBABILITY-AND-BAYES/4.11-Classic-Puzzles/4.11.5-Gamblers-Ruin.md), and [18.2.4](18.2.4-Recurrence-and-Transience.md) uses the reflection counting of [18.2.3](18.2.3-Reflection-Principle.md).

## Topics

| # | Topic | What it is about |
|---|---|---|
| 18.2.1 | [Simple Random Walk](18.2.1-Simple-Random-Walk.md) | The position $S_n = 2K - n$ is a binomial in disguise, and a fair walk is about $\sqrt{n}$ away from the start |
| 18.2.2 | [Gambler's Ruin](18.2.2-Gamblers-Ruin.md) | Expected duration $k(N-k)$, the biased game, and ruin against unlimited money |
| 18.2.3 | [Reflection Principle](18.2.3-Reflection-Principle.md) | Mirror paths give the distribution of the maximum, first passage times and the ballot theorem |
| 18.2.4 | [Recurrence and Transience](18.2.4-Recurrence-and-Transience.md) | Does the walk come back? Yes on a line and a plane, not always in space or with a bias |

---

[↑ Module 18: Stochastic Processes](../README.md)
