# Module 20: Advanced Probability (Measure Theory)

[Probability](../README.md) / Module 20

**Level:** 5 (Hero) · **Time:** about 3 weeks · **Importance:** ★★★☆☆ (optional for most readers)

> **Big idea:** Measure theory chooses exactly which sets may have a probability (a $\sigma$-algebra), makes expectation an integral, and turns "almost surely", "infinitely often" and "a fair game" into precise statements with short, rigorous proofs.

---

## What You Will Learn

This module is optional. You can use probability well without it. It is here for the reader who wants to know **why** the rules of Modules 01 to 19 are safe, and who wants to read research papers.

After this module you will be able to:

- Explain why not every subset of $[0, 1]$ can have a length, and define a $\sigma$-algebra and a probability space $(\Omega, \mathcal{F}, P)$.
- Treat a random variable as a measurable function, and find the information $\sigma(X)$ that it carries.
- Define expectation as a Lebesgue integral, and use the monotone, Fatou and dominated convergence theorems to swap limits and expectations.
- Prove and apply the Borel-Cantelli lemmas, and recognize tail events with Kolmogorov's zero-one law.
- Define martingales and stopping times, show that no betting system beats a fair game, and prove the gambler's ruin probability $\frac{k}{N}$ with optional stopping.
- Explain where densities come from (Radon-Nikodym), and why the Cantor distribution has none.
- Check each result with a Python simulation.

## Before You Start

You should be comfortable with:

