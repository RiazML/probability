# Module 22: Probability for Life

[Probability](../README.md) / Module 22

**Level:** Uses (Life) · **Time:** about 1 week to read, and a lifetime to practice · **Importance:** ★★★★★

> **Big idea:** Every important decision in health, money, study and work is made without knowing what will happen, and probability gives you a short list of habits (ask how common it is, update gently, count the average and the worst case, beware of streaks, small samples, hidden causes and missing data) that make those decisions better.

---

## What You Will Learn

After this module you will be able to:

- Start from the base rate, and update a belief with odds and likelihood ratios as clues arrive.
- Compare choices by expected value, and also by risk, repeated exposure and the chance of ruin.
- Spot the common traps of chance: the gambler's fallacy, regression to the mean, and the law of small numbers.
- Spot the common traps of data: correlation taken as cause, Simpson's paradox and survivorship bias.
- Spot the traps of stories and tails: the conjunction fallacy, compounding small risks and fat tails.
- Choose a bet size with the Kelly criterion, and keep a prediction journal to measure your own calibration.

## Before You Start

This module uses ideas from the whole book, but each file names the exact topics it needs. You should be comfortable with:

- [Module 21: Applications of Probability](../21-APPLICATIONS-OF-PROBABILITY/README.md): the previous module. It shows the same tools in AI, statistics, medicine, games and weather. This module turns them into habits.
- [Module 04: Conditional Probability and Bayes](../04-CONDITIONAL-PROBABILITY-AND-BAYES/README.md): Bayes' theorem, the odds form and independence. Files 22.1, 22.2, 22.5, 22.9 and 22.10 use them.
- [Module 06: Expectation, Variance and Moments](../06-EXPECTATION-VARIANCE-AND-MOMENTS/README.md): expected value and standard deviation, for 22.3 and 22.4.
- [Module 11: Covariance and Correlation](../11-COVARIANCE-AND-CORRELATION/README.md) and [Module 12: Multivariate Gaussian](../12-MULTIVARIATE-GAUSSIAN/README.md): correlation and regression to the mean, for 22.6 and 22.8.
- [Module 16: Inequalities and Concentration](../16-INEQUALITIES-AND-CONCENTRATION/README.md) and [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md): the union bound, Jensen, and the Law of Large Numbers, for 22.12 and 22.14.
- [Module 09: Continuous Distributions](../09-CONTINUOUS-DISTRIBUTIONS/README.md): heavy tails, for 22.13.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 22.1 | [Base Rates](22.1-Base-Rates.md) | Ask "how common is this?" first: a good test can still give mostly false alarms |
| 22.2 | [Bayesian Updating in Daily Life](22.2-Bayesian-Updating-in-Daily-Life.md) | Move your belief with each clue by its likelihood ratio, not more and not less |
| 22.3 | [Expected Value Decisions](22.3-Expected-Value-Decisions.md) | Compare choices by chance times size, and find the break-even chance |
| 22.4 | [Variance and Risk](22.4-Variance-and-Risk.md) | Same average, different risk: spread, the bad end, and diversification |
| 22.5 | [Gambler's Fallacy](22.5-Gamblers-Fallacy.md) | Coins have no memory: "due" does not exist, and streaks are common |
| 22.6 | [Regression to the Mean](22.6-Regression-to-the-Mean.md) | Extreme results are partly luck, so the next one is usually less extreme |
| 22.7 | [Law of Small Numbers](22.7-Law-of-Small-Numbers.md) | Small samples swing wildly, and the best and worst groups are the smallest |
| 22.8 | [Correlation vs Causation](22.8-Correlation-vs-Causation.md) | Four reasons why two things move together, and why a random experiment settles it |
| 22.9 | [Simpson's Paradox](22.9-Simpsons-Paradox.md) | A trend can flip when groups are combined, and the cause story says which table to trust |
| 22.10 | [Survivorship Bias](22.10-Survivorship-Bias.md) | You see only the cases that passed a filter, so ask who is missing |
| 22.11 | [Conjunction Fallacy](22.11-Conjunction-Fallacy.md) | More details make a story more believable and less probable |
| 22.12 | [Compounding Small Risks](22.12-Compounding-Small-Risks.md) | A small risk repeated $n$ times happens at least once with chance $1 - (1 - p)^n$ |
| 22.13 | [Fat Tails](22.13-Fat-Tails.md) | When one rare event can outweigh all the others, the average and the worst case so far mislead |
| 22.14 | [Kelly Criterion](22.14-Kelly-Criterion.md) | The bet size that grows money fastest, and why you never bet it all |
| 22.15 | [Calibration](22.15-Calibration.md) | Keep score of your predictions, so that your 70% means 70% |
| 22.16 | [Practice Problems](22.16-Practice-Problems.md) | Real-life scenarios, the one-page thinking checklist, and what to read next |

## Map of This Module

```text
   22.1 Base rates --> 22.2 Updating --> 22.3 Expected value --> 22.4 Risk
                                                                     |
              +------------------------------------------------------+
              v
   FOOLED BY CHANCE            FOOLED BY DATA              FOOLED BY STORIES
   22.5 Gambler's fallacy      22.8 Correlation/cause      22.11 Conjunction
   22.6 Regression to mean     22.9 Simpson's paradox
   22.7 Small numbers          22.10 Survivorship
              |                          |                         |
              +--------------------------+-------------------------+
                                         v
              REPEATED RISK:  22.12 Compounding --> 22.13 Fat tails
                                         |
                                         v
                       22.14 Kelly  --> 22.15 Calibration
                                         |
                                         v
                                22.16 Practice and checklist
```

The first four files give the basic tools for a decision. The three middle groups are the traps that fool us. The last files are about acting wisely when the risk repeats, and about measuring how honest your own numbers are.

## Key Formulas

| Idea | Formula |
|---|---|
| Base rate (22.1) | $P(H \mid +) = \frac{\pi s}{\pi s + (1 - \pi) f}$ |
| Updating in odds (22.2) | $\text{posterior odds} = \text{prior odds} \times \frac{P(E \mid H)}{P(E \mid H^c)}$ |
| Expected value (22.3) | $E[V] = \sum_i p_i v_i$, break-even $p^{\ast} = \frac{L}{W + L}$ |
| Risk of an average (22.4) | $\operatorname{Var}(\bar{X}) = \frac{\sigma^2}{n}\left(1 + (n-1)\rho\right)$ |
| No memory (22.5) | $P(X_{n+1} = \text{H} \mid X_1 = \dots = X_n = \text{H}) = \frac{1}{2}$ |
| Regression to the mean (22.6) | $E[X_2 \mid X_1 = x] = \mu + \rho (x - \mu)$ |
| Small samples (22.7) | $\sigma_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}} \le \frac{1}{2\sqrt{n}}$ |
| Hidden cause (22.8) | $\rho_{XY} = \frac{ab \sigma_Z^2}{\sqrt{(a^2 \sigma_Z^2 + s_1^2)(b^2 \sigma_Z^2 + s_2^2)}}$ with no arrow from $X$ to $Y$ |
| Simpson (22.9) | $r_A - r_B = \sum_g u_g (r_{Ag} - r_{Bg}) + \sum_g (u_g - v_g) r_{Bg}$ |
| Survivorship (22.10) | $P(A \mid S) = \frac{P(S \mid A) P(A)}{P(S)}$ |
| Conjunction (22.11) | $P(A \cap B) = P(A) P(B \mid A) \le P(A)$ |
| Compounding (22.12) | $P(\text{at least once in } n \text{ tries}) = 1 - (1 - p)^n$ |
| Fat tail (22.13) | $P(X \gt x) = \left( \frac{x_m}{x} \right)^{\alpha}$, worst of $m$ values about $x_m \left( \frac{m}{\ln 2} \right)^{1/\alpha}$ |
| Kelly (22.14) | $f^{\ast} = p - \frac{1 - p}{b}$ |
| Calibration (22.15) | $\text{Brier} = \frac{1}{n} \sum_i (p_i - y_i)^2$ |

