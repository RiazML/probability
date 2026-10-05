# CLAUDE.md

```text
  ____            _           _     _ _ _ _
 |  _ \ _ __ ___ | |__   __ _| |__ (_) (_) |_ _   _
 | |_) | '__/ _ \| '_ \ / _` | '_ \| | | | __| | | |
 |  __/| | | (_) | |_) | (_| | |_) | | | | |_| |_| |
 |_|   |_|  \___/|_.__/ \__,_|_.__/|_|_|_|\__|\__, |
                                              |___/
                 W R I T I N G   G U I D E
```

This file tells Claude (and any human helper) how to write in this repository.
Read it fully before writing anything.

---

## What This Repo Is

A self-study book on **probability, and only probability**, from zero to hero:
22 modules, from sample spaces to Markov chains and martingales, plus where
probability is used in the real world.

- `SYLLABUS.md` is the master plan: every module, topic, key formula and
  practice idea. It is the source of truth for **what** to write.
- This file and `.claude/rules/` are the source of truth for **how** to write it.

## Who Reads It

A **computer science student** learning probability for AI/ML and for life.
**English is their second language.** Write simple, clear, correct English.
Teach the "why", not just the "what".

## Golden Rules

1. **Probability only.** Stay inside the topic list in `SYLLABUS.md`. No general
   calculus, linear algebra, statistics or machine learning lessons. Mention them
   only to show where probability is used.
2. **Simple English.** Short sentences. Common words. Define every new term in
   **bold** the first time.
3. **Same path every time:** story, picture, definition, proof, examples, code,
   practice. Use the topic template.
4. **Math must render on GitHub and in VS Code.** Follow `.claude/rules/latex.md`
   and run `python3 tools/check_math.py` until it reports 0 errors.
5. **Never wrong.** Compute every number. Check results with a simulation.
   Never guess program output; run the code and paste the real output.
6. **One notation for the whole repo.** Use the notation table in `latex.md`.
7. **The structure is fixed.** Do not rename, move, add or delete files or folders
   unless the user asks.
8. **Every file stands alone** but links to what comes before and after it.
9. **When in doubt, ask** the user before a big change, instead of guessing.

## Repository Map

```text
probability/
|-- CLAUDE.md                     <- you are here
|-- README.md                     <- front page with the module table
|-- SYLLABUS.md                   <- master plan (what to write)
|-- tools/
|   `-- check_math.py             <- math checker: run it after every edit
|-- .claude/
|   |-- rules/                    <- detailed rules (load for every .md file)
|   |   |-- writing-style.md      <- voice, file structure, examples, practice
|   |   |-- latex.md              <- math that renders on GitHub AND VS Code
|   |   `-- diagrams-and-code.md  <- ASCII diagrams and Python simulations
|   `-- templates/                <- copy these to start a file
|       |-- topic.md
|       |-- module-readme.md
|       `-- section-readme.md
|-- 01-SETS-SAMPLE-SPACES-AND-EVENTS/
|   |-- README.md                 <- module overview (module-readme template)
|   |-- 1.1-What-is-Probability.md   <- one topic (topic template)
|   `-- ...
|-- 02-COUNTING/
|   |-- ...
|   `-- 2.11-Classic-Counting-Problems/   <- subfolder for a group of topics
|       |-- README.md                     <- section-readme template
|       `-- 2.11.1-Birthday-Problem.md
`-- ... 22-PROBABILITY-FOR-LIFE/
```

**Names:** module folders are `NN-UPPER-CASE-TITLE` (two digits). Topic files
are `N.k-Title-Case-Name.md`, and files in a subfolder are `N.k.j-Name.md`.
Every folder has a `README.md`.

## How to Write a File

1. **Read first.** Read the module's section in `SYLLABUS.md`, the module
   `README.md`, and the topic files just before and after this one.
2. **Copy the template** that matches the file type from `.claude/templates/`.
3. **Write** following `.claude/rules/writing-style.md`. Keep the exact section
   headings of the template.
4. **Math:** follow `.claude/rules/latex.md`. Use only whitelisted commands.
5. **Pictures and code:** follow `.claude/rules/diagrams-and-code.md`. Run every
   Python block and paste its real output.
6. **Check the math:**

   ```bash
   python3 tools/check_math.py 04-CONDITIONAL-PROBABILITY-AND-BAYES/4.4-Bayes-Theorem.md
   ```

   Fix every ERROR. A WARNING means a command has not been tested yet: replace
   it with a whitelisted one, or test it on GitHub and in VS Code first.
7. **Check the links:** every relative link must point to a file that exists.
8. **Review** with the checklist below, then commit.

## Before You Finish: Checklist

- [ ] The file follows its template, with all sections in order.
- [ ] Every `{{placeholder}}` and `<!-- comment -->` from the template is gone.
- [ ] The **Big idea** is one clear sentence.
- [ ] Every new term is **bold** and explained in plain words.
- [ ] Every important formula has an **In words:** line.
- [ ] At least 2 worked examples, with every step of arithmetic shown.
- [ ] The Python runs, uses `default_rng(42)`, and the output shown is real.
- [ ] 4-6 practice problems with answers in `<details>`.
- [ ] `python3 tools/check_math.py <file>` reports **0 errors**.
- [ ] All links work, including the previous / module / next footer.
- [ ] Notation matches `latex.md`, section 6.
- [ ] Nothing outside the topic's scope; later ideas are linked, not taught.

## Git

- Work on `main` unless the user says otherwise.
- One topic (or one module README) per commit when possible.
- Commit messages: imperative and specific, such as
  `Write 4.4 Bayes' Theorem` or `Fix set notation in Module 01`.
- Run the math checker on the whole repo before pushing:
  `python3 tools/check_math.py`.

## Quick Math Reference

The full rules are in `.claude/rules/latex.md`. These five cause most problems:

| Never | Always |
|---|---|
| `\{ \}` | `\lbrace \rbrace` |
| `\,` `\;` `\!` | `\thinspace`, `\quad`, or nothing |
| `P(A \| B)` | `P(A \mid B)` |
| `f^*` | `f^{\ast}` |
| multi-line `$$` inside a list or `<details>` | one line: `$$ ... $$`, rows split with `\cr` |
