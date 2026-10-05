# Module 04: Conditional Probability, Independence and Bayes

[Probability](../README.md) / Module 04

**Level:** 1 (Zero) · **Time:** about 2 weeks · **Importance:** ★★★★★

> **Big idea:** Conditional probability is how you update what you believe when you learn something new, and Bayes' theorem is the rule that turns "how likely is this evidence if my idea is true" into "how likely is my idea now that I have seen the evidence".

---

## What You Will Learn

After this module you will be able to:

- Compute conditional probabilities by shrinking the sample space, and tell
  $P(A \mid B)$ apart from $P(B \mid A)$.
- Break hard problems into cases with the chain rule, the law of total probability
  and tree diagrams.
- Apply Bayes' theorem with natural frequencies, Bayes tables and the odds form, and
  update beliefs one piece of evidence at a time.
- Decide whether events are independent, pairwise independent, mutually independent
  or conditionally independent, and explain why the difference matters.
- Solve and explain classic puzzles: Monty Hall, medical testing, the prosecutor's
  fallacy, Simpson's paradox and gambler's ruin.
- Simulate conditional probabilities in Python by filtering on the condition.

## Before You Start

You should be comfortable with:

- [Module 01: Sets, Sample Spaces and Events](../01-SETS-SAMPLE-SPACES-AND-EVENTS/README.md):
  intersections, complements and partitions.
- [Module 02: Counting](../02-COUNTING/README.md): counting outcomes, for problems with
  cards and draws without replacement.
- [Module 03: Axioms of Probability](../03-AXIOMS-OF-PROBABILITY/README.md): the axioms,
  the complement rule and the addition rule.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 4.1 | [Conditional Probability](4.1-Conditional-Probability.md) | Learning B happened: keep only B and rescale |
