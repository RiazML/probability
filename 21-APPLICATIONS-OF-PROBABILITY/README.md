# Module 21: Applications of Probability

[Probability](../README.md) / Module 21

**Level:** Uses (Applications) · **Time:** about 2 weeks · **Importance:** ★★★★★

> **Big idea:** Every field that deals with uncertainty uses the same few probability tools (Bayes' theorem, expectation, the common distributions, the limit theorems and Markov chains), and each file here shows one field and the exact tools it relies on.

---

## What You Will Learn

After this module you will be able to:

- Recognize the probability model behind a machine learning method, such as Naive Bayes, cross-entropy, next-token sampling, a latent variable model, a bandit or a calibration check.
- Turn a data problem into a statement about a sampling distribution, and read a confidence interval or a p-value correctly.
- Use expectation, concentration and counting to analyze randomized algorithms, hash tables, Bloom filters and queues.
- Apply Bayes' theorem and base rates to tests in medicine and security, and the exponential and Weibull laws to the lifetime of machines.
- Model prices, populations, games and the weather with random walks, branching processes and simulation.
- Check each model with a short Python simulation, as in every earlier module.

## Before You Start

This module applies everything before it. You should be comfortable with:

- [Module 20: Advanced Probability](../20-ADVANCED-PROBABILITY/README.md): the previous module. It is optional. Here you only need the words "fair game" and "almost surely".
- [Module 04: Conditional Probability and Bayes](../04-CONDITIONAL-PROBABILITY-AND-BAYES/README.md): Bayes' theorem, the chain rule and conditional independence ([4.4](../04-CONDITIONAL-PROBABILITY-AND-BAYES/4.4-Bayes-Theorem.md), [4.9](../04-CONDITIONAL-PROBABILITY-AND-BAYES/4.9-Conditional-Independence.md)).
- [Module 02: Counting](../02-COUNTING/README.md) and [Module 03: Axioms of Probability](../03-AXIOMS-OF-PROBABILITY/README.md): counting outcomes, the birthday problem and the union bound.
- [Module 06: Expectation, Variance and Moments](../06-EXPECTATION-VARIANCE-AND-MOMENTS/README.md) and [Module 07: Discrete Distributions](../07-DISCRETE-DISTRIBUTIONS/README.md): linearity, the indicator trick, and the Bernoulli, binomial, geometric, Poisson and categorical laws.
- [Module 08: Continuous Random Variables](../08-CONTINUOUS-RANDOM-VARIABLES/README.md) and [Module 09: Continuous Distributions](../09-CONTINUOUS-DISTRIBUTIONS/README.md): densities, and the normal, exponential, Beta and Weibull laws.
- [Module 10: Joint Distributions](../10-JOINT-DISTRIBUTIONS/README.md) to [Module 14: Conditional Expectation](../14-CONDITIONAL-EXPECTATION/README.md): joint laws and mixtures, covariance, the multivariate Gaussian, functions of random variables, and the tower rule.
- [Module 16: Inequalities and Concentration](../16-INEQUALITIES-AND-CONCENTRATION/README.md) and [Module 17: Limit Theorems](../17-LIMIT-THEOREMS/README.md): Markov, Chernoff and Hoeffding bounds, the Law of Large Numbers and the Central Limit Theorem.
- [Module 18: Stochastic Processes](../18-STOCHASTIC-PROCESSES/README.md) and [Module 19: Simulation and Monte Carlo](../19-SIMULATION-AND-MONTE-CARLO/README.md): random walks, Markov chains, the Poisson process, and simulation.

## Topics

| # | Topic | What it is about |
|---|---|---|
| 21.1 | [AI and Machine Learning](21.1-AI-and-Machine-Learning/README.md) | Six probability models behind AI (a subfolder, 21.1.1 to 21.1.6, listed below) |
| 21.2 | [Statistics and Data Science](21.2-Statistics-and-Data-Science.md) | Samples, standard errors, confidence intervals, p-values and many tests |
| 21.3 | [Computer Science](21.3-Computer-Science/README.md) | Randomized algorithms, hashing and Bloom filters, average-case analysis, networks and queues (a subfolder) |
| 21.4 | [Cryptography and Security](21.4-Cryptography-and-Security.md) | Uniform random keys, guessing and counting attacks |
| 21.5 | [Finance and Insurance](21.5-Finance-and-Insurance.md) | Expected value, risk, covariance of assets, random-walk prices |
| 21.6 | [Medicine and Diagnostic Testing](21.6-Medicine-and-Diagnostic-Testing.md) | Sensitivity, specificity, base rates and Bayes' theorem |
| 21.7 | [Engineering and Reliability](21.7-Engineering-and-Reliability.md) | Lifetimes with the exponential and Weibull laws, and systems built from parts |
| 21.8 | [Physics](21.8-Physics.md) | Random walks, diffusion and Monte Carlo in physical models |
| 21.9 | [Biology and Genetics](21.9-Biology-and-Genetics.md) | Binomial inheritance and branching processes for populations |
| 21.10 | [Games, Gambling and Sports](21.10-Games-Gambling-and-Sports.md) | Counting, expected value and the Law of Large Numbers (why the house wins) |
| 21.11 | [Weather and Forecasting](21.11-Weather-and-Forecasting.md) | Conditional probability, ensembles and checking a forecast |

The six files inside 21.1:

| # | Topic | What it is about |
|---|---|---|
| 21.1.1 | [Probabilistic Classifiers and Naive Bayes](21.1-AI-and-Machine-Learning/21.1.1-Probabilistic-Classifiers-and-Naive-Bayes.md) | Bayes' theorem plus conditional independence: a tiny spam filter |
| 21.1.2 | [Loss Functions as Probability](21.1-AI-and-Machine-Learning/21.1.2-Loss-Functions-as-Probability.md) | Cross-entropy and squared error as negative log-likelihoods |
| 21.1.3 | [Language Models](21.1-AI-and-Machine-Learning/21.1.3-Language-Models.md) | The chain rule, next-token sampling and temperature |
| 21.1.4 | [Generative Models](21.1-AI-and-Machine-Learning/21.1.4-Generative-Models.md) | Latent variables, mixtures and the linear Gaussian model |
| 21.1.5 | [Reinforcement Learning](21.1-AI-and-Machine-Learning/21.1.5-Reinforcement-Learning.md) | Value as a conditional expectation, and Thompson sampling |
| 21.1.6 | [Uncertainty and Calibration](21.1-AI-and-Machine-Learning/21.1.6-Uncertainty-and-Calibration.md) | Predicted probabilities against real frequencies |

## Map of This Module

```text
+------------------------------+--------------------------------+----------+
| Field / use                  | Probability behind it          | Modules  |
+------------------------------+--------------------------------+----------+
| 21.1.1 Naive Bayes           | Bayes, cond. independence      | 04 10    |
| 21.1.2 Loss functions        | Expectation, likelihood        | 06 07 09 |
| 21.1.3 Language models       | Chain rule, categorical        | 04 07 18 |
| 21.1.4 Generative models     | Gaussian vectors, sampling     | 12 19    |
| 21.1.5 RL and bandits        | Markov chains, cond. mean      | 14 18    |
| 21.1.6 Calibration           | Probabilities and frequencies  | 03 14 17 |
| 21.2 Statistics and data     | Distributions, LLN, CLT        | 07-09 17 |
| 21.3 Randomized algorithms   | Expectation, concentration     | 06 16    |
| 21.3 Hashing, Bloom filters  | Counting, birthday problem     | 02 03    |
| 21.3 Networks and queues     | Poisson process, Markov chains | 18       |
| 21.4 Cryptography, security  | Uniform randomness, counting   | 02 07    |
| 21.5 Finance, insurance      | Covariance, Brownian motion    | 06 11 18 |
| 21.6 Medicine, testing       | Bayes, base rates              | 04       |
| 21.7 Engineering reliability | Exponential, Weibull, min/max  | 09 13    |
| 21.8 Physics                 | Distributions, walks, MC       | 09 18 19 |
| 21.9 Biology, genetics       | Binomial, branching processes  | 07 18    |
| 21.10 Games, gambling        | Counting, expectation, LLN     | 02 06 17 |
| 21.11 Weather, forecasting   | Conditional prob., simulation  | 04 19    |
+------------------------------+--------------------------------+----------+
```

For each application, the "Modules" column lists where its probability is taught. The earlier modules are the tools. This module is where you use them.

## Key Formulas

| Use | Formula |
|---|---|
| Naive Bayes (21.1.1) | $P(C = c \mid \mathbf{x}) \propto P(C = c) \prod_{i} P(x_i \mid C = c)$ |
| Cross-entropy loss (21.1.2) | $H(p, q) = -\sum_{j} p_j \ln q_j = H(p) + D(p \Vert q)$ |
| Chain rule and temperature (21.1.3) | $P(w_1, \dots, w_T) = \prod_{t} P(w_t \mid w_{\lt t})$ and $q_j(T) = \frac{e^{z_j/T}}{\sum_m e^{z_m/T}}$ |
| Latent variable model (21.1.4) | $p(x) = \sum_{z} p(x \mid z) \thinspace p(z)$ and $\ln p(x) \ge E_q\left[ \ln \frac{p(x, z)}{q(z)} \right]$ |
| Bellman equation (21.1.5) | $V(s) = r(s) + \gamma \sum_{s'} P(s' \mid s) \thinspace V(s')$ |
| Calibration (21.1.6) | $P(Y = 1 \mid \hat{p} = p) = p$ and $E[(\hat{p} - Y)^2] = E[(\hat{p} - q)^2] + E[q(1 - q)]$ |
| Confidence interval (21.2) | $\bar{X}_n \pm 1.96 \thinspace s / \sqrt{n}$ |
| Many tests (21.2) | $P(\text{at least one false alarm}) = 1 - (1 - \alpha)^m$ |
| Random pivot quicksort (21.3) | $E[\text{comparisons}] \approx 2 n \ln n$ |
| Hash collision (21.3) | $P(\text{collision}) \approx 1 - e^{-n(n-1)/(2m)}$ for $n$ items in $m$ slots |
| Bloom filter (21.3) | false positive rate $\approx \left( 1 - e^{-kn/m} \right)^k$ |
| Queue with load $\rho = \lambda / \mu \lt 1$ (21.3) | mean number in system $= \frac{\rho}{1 - \rho}$ |
| Guessing a random key (21.4) | $P(\text{guess right}) = 2^{-b}$ for a uniform $b$-bit key |
| Portfolio risk (21.5) | $\operatorname{Var}(aX + bY) = a^2 \sigma_X^2 + b^2 \sigma_Y^2 + 2ab \operatorname{Cov}(X, Y)$ |
| Diagnostic test (21.6) | $P(D \mid +) = \frac{\text{sens} \cdot \text{prev}}{\text{sens} \cdot \text{prev} + (1 - \text{spec})(1 - \text{prev})}$ |
| Reliability (21.7) | series: $R = \prod_i R_i$; parallel: $R = 1 - \prod_i (1 - R_i)$; exponential: $R(t) = e^{-\lambda t}$ |
| Random walk (21.8) | $E[S_n] = 0$ and $\operatorname{Var}(S_n) = n$ for $n$ steps of size $\pm 1$ |
| Branching process (21.9) | extinction probability is the smallest root $s \ge 0$ of $s = G(s)$ |
| House edge (21.10) | $E[\text{profit per bet}] = \sum \text{prize} \times \text{probability}$; a straight-up bet on a single-zero roulette wheel has mean $-\frac{1}{37}$ |
| Forecast score (21.11) | Brier score $= E[(\hat{p} - Y)^2]$ |

## Study Tips

- Read 21.1.1 and 21.1.2 first. Almost every later file in this module uses either Bayes' theorem or the idea of a likelihood. The other files can be read in any order, so start with the field you care about.
- For each file, find the "Modules" entry in the map and re-read the one topic named there if it feels shaky. The files link to the exact topics.
- The syllabus lists eight mini projects (a spam filter, a Bayesian coin, a Markov chain text generator, and more). The code in 21.1.1, 21.1.3 and 21.1.5 is a starting point for three of them.
- Always check a model by simulation, then ask what the model leaves out. Naive Bayes ignores that words are linked ([21.1.1](21.1-AI-and-Machine-Learning/21.1.1-Probabilistic-Classifiers-and-Naive-Bayes.md)), a normal interval needs a large sample ([21.2](21.2-Statistics-and-Data-Science.md)).
- A classic mistake in this module is to confuse $P(\text{data} \mid \text{hypothesis})$ with $P(\text{hypothesis} \mid \text{data})$. It appears in spam filters, p-values and medical tests.

## Where This Leads

- [Module 22: Probability for Life](../22-PROBABILITY-FOR-LIFE/README.md) turns the same tools into habits for daily decisions: base rates, expected value, regression to the mean and risk.
- Beyond this book: machine learning, statistics, stochastic calculus and information theory all build on the models you met here.
- In AI and machine learning, the models in 21.1 are the starting point for reading research papers in the field.

---

[← Module 20](../20-ADVANCED-PROBABILITY/README.md) · [Syllabus](../SYLLABUS.md#module-21-applications-of-probability) · [Module 22 →](../22-PROBABILITY-FOR-LIFE/README.md)
