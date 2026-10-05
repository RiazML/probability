<!--
TOPIC FILE TEMPLATE
Copy this file over an empty topic file, replace every {{placeholder}},
follow the comments, then delete ALL comments and placeholders.
Rules: .claude/rules/writing-style.md, latex.md, diagrams-and-code.md
Check: python3 tools/check_math.py path/to/file.md
Links below assume the file sits directly in a module folder. For a file in
a subfolder (for example 4.11-Classic-Puzzles/), add one more "../" and link
the section README as README.md and the module README as ../README.md.
-->

# {{N.k}} {{Topic Title}}

[Probability](../README.md) / [Module {{NN}}: {{Module Title}}](README.md) / {{N.k}} {{Topic Title}}

**Level:** {{1-5}} · **Time:** about {{30}} minutes · **Before this:** [{{N.k-1}} {{Previous Topic}}]({{N.k-1}}-{{Previous-Topic}}.md)

> **Big idea:** {{The whole topic in one sentence a friend could repeat.}}

---

## Why It Matters

<!-- 2-4 sentences. What problem does this idea solve? Where will the reader meet it again? -->

{{...}}

## Intuition

<!-- A story with real numbers, no formulas yet. Dice, cards, exams, cricket, weather, servers, spam. -->

{{...}}

## Picture

```text
{{ASCII diagram, at most 76 characters wide.}}
```

{{One sentence that says what the picture shows.}}

## Definition

<!-- Name the idea in **bold**, say it in plain words, then give the formula. -->

{{A **term** is ...}}

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

where:

- $P(A \cap B)$ is {{...}}
- $P(B)$ is {{...}}, and it must be greater than $0$.

**In words:** {{Read the formula as one sentence.}}

## Why It Is True

<!-- One step per line. Give the reason for each step on the right. -->

{{Start from what the reader already knows.}}

$$
\begin{aligned}
E[aX + b] &= \sum_{x} (ax + b) \thinspace p(x) && \text{(LOTUS)} \\
&= a \sum_{x} x \thinspace p(x) + b \sum_{x} p(x) && \text{(split the sum)} \\
&= a E[X] + b && \text{(the PMF sums to 1)}
\end{aligned}
$$

## Worked Examples

### Example 1: {{Short Title}}

**Problem.** {{...}}

**Solution.**

1. {{Write down what we know, with symbols.}}
2. {{Apply the idea, showing the arithmetic.}}
3. {{Finish the calculation.}}

**Answer.** $P(D \mid +) \approx 0.167$ {{(replace with the result, then say it in words)}}

**Check.** {{Why the answer makes sense: a bound, a special case, or the simulation.}}

### Example 2: {{A Real-World or Computer Science Example}}

**Problem.** {{...}}

**Solution.**

1. {{...}}

**Answer.** {{...}}

## Simulate It

{{One sentence saying what the code checks.}}

```python
import numpy as np

rng = np.random.default_rng(42)
n_trials = 100_000

# {{Comment about the probability, not the Python.}}
samples = rng.integers(1, 7, size=n_trials)   # rolls of a fair die

estimate = np.mean(samples % 2 == 0)          # P(even)
exact = 1 / 2

print(f"Simulation: {estimate:.4f}")
print(f"Exact:      {exact:.4f}")
```

Output:

```text
{{Paste the REAL output after running the code.}}
```

## Common Mistakes

- **{{The mistake}}.** {{Why it is wrong, and what to do instead.}}
- **{{The mistake}}.** {{...}}
- **{{The mistake}}.** {{...}}

## Where It Is Used

- **AI and machine learning:** {{...}}
- **Computer science:** {{...}}
- **{{Another field}}:** {{...}}
- **Everyday life:** {{...}}

## Practice

**1. (Easy)** {{Problem.}}

<details>
<summary>Answer</summary>

{{Short solution. Display math inside details must be on ONE line:}}

$$P(\text{even}) = \frac{3}{6} = \frac{1}{2}$$

</details>

**2. (Easy)** {{Problem.}}

<details>
<summary>Answer</summary>

{{...}}

</details>

**3. (Medium)** {{Problem.}}

<details>
<summary>Answer</summary>

{{Several steps: write one chain on one line (no aligned or cases inside details):}}

$$E[X] = 0 \cdot \tfrac{1}{2} + 1 \cdot \tfrac{1}{2} = \tfrac{1}{2}$$

</details>

**4. (Hard)** {{Problem. Can be a proof.}}

<details>
<summary>Answer</summary>

{{...}}

</details>

**5. (Simulate)** {{Write code that checks the answer to an earlier problem.}}

<details>
<summary>Answer</summary>

```python
{{short solution code}}
```

</details>

## Summary

- {{Key idea 1.}}
- {{Key idea 2.}}
- {{Key idea 3.}}

The one formula to remember:

$$
\boxed{P(A \mid B) = \frac{P(A \cap B)}{P(B)}}
$$

---

[← {{N.k-1}} {{Previous Topic}}]({{N.k-1}}-{{Previous-Topic}}.md) · [Module {{NN}}](README.md) · [{{N.k+1}} {{Next Topic}} →]({{N.k+1}}-{{Next-Topic}}.md)
