---
paths:
  - "**/*.md"
---

# Writing Style

## 1. The Reader

Write for one person: a **computer science student** who wants to learn
probability from zero to hero, use it in AI/ML, and use it in life.

- **English is their second language.** Simple words and short sentences are
  not "dumbing down". They make the ideas easier to get.
- They know school algebra. Calculus starts in Module 08; a little matrix
  algebra appears in Modules 11 and 12. Explain these tools briefly the first
  time they are needed.
- They learn by **seeing why**, not by memorizing. Every result needs a reason.
- They write code, so a short simulation often teaches faster than a proof.

## 2. Voice

| Do | Don't |
|---|---|
| Short sentences, about 20 words or fewer | Long sentences with many commas |
| One idea per sentence, one topic per paragraph (at most 4 sentences) | Walls of text |
| "You" and "we", active voice, present tense | "It can be shown that ..." |
| Common words: *use, show, about, need, so* | *utilize, demonstrate, approximately, necessitate, hence* |
| Plain explanations | Idioms and slang ("a piece of cake", "rule of thumb") |
| Start with the point | "In this section we will discuss ..." |
| "Here is why: ..." | "Obviously", "clearly", "trivially", "it is easy to see", "simply" |
| State assumptions: "if the flips are independent ..." | Hidden assumptions |

- **New terms:** the first time a term appears, write it in **bold** and explain
  it in plain words in the same sentence. Example: "A **random variable** is a
  rule that turns each outcome into a number."
- **Formulas in words:** after every important formula, add a line that starts
  with **In words:** and reads the formula as a sentence.
- **Concrete before abstract:** show real numbers (a die, 100 people, 0.01)
  before general symbols.
- **Show every step** of arithmetic in worked examples. Never skip "easy" steps.
- **No emoji.** Use plain text labels.
- **Be exact.** Every number, formula and claim must be correct. Compute it, then
  check it with a simulation when you can.

## 3. Teaching Order

Every topic follows the same path, because understanding grows in this order:

```text
  story  ->  picture  ->  definition  ->  why it is true  ->  examples  ->  code  ->  practice
 (feel it)  (see it)     (state it)       (prove it)         (use it)    (test it)  (own it)
```

## 4. The Three File Types

| File | Example | Template |
|---|---|---|
| Topic file | `04-.../4.4-Bayes-Theorem.md` | `.claude/templates/topic.md` |
| Module README | `04-.../README.md` | `.claude/templates/module-readme.md` |
| Section README (subfolder) | `04-.../4.11-Classic-Puzzles/README.md` | `.claude/templates/section-readme.md` |

Copy the template, replace every `{{placeholder}}`, follow the `<!-- -->`
comments, then **delete every comment and placeholder**.

## 5. Topic File: Required Sections

Use these exact `##` headings, in this order, so every file looks the same:

| # | Heading | What goes in it | Size |
|---|---|---|---|
| 0 | `# N.k Title` | Number and name. Same name as the file, with normal spelling | 1 line |
| | Breadcrumb + meta line | Links up, level, time, prerequisites | 2 lines |
| | `> **Big idea:**` | The whole topic in one sentence | 1 sentence |
| 1 | `## Why It Matters` | What problem this solves and where it appears again | 2-4 sentences |
| 2 | `## Intuition` | A story with real numbers. No formulas yet | 1-3 paragraphs |
| 3 | `## Picture` | An ASCII diagram with a one-line caption | 1 diagram |
| 4 | `## Definition` | Formal statement in display math, every symbol explained, then **In words:** | short |
| 5 | `## Why It Is True` | Derivation or proof, one step per line, reason on the right | as needed |
| 6 | `## Worked Examples` | At least 2: one basic, one real-world or computer science | 2-4 examples |
| 7 | `## Simulate It` | Python that checks a result from this file, plus its real output | under 30 lines |
| 8 | `## Common Mistakes` | 3-5 mistakes, each with the fix | bullets |
| 9 | `## Where It Is Used` | 3-6 uses: AI/ML, computer science, other fields, everyday life | bullets |
| 10 | `## Practice` | 4-6 problems marked (Easy), (Medium), (Hard); answers hidden in `<details>` | |
| 11 | `## Summary` | 3-5 key ideas and the one formula to remember | short |
| | Footer | Previous, module, and next links | 1 line |