| 4.2 | [Multiplication Rule and Chain Rule](4.2-Multiplication-Rule-and-Chain-Rule.md) | The chance that several things all happen, step by step |
| 4.3 | [Law of Total Probability](4.3-Law-of-Total-Probability.md) | Split into cases, solve each, take the weighted average |
| 4.4 | [Bayes' Theorem](4.4-Bayes-Theorem.md) | Prior, likelihood, evidence, posterior: learning from evidence |
| 4.5 | [Odds Form of Bayes](4.5-Odds-Form-of-Bayes.md) | Posterior odds = likelihood ratio x prior odds |
| 4.6 | [Sequential Bayesian Updating](4.6-Sequential-Bayesian-Updating.md) | Today's posterior is tomorrow's prior |
| 4.7 | [Independence](4.7-Independence.md) | When one event tells you nothing about another |
| 4.8 | [Pairwise vs Mutual Independence](4.8-Pairwise-vs-Mutual-Independence.md) | Independent in pairs does not mean independent as a group |
| 4.9 | [Conditional Independence](4.9-Conditional-Independence.md) | Common causes, common effects and explaining away |
| 4.10 | [Tree Diagrams](4.10-Tree-Diagrams.md) | Multiply along, add across, divide to condition |
| 4.11 | [Classic Puzzles](4.11-Classic-Puzzles/README.md) | Monty Hall, medical tests, the prosecutor's fallacy, Simpson's paradox, gambler's ruin |
| 4.12 | [Practice Problems](4.12-Practice-Problems.md) | Mixed problems for the whole module |

## Map of This Module

```text
                    4.1 Conditional probability
                                |
                                v
                 4.2 Multiplication rule / chain rule
                                |
                                v
                   4.3 Law of total probability
                       /                 \
                      v                   v
             4.4 Bayes' theorem      4.7 Independence
                 |                        |
                 v                        v
         4.5 Odds form          4.8 Pairwise vs mutual
                 |                        |
                 v                        v
     4.6 Sequential updating <--- 4.9 Conditional independence
                 \                        /
                  v                      v
                       4.10 Tree diagrams
                                |
                                v
       4.11 Classic puzzles (Monty Hall, medical testing,
            prosecutor's fallacy, Simpson's paradox,
            gambler's ruin)
                                |
                                v
                     4.12 Practice problems
```

Start at the top; each arrow means "you need this first". Sequential updating uses
conditional independence, so you may read 4.9 before or right after 4.6.

## Key Formulas

| Name | Formula |
|---|---|
| Conditional probability | $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$, with $P(B) \gt 0$ |
| Multiplication rule | $P(A \cap B) = P(A) \thinspace P(B \mid A)$ |
| Chain rule | $P(A_1 \cap \dots \cap A_n) = P(A_1) P(A_2 \mid A_1) \cdots P(A_n \mid A_1 \cap \dots \cap A_{n-1})$ |
| Law of total probability | $P(A) = \sum_{i} P(A \mid B_i) P(B_i)$, for a partition $B_1, \dots, B_n$ |
| Bayes' theorem | $P(H \mid E) = \frac{P(E \mid H) P(H)}{P(E)}$ |
| Bayes, many hypotheses | $P(H_j \mid E) = \frac{P(E \mid H_j) P(H_j)}{\sum_{i} P(E \mid H_i) P(H_i)}$ |
| Odds form | $\frac{P(H \mid E)}{P(H^c \mid E)} = \frac{P(E \mid H)}{P(E \mid H^c)} \cdot \frac{P(H)}{P(H^c)}$ |
| Independence | $P(A \cap B) = P(A) P(B)$, same as $P(A \mid B) = P(A)$ |
| Conditional independence | $P(A \cap B \mid C) = P(A \mid C) P(B \mid C)$ |
| Gambler's ruin (fair game) | $P(\text{reach } N \text{ from } k) = \frac{k}{N}$ |

## Study Tips

- **Bayes' theorem (4.4) is the heart of the module.** Solve every Bayes problem three
  ways until they feel the same: natural frequencies ("out of 10,000 people ..."), a
  tree or a Bayes table, and the odds form.
- **Always ask "given what?"** Before you compute, say the conditional probability in
  words and check which event is known. Swapping $P(A \mid B)$ and $P(B \mid A)$ is the
  most common error in all of probability.
- **Check your answers.** Posteriors add up to 1; a total probability lies between
  its case rates; tree leaves add up to 1.
- **Simulate.** In code, conditioning is filtering: `A[B].mean()`. When a puzzle feels
  wrong (Monty Hall!), simulate it.
- **The practice problems that matter most:** the medical test with different
  prevalences, Monty Hall with Bayes, the pairwise-but-not-mutual example, and
  gambler's ruin by first-step analysis.

## Where This Leads

- [Module 05: Discrete Random Variables](../05-DISCRETE-RANDOM-VARIABLES/README.md)
  turns outcomes into numbers; independence of events becomes independence of random
  variables in [Module 10](../10-JOINT-DISTRIBUTIONS/README.md).
- [10.7 Bayes for Random Variables](../10-JOINT-DISTRIBUTIONS/10.7-Bayes-for-Random-Variables.md)
  uses Bayes' theorem to learn unknown parameters from data, and
  [Module 14](../14-CONDITIONAL-EXPECTATION/README.md) extends conditioning to averages.
- [Module 18: Stochastic Processes](../18-STOCHASTIC-PROCESSES/README.md) builds on
  first-step analysis and the chain rule (Markov chains, random walks).
- In AI and computer science: Naive Bayes spam filters, language models (the chain
  rule), Bayesian networks (conditional independence), A/B testing and anomaly
  detection all rest on this module.

---

[← Module 03](../03-AXIOMS-OF-PROBABILITY/README.md) · [Syllabus](../SYLLABUS.md#module-04-conditional-probability-independence-and-bayes) · [Module 05 →](../05-DISCRETE-RANDOM-VARIABLES/README.md)