- [Module 03: Axioms of Probability](../03-AXIOMS-OF-PROBABILITY/README.md): the three axioms and continuity of probability ([3.9](../03-AXIOMS-OF-PROBABILITY/3.9-Continuity-of-Probability.md)).
- [Module 05: Discrete Random Variables](../05-DISCRETE-RANDOM-VARIABLES/README.md) and [Module 08: Continuous Random Variables](../08-CONTINUOUS-RANDOM-VARIABLES/README.md): random variables, densities, expectation.
- [Module 14: Conditional Expectation](../14-CONDITIONAL-EXPECTATION/README.md): $E[Y \mid X]$ as a random variable, the tower rule and taking out what is known.
- [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md): almost sure convergence and the Strong Law.
- [Module 18: Stochastic Processes](../18-STOCHASTIC-PROCESSES/README.md): the random walk and gambler's ruin ([18.2.2](../18-STOCHASTIC-PROCESSES/18.2-Random-Walks/18.2.2-Gamblers-Ruin.md)).
- [Module 19: Simulation and Monte Carlo](../19-SIMULATION-AND-MONTE-CARLO/README.md): the previous module. The importance weight of [19.6](../19-SIMULATION-AND-MONTE-CARLO/19.6-Importance-Sampling.md) appears again in [20.10](20.10-Radon-Nikodym-and-Densities.md).
- A comfort with proofs. Some arguments here are short but need care. Each one is in plain steps.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 20.1 | [Why Measure Theory](20.1-Why-Measure-Theory.md) | Vitali's set: no length for every subset; "uniform on whole numbers" fails |
| 20.2 | [Sigma-Algebras and Measurable Spaces](20.2-Sigma-Algebras-and-Measurable-Spaces.md) | The allowed events; information as a partition; the Borel sets |
| 20.3 | [Probability Measures](20.3-Probability-Measures.md) | $(\Omega, \mathcal{F}, P)$, continuity, uniqueness, and the infinite coin from one uniform number |
| 20.4 | [Random Variables as Measurable Functions](20.4-Random-Variables-as-Measurable-Functions.md) | Measurability, the law $P_X$, $\sigma(X)$, and independence |
| 20.5 | [Lebesgue Integral and Expectation](20.5-Lebesgue-Integral-and-Expectation.md) | $E[X] = \int X \thinspace dP$ and the three convergence theorems |
| 20.6 | [Borel-Cantelli Lemmas](20.6-Borel-Cantelli-Lemmas.md) | Finite sum: finitely often. Independent and infinite sum: infinitely often |
| 20.7 | [Kolmogorov's Zero-One Law](20.7-Kolmogorov-Zero-One-Law.md) | Tail events of independent variables have probability 0 or 1 |
| 20.8 | [Martingales](20.8-Martingales.md) | Fair games, betting systems, and the full proof of McDiarmid's inequality |
| 20.9 | [Stopping Times and Optional Stopping](20.9-Stopping-Times-and-Optional-Stopping.md) | Stopping a fair game; gambler's ruin in a few lines; Wald's identity |
| 20.10 | [Radon-Nikodym and Densities](20.10-Radon-Nikodym-and-Densities.md) | A density is a ratio of measures; mixed and singular laws; importance weights |
| 20.11 | [Practice Problems](20.11-Practice-Problems.md) | Mixed problems, proofs and simulation projects for the whole module |

## Map of This Module

```text
   20.1 Why measure theory (Vitali)
            |
            v
   20.2 Sigma-algebras  -->  20.3 Probability measures
                                   |
              +--------------------+---------------------+
              |                    |                     |
              v                    v                     v
   20.4 Random variables     20.6 Borel-Cantelli    20.10 Radon-Nikodym
              |                    |                     |
              v                    v                     |
   20.5 Lebesgue integral    20.7 Zero-one law           |
        and expectation                                  |
              |                                          |
              +---------------------+--------------------+
                                    |
                                    v
                         20.8 Martingales
                                    |
                                    v
                         20.9 Stopping times
                                    |
                                    v
                         20.11 Practice problems
```

Start at the top. Each arrow means "you need this first". Topics 20.6 and 20.7 need only 20.3 and the expectation of 20.5 for one proof. Topic 20.8 uses conditional expectation, which exists by 20.10, but you can read 20.8 without reading the proof of existence.

## Key Formulas

| Name | Formula |
|---|---|
| $\sigma$-algebra | $\Omega \in \mathcal{F}$; $A \in \mathcal{F} \implies A^c \in \mathcal{F}$; $A_1, A_2, \dots \in \mathcal{F} \implies \bigcup_n A_n \in \mathcal{F}$ |
| Probability space | $(\Omega, \mathcal{F}, P)$ with $P\big( \bigcup_n A_n \big) = \sum_n P(A_n)$ for disjoint $A_n$, and $P(\Omega) = 1$ |
| Random variable | $X^{-1}(B) \in \mathcal{F}$ for every Borel set $B$; law $P_X(B) = P(X \in B)$ |
| Expectation | $E[X] = \int X \thinspace dP$, and $E[g(X)] = \int g \thinspace dP_X$ |
| Dominated convergence | $X_n \to X$ a.s. and $\lvert X_n \rvert \le Y$ with $E[Y] \lt \infty$ imply $E[X_n] \to E[X]$ |
| Borel-Cantelli 1 | $\sum_n P(A_n) \lt \infty \implies P(A_n \text{ i.o.}) = 0$ |
| Borel-Cantelli 2 | $A_n$ independent, $\sum_n P(A_n) = \infty \implies P(A_n \text{ i.o.}) = 1$ |
| Zero-one law | independent $X_n$ and a tail event $A$ imply $P(A) \in \lbrace 0, 1 \rbrace$ |
| Martingale | $E[M_{n+1} \mid \mathcal{F}_n] = M_n$ |
| Optional stopping | $E[M_T] = E[M_0]$ (under suitable conditions) |
| Gambler's ruin | $P(\text{reach } N) = \frac{k}{N}$, and $E[T] = k(N - k)$ in a fair game |
| Wald's identity | $E[S_T] = E[X_1] \thinspace E[T]$ for a stopping time $T$ |
| Azuma-Hoeffding / McDiarmid | $P(f - E[f] \ge t) \le \exp\left( -\frac{2t^2}{\sum c_i^2} \right)$ |
| Density | $\nu(A) = \int_A f \thinspace d\mu$, with $f = \frac{d\nu}{d\mu}$ |

## Study Tips

- Do not try to read all eleven topics in one week. Each topic has a main result and a proof of it. Learn the **statement** first, check it on the simple example (a die, a coin), and only then read the proof.
- The topics that pay off most are 20.6 (Borel-Cantelli), 20.8 (martingales) and 20.9 (optional stopping). If time is short, read 20.1 for the motivation, then jump to these.
- Always ask in a proof: which tool turns an infinite statement into a countable one? The usual answers are countable subadditivity, a Borel-Cantelli lemma, or a convergence theorem.
- Classic mistakes: using the second Borel-Cantelli lemma without independence, swapping a limit and an expectation without a dominating variable, and applying optional stopping without checking that the stopped process is bounded.
- The most important practice problems are the gambler's ruin by optional stopping (20.9 and C4 in [20.11](20.11-Practice-Problems.md)), the proof of the second Borel-Cantelli lemma, and the Polya urn martingale.

## Where This Leads

- [Module 21: Applications of Probability](../21-APPLICATIONS-OF-PROBABILITY/README.md) uses these ideas behind the scenes: concentration bounds in learning theory, martingales in finance, and importance weights in reinforcement learning.
- In AI and machine learning, convergence proofs for stochastic gradient descent and Q-learning use martingale convergence and Borel-Cantelli, and generalization bounds use McDiarmid's inequality ([20.8](20.8-Martingales.md)).
- In mathematical finance, the fair price of an asset is a martingale, and the change of measure of [20.10](20.10-Radon-Nikodym-and-Densities.md) moves between real and risk-neutral probabilities.
- For further reading: a graduate textbook on probability theory (for example Williams, *Probability with Martingales*, or Durrett, *Probability: Theory and Examples*) continues with the central limit theorem by characteristic functions, Brownian motion and stochastic integrals.

---

[← Module 19](../19-SIMULATION-AND-MONTE-CARLO/README.md) · [Syllabus](../SYLLABUS.md#module-20-advanced-probability-measure-theory) · [Module 21 →](../21-APPLICATIONS-OF-PROBABILITY/README.md)
