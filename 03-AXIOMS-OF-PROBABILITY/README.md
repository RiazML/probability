# Module 03: Axioms of Probability

[Probability](../README.md) / Module 03

**Level:** 1 (Zero) · **Time:** about 1 week · **Importance:** ★★★★★

> **Big idea:** Three simple rules, Kolmogorov's axioms, are all you need to assume; every other rule of probability is proved from them.

---

## What You Will Learn

After this module you will be able to:

- Explain the classical, frequentist and Bayesian meanings of probability, and why
  all three follow the same rules.
- State Kolmogorov's three axioms and check whether a model is a valid probability.
- Prove the complement rule, monotonicity, the addition rule and inclusion-exclusion
  from the axioms alone.
- Bound the chance of "at least one failure" with the union bound.
- Compute probabilities by counting equally likely outcomes, or by measuring lengths
  and areas, and know when each method is valid.
- Use continuity of probability to answer "eventually" and "forever" questions.

## Before You Start

You should be comfortable with:

- [Module 01: Sets, Sample Spaces and Events](../01-SETS-SAMPLE-SPACES-AND-EVENTS/README.md):
  events as sets, union, intersection, complement, disjoint events and De Morgan's laws.
- [Module 02: Counting](../02-COUNTING/README.md): permutations, combinations and the
  counting form of inclusion-exclusion, used in 3.5 and 3.7.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 3.1 | [Interpretations of Probability](3.1-Interpretations-of-Probability.md) | Symmetry, long-run frequency and degree of belief, and why they share one set of rules |
| 3.2 | [Kolmogorov Axioms](3.2-Kolmogorov-Axioms.md) | The three rules every probability must obey |
| 3.3 | [Consequences of the Axioms](3.3-Consequences-of-the-Axioms.md) | Complement rule, empty event, monotonicity, all proved from the axioms |
| 3.4 | [Addition Rule](3.4-Addition-Rule.md) | "A or B" for any two events: add, then subtract the overlap |
| 3.5 | [Inclusion-Exclusion for Probability](3.5-Inclusion-Exclusion-for-Probability.md) | "At least one" of many events, with switching signs |
| 3.6 | [Union Bound](3.6-Union-Bound.md) | The chance of any failure is at most the sum of the failure chances |
| 3.7 | [Equally Likely Outcomes](3.7-Equally-Likely-Outcomes.md) | When "favorable over total" is valid, and when it fails |
| 3.8 | [Geometric Probability](3.8-Geometric-Probability.md) | Probability as length or area for a uniform random point |
| 3.9 | [Continuity of Probability](3.9-Continuity-of-Probability.md) | Limits of growing and shrinking events |
| 3.10 | [Practice Problems](3.10-Practice-Problems.md) | Mixed problems, proofs and simulation projects for the whole module |

## Map of This Module

```text
   3.1 What does a probability mean?
                 |
                 v
   3.2 Kolmogorov axioms -----------------------+
                 |                              |
                 v                              v
   3.3 Consequences of the axioms      3.7 Equally likely outcomes
                 |                              |
                 v                              v
   3.4 Addition rule                   3.8 Geometric probability
          /             \                       |
         v               v                      |
   3.5 Inclusion-    3.6 Union bound            |
       exclusion          |                     |
                          v                     |
                 3.9 Continuity of probability <+
                          |
                          v
                 3.10 Practice problems
```

Start at the top. Each arrow means "you need this first". The left path builds the
general rules; the right path builds concrete models where the rules are used.

## Key Formulas

| Name | Formula |
|---|---|
| Axiom 1 (non-negativity) | $P(A) \ge 0$ |
| Axiom 2 (normalization) | $P(\Omega) = 1$ |
| Axiom 3 (countable additivity) | $P(A_1 \cup A_2 \cup \dots) = P(A_1) + P(A_2) + \dots$ for pairwise disjoint $A_i$ |
| Empty event | $P(\varnothing) = 0$ |
| Complement rule | $P(A^c) = 1 - P(A)$ |
| Monotonicity | $A \subseteq B \implies P(A) \le P(B)$ |
| Addition rule | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Inclusion-exclusion (3 events) | $P(A \cup B \cup C) = \sum P(\text{singles}) - \sum P(\text{pairs}) + P(A \cap B \cap C)$ |
| Union bound | $P(A_1 \cup \dots \cup A_n) \le P(A_1) + \dots + P(A_n)$ |
| Equally likely outcomes | $P(A) = \frac{\lvert A \rvert}{\lvert \Omega \rvert}$ |
| Geometric probability | $P(A) = \frac{\text{size}(A)}{\text{size}(\Omega)}$ |
| Continuity (increasing events) | $A_1 \subseteq A_2 \subseteq \dots \implies P(\bigcup A_n) = \lim P(A_n)$ |

## Study Tips

- The hardest topic is usually 3.9, continuity of probability. Draw the growing or
  shrinking events as nested boxes before you write any formula, and check that the
  sequence really is increasing or decreasing.
- Do the proofs in 3.3 yourself, with the book closed. Each one is 2 or 3 lines, and
  doing them once makes every later proof in the book easier.
- For any "at least one" question, first try the complement rule. Use
  inclusion-exclusion when the intersections are easy, and the union bound when you
  only need an upper limit.
- The classic mistake of this module is using "favorable over total" with outcomes
  that are not equally likely (3.7), or saying "at random" without saying what is
  uniform (3.8).
- Most important practice problems: C1 (proving the rules), C2 (inclusion-exclusion),
  H1 (the union bound for "everything works"), and both simulation projects.

## Where This Leads

- [Module 04: Conditional Probability, Independence and Bayes](../04-CONDITIONAL-PROBABILITY-AND-BAYES/README.md)
  defines a new probability, "probability given B", and checks it with these same axioms.
- [Module 05: Discrete Random Variables](../05-DISCRETE-RANDOM-VARIABLES/README.md) and
  [Module 08: Continuous Random Variables](../08-CONTINUOUS-RANDOM-VARIABLES/README.md)
  grow out of the weights of 3.2 and the lengths and areas of 3.8.
- [Module 16](../16-INEQUALITIES-AND-CONCENTRATION/README.md) returns to the union bound
  as a main tool of learning theory, and [Module 20](../20-ADVANCED-PROBABILITY/README.md)
  rebuilds the axioms with measure theory.
- In AI and computer science, every softmax output, every randomized algorithm and every
  "with high probability" guarantee rests on the rules of this module.

---

[← Module 02](../02-COUNTING/README.md) · [Syllabus](../SYLLABUS.md#module-03-axioms-of-probability) · [Module 04 →](../04-CONDITIONAL-PROBABILITY-AND-BAYES/README.md)
