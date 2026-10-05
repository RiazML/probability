---
paths:
  - "**/*.md"
---

# Diagrams and Code

## 1. ASCII Diagrams

A good picture often teaches more than a page of text. Every topic file should
have at least one.

**Rules**

- Put every diagram in a ```` ```text ```` block. Nothing in it is rendered as
  Markdown or math, so it looks the same everywhere.
- At most **76 characters wide**, so it fits on a phone and in a split editor.
- Draw lines and boxes with plain ASCII only: `+ - | / \ < > ^ v . : ' = #`.
  Do not use Unicode box-drawing characters (`┌ ─ │`). They have different widths
  in different fonts.
- Labels may use simple Unicode symbols (`μ σ λ Ω ≤ ≥ ∩ ∪`), but never combining
  characters such as `X̄`; they break the alignment. Write `Xbar` instead.
- Every line of a box must have the same width. Count the characters.
- Put a one-line caption right after the block that says what the picture shows.

**Patterns to reuse**

Probability tree (conditional probability, Bayes):

```text
                        +-- 0.99 --> Positive   P = 0.01 x 0.99 = 0.0099
          +-- 0.01 --> Sick
          |             +-- 0.01 --> Negative   P = 0.01 x 0.01 = 0.0001
  Start --+
          |             +-- 0.05 --> Positive   P = 0.99 x 0.05 = 0.0495
          +-- 0.99 --> Healthy
                        +-- 0.95 --> Negative   P = 0.99 x 0.95 = 0.9405
```

Venn diagram (events):

```text
    Ω
   +-------------------------------------+
   |      +-----------+                  |
   |      |  A    +---+-------+          |
   |      |       |A∩B|   B   |          |
   |      +-------+---+       |          |
   |              +-----------+          |
   +-------------------------------------+
```

Grid of outcomes (two dice, counting):

```text
          Die 2
          1  2  3  4  5  6
   Die 1 +------------------
     1   | 2  3  4  5  6  7
     2   | 3  4  5  6  7  8
     3   | 4  5  6  7  8  9
     4   | 5  6  7  8  9 10
     5   | 6  7  8  9 10 11
     6   | 7  8  9 10 11 12
```

Bar chart of a PMF:

```text
  P(X = k)
  0.375 |       ###   ###
  0.250 |       ###   ###
  0.125 | ###   ###   ###   ###
        +--+-----+-----+-----+---
           0     1     2     3      k      X ~ Bin(3, 0.5)
```

Density curve with a shaded area:

```text
  f(x)
   |            .-'''-.
   |          .'  ###  '.        shaded area = P(a <= X <= b)
   |        .'    ###    '.
   |   __.-'      ###      '-.__
   +--------------###--------------- x
                  a b
```

States of a Markov chain:

```text
           0.3                0.4
     +-----------+      +-----------+
     |           v      |           v
   +---+  0.7  +---+  0.6  +---+
   | A | ----> | B | ----> | C |
   +---+       +---+       +---+
```

## 2. Python Simulations

Simulation is how a programmer checks probability. Every topic file has a
`## Simulate It` section.

**Rules**

- Python 3.10 or later. Use `numpy` only. Add `scipy.stats` only when you need
  an exact PDF/CDF, and `matplotlib` only when a plot is the point.
- Always use a seeded generator, so every reader gets the same output:
  `rng = np.random.default_rng(42)`. Never the old `np.random.seed()` API.
- Keep it short: under 30 lines, a plain script with no classes. Use vectorized
  numpy instead of Python loops when it stays readable.
- Use clear names (`n_trials`, `is_sick`, `estimate`) and write numbers like
  `100_000`.
- Comments explain the **probability**, not the Python.
- Always print the simulated value **next to** the exact value from the text,
  so the reader sees them agree.
- **Run the code** and paste its real output in a ```` ```text ```` block right
  after it, introduced by the word "Output:". Never write output by hand or guess it.

**Pattern**

```python
import numpy as np

rng = np.random.default_rng(42)
n_trials = 1_000_000

# Each person is sick with probability 0.01.
is_sick = rng.random(n_trials) < 0.01

# The test is positive with probability 0.99 if sick, 0.05 if healthy.
p_positive = np.where(is_sick, 0.99, 0.05)
is_positive = rng.random(n_trials) < p_positive

estimate = is_sick[is_positive].mean()   # P(sick | positive)
exact = 0.0099 / 0.0594

print(f"Simulation: {estimate:.4f}")
print(f"Exact:      {exact:.4f}")
```

Output:

```text
Simulation: 0.1679
Exact:      0.1667
```

> **Tip:** When the event you condition on is rare, the estimate is noisy. Use
> more trials (here 1,000,000; with 100,000 the estimate was 0.1750).

## 3. Images

Prefer ASCII diagrams. Use an image only when ASCII really cannot show the
idea, such as a smooth 2-D density.

- Make it with the Python in the same file and save it as PNG in an `images/`
  folder inside the module folder.
- Link it relatively with real alt text:
  `![Contours of a 2-D Gaussian with correlation 0.8](images/gaussian-contours.png)`.
- Keep each image under 200 KB.
