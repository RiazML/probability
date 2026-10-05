# Module 02: Counting

[Probability](../README.md) / Module 02

**Level:** 1 (Zero) · **Time:** about 1 week · **Importance:** ★★★★☆

> **Big idea:** When all outcomes are equally likely, a probability is one count divided by another, and a few counting tools let you find both counts without listing anything.

---

## What You Will Learn

After this module you will be able to:

- Count outcomes with the multiplication rule and the addition rule.
- Choose the right formula for ordered or unordered samples, with or without
  replacement.
- Count splits and arrangements with stars and bars and multinomial coefficients.
- Correct double counting with inclusion-exclusion, and prove certainty with the
  pigeonhole principle.
- Prove binomial identities by counting the same set in two ways.
- Solve and simulate the classic problems: birthdays, derangements and poker hands.

## Before You Start

You should be comfortable with:

- [Module 01: Sets, Sample Spaces and Events](../01-SETS-SAMPLE-SPACES-AND-EVENTS/README.md):
  sample spaces, events as sets, unions, intersections and complements, and the counting
  rule $P(A) = \frac{\text{outcomes in } A}{\text{all outcomes}}$ from
  [1.1 What is Probability](../01-SETS-SAMPLE-SPACES-AND-EVENTS/1.1-What-is-Probability.md).

## Topics

| # | Topic | What it is about |
|---|---|---|
| 2.1 | [Multiplication and Addition Rules](2.1-Multiplication-and-Addition-Rules.md) | "And then" multiplies; "or" (with no overlap) adds |
| 2.2 | [Permutations](2.2-Permutations.md) | Ordered arrangements without repeats, $n!$, and Stirling's approximation |
| 2.3 | [Combinations](2.3-Combinations.md) | Unordered groups: n choose k |
| 2.4 | [Sampling With Replacement](2.4-Sampling-With-Replacement.md) | $n^k$ sequences, multisets, and the full counting table |
| 2.5 | [Stars and Bars](2.5-Stars-and-Bars.md) | Splitting identical items among labeled boxes |
| 2.6 | [Multinomial Coefficients](2.6-Multinomial-Coefficients.md) | Splitting into several groups; words with repeated letters |
| 2.7 | [Binomial Theorem and Pascal's Triangle](2.7-Binomial-Theorem-and-Pascals-Triangle.md) | The coefficients of $(x + y)^n$ and the triangle that builds them |
| 2.8 | [Inclusion-Exclusion](2.8-Inclusion-Exclusion.md) | Counting a union of overlapping sets exactly |
| 2.9 | [Pigeonhole Principle](2.9-Pigeonhole-Principle.md) | More objects than boxes forces a collision |
| 2.10 | [Story Proofs](2.10-Story-Proofs.md) | Proving identities by counting one set in two ways |
| 2.11 | [Classic Counting Problems](2.11-Classic-Counting-Problems/README.md) | Birthday problem, derangements and poker hands (a subfolder) |
| 2.12 | [Practice Problems](2.12-Practice-Problems.md) | Mixed problems and simulation projects for the whole module |

## Map of This Module

```text
                 2.1 Multiplication and addition rules
                                  |
              +-------------------+-------------------+
              v                   v                   v
       2.2 Permutations    2.4 With replacement   2.9 Pigeonhole
              |                   |
              v                   v
       2.3 Combinations -----> 2.5 Stars and bars
              |
     +--------+-----------+--------------------+
     v                    v                    v
 2.6 Multinomial   2.7 Binomial theorem   2.8 Inclusion-exclusion
                          |                    |
                          v                    |
                   2.10 Story proofs           |
                          |                    |
                          v                    v
       2.11 Classic problems: birthday, derangements, poker
                                  |
                                  v
                       2.12 Practice problems
```

Start at the top. Each arrow means "you need this first".

## Key Formulas

| Name | Formula |
|---|---|
| Multiplication rule | $\lvert A \times B \rvert = \lvert A \rvert \cdot \lvert B \rvert$ |
| Ordered, no replacement | $\frac{n!}{(n-k)!} = n (n-1) \cdots (n-k+1)$ |
| Unordered, no replacement | $\binom{n}{k} = \frac{n!}{k! \thinspace (n-k)!}$ |
| Ordered, with replacement | $n^k$ |
| Unordered, with replacement | $\binom{n+k-1}{k}$ |
| Stars and bars | solutions of $x_1 + \dots + x_r = n$ with all $x_i \ge 0$: $\binom{n+r-1}{r-1}$ |
| Multinomial coefficient | $\frac{n!}{n_1! \thinspace n_2! \cdots n_r!}$ with $n_1 + \dots + n_r = n$ |
| Binomial theorem | $(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$ |
| Pascal's rule | $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ |
| Inclusion-exclusion | $\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert$ |
| Stirling's approximation | $n! \approx \sqrt{2 \pi n} \thinspace (n/e)^n$ |
| Derangements | $\frac{D_n}{n!} = \sum_{k=0}^{n} \frac{(-1)^k}{k!} \approx \frac{1}{e}$ |

## Study Tips

- Before every problem, ask two questions: **does order matter?** and **can an item be
  chosen twice?** The answers pick the formula from the counting table in
  [2.4](2.4-Sampling-With-Replacement.md).
- The most common error is double counting. Write what one outcome looks like, and
  check that your method produces it exactly once.
- For "at least one", count the complement ("none") and subtract.
- Countable is not the same as equally likely: multisets and stars-and-bars splits are
  usually **not** equally likely. Divide only counts of equally likely outcomes.
- Inclusion-exclusion (2.8) and story proofs (2.10) are the hardest topics. Check every
  formula on a case small enough to list by hand.
- Do the simulation problems. A ten-line simulation catches most counting mistakes.

## Where This Leads

- [Module 03: Axioms of Probability](../03-AXIOMS-OF-PROBABILITY/README.md) turns the
  counting rule into a general theory, with inclusion-exclusion for probabilities.
- [Module 07: Discrete Distributions](../07-DISCRETE-DISTRIBUTIONS/README.md) builds the
  binomial, hypergeometric and multinomial distributions from $\binom{n}{k}$ and the
  multinomial coefficient.
- In computer science, counting sizes search spaces and password strength, and the
  birthday problem predicts hash collisions.
- In AI and machine learning, counting explains bootstrap samples, feature subsets and
  polynomial features.

---

[← Module 01](../01-SETS-SAMPLE-SPACES-AND-EVENTS/README.md) · [Syllabus](../SYLLABUS.md#module-02-counting) · [Module 03 →](../03-AXIOMS-OF-PROBABILITY/README.md)
