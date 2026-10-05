# Module 01: Sets, Sample Spaces and Events

[Probability](../README.md) / Module 01

**Level:** 1 (Zero) · **Time:** about 1 week · **Importance:** ★★★★★

> **Big idea:** Before you can measure uncertainty, you must describe exactly what can happen, and sets are the language for that.

---

## What You Will Learn

After this module you will be able to:

- Explain what a probability is and where its numbers come from.
- Write the sample space of an experiment, such as rolling two dice.
- Describe events as sets, and combine them with OR, AND and NOT.
- Draw and read Venn diagrams.
- Use De Morgan's laws and partitions to break a hard event into easy pieces.
- Tell finite, countably infinite and uncountable sample spaces apart.

## Before You Start

Nothing. This is the first module. You only need school arithmetic and fractions.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 1.1 | [What is Probability](1.1-What-is-Probability.md) | A number from 0 to 1 that measures how likely something is |
| 1.2 | [Random Experiments and Sample Spaces](1.2-Random-Experiments-and-Sample-Spaces.md) | The list of everything that can happen |
| 1.3 | [Events as Subsets](1.3-Events-as-Subsets.md) | An event is a set of outcomes |
| 1.4 | [Set Operations on Events](1.4-Set-Operations-on-Events.md) | OR is union, AND is intersection, NOT is complement |
| 1.5 | [Venn Diagrams](1.5-Venn-Diagrams.md) | Pictures that make set operations easy to see |
| 1.6 | [Mutually Exclusive Events](1.6-Mutually-Exclusive-Events.md) | Events that cannot happen together |
| 1.7 | [Partitions](1.7-Partitions.md) | Cutting the sample space into pieces that do not overlap |
| 1.8 | [De Morgan's Laws](1.8-De-Morgans-Laws.md) | How NOT works with OR and AND |
| 1.9 | [Finite, Countable and Uncountable Spaces](1.9-Finite-Countable-and-Uncountable-Spaces.md) | How big a sample space can be, and why it matters |
| 1.10 | [Practice Problems](1.10-Practice-Problems.md) | Mixed problems for the whole module |

## Map of This Module

```text
   1.1 What is probability?
            |
            v
   1.2 Sample space  ----->  1.3 Events = subsets  ----->  1.9 Size of the space
                                     |
                                     v
                           1.4 OR / AND / NOT
                            /        |        \
                           v         v         v
                1.5 Venn       1.6 Mutually     1.8 De Morgan's
                diagrams       exclusive        laws
                                     |
                                     v
                              1.7 Partitions
                                     |
                                     v
                         1.10 Practice problems
```

Start at the top. Each arrow means "you need this first".

## Key Formulas

| Name | Formula |
|---|---|
| Counting rule (equally likely outcomes) | $P(A) = \frac{\text{outcomes in } A}{\text{all outcomes}}$ |
| Union (OR) | $A \cup B = \lbrace \omega : \omega \in A \text{ or } \omega \in B \rbrace$ |
| Intersection (AND) | $A \cap B = \lbrace \omega : \omega \in A \text{ and } \omega \in B \rbrace$ |
| Complement (NOT) | $A^c = \lbrace \omega \in \Omega : \omega \notin A \rbrace$ |
| De Morgan's laws | $(A \cup B)^c = A^c \cap B^c$ and $(A \cap B)^c = A^c \cup B^c$ |
| Mutually exclusive | $A \cap B = \varnothing$ |

## Study Tips

- Always write the sample space **first**, before you compute anything. Most
  mistakes in probability come from a wrong or fuzzy sample space.
- Draw a Venn diagram for every problem with two or three events. It takes ten
  seconds and catches many errors.
- Read $\cup$ as "or", $\cap$ as "and", and $A^c$ as "not $A$". Say the words out loud.
- De Morgan's laws feel strange at first. Check them on a small example, like one
  roll of a die, until they feel obvious.

## Where This Leads

- [Module 02: Counting](../02-COUNTING/README.md) teaches you to count large sample
  spaces without listing them.
- [Module 03: Axioms of Probability](../03-AXIOMS-OF-PROBABILITY/README.md) gives the
  three rules that every probability must follow, using the set language from here.
- In AI and computer science, the set of possible labels, tokens or network states
  is a sample space.

---

[Syllabus](../SYLLABUS.md#module-01-sets-sample-spaces-and-events) · [Module 02 →](../02-COUNTING/README.md)