- **Length:** usually 150-400 lines. Long enough to teach, short enough to finish
  in one sitting.
- **Scope:** teach only this topic. When a later idea is needed, give one sentence
  and link to its file.
- `## Picture` and `## Why It Is True` may be left out only when they truly add
  nothing (for example a pure list of definitions). Never leave out examples,
  practice or the summary.
- A long or hard proof goes in `<details><summary>Full proof (optional)</summary>`.

## 6. Worked Examples Format

```markdown
### Example 1: Rare Disease Test

**Problem.** One person in 100 has a disease. ...

**Solution.**

1. Write what we know: $P(D) = 0.01$, ...
2. Use the law of total probability: ...

**Answer.** $P(D \mid +) \approx 0.167$, so only about 1 in 6.

**Check.** The answer is much smaller than 0.99 because healthy people are 99 times
more common. The simulation in "Simulate It" agrees.
```

## 7. Practice Problems Format

- Mix the problem types: compute, prove, explain in words, and simulate.
- Mark the difficulty in the label: **1. (Easy)**, **2. (Medium)**, **3. (Hard)**.
- Put the answer in `<details>`, with a blank line after `<summary>` and before
  `</details>`. Inside `<details>`, display math must be on **one line**
  (see `latex.md`).

```markdown
**1. (Easy)** Roll a fair die. What is $P(\text{even})$?

<details>
<summary>Answer</summary>

There are 3 even faces out of 6:

$$P(\text{even}) = \frac{3}{6} = \frac{1}{2}$$

</details>
```

## 8. Headings, Emphasis and Callouts

- Exactly one `#` heading per file. Use `##` for sections and `###` for parts of
  a section. Never go deeper than `####`.
- Title Case for headings. No math, no ending punctuation in headings.
- **Bold** for new terms and key results. Use *italics* rarely. Never ALL CAPS.
- **Callouts** are blockquotes with a bold label. They look good on GitHub
  **and** in VS Code (GitHub's `> [!NOTE]` alerts do not render in VS Code, so do
  not use them):

  ```markdown
  > **Big idea:** ...       (once, at the top of every file)
  > **Note:** ...           extra information
  > **Tip:** ...            a helpful shortcut or way to think
  > **Warning:** ...        a common trap
  ```

  At most 3 callouts per file besides the Big idea, and never two in a row.

## 9. Lists, Tables and Links

- Numbered lists for steps in order; bullets for everything else. Start all items
  in a list the same way (all verbs, or all nouns).
- Tables for comparisons. Keep cells short. Math in cells must be inline and
  must never contain a bare `|` (see `latex.md`).
- **Links are always relative** and must point to files that exist:
  - same folder: `[4.3 Law of Total Probability](4.3-Law-of-Total-Probability.md)`
  - module README: `[Module 04](README.md)` or `[Module 04](../README.md)` from a subfolder
  - another module: `[Module 07](../07-DISCRETE-DISTRIBUTIONS/README.md)`
  - syllabus section: `[Syllabus](../SYLLABUS.md#module-04-conditional-probability-independence-and-bayes)`
- Link every prerequisite the first time it is used.

## 10. Examples and Numbers

- Vary the settings: dice, coins and cards, but also exams, cricket, weather,
  medical tests, servers, networks, games and money.
- Use a computer science example whenever it fits naturally (hashing, algorithms,
  networks, spam filters, machine learning).
- Write money in words: "5 dollars", "Tk 500". A `$` sign starts math by mistake.
- Write probabilities as fractions or decimals inside math (`$\frac{1}{6}$`,
  `$0.25$`). Percentages go in normal text: "about 17%".

## 11. Keep the Repo Consistent

- Folder and file names are fixed. Do not rename, move or add files without asking.
- The topics in each module must match its checklist in `SYLLABUS.md`. If a topic
  changes, update both, and the module README.
- Use the notation table in `latex.md` in every file.
- Before writing a topic, read the files just before and after it so the story
  flows and nothing is repeated.