## Study Tips

- Read the files in order the first time. Each one ends with a short "Try this today" habit. Do at least one of them for real before you move on: a few small habits change your thinking more than reading all the files twice.
- Start your prediction journal of [22.15](22.15-Calibration.md) now, while you read. By the time you finish the module, you will have your first results.
- The hardest files are [22.9 Simpson's Paradox](22.9-Simpsons-Paradox.md) (deciding which table to trust needs a story of causes) and [22.14 Kelly Criterion](22.14-Kelly-Criterion.md) (it uses logs and Jensen's inequality). If they feel heavy, run the code first and read the output.
- In the last practice set, [22.16](22.16-Practice-Problems.md), try the "Probability Thinking Checklist" on a real decision of your own, such as a purchase, a job offer or a study plan.
- A classic mistake in this module is to use a model blindly. Every file names the assumption that is most likely to be false (independence, a known chance, a stable world). Say it out loud before you use the number.
- All numbers in this module are made up to teach an idea. None of it is medical, legal or financial advice.

## Where This Leads

- This is the last module of the book. The [front page](../README.md) lists all 22 modules, so you can return to any topic you want to see again.
- [Module 21: Applications of Probability](../21-APPLICATIONS-OF-PROBABILITY/README.md) is the best companion: it shows the same tools inside AI and machine learning, statistics, computer science, medicine, finance, games and weather.
- For AI and machine learning, base rates and calibration are everyday tools (precision on rare classes, reliable confidence), and the traps of this module (confounders, selection, small test sets, overfitting to a lucky score) appear in every real project.
- The reading list in [22.16](22.16-Practice-Problems.md) (taken from Appendix D of the Syllabus) tells you which books and courses to use next.

---

[← Module 21](../21-APPLICATIONS-OF-PROBABILITY/README.md) · [Syllabus](../SYLLABUS.md#module-22-probability-for-life) · [Book front page →](../README.md)
