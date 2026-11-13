# 21.3 Computer Science

[Probability](../../README.md) / [Module 21: Applications of Probability](../README.md) / 21.3 Computer Science

> **Big idea:** Computer science uses probability in two ways: as a tool to build faster algorithms (flip coins inside the program), and as a model to predict how a system behaves (what happens on average, and how long a line gets).

Many fast algorithms and data structures flip coins on purpose. A random pivot, a random hash function or a random check makes a bad input rare instead of fatal, and the analysis is a short calculation with expectation. The other use is on the outside: we do not control the data, but we can say what is typical, and a model of arrivals and service times tells us how long a queue will be. This section shows both uses with four small, real examples that you can run in a few lines of numpy.

Read the files in order. 21.3.1 introduces the main trick (the indicator trick and linearity of expectation). 21.3.2 uses counting and the birthday problem for hash tables and Bloom filters. 21.3.3 asks what "average" means when we analyze an algorithm. 21.3.4 ends with queues and networks, where a Poisson process and a Markov chain give the answer.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 21.3.1 | [Randomized Algorithms](21.3.1-Randomized-Algorithms.md) | Random pivot quicksort has about $2 n \ln n$ expected comparisons, and a random check makes a wrong answer unlikely |
| 21.3.2 | [Hashing and Bloom Filters](21.3.2-Hashing-and-Bloom-Filters.md) | Collisions and the birthday problem, and the false positive rate of a Bloom filter |
| 21.3.3 | [Average-Case Analysis](21.3.3-Average-Case-Analysis.md) | Expected cost over a random input, with linear search and the number of records of a random list |
| 21.3.4 | [Networks and Queues](21.3.4-Networks-and-Queues.md) | Poisson arrivals, the M/M/1 queue, the mean number $\frac{\rho}{1 - \rho}$, and Little's law |

---

[↑ Module 21: Applications of Probability](../README.md)
