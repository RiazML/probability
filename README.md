# Probability: Zero to Hero

A self-study book on probability, and only probability: from sample spaces and
Bayes' theorem to Markov chains and martingales, plus where probability is used
in AI, computer science, finance, medicine, games and everyday life.

- **22 modules** and **255 lessons**, each with an intuition, a picture, a proof,
  worked examples, a simulation, common mistakes and practice problems.
- **550 Python examples** that you can run. Each one shows the output it prints,
  and the output is checked by a script.
- Written in simple English for computer science students.

**New here? Start with [SYLLABUS.md](SYLLABUS.md)**, the full roadmap with the
topics, key formulas, uses and practice ideas for every module. Then read the
modules in order, from Module 01.

## How to Read This Book

1. Read one lesson, then close the book and try to say it in your own words.
2. Do the practice problems before you open the hidden answers.
3. Run the Python example and change a number. Watch what happens.
4. At the end of a module, do its problem set before you move on.

Calculus starts in Module 08, and a little matrix algebra appears in Modules 11
and 12. Each tool is explained briefly the first time it is needed. Module 20
(measure theory) is optional.

## Modules

| Level | Module |
|---|---|
| 1. Zero | [01 Sets, Sample Spaces and Events](01-SETS-SAMPLE-SPACES-AND-EVENTS/) |
| | [02 Counting](02-COUNTING/) |
| | [03 Axioms of Probability](03-AXIOMS-OF-PROBABILITY/) |
| | [04 Conditional Probability and Bayes](04-CONDITIONAL-PROBABILITY-AND-BAYES/) |
| 2. Random variables | [05 Discrete Random Variables](05-DISCRETE-RANDOM-VARIABLES/) |
| | [06 Expectation, Variance and Moments](06-EXPECTATION-VARIANCE-AND-MOMENTS/) |
| | [07 Discrete Distributions](07-DISCRETE-DISTRIBUTIONS/) |
| | [08 Continuous Random Variables](08-CONTINUOUS-RANDOM-VARIABLES/) |
| | [09 Continuous Distributions](09-CONTINUOUS-DISTRIBUTIONS/) |
| 3. Many variables | [10 Joint Distributions](10-JOINT-DISTRIBUTIONS/) |
| | [11 Covariance and Correlation](11-COVARIANCE-AND-CORRELATION/) |
| | [12 Multivariate Gaussian](12-MULTIVARIATE-GAUSSIAN/) |
| | [13 Functions of Random Variables](13-FUNCTIONS-OF-RANDOM-VARIABLES/) |
| | [14 Conditional Expectation](14-CONDITIONAL-EXPECTATION/) |
| 4. Big theorems | [15 Generating Functions](15-GENERATING-FUNCTIONS/) |
| | [16 Inequalities and Concentration](16-INEQUALITIES-AND-CONCENTRATION/) |
| | [17 Limit Theorems](17-LIMIT-THEOREMS/) |
| 5. Hero | [18 Stochastic Processes](18-STOCHASTIC-PROCESSES/) |
| | [19 Simulation and Monte Carlo](19-SIMULATION-AND-MONTE-CARLO/) |
| | [20 Advanced Probability](20-ADVANCED-PROBABILITY/) |
| Uses | [21 Applications of Probability](21-APPLICATIONS-OF-PROBABILITY/) |
| | [22 Probability for Life](22-PROBABILITY-FOR-LIFE/) |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install numpy scipy matplotlib jupyter
```

## For Contributors

Writing rules are in [CLAUDE.md](CLAUDE.md) and in `.claude/rules/`. Four scripts
in `tools/` keep the book correct. Run them after any edit:

```bash
python3 tools/check_math.py     # math renders on GitHub and in VS Code
python3 tools/check_links.py    # no broken links, no empty files
python3 tools/check_widths.py   # diagrams fit in 76 characters
python3 tools/check_code.py     # every Python example prints what the book shows
```
