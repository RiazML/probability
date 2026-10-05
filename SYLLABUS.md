# Probability: The Complete Syllabus

```text
 ____            _           _     _ _ _ _
|  _ \ _ __ ___ | |__   __ _| |__ (_) (_) |_ _   _
| |_) | '__/ _ \| '_ \ / _` | '_ \| | | | __| | | |
|  __/| | | (_) | |_) | (_| | |_) | | | | |_| |_| |
|_|   |_|  \___/|_.__/ \__,_|_.__/|_|_|_|\__|\__, |
                                             |___/

     From coin flips  -->  Bayes  -->  Gaussians  -->  Entropy  -->  AI / ML
```

> A full, self-study syllabus for probability, built for three goals:
>
> 1. **Understand the math.** Know why each formula is true, not just what it is.
> 2. **Use it in AI/ML.** Know where each idea shows up in real models.
> 3. **Use it in life.** Make better decisions under uncertainty.

---

## Table of Contents

- [How to Use This Syllabus](#how-to-use-this-syllabus)
- [The Big Picture Roadmap](#the-big-picture-roadmap)
- [Module 00: Prerequisites](#module-00-prerequisites)
- **Part I: Foundations**
  - [Module 01: Sets, Sample Spaces and Events](#module-01-sets-sample-spaces-and-events)
  - [Module 02: Counting (Combinatorics)](#module-02-counting-combinatorics)
  - [Module 03: Axioms of Probability](#module-03-axioms-of-probability)
  - [Module 04: Conditional Probability, Independence and Bayes](#module-04-conditional-probability-independence-and-bayes)
- **Part II: Random Variables**
  - [Module 05: Discrete Random Variables](#module-05-discrete-random-variables)
  - [Module 06: Expectation, Variance and Moments](#module-06-expectation-variance-and-moments)
  - [Module 07: Discrete Distributions](#module-07-discrete-distributions)
  - [Module 08: Continuous Random Variables](#module-08-continuous-random-variables)
  - [Module 09: Continuous Distributions](#module-09-continuous-distributions)
- **Part III: Many Random Variables**
  - [Module 10: Joint, Marginal and Conditional Distributions](#module-10-joint-marginal-and-conditional-distributions)
  - [Module 11: Covariance, Correlation and the Covariance Matrix](#module-11-covariance-correlation-and-the-covariance-matrix)
  - [Module 12: The Multivariate Gaussian](#module-12-the-multivariate-gaussian)
  - [Module 13: Functions of Random Variables](#module-13-functions-of-random-variables)
  - [Module 14: Conditional Expectation](#module-14-conditional-expectation)
- **Part IV: Tools and Theorems**
  - [Module 15: Generating Functions](#module-15-generating-functions)
  - [Module 16: Inequalities and Concentration](#module-16-inequalities-and-concentration)
  - [Module 17: Limit Theorems (LLN and CLT)](#module-17-limit-theorems-lln-and-clt)
- **Part V: Learning from Data**
  - [Module 18: Statistical Inference (MLE, MAP, Bayesian)](#module-18-statistical-inference-mle-map-bayesian)
  - [Module 19: Information Theory](#module-19-information-theory)
- **Part VI: Randomness Over Time and Computation**
  - [Module 20: Stochastic Processes and Markov Chains](#module-20-stochastic-processes-and-markov-chains)
  - [Module 21: Sampling and Computational Probability](#module-21-sampling-and-computational-probability)
- **Part VII: Putting It to Work**
  - [Module 22: Probability in AI/ML: The Map](#module-22-probability-in-aiml-the-map)
  - [Module 23: Probability for Life](#module-23-probability-for-life)
- [Study Plan (About 30 Weeks)](#study-plan-about-30-weeks)
- [Appendix A: Notation Cheat Sheet](#appendix-a-notation-cheat-sheet)
- [Appendix B: Distribution Cheat Sheet](#appendix-b-distribution-cheat-sheet)
- [Appendix C: The One-Page Formula Sheet](#appendix-c-the-one-page-formula-sheet)
- [Appendix D: Resources](#appendix-d-resources)
- [Appendix E: Progress Tracker](#appendix-e-progress-tracker)

---

## How to Use This Syllabus

Every module has the same layout:

```text
+-----------------------------------------------------------------+
|  MODULE NN  ::  TITLE                                           |
+-----------------------------------------------------------------+
|  Why it matters  -> the one-line reason to care                 |
|  Topics          -> checklist of everything to learn            |
|  Key formulas    -> the results you must know by heart          |
|  In AI/ML        -> where it shows up in real models            |
|  In life         -> how it helps you think and decide           |
|  Practice        -> pen-and-paper + Python exercises            |
+-----------------------------------------------------------------+
```

**Importance markers:**

```text
  [*****]  Core. Used everywhere. Master it.
  [**** ]  Very important for ML.
  [***  ]  Important. Learn it well.
  [**   ]  Good to know. Come back later if short on time.
```

**The study loop for every module:**

```text
     +--------+      +---------+      +---------+      +--------+
     |  READ  | ---> | DERIVE  | ---> |  CODE   | ---> | EXPLAIN|
     | theory |      | by hand |      | simulate|      | in own |
     +--------+      +---------+      +---------+      | words  |
          ^                                            +--------+
          |                                                 |
          +------------------- repeat ----------------------+
```

1. **Read** the theory from a book or lecture (see [Resources](#appendix-d-resources)).
2. **Derive** the key formulas yourself on paper.
3. **Code** a simulation in Python and check that it matches the formula.
4. **Explain** it in your own words in a notes file in this repo.

---

## The Big Picture Roadmap

```text
                           +--------------------------+
                           |   00  PREREQUISITES      |
                           | sets, calculus, lin.alg  |
                           +------------+-------------+
                                        |
          +-----------------------------v------------------------------+
          |  PART I  FOUNDATIONS                                       |
          |  01 Sets/Events -> 02 Counting -> 03 Axioms -> 04 Bayes    |
          +-----------------------------+------------------------------+
                                        |
          +-----------------------------v------------------------------+
          |  PART II  RANDOM VARIABLES                                 |
          |  05 Discrete RV -> 06 E[X], Var -> 07 Discrete dists       |
          |  08 Continuous RV ----------------> 09 Continuous dists    |
          +-----------------------------+------------------------------+
                                        |
          +-----------------------------v------------------------------+
          |  PART III  MANY RANDOM VARIABLES                           |
          |  10 Joint -> 11 Covariance -> 12 Multivariate Gaussian     |
          |  13 Functions of RVs -> 14 Conditional Expectation         |
          +-----------------------------+------------------------------+
                                        |
          +-----------------------------v------------------------------+
          |  PART IV  TOOLS AND THEOREMS                               |
          |  15 Generating fns -> 16 Inequalities -> 17 LLN and CLT    |
          +-----------------------------+------------------------------+
                                        |
               +------------------------+------------------------+
               |                                                 |
  +------------v---------------+               +-----------------v-----------+
  | PART V  LEARNING FROM DATA |               | PART VI  PROCESSES/COMPUTE  |
  | 18 MLE, MAP, Bayesian      |               | 20 Markov chains, MDPs      |
  | 19 Entropy, KL, CE         |               | 21 Monte Carlo, MCMC, VI    |
  +------------+---------------+               +-----------------+-----------+
               |                                                 |
               +------------------------+------------------------+
                                        |
          +-----------------------------v------------------------------+
          |  PART VII  PUTTING IT TO WORK                              |
          |  22 Probability in AI/ML        23 Probability for life    |
          +------------------------------------------------------------+
```

**Shortest path to ML** (if you are in a hurry):

```text
 00 -> 01 -> 03 -> 04 -> 05 -> 06 -> 07 -> 08 -> 09 -> 10 -> 11 -> 12
    -> 14 -> 17 -> 18 -> 19 -> 21 -> 22
```

Then come back for 02, 13, 15, 16 and 20.

---

## Module 00: Prerequisites

```text
+-----------------------------------------------------------------+
|  MODULE 00  ::  PREREQUISITES                    [*****]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Probability is written in the language of sets, sums,
integrals and matrices. Weakness here shows up as confusion later.

**Topics**

- [ ] Set notation: element of, subset, union, intersection, complement
- [ ] Functions: domain, range, one-to-one, inverse functions
- [ ] Summation and product notation (Σ, Π) and their rules
- [ ] Series: arithmetic, geometric, and the exponential series
- [ ] Logarithms and exponentials (log turns products into sums)
- [ ] Derivatives: chain rule, product rule, partial derivatives, gradients
- [ ] Integrals: definite integrals, substitution, integration by parts
- [ ] Double integrals, changing the order of integration, polar coordinates
- [ ] Linear algebra: vectors, matrices, transpose, inverse, determinant
- [ ] Eigenvalues and eigenvectors; symmetric and positive semi-definite matrices
- [ ] Python: `numpy`, `matplotlib`, `scipy.stats`

**Key formulas**

```text
  Geometric series      Σ_{k=0}^{∞} r^k      = 1 / (1 - r)          for |r| < 1
  Finite geometric      Σ_{k=0}^{n-1} r^k    = (1 - r^n) / (1 - r)
  Exponential series    e^x                  = Σ_{k=0}^{∞} x^k / k!
  Limit for e           (1 + x/n)^n          -> e^x                 as n -> ∞
  Log rules             log(ab) = log a + log b,   log(a^k) = k log a
  Integration by parts  ∫ u dv               = uv - ∫ v du
  Gaussian integral     ∫_{-∞}^{∞} e^{-x²} dx = √π
```

**In AI/ML:** Log-likelihoods turn products of probabilities into sums so
computers can optimize them. Gradients drive all of deep learning. Matrices
hold covariance, data and weights.

**Practice**

1. Prove the finite geometric series formula.
2. Compute ∫ x e^{-x} dx from 0 to ∞ using integration by parts (answer: 1).
3. Prove the Gaussian integral using polar coordinates.
4. In `numpy`, generate 10,000 random numbers and plot a histogram.

---

# Part I: Foundations

## Module 01: Sets, Sample Spaces and Events

```text
+-----------------------------------------------------------------+
|  MODULE 01  ::  SETS, SAMPLE SPACES AND EVENTS   [*****]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Before you can measure uncertainty, you must describe
exactly what can happen.

**Topics**

- [ ] Random experiment, outcome, sample space Ω
- [ ] Events as subsets of Ω
- [ ] Set operations on events: union (OR), intersection (AND), complement (NOT)
- [ ] Venn diagrams
- [ ] Mutually exclusive (disjoint) events
- [ ] Partitions of the sample space
- [ ] De Morgan's laws
- [ ] Finite, countably infinite and uncountable sample spaces
- [ ] Intuition for σ-algebras (which subsets we are allowed to measure)

**Picture**

```text
     Ω  (everything that can happen)
    +-----------------------------------------+
    |        +-----------+                    |
    |        |     A  +--+--------+           |
    |        |        |A∩B|       |           |
    |        +--------+--+    B   |           |
    |                 +-----------+           |
    +-----------------------------------------+

    A ∪ B = "A or B"     A ∩ B = "A and B"     Aᶜ = "not A"
```

**Key formulas**

```text
  De Morgan       (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
                  (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
  Partition       B₁, ..., Bₙ disjoint and B₁ ∪ ... ∪ Bₙ = Ω
  Distributive    A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
```

**In AI/ML:** The set of possible labels in classification is a sample
space. The vocabulary of a language model is the sample space for the next
token.

**Practice**

1. Write the sample space for rolling two dice. How many outcomes?
2. For two dice, write the event "sum is 7" as a set.
3. Prove both De Morgan laws.

---

## Module 02: Counting (Combinatorics)

```text
+-----------------------------------------------------------------+
|  MODULE 02  ::  COUNTING                         [***  ]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** When all outcomes are equally likely,
probability = (favorable outcomes) / (total outcomes). Counting is how you
get both numbers.

**Topics**

- [ ] Multiplication rule (product rule)
- [ ] Addition rule
- [ ] Permutations: ordered, without replacement
- [ ] Combinations: unordered, without replacement
- [ ] Sampling with replacement (ordered and unordered)
- [ ] Stars and bars
- [ ] Multinomial coefficients
- [ ] Binomial theorem and Pascal's triangle
- [ ] Inclusion-exclusion principle
- [ ] Pigeonhole principle
- [ ] Story proofs (proving identities by counting two ways)
- [ ] Classic problems: birthday problem, matching (derangements), poker hands

**The counting table**

```text
  Choose k from n         |  Order matters        |  Order does not matter
  ------------------------+-----------------------+---------------------------
  Without replacement     |  n! / (n-k)!          |  C(n,k) = n! / (k!(n-k)!)
  With replacement        |  n^k                  |  C(n+k-1, k)
```

**Key formulas**

```text
  Binomial theorem     (x + y)^n = Σ_{k=0}^{n} C(n,k) x^k y^(n-k)
  Pascal's rule        C(n,k) = C(n-1,k-1) + C(n-1,k)
  Multinomial          n! / (n₁! n₂! ... n_r!)      where n₁ + ... + n_r = n
  Incl.-excl. (2 sets) |A ∪ B| = |A| + |B| - |A ∩ B|
  Incl.-excl. (3 sets) |A ∪ B ∪ C| = |A|+|B|+|C| - |A∩B|-|A∩C|-|B∩C| + |A∩B∩C|
  Stirling             n! ≈ √(2πn) (n/e)^n
```

**In AI/ML:** Size of hyperparameter grids, number of possible feature
subsets, n-gram counts, and why brute force search explodes.

**In life:** Lottery odds, password strength, and why "23 people share a
birthday half the time" surprises everyone.

**Practice**

1. How many 5-card poker hands are a full house?
2. Birthday problem: find P(at least two share a birthday) for n people.
   Plot it for n = 1..60. Where does it cross 50%? (Answer: n = 23.)
3. Derangements: what is the probability nobody gets their own hat back
   among n people? Show that it tends to 1/e.
4. Simulate the birthday problem in Python and compare with your formula.

---

## Module 03: Axioms of Probability

```text
+-----------------------------------------------------------------+
|  MODULE 03  ::  AXIOMS OF PROBABILITY            [*****]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Three simple rules (Kolmogorov's axioms) generate
everything else in probability.

**Topics**

- [ ] Interpretations: classical, frequentist, Bayesian (degree of belief)
- [ ] Kolmogorov's three axioms
- [ ] Consequences: complement rule, P(∅) = 0, monotonicity
- [ ] Addition rule for any two events
- [ ] Inclusion-exclusion for probabilities
- [ ] Union bound (Boole's inequality)
- [ ] Equally likely outcomes (naive definition) and its limits
- [ ] Geometric probability (probability as area or length)
- [ ] Continuity of probability (limits of increasing/decreasing events)

**Key formulas**

```text
  AXIOM 1   P(A) ≥ 0                                  (non-negative)
  AXIOM 2   P(Ω) = 1                                  (something happens)
  AXIOM 3   P(A₁ ∪ A₂ ∪ ...) = P(A₁) + P(A₂) + ...    (for disjoint Aᵢ)

  Complement     P(Aᶜ) = 1 - P(A)
  Addition       P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
  Monotonicity   A ⊆ B  =>  P(A) ≤ P(B)
  Union bound    P(A₁ ∪ ... ∪ Aₙ) ≤ P(A₁) + ... + P(Aₙ)
```

**In AI/ML:** Every model output that is a probability must obey these
axioms. That is why softmax outputs are non-negative and sum to 1. The union
bound appears in learning theory proofs.

**Practice**

1. Prove the complement rule and the addition rule from the axioms only.
2. A stick is broken at two uniform random points. What is the probability
   the three pieces form a triangle? (Answer: 1/4.) Verify by simulation.
3. Estimate π by throwing random points into a square (Monte Carlo).

---

## Module 04: Conditional Probability, Independence and Bayes

```text
+-----------------------------------------------------------------+
|  MODULE 04  ::  CONDITIONAL PROB. AND BAYES      [*****]  2 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** This is the single most important module. Conditional
probability is how you update beliefs with evidence. All of machine learning
is, in some sense, computing P(answer | data).

**Topics**

- [ ] Definition of conditional probability
- [ ] Multiplication rule and the chain rule of probability
- [ ] Law of total probability
- [ ] Bayes' theorem: prior, likelihood, evidence, posterior
- [ ] Odds form of Bayes' theorem
- [ ] Sequential updating (today's posterior is tomorrow's prior)
- [ ] Independence of two events
- [ ] Pairwise independence vs mutual independence
- [ ] Conditional independence
- [ ] Tree diagrams
- [ ] Classic puzzles: Monty Hall, medical testing, prosecutor's fallacy,
      Simpson's paradox, gambler's ruin

**Bayes' theorem: the picture**

```text
                   likelihood      prior
                   +--------+    +------+
                   |P(E | H)|  x | P(H) |
     P(H | E)  =   +--------+----+------+
     posterior            P(E)
                        evidence
                (normalizing constant)

     posterior  ∝  likelihood  x  prior
```

**Key formulas**

```text
  Conditional       P(A | B) = P(A ∩ B) / P(B)                     (P(B) > 0)
  Multiplication    P(A ∩ B) = P(A | B) P(B) = P(B | A) P(A)
  Chain rule        P(A₁ ∩ ... ∩ Aₙ) = P(A₁) P(A₂|A₁) P(A₃|A₁,A₂) ... P(Aₙ|A₁..Aₙ₋₁)
  Total prob.       P(A) = Σᵢ P(A | Bᵢ) P(Bᵢ)          (B₁..Bₙ a partition)
  Bayes             P(B | A) = P(A | B) P(B) / P(A)
  Bayes (expanded)  P(Bⱼ | A) = P(A | Bⱼ) P(Bⱼ) / Σᵢ P(A | Bᵢ) P(Bᵢ)
  Odds form         posterior odds = likelihood ratio x prior odds
  Independence      P(A ∩ B) = P(A) P(B)   <=>   P(A | B) = P(A)
  Cond. indep.      P(A ∩ B | C) = P(A | C) P(B | C)
```

**Worked example: the medical test**

```text
  Disease prevalence     P(D)      = 0.01
  Test sensitivity       P(+ | D)  = 0.99
  False positive rate    P(+ | Dᶜ) = 0.05

  P(+) = 0.99 x 0.01  +  0.05 x 0.99  = 0.0099 + 0.0495 = 0.0594

  P(D | +) = 0.0099 / 0.0594 ≈ 0.167    <-- only 16.7%, not 99%!

  Out of 10,000 people:
     100 sick   -->  99 test positive
   9,900 healthy --> 495 test positive
   Positive tests = 594, of which only 99 are sick.
```

**In AI/ML:**
- **Naive Bayes** classifier: Bayes' theorem + conditional independence of features.
- **Language models** use the chain rule:
  P(w₁, ..., wₙ) = Π P(wᵢ | w₁, ..., wᵢ₋₁).
- **Bayesian networks** and graphical models are built on conditional independence.
- **Spam filters**, medical AI, and any classifier's precision vs recall.

**In life:** Do not panic at a single positive test. Always ask: "What is the
base rate?" Update your beliefs gradually with each piece of evidence.

**Practice**

1. Solve Monty Hall with Bayes' theorem, then simulate 100,000 games.
2. Rework the medical example with prevalence 0.1. What changes, and why?
3. Find three events that are pairwise independent but not mutually independent.
4. Build a tiny Naive Bayes spam classifier from scratch on 10 example emails.

---

# Part II: Random Variables

## Module 05: Discrete Random Variables

```text
+-----------------------------------------------------------------+
|  MODULE 05  ::  DISCRETE RANDOM VARIABLES        [*****]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** A random variable turns outcomes into numbers so we can
do math on them.

**Topics**

- [ ] Random variable as a function X: Ω -> ℝ
- [ ] Discrete vs continuous random variables
- [ ] Probability mass function (PMF)
- [ ] Cumulative distribution function (CDF) and its properties
- [ ] Indicator random variables
- [ ] Functions of a random variable, Y = g(X)
- [ ] Distribution vs random variable (same distribution, different variables)
- [ ] Support of a random variable

**Picture: a random variable is a function**

```text
     Ω (outcomes)                  ℝ (numbers)
   +--------------+              +-----------+
   |  HH  --------+------------> |    2      |
   |  HT  --------+----+         |           |
   |  TH  --------+----+-------> |    1      |     X = number of heads
   |  TT  --------+------------> |    0      |
   +--------------+              +-----------+

     PMF:  P(X=0)=1/4   P(X=1)=1/2   P(X=2)=1/4
```

**Key formulas**

```text
  PMF          p(x) = P(X = x),     p(x) ≥ 0,     Σₓ p(x) = 1
  CDF          F(x) = P(X ≤ x) = Σ_{t ≤ x} p(t)
  CDF facts    non-decreasing,  F(-∞) = 0,  F(+∞) = 1,  right-continuous
  Interval     P(a < X ≤ b) = F(b) - F(a)
  Indicator    I_A = 1 if A happens, else 0
```

**In AI/ML:** A classifier's output is a PMF over classes. The label `y` in a
dataset is a random variable.

**Practice**

1. Write the PMF and draw the CDF for the sum of two dice.
2. Show that a CDF of a discrete variable is a step function.
3. Simulate the sum of two dice 100,000 times and compare with the PMF.

---

## Module 06: Expectation, Variance and Moments

```text
+-----------------------------------------------------------------+
|  MODULE 06  ::  EXPECTATION, VARIANCE, MOMENTS   [*****]  1.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** Expectation is the "center" of a distribution and the
basis of every loss function. Variance measures spread and risk.

**Topics**

- [ ] Expected value (mean) of a discrete random variable
- [ ] Linearity of expectation (works even without independence!)
- [ ] LOTUS: law of the unconscious statistician
- [ ] Indicator trick: E[I_A] = P(A)
- [ ] Variance and standard deviation
- [ ] Properties of variance under shifting and scaling
- [ ] Moments: raw and central; skewness and kurtosis
- [ ] Median, mode and quantiles
- [ ] Tail-sum formula for non-negative integer variables
- [ ] Expected value as the best constant predictor under squared error

**Key formulas**

```text
  Expectation     E[X] = Σₓ x p(x)
  LOTUS           E[g(X)] = Σₓ g(x) p(x)
  Linearity       E[aX + bY + c] = a E[X] + b E[Y] + c
  Indicator       E[I_A] = P(A)
  Variance        Var(X) = E[(X - μ)²] = E[X²] - (E[X])²
  Scaling         Var(aX + b) = a² Var(X)
  Std. dev.       σ = √Var(X)
  k-th moment     E[X^k]
  Skewness        E[(X - μ)³] / σ³
  Kurtosis        E[(X - μ)⁴] / σ⁴
  Tail sum        E[X] = Σ_{k=1}^{∞} P(X ≥ k)       (X ∈ {0, 1, 2, ...})
  Best constant   argmin_c E[(X - c)²] = E[X]
                  argmin_c E[|X - c|]  = median(X)
```

**In AI/ML:**
- **Risk** of a model is an expectation: R(f) = E[ L(f(X), Y) ].
- **Training** minimizes empirical risk: (1/n) Σ L(f(xᵢ), yᵢ).
- **SGD** works because a mini-batch gradient is an unbiased estimate of the
  true gradient (its expectation equals the full gradient).
- MSE loss predicts the **mean**; MAE loss predicts the **median**.

**In life:** Expected value tells you whether a bet, a job offer or an
insurance plan is worth it on average. Variance tells you how much it can
hurt.

**Practice**

1. Use indicators to find the expected number of fixed points in a random
   permutation of n items. (Answer: 1, for every n.)
2. Prove E[X²] ≥ (E[X])².
3. Prove that E[X] minimizes E[(X - c)²] over c.
4. A game costs $5. You roll a die and win $(2 x roll). Should you play?

---

## Module 07: Discrete Distributions

```text
+-----------------------------------------------------------------+
|  MODULE 07  ::  DISCRETE DISTRIBUTIONS           [*****]  1.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** A small set of named distributions models most
real-world counts. Learn their stories, not just their formulas.

**Topics**

- [ ] Bernoulli: one yes/no trial
- [ ] Binomial: number of successes in n independent trials
- [ ] Geometric: trials until the first success (memoryless)
- [ ] Negative binomial: failures before the r-th success
- [ ] Poisson: number of rare events in a fixed interval
- [ ] Hypergeometric: draws without replacement
- [ ] Discrete uniform
- [ ] Categorical: one roll of a k-sided die
- [ ] Multinomial: counts from n rolls of a k-sided die
- [ ] Poisson approximation to the binomial
- [ ] Relationships between distributions

**The family tree**

```text
                      Bernoulli(p)
                     /     |      \
          sum of n  /      |       \  trials until 1st success
                   v       |        v
           Binomial(n,p)   |     Geometric(p)
                |          |           |
    n->∞, p->0  |          |           | failures before r-th success
    np = λ      v          |           v
            Poisson(λ)     |     Negative Binomial(r,p)
                           |
                 k outcomes|
                           v
                   Categorical(p₁..pₖ)
                           |
                  n trials |
                           v
                  Multinomial(n, p₁..pₖ)
```

**Key formulas**

```text
  Distribution      PMF P(X = k)                         Mean      Variance
  ---------------   -----------------------------------  --------  -------------
  Bernoulli(p)      p^k (1-p)^(1-k),   k ∈ {0,1}         p         p(1-p)
  Binomial(n,p)     C(n,k) p^k (1-p)^(n-k)               np        np(1-p)
  Geometric(p)      (1-p)^(k-1) p,     k = 1,2,...       1/p       (1-p)/p²
  NegBin(r,p)       C(k+r-1,k) p^r (1-p)^k, k = 0,1,...  r(1-p)/p  r(1-p)/p²
  Poisson(λ)        e^(-λ) λ^k / k!,   k = 0,1,...       λ         λ
  Hypergeom(N,K,n)  C(K,k) C(N-K,n-k) / C(N,n)           nK/N      n(K/N)(1-K/N)(N-n)/(N-1)
  Uniform{a..b}     1 / (b-a+1)                          (a+b)/2   ((b-a+1)² - 1)/12

  Memoryless (geometric):   P(X > m + n | X > m) = P(X > n)
```

**In AI/ML:**
- **Bernoulli** -> binary classification, logistic regression, dropout masks.
- **Categorical** -> softmax output of every classifier and every LLM token.
- **Binomial** -> accuracy on a test set of n examples; A/B tests.
- **Poisson** -> count data (clicks, arrivals, word counts), Poisson regression.
- **Multinomial** -> bag-of-words models, topic models (LDA).

**Practice**

1. Derive the mean and variance of the binomial using indicators.
2. Show Binomial(n, λ/n) -> Poisson(λ) as n -> ∞.
3. Prove the geometric distribution is memoryless.
4. Plot every PMF above with `scipy.stats` for a few parameter values.

---

## Module 08: Continuous Random Variables

```text
+-----------------------------------------------------------------+
|  MODULE 08  ::  CONTINUOUS RANDOM VARIABLES      [*****]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Heights, weights, time, pixel intensities and neural
network weights are continuous. Probability becomes area under a curve.

**Topics**

- [ ] Probability density function (PDF)
- [ ] Why P(X = x) = 0 for a continuous variable
- [ ] A density can be greater than 1 (it is not a probability)
- [ ] CDF and its relationship with the PDF
- [ ] Expectation and variance using integrals
- [ ] LOTUS for continuous variables
- [ ] Quantile function (inverse CDF), median, percentiles
- [ ] Change of variables for one variable (monotonic g)
- [ ] Mixed discrete-continuous distributions (intuition)

**Picture**

```text
   f(x)
    |              ___
    |            /     \
    |          /  #####  \               P(a ≤ X ≤ b) = shaded area
    |        /    #####    \                          = ∫ₐᵇ f(x) dx
    |      /      #####      \
    |____/________#####________\______
                  a   b                x
```

**Key formulas**

```text
  PDF rules       f(x) ≥ 0,     ∫_{-∞}^{∞} f(x) dx = 1
  Probability     P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx = F(b) - F(a)
  CDF <-> PDF     F(x) = ∫_{-∞}^{x} f(t) dt,       f(x) = F'(x)
  Expectation     E[X] = ∫ x f(x) dx
  LOTUS           E[g(X)] = ∫ g(x) f(x) dx
  Quantile        Q(u) = F⁻¹(u)
  Change of var.  Y = g(X), g monotonic:
                  f_Y(y) = f_X(g⁻¹(y)) · | d g⁻¹(y) / dy |
```

**In AI/ML:**
- **Normalizing flows** are built entirely on the change-of-variables formula.
- **Inverse transform sampling** uses the quantile function to generate samples.
- **Likelihood** of continuous data uses densities, which is why
  log-likelihoods can be positive.

**Practice**

1. Find c so that f(x) = c x² on [0, 1] is a PDF. Find its mean and variance.
2. If X ~ Uniform(0, 1), find the PDF of Y = -ln(X). (It is Exponential(1).)
3. Show by example that a density can exceed 1.

---

## Module 09: Continuous Distributions

```text
+-----------------------------------------------------------------+
|  MODULE 09  ::  CONTINUOUS DISTRIBUTIONS         [*****]  2 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** The normal distribution alone is the backbone of
statistics and ML. The others model waiting times, proportions, and priors.

**Topics**

- [ ] Uniform
- [ ] Normal (Gaussian): standardization, z-scores, 68-95-99.7 rule
- [ ] Exponential: waiting times, memoryless
- [ ] Gamma: sum of exponentials; the Gamma function
- [ ] Beta: distribution over probabilities
- [ ] Chi-square, Student's t, F (needed for statistics)
- [ ] Laplace (double exponential)
- [ ] Log-normal
- [ ] Cauchy (a distribution with no mean)
- [ ] Logistic and Gumbel
- [ ] Dirichlet: distribution over probability vectors
- [ ] Heavy tails vs light tails

**The normal curve**

```text
                            |
                         .--+--.
                       /    |    \
                     /      |      \
                   /|       |       |\
                 /  |       |       |  \
              _/    |       |       |    \_
          ___/      |       |       |      \___
     ----+-----+----+-------+-------+----+-----+----
       μ-3σ  μ-2σ  μ-σ      μ      μ+σ  μ+2σ  μ+3σ
                    |<----68%------>|
               |<---------95%----------->|
          |<-------------99.7%--------------->|
```

**Key formulas**

```text
  Distribution     PDF f(x)                                  Mean        Variance
  ---------------  ----------------------------------------  ----------  ------------------
  Uniform(a,b)     1/(b-a),  a ≤ x ≤ b                       (a+b)/2     (b-a)²/12
  Normal(μ,σ²)     (1/√(2πσ²)) exp(-(x-μ)²/(2σ²))            μ           σ²
  Exponential(λ)   λ e^(-λx),  x ≥ 0                         1/λ         1/λ²
  Gamma(α,β)       β^α x^(α-1) e^(-βx) / Γ(α),  x > 0        α/β         α/β²
  Beta(α,β)        x^(α-1) (1-x)^(β-1) / B(α,β),  0<x<1      α/(α+β)     αβ/((α+β)²(α+β+1))
  Laplace(μ,b)     (1/(2b)) exp(-|x-μ|/b)                    μ           2b²
  Chi-square(k)    = Gamma(k/2, 1/2)                         k           2k
  Student-t(ν)     heavy-tailed bell                         0 (ν>1)     ν/(ν-2)  (ν>2)
  Log-normal(μ,σ²) ln X ~ Normal(μ, σ²)                      e^(μ+σ²/2)  (e^σ² - 1) e^(2μ+σ²)
  Cauchy           1 / (π(1 + x²))                           undefined   undefined

  Gamma function   Γ(α) = ∫₀^∞ x^(α-1) e^(-x) dx,   Γ(n) = (n-1)!,   Γ(1/2) = √π
  Beta function    B(α,β) = Γ(α)Γ(β) / Γ(α+β)
  Standardize      Z = (X - μ) / σ  ~  Normal(0, 1)
  Dirichlet(α)     mean of component i = αᵢ / Σⱼ αⱼ
```

**In AI/ML:**
- **Normal** -> weight initialization, noise models, linear regression, VAEs,
  diffusion models, batch normalization.
- **Uniform** -> random initialization, random search, data augmentation.
- **Beta** -> prior for a probability (click-through rate, Thompson sampling).
- **Dirichlet** -> prior over class probabilities, topic models.
- **Laplace** -> the prior behind L1 regularization (Lasso).
- **Gumbel** -> Gumbel-softmax trick for sampling discrete variables in a
  differentiable way.
- **Student-t** -> robust regression; t-SNE uses a t-distribution in low
  dimensions.

**Practice**

1. Show that the exponential distribution is memoryless.
2. Prove that the sum of n independent Exponential(λ) is Gamma(n, λ).
3. Show that Beta(1, 1) is Uniform(0, 1).
4. Simulate the Cauchy distribution and watch the running mean never settle.

---

# Part III: Many Random Variables

## Module 10: Joint, Marginal and Conditional Distributions

```text
+-----------------------------------------------------------------+
|  MODULE 10  ::  JOINT DISTRIBUTIONS              [*****]  1.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** Data has many features. To model them you need to
describe several random variables at once.

**Topics**

- [ ] Joint PMF and joint PDF
- [ ] Joint CDF
- [ ] Marginal distributions (sum or integrate out the other variable)
- [ ] Conditional distributions
- [ ] Independence of random variables
- [ ] i.i.d. (independent and identically distributed)
- [ ] Bayes' theorem for random variables (discrete and continuous)
- [ ] Mixture distributions

**Picture: a joint table**

```text
                    Y = 0     Y = 1   |  P(X = x)   <-- marginal of X
              +---------+---------+   +----------
      X = 0   |  0.10   |  0.20   |   |   0.30
      X = 1   |  0.30   |  0.40   |   |   0.70
              +---------+---------+   +----------
   P(Y = y)      0.40      0.60       |   1.00
                    ^
                    +-- marginal of Y

   P(Y = 1 | X = 1) = 0.40 / 0.70 ≈ 0.571
```

**Key formulas**

```text
  Marginal (disc.)    p_X(x) = Σ_y p(x, y)
  Marginal (cont.)    f_X(x) = ∫ f(x, y) dy
  Conditional         f(y | x) = f(x, y) / f_X(x)
  Joint = cond x marg f(x, y) = f(y | x) f_X(x)
  Independence        f(x, y) = f_X(x) f_Y(y)    for all x, y
  Bayes for RVs       f(x | y) = f(y | x) f_X(x) / ∫ f(y | x') f_X(x') dx'
  Mixture             f(x) = Σₖ πₖ fₖ(x),   πₖ ≥ 0,   Σ πₖ = 1
```

**In AI/ML:**
- **Generative models** learn the joint p(x, y). **Discriminative models**
  learn the conditional p(y | x).
- Most ML assumes training data is **i.i.d.**; distribution shift is what
  happens when that fails.
- **Gaussian mixture models** are mixture distributions.

**Practice**

1. For the table above, are X and Y independent? Show why.
2. If (X, Y) is uniform on the unit disk, find the marginal of X.
3. Write the joint, marginal and conditional for a 3x3 table of your choice.

---

## Module 11: Covariance, Correlation and the Covariance Matrix

```text
+-----------------------------------------------------------------+
|  MODULE 11  ::  COVARIANCE AND CORRELATION       [*****]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Covariance measures how two variables move together. The
covariance matrix is at the heart of PCA, Gaussians and optimization.

**Topics**

- [ ] Covariance and its properties
- [ ] Correlation coefficient and why it is between -1 and 1
- [ ] Variance of a sum
- [ ] Uncorrelated does NOT imply independent
- [ ] Random vectors, mean vector, covariance matrix
- [ ] Covariance matrix is symmetric and positive semi-definite
- [ ] Linear transformation of a random vector
- [ ] Sample mean, sample covariance
- [ ] Correlation vs causation

**Picture**

```text
   ρ ≈ +1           ρ ≈ 0              ρ ≈ -1          ρ = 0 but dependent
   y |     .:       y |  .  : .        y | :.            y | .         .
     |   .:'          | : . .: .         |  ':.            |  .       .
     | .:'            |.  :. . :         |    ':.          |   ' . . '
     +------ x        +-------- x        +------- x        +--------- x
                                                             (Y = X²)
```

**Key formulas**

```text
  Covariance       Cov(X,Y) = E[(X - μ_X)(Y - μ_Y)] = E[XY] - E[X]E[Y]
  Correlation      ρ = Cov(X,Y) / (σ_X σ_Y),      -1 ≤ ρ ≤ 1
  Bilinearity      Cov(aX + b, cY + d) = ac Cov(X,Y)
  Var of sum       Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X,Y)
  Independent =>   Cov(X,Y) = 0     (but NOT the other way around)
  Cov. matrix      Σ = E[(X - μ)(X - μ)ᵀ],    Σᵢⱼ = Cov(Xᵢ, Xⱼ)
  Linear map       Y = AX + b  =>  E[Y] = Aμ + b,   Cov(Y) = A Σ Aᵀ
  Var of a·X       Var(aᵀX) = aᵀ Σ a ≥ 0      (so Σ is positive semi-definite)
  Sample cov.      S = (1/(n-1)) Σᵢ (xᵢ - x̄)(xᵢ - x̄)ᵀ
```

**In AI/ML:**
- **PCA** = eigen-decomposition of the covariance matrix.
- **Whitening** and **batch/layer normalization** fix means and variances.
- **Feature correlation** analysis, multicollinearity in regression.
- **Weight initialization** (Xavier/He) is chosen to keep variance stable
  through layers.

**Practice**

1. Let X ~ Uniform(-1, 1) and Y = X². Show Cov(X, Y) = 0 but they are dependent.
2. Prove Var(aᵀX) = aᵀ Σ a.
3. Compute the covariance matrix of a real dataset (e.g. Iris) with `numpy`
   and run PCA by hand using `np.linalg.eigh`.

---

## Module 12: The Multivariate Gaussian

```text
+-----------------------------------------------------------------+
|  MODULE 12  ::  THE MULTIVARIATE GAUSSIAN        [*****]  1.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** The most important distribution in ML. It stays Gaussian
under linear maps, marginalization and conditioning, so many problems have
exact answers.

**Topics**

- [ ] PDF of the multivariate normal
- [ ] Geometry: contours are ellipses set by the eigenvectors of Σ
- [ ] Mahalanobis distance
- [ ] Standard normal vector and the Cholesky trick for sampling
- [ ] Affine transformations stay Gaussian
- [ ] Marginals are Gaussian
- [ ] Conditionals are Gaussian (formula below)
- [ ] For Gaussians, uncorrelated <=> independent
- [ ] Sums of independent Gaussians
- [ ] Product of Gaussian densities (used in Bayesian updates)

**Picture: contours**

```text
     x₂
      |          .--------.
      |       .'   .----.   '.          Ellipses = points with equal density.
      |     /    .'  μ   '.   \         Axes point along eigenvectors of Σ.
      |     \    '.      .'   /         Axis lengths ∝ √(eigenvalues).
      |       '.   '----'   .'
      |          '--------'
      +--------------------------- x₁
```

**Key formulas**

```text
  PDF           f(x) = (2π)^(-d/2) |Σ|^(-1/2) exp( -½ (x - μ)ᵀ Σ⁻¹ (x - μ) )
  Mahalanobis   D²(x) = (x - μ)ᵀ Σ⁻¹ (x - μ)
  Sampling      x = μ + L z,   where Σ = L Lᵀ (Cholesky),  z ~ N(0, I)
  Affine        X ~ N(μ, Σ)  =>  AX + b ~ N(Aμ + b, A Σ Aᵀ)

  Partition     x = [x₁; x₂],   μ = [μ₁; μ₂],   Σ = [Σ₁₁ Σ₁₂; Σ₂₁ Σ₂₂]
  Marginal      x₁ ~ N(μ₁, Σ₁₁)
  Conditional   x₁ | x₂ ~ N( μ₁ + Σ₁₂ Σ₂₂⁻¹ (x₂ - μ₂),   Σ₁₁ - Σ₁₂ Σ₂₂⁻¹ Σ₂₁ )
  Sum           X ~ N(μ₁,σ₁²), Y ~ N(μ₂,σ₂²) indep.  =>  X+Y ~ N(μ₁+μ₂, σ₁²+σ₂²)
```

**In AI/ML:**
- **Gaussian processes** (conditioning formula = GP prediction).
- **Kalman filters** for tracking and robotics.
- **VAEs** and **diffusion models** use Gaussian latents and Gaussian noise.
- **Gaussian Mixture Models**, **LDA/QDA** classifiers.
- **Linear regression** with Gaussian noise; Bayesian linear regression.

**Practice**

1. Derive the 1-D normal PDF as a special case of the multivariate one.
2. Sample from a 2-D Gaussian with a given Σ using Cholesky. Plot the cloud
   and its contour ellipses.
3. Derive the conditional mean formula for the 2-D case.
4. Show that the squared Mahalanobis distance of x ~ N(μ, Σ) in d dimensions
   follows a chi-square(d) distribution (by simulation).

---

## Module 13: Functions of Random Variables

```text
+-----------------------------------------------------------------+
|  MODULE 13  ::  FUNCTIONS OF RANDOM VARIABLES    [***  ]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Neural networks are functions of random variables. To
know the distribution of an output you must transform distributions.

**Topics**

- [ ] CDF method
- [ ] Change of variables in one dimension (review)
- [ ] Multivariate change of variables and the Jacobian
- [ ] Sums of independent random variables: convolution
- [ ] Sums of known distributions (Poisson + Poisson, Normal + Normal, ...)
- [ ] Maximum and minimum of random variables
- [ ] Order statistics
- [ ] Box-Muller transform

**Key formulas**

```text
  CDF method       F_Y(y) = P(g(X) ≤ y),   then differentiate
  Jacobian (n-D)   Y = g(X), g invertible:
                   f_Y(y) = f_X(g⁻¹(y)) · | det J_{g⁻¹}(y) |
  Log form         log f_Y(y) = log f_X(x) - log | det J_g(x) |,   x = g⁻¹(y)
  Convolution      f_{X+Y}(z) = ∫ f_X(x) f_Y(z - x) dx
  Poisson sum      Pois(λ₁) + Pois(λ₂) = Pois(λ₁ + λ₂)        (independent)
  Max of n iid     F_max(x) = F(x)^n
  Min of n iid     F_min(x) = 1 - (1 - F(x))^n
  Box-Muller       U₁, U₂ ~ U(0,1):  Z = √(-2 ln U₁) cos(2π U₂) ~ N(0, 1)
```

**In AI/ML:**
- **Normalizing flows**: the log-determinant of the Jacobian is the key term.
- **Max pooling** and extreme value statistics use the max of variables.
- **Reparameterization trick** expresses a random variable as a function of
  simple noise.

**Practice**

1. If X, Y ~ Uniform(0,1) independent, find the PDF of X + Y (a triangle).
2. Find the distribution of the minimum of n independent Exponential(λ).
3. Implement Box-Muller and check the result with a histogram and a QQ plot.

---

## Module 14: Conditional Expectation

```text
+-----------------------------------------------------------------+
|  MODULE 14  ::  CONDITIONAL EXPECTATION          [**** ]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** E[Y | X] is the best possible prediction of Y from X.
That is exactly what regression tries to learn.

**Topics**

- [ ] Conditional expectation E[Y | X = x] as a number
- [ ] E[Y | X] as a random variable
- [ ] Law of total expectation (tower property)
- [ ] Law of total variance (Eve's law)
- [ ] E[Y | X] is the best predictor under squared error
- [ ] Taking out what is known: E[g(X) Y | X] = g(X) E[Y | X]
- [ ] Random sums (sum of a random number of variables)
- [ ] Martingales (intuition only)

**Key formulas**

```text
  Discrete        E[Y | X = x] = Σ_y y P(Y = y | X = x)
  Continuous      E[Y | X = x] = ∫ y f(y | x) dy
  Tower (Adam)    E[ E[Y | X] ] = E[Y]
  Eve's law       Var(Y) = E[ Var(Y | X) ] + Var( E[Y | X] )
                           (within-group)    (between-group)
  Known factor    E[ g(X) Y | X ] = g(X) E[Y | X]
  Best predictor  argmin_h E[(Y - h(X))²] = E[Y | X]
  Random sum      N indep. of Xᵢ iid:  E[Σ_{i=1}^{N} Xᵢ] = E[N] E[X]
```

**In AI/ML:**
- **Regression** learns f(x) ≈ E[Y | X = x].
- **Reinforcement learning**: the value function is a conditional expectation,
  V(s) = E[ return | state = s ], and the Bellman equation is the tower
  property applied one step at a time.
- **Bias-variance decomposition** and **EM algorithm** use these laws.

**Practice**

1. Prove the tower property for discrete variables.
2. Prove that E[Y | X] minimizes mean squared error.
3. A store has N ~ Poisson(λ) customers a day, each spending X with mean μ.
   Find the expected total revenue.

---

# Part IV: Tools and Theorems

## Module 15: Generating Functions

```text
+-----------------------------------------------------------------+
|  MODULE 15  ::  GENERATING FUNCTIONS             [**   ]  0.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** Generating functions turn hard problems (sums of
variables, moments) into easy algebra, and they are the tool used to prove
the Central Limit Theorem.

**Topics**

- [ ] Moment generating function (MGF)
- [ ] Getting moments by differentiating the MGF
- [ ] MGF of a sum of independent variables = product of MGFs
- [ ] Uniqueness: same MGF => same distribution
- [ ] Probability generating function (PGF)
- [ ] Characteristic function (always exists)
- [ ] Cumulants (intuition)

**Key formulas**

```text
  MGF                M_X(t) = E[e^(tX)]
  Moments            E[X^n] = M_X^(n)(0)     (n-th derivative at 0)
  Sum (indep.)       M_{X+Y}(t) = M_X(t) M_Y(t)
  PGF                G_X(s) = E[s^X],    P(X = k) = G^(k)(0) / k!
  Characteristic     φ_X(t) = E[e^(itX)]

  Bernoulli(p)       M(t) = 1 - p + p e^t
  Binomial(n,p)      M(t) = (1 - p + p e^t)^n
  Poisson(λ)         M(t) = exp(λ(e^t - 1))
  Exponential(λ)     M(t) = λ / (λ - t),        t < λ
  Normal(μ,σ²)       M(t) = exp(μt + σ²t²/2)
```

**In AI/ML:** Chernoff bounds (Module 16) are built from MGFs. Cumulants
appear in some theory of neural networks at initialization.

**Practice**

1. Use MGFs to prove that the sum of independent Poissons is Poisson.
2. Find the mean and variance of Exponential(λ) from its MGF.

---

## Module 16: Inequalities and Concentration

```text
+-----------------------------------------------------------------+
|  MODULE 16  ::  INEQUALITIES AND CONCENTRATION   [**** ]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Often you cannot compute a probability exactly, but you
can bound it. These bounds explain why ML models generalize from finite data.

**Topics**

- [ ] Markov's inequality
- [ ] Chebyshev's inequality
- [ ] Jensen's inequality (convex functions)
- [ ] Cauchy-Schwarz inequality
- [ ] Union bound (review)
- [ ] Chernoff bounds
- [ ] Hoeffding's inequality
- [ ] Concentration of measure (intuition): averages of many variables are
      very predictable

**Key formulas**

```text
  Markov        X ≥ 0, a > 0:      P(X ≥ a) ≤ E[X] / a
  Chebyshev     P(|X - μ| ≥ kσ) ≤ 1 / k²
  Jensen        f convex:          f(E[X]) ≤ E[f(X)]
                f concave:         f(E[X]) ≥ E[f(X)]     (e.g. log)
  Cauchy-Schw.  |E[XY]| ≤ √(E[X²] E[Y²])
  Chernoff      P(X ≥ a) ≤ min_{t>0} e^(-ta) M_X(t)
  Hoeffding     X₁..Xₙ indep., Xᵢ ∈ [a, b]:
                P( |X̄ - E[X̄]| ≥ ε ) ≤ 2 exp( -2nε² / (b - a)² )
```

**In AI/ML:**
- **Generalization bounds / PAC learning** use Hoeffding + union bound.
- **Jensen** proves KL divergence ≥ 0 and gives the **ELBO** in VAEs.
- **Bandits**: the UCB algorithm comes straight from Hoeffding.
- **How many test examples do I need?** Hoeffding gives an answer.

**In life:** Chebyshev says at least 75% of any data is within 2 standard
deviations of the mean, whatever the distribution.

**Practice**

1. Prove Markov's inequality, then derive Chebyshev from it.
2. Use Jensen to show E[log X] ≤ log E[X].
3. Using Hoeffding, how many test examples do you need to know a classifier's
   accuracy within ±2% with 95% confidence?

---

## Module 17: Limit Theorems (LLN and CLT)

```text
+-----------------------------------------------------------------+
|  MODULE 17  ::  LIMIT THEOREMS                   [*****]  1.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** The Law of Large Numbers says averages converge to the
truth. The Central Limit Theorem says those averages look Gaussian. Together
they justify almost all of statistics and Monte Carlo methods.

**Topics**

- [ ] Modes of convergence: in probability, almost surely, in distribution,
      in mean square
- [ ] How the modes relate to each other
- [ ] Weak Law of Large Numbers (WLLN)
- [ ] Strong Law of Large Numbers (SLLN)
- [ ] Central Limit Theorem (CLT)
- [ ] Normal approximation to the binomial and Poisson; continuity correction
- [ ] Standard error and the 1/√n rate
- [ ] Delta method
- [ ] Slutsky's theorem (intuition)
- [ ] When the CLT fails (infinite variance, e.g. Cauchy)

**Picture: the CLT in action**

```text
   n = 1 (one die)       n = 2 (avg of 2)      n = 30 (avg of 30)
   +-+-+-+-+-+-+          .                        .
   | | | | | | |         .:.                      .:.
   | | | | | | |        .:::.                    .:::.
   | | | | | | |       .:::::.                  .:::::.
   +-+-+-+-+-+-+      .:::::::.              ..:::::::::..
     flat               triangle               bell curve!
```

**Key formulas**

```text
  Convergence chain   almost surely  =>  in probability  =>  in distribution
  WLLN                X̄ₙ -> μ in probability:  P(|X̄ₙ - μ| > ε) -> 0
  SLLN                X̄ₙ -> μ almost surely
  CLT                 √n (X̄ₙ - μ) / σ  ->  N(0, 1)     in distribution
  Practical CLT       X̄ₙ ≈ N(μ, σ²/n),     Σ Xᵢ ≈ N(nμ, nσ²)
  Standard error      SE(X̄) = σ / √n
  Delta method        √n (g(X̄ₙ) - g(μ))  ->  N(0, g'(μ)² σ²)
```

**In AI/ML:**
- **Mini-batch gradients** are averages, so they are approximately Gaussian
  and concentrate around the true gradient.
- **Monte Carlo** error shrinks like 1/√n: 100x more samples = 10x accuracy.
- **Confidence intervals** for model accuracy and A/B tests.
- **Ensembles** reduce variance by averaging.

**In life:** Small samples lie. A restaurant with 3 reviews averaging 5 stars
tells you much less than one with 3,000 reviews averaging 4.6.

**Practice**

1. Prove the WLLN using Chebyshev's inequality.
2. Simulate the CLT: averages of n draws from Exponential(1) for
   n = 1, 2, 5, 30, 100. Plot histograms.
3. Show by simulation that the running average of Cauchy samples does not
   converge.

---

# Part V: Learning from Data

## Module 18: Statistical Inference (MLE, MAP, Bayesian)

```text
+-----------------------------------------------------------------+
|  MODULE 18  ::  STATISTICAL INFERENCE            [*****]  3 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Probability goes from model to data. Inference goes from
data back to the model. Training an ML model IS statistical inference.

**Topics**

*Estimation basics*
- [ ] Population vs sample, parameters vs statistics
- [ ] Estimators: bias, variance, mean squared error, consistency
- [ ] Sample mean and sample variance (why divide by n - 1)
- [ ] Bias-variance tradeoff

*Maximum Likelihood (MLE)*
- [ ] Likelihood function and log-likelihood
- [ ] MLE for Bernoulli, Binomial, Poisson, Normal, Exponential
- [ ] Properties: consistency, asymptotic normality, invariance
- [ ] Fisher information and the Cramér-Rao bound (intuition)
- [ ] Negative log-likelihood (NLL) as a loss function

*Bayesian inference*
- [ ] Prior, likelihood, posterior
- [ ] Conjugate priors
- [ ] MAP estimation and its link to regularization
- [ ] Posterior predictive distribution
- [ ] Credible intervals vs confidence intervals

*Frequentist tools*
- [ ] Confidence intervals
- [ ] Hypothesis testing: null and alternative, p-values
- [ ] Type I and Type II errors, significance level, power
- [ ] z-test, t-test, chi-square test
- [ ] A/B testing in practice
- [ ] Multiple testing problem
- [ ] Bootstrap

**MLE vs MAP vs Bayesian**

```text
  +--------------+----------------------------------+-------------------------+
  | Method       | What it computes                 | Output                  |
  +--------------+----------------------------------+-------------------------+
  | MLE          | argmax_θ  p(data | θ)            | one best θ              |
  | MAP          | argmax_θ  p(data | θ) p(θ)       | one best θ (with prior) |
  | Full Bayes   | p(θ | data) ∝ p(data | θ) p(θ)   | whole distribution      |
  +--------------+----------------------------------+-------------------------+
```

**Key formulas**

```text
  Likelihood       L(θ) = Πᵢ p(xᵢ | θ)
  Log-likelihood   ℓ(θ) = Σᵢ log p(xᵢ | θ)
  MLE              θ̂_MLE = argmax_θ ℓ(θ)
  MAP              θ̂_MAP = argmax_θ [ ℓ(θ) + log p(θ) ]
  Posterior        p(θ | x) = p(x | θ) p(θ) / p(x)
  Predictive       p(x_new | x) = ∫ p(x_new | θ) p(θ | x) dθ

  MSE of estimator MSE(θ̂) = Bias(θ̂)² + Var(θ̂)
  Bias-variance    E[(y - f̂(x))²] = Bias² + Variance + σ²_noise
  Sample variance  s² = (1/(n-1)) Σ (xᵢ - x̄)²          (unbiased)
  Fisher info      I(θ) = -E[ ∂² log p(X | θ) / ∂θ² ]
  Cramér-Rao       Var(θ̂) ≥ 1 / (n I(θ))               (unbiased θ̂)
  CI for mean      x̄ ± z_{α/2} · σ / √n                (95%: z = 1.96)

  MLE results:     Bernoulli p̂ = x̄        Poisson λ̂ = x̄
                   Normal μ̂ = x̄,  σ̂² = (1/n) Σ (xᵢ - x̄)²
                   Exponential λ̂ = 1 / x̄
```

**Conjugate priors**

```text
  Likelihood          Prior               Posterior
  ------------------  ------------------  ------------------------------------
  Bernoulli/Binomial  Beta(α, β)          Beta(α + successes, β + failures)
  Poisson             Gamma(α, β)         Gamma(α + Σxᵢ, β + n)
  Normal (known σ²)   Normal(μ₀, τ²)      Normal (precision-weighted average)
  Categorical/Multi.  Dirichlet(α)        Dirichlet(α + counts)
```

**In AI/ML: the most important connections in this whole syllabus**

```text
  +-----------------------------+--------------------------------------------+
  | You write this loss...      | ...and you are actually doing this         |
  +-----------------------------+--------------------------------------------+
  | Mean squared error          | MLE with Gaussian noise                    |
  | Binary cross-entropy        | MLE with Bernoulli outputs                 |
  | Categorical cross-entropy   | MLE with Categorical (softmax) outputs     |
  | MSE + L2 penalty (Ridge)    | MAP with a Gaussian prior on weights       |
  | MSE + L1 penalty (Lasso)    | MAP with a Laplace prior on weights        |
  | Label smoothing             | Mixing targets with a uniform distribution |
  +-----------------------------+--------------------------------------------+
```

- **Overfitting / underfitting** = the bias-variance tradeoff.
- **Thompson sampling** and Bayesian optimization use posteriors.
- **A/B testing** for product decisions uses hypothesis tests.

**Practice**

1. Derive the MLE for Bernoulli, Poisson and Normal by hand.
2. Prove that minimizing MSE equals maximizing a Gaussian likelihood.
3. Prove that L2 regularization equals a Gaussian prior (MAP).
4. Coin flips: start with a Beta(1,1) prior, update after each flip, and
   plot how the posterior narrows.
5. Bootstrap a 95% confidence interval for the median of a dataset.

---

## Module 19: Information Theory

```text
+-----------------------------------------------------------------+
|  MODULE 19  ::  INFORMATION THEORY               [**** ]  1.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** Entropy, cross-entropy and KL divergence are the loss
functions and measuring tools of modern deep learning.

**Topics**

- [ ] Information content (surprise) of an event
- [ ] Entropy: average surprise, measured in bits or nats
- [ ] Joint and conditional entropy, chain rule
- [ ] Cross-entropy
- [ ] KL divergence: properties, asymmetry, forward vs reverse KL
- [ ] Mutual information
- [ ] Jensen-Shannon divergence
- [ ] Maximum entropy distributions (uniform, exponential, Gaussian)
- [ ] Perplexity
- [ ] Source coding intuition (entropy = shortest average code length)

**Picture**

```text
   |<------------------- H(X,Y) ------------------->|
   +------------------+----------+------------------+
   |      H(X|Y)      |  I(X;Y)  |      H(Y|X)      |
   +------------------+----------+------------------+
   |<---------- H(X) ----------->|
                      |<---------- H(Y) ----------->|

   Mutual information I(X;Y) is the overlap: what X and Y share.
```

**Key formulas**

```text
  Surprise         I(x) = -log p(x)
  Entropy          H(X) = -Σ p(x) log p(x)                (max = log k, uniform)
  Joint            H(X,Y) = -Σ p(x,y) log p(x,y)
  Conditional      H(Y | X) = H(X,Y) - H(X)
  Chain rule       H(X,Y) = H(X) + H(Y | X)
  Cross-entropy    H(p, q) = -Σ p(x) log q(x)
  KL divergence    D_KL(p || q) = Σ p(x) log( p(x) / q(x) ) ≥ 0
  Key identity     H(p, q) = H(p) + D_KL(p || q)
  Mutual info      I(X;Y) = H(X) - H(X | Y) = D_KL( p(x,y) || p(x)p(y) )
  JS divergence    JS(p, q) = ½ D_KL(p || m) + ½ D_KL(q || m),   m = ½(p + q)
  Perplexity       PPL = exp( cross-entropy in nats )
  KL of Gaussians  D_KL( N(μ,σ²) || N(0,1) ) = ½ ( σ² + μ² - 1 - ln σ² )
```

**In AI/ML:**
- **Cross-entropy loss** for every classifier and every LLM.
- Minimizing cross-entropy = minimizing KL to the true distribution
  = maximizing likelihood.
- **VAEs**: the loss has a KL term (formula above).
- **RLHF / PPO**: a KL penalty keeps the fine-tuned model near the base model.
- **Knowledge distillation**: KL between teacher and student outputs.
- **Decision trees**: information gain = mutual information.
- **GANs**: the original GAN minimizes a Jensen-Shannon divergence.
- **LLM evaluation**: perplexity.

**Practice**

1. Compute the entropy of a fair coin, a biased coin (p = 0.9), and a fair die.
2. Prove D_KL(p || q) ≥ 0 using Jensen's inequality.
3. Show D_KL(p || q) ≠ D_KL(q || p) with a numeric example.
4. Derive the KL between N(μ, σ²) and N(0, 1).
5. Compute the cross-entropy loss of a softmax output by hand and in `numpy`.

---

# Part VI: Randomness Over Time and Computation

## Module 20: Stochastic Processes and Markov Chains

```text
+-----------------------------------------------------------------+
|  MODULE 20  ::  STOCHASTIC PROCESSES             [**** ]  2 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Many things evolve randomly over time: text, prices,
game states, robots. Reinforcement learning and MCMC are built on Markov
chains.

**Topics**

- [ ] What a stochastic process is
- [ ] Random walks and gambler's ruin
- [ ] Markov property ("the future depends only on the present")
- [ ] Transition matrix, n-step transitions
- [ ] Classification of states: recurrent, transient, absorbing, periodic
- [ ] Irreducible and aperiodic chains
- [ ] Stationary distribution and convergence to it
- [ ] Detailed balance (reversibility)
- [ ] Absorbing chains: absorption probabilities and expected time
- [ ] Poisson process: arrivals, exponential inter-arrival times
- [ ] Brownian motion (intuition)
- [ ] Hidden Markov Models: forward algorithm, Viterbi
- [ ] Markov Decision Processes (MDPs) and the Bellman equation

**Picture: a 3-state weather chain**

```text
                         0.2
           +-------+  -------->  +--------+
     0.7   | SUNNY |             | CLOUDY |   0.5
    (stay) +-------+  <--------  +--------+  (stay)
            |    ^       0.3       |    ^
        0.1 |    | 0.3         0.2 |    | 0.4
            v    |                 v    |
           +-----------------------------+
           |            RAINY            |   0.3 (stay)
           +-----------------------------+

                   to: Sun  Cld  Rain
         P = from Sun [ 0.7  0.2  0.1 ]     each row sums to 1
                  Cld [ 0.3  0.5  0.2 ]
                  Rain[ 0.3  0.4  0.3 ]
```

**Key formulas**

```text
  Markov property   P(X_{n+1} | X_n, X_{n-1}, ..., X_0) = P(X_{n+1} | X_n)
  n-step            P(X_n = j | X_0 = i) = (Pⁿ)ᵢⱼ
  Chapman-Kolm.     P^(m+n) = P^m P^n
  Stationary        π = π P,    Σᵢ πᵢ = 1
  Detailed balance  πᵢ Pᵢⱼ = πⱼ Pⱼᵢ    =>  π is stationary
  Poisson process   N(t) ~ Poisson(λt),   inter-arrival times ~ Exponential(λ)
  Bellman (MDP)     V(s) = maxₐ Σ_{s'} P(s' | s, a) [ R(s, a, s') + γ V(s') ]
```

**In AI/ML:**
- **Reinforcement learning** is built on MDPs and Bellman equations.
- **PageRank** is the stationary distribution of a random surfer.
- **MCMC** sampling designs a Markov chain whose stationary distribution is
  the target.
- **Diffusion models**: the forward process is a Markov chain adding Gaussian noise.
- **HMMs** for speech, part-of-speech tagging, and time series.
- **Language models** generate text one token at a time (autoregressive).

**Practice**

1. Find the stationary distribution of the weather chain above by hand and
   by computing Pⁿ for large n in `numpy`.
2. Gambler's ruin: start with $10, bet $1 on fair flips until $0 or $20.
   Find P(reach $20) and simulate it.
3. Implement PageRank on a 5-page toy web.
4. Solve a tiny grid-world MDP with value iteration.

---

## Module 21: Sampling and Computational Probability

```text
+-----------------------------------------------------------------+
|  MODULE 21  ::  SAMPLING AND MONTE CARLO         [**** ]  2 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Most real probability problems have no closed-form
answer. You simulate. Modern generative AI is, at its core, sampling.

**Topics**

- [ ] Pseudo-random number generators and seeds
- [ ] Monte Carlo estimation and its error
- [ ] Inverse transform sampling
- [ ] Rejection sampling
- [ ] Importance sampling
- [ ] Markov Chain Monte Carlo (MCMC): Metropolis-Hastings
- [ ] Gibbs sampling
- [ ] Burn-in, mixing, autocorrelation, diagnostics
- [ ] Variational inference and the ELBO
- [ ] Reparameterization trick
- [ ] Score function (REINFORCE) gradient estimator
- [ ] Gumbel-max and Gumbel-softmax
- [ ] Sampling from language models: temperature, top-k, top-p (nucleus)
- [ ] Bootstrap resampling (review)

**Key formulas**

```text
  Monte Carlo       E[f(X)] ≈ (1/n) Σᵢ f(xᵢ),   xᵢ ~ p,   error ≈ σ_f / √n
  Inverse transform U ~ Uniform(0,1)  =>  X = F⁻¹(U) has CDF F
  Rejection         sample x ~ q, accept with prob. p(x) / (M q(x)),  p ≤ Mq
  Importance        E_p[f(X)] = E_q[ f(X) p(X) / q(X) ]
  Metropolis-H.     accept x' with prob. min(1, p(x') q(x | x') / (p(x) q(x' | x)))
  ELBO              log p(x) ≥ E_q[ log p(x | z) ] - D_KL( q(z | x) || p(z) )
  Reparam. trick    z = μ + σ ⊙ ε,   ε ~ N(0, I)   (gradients flow through μ, σ)
  Score function    ∇_θ E_{p_θ}[f(X)] = E_{p_θ}[ f(X) ∇_θ log p_θ(X) ]
  Gumbel-max        argmaxᵢ (log πᵢ + Gᵢ) ~ Categorical(π),   Gᵢ ~ Gumbel(0,1)
  Temperature       pᵢ = exp(zᵢ / T) / Σⱼ exp(zⱼ / T)
                    T < 1 sharper (safer),  T > 1 flatter (more random)
```

**In AI/ML:**
- **VAEs**: ELBO + reparameterization trick.
- **Policy gradient RL** (REINFORCE, PPO): score function estimator.
- **Diffusion models** and **LLMs** generate by sampling.
- **Bayesian deep learning**: MCMC and variational inference over weights.
- **Off-policy RL** uses importance sampling.

**Practice**

1. Sample from Exponential(λ) using inverse transform. Check the histogram.
2. Estimate ∫₀¹ e^(-x²) dx with Monte Carlo and compare to `scipy`.
3. Implement Metropolis-Hastings to sample from a 2-peaked 1-D distribution.
4. Implement temperature, top-k and top-p sampling on a toy logits vector.

---

# Part VII: Putting It to Work

## Module 22: Probability in AI/ML: The Map

```text
+-----------------------------------------------------------------+
|  MODULE 22  ::  PROBABILITY IN AI/ML: THE MAP    [*****]  always|
+-----------------------------------------------------------------+
```

**Why it matters:** This module connects every earlier module to real models.
Come back to it as you learn ML.

**The map**

```text
+----------------------------+------------------------------------+---------+
| ML model / technique       | Probability behind it              | Modules |
+----------------------------+------------------------------------+---------+
| Linear regression          | Gaussian likelihood, MLE           | 09 18   |
| Ridge / Lasso              | MAP with Gaussian / Laplace prior  | 09 18   |
| Logistic regression        | Bernoulli likelihood, MLE          | 07 18   |
| Softmax classifier         | Categorical, cross-entropy         | 07 19   |
| Naive Bayes                | Bayes + conditional independence   | 04 10   |
| k-means / GMM              | Mixtures, multivariate Gaussian,EM | 10 12 14|
| PCA                        | Covariance matrix, eigenvectors    | 11 12   |
| Decision trees             | Entropy, information gain          | 19      |
| Random forests / bagging   | Bootstrap, variance reduction      | 17 18   |
| Neural net initialization  | Variance of sums of random vars    | 06 11   |
| Dropout                    | Bernoulli masks                    | 07      |
| Batch / layer norm         | Mean and variance                  | 06 11   |
| SGD                        | Unbiased gradient estimates, LLN   | 06 17   |
| Language models (LLMs)     | Chain rule, categorical, CE, PPL   | 04 07 19|
| LLM decoding               | Temperature, top-k, top-p sampling | 21      |
| VAEs                       | Latent Gaussians, ELBO, KL, reparam| 12 19 21|
| GANs                       | JS divergence, implicit models     | 19      |
| Diffusion models           | Gaussian Markov chain, score fn    | 12 20 21|
| Normalizing flows          | Change of variables, Jacobian      | 08 13   |
| Gaussian processes         | Conditioning multivariate Gaussian | 12      |
| HMMs                       | Markov chains, forward/Viterbi     | 20      |
| Bayesian networks          | Conditional independence           | 04 10   |
| Reinforcement learning     | MDPs, expectations, Bellman        | 14 20   |
| Policy gradients (PPO)     | Score function, importance ratio   | 21      |
| RLHF                       | KL penalty to a reference model    | 19      |
| Multi-armed bandits        | Hoeffding (UCB), Beta (Thompson)   | 16 18   |
| Bayesian optimization      | Gaussian processes, expected gain  | 12 18   |
| Calibration / uncertainty  | Probabilities that match frequency | 03 18   |
| A/B testing                | Hypothesis tests, CIs, power       | 17 18   |
| Generalization theory      | Concentration inequalities         | 16      |
+----------------------------+------------------------------------+---------+
```

**Must-know derivations for ML interviews and research**

- [ ] MSE loss = Gaussian MLE
- [ ] Cross-entropy loss = Bernoulli / Categorical MLE
- [ ] L2 regularization = Gaussian prior; L1 = Laplace prior
- [ ] Bias-variance decomposition
- [ ] Softmax + cross-entropy gradient = (predicted - true)
- [ ] KL divergence between two Gaussians
- [ ] ELBO derivation via Jensen's inequality
- [ ] Reparameterization trick
- [ ] EM algorithm for Gaussian mixtures
- [ ] Xavier/He initialization variance
- [ ] Bellman equation from the tower property

**Mini projects (put them in this repo)**

```text
  [ ] P1  Monte Carlo playground: π, birthday problem, Monty Hall
  [ ] P2  CLT visualizer for any distribution
  [ ] P3  Naive Bayes spam filter from scratch
  [ ] P4  Bayesian coin: animate a Beta posterior updating
  [ ] P5  Logistic regression from scratch as MLE with gradient descent
  [ ] P6  Gaussian mixture model with EM from scratch
  [ ] P7  Markov chain text generator, then compare to a bigram LM
  [ ] P8  Metropolis-Hastings sampler with diagnostics
  [ ] P9  Thompson sampling vs UCB on a multi-armed bandit
  [ ] P10 Tiny VAE on MNIST (KL + reparameterization)
```

---

## Module 23: Probability for Life

```text
+-----------------------------------------------------------------+
|  MODULE 23  ::  PROBABILITY FOR LIFE             [*****]  always|
+-----------------------------------------------------------------+
```

**Why it matters:** Probability is the logic of uncertainty. Every important
decision (health, money, career, relationships) is made under uncertainty.

**Ideas to live by**

```text
+--------------------------+--------------------------------------------------+
| Idea                     | What it teaches you                              |
+--------------------------+--------------------------------------------------+
| Base rates               | Ask "how common is this in general?" first.      |
| Bayesian updating        | Change your mind gradually as evidence arrives.  |
| Expected value           | Judge choices by average outcome, not best case. |
| Variance and risk        | Same average, different risk. Avoid ruin.        |
| Gambler's fallacy        | Coins have no memory. "Due" is not a thing.      |
| Regression to the mean   | Extreme results are usually followed by normal.  |
| Law of small numbers     | Small samples swing wildly. Wait for more data.  |
| Correlation vs causation | Two things moving together may share a cause.    |
| Simpson's paradox        | A trend can reverse when groups are combined.    |
| Survivorship bias        | You only see the winners who survived.           |
| Conjunction fallacy      | P(A and B) can never exceed P(A).                |
| Compounding small risks  | P(at least once in n tries) = 1 - (1 - p)^n      |
| Fat tails                | Rare events can dominate (crashes, pandemics).   |
| Kelly criterion          | Bet size f* = p - (1 - p)/b, never bet it all.   |
| Calibration              | When you say 70% sure, be right 70% of the time. |
+--------------------------+--------------------------------------------------+
```

**Practice**

1. A 1% daily risk sounds small. What is the chance it happens at least once
   in a year? (Answer: 1 - 0.99^365 ≈ 97.4%.)
2. Find a news headline that confuses correlation with causation.
3. Keep a prediction journal for a month: write down events with your
   probability, then check how calibrated you were.
4. Compute the expected value of a lottery ticket in your country.

---

## Study Plan (About 30 Weeks)

About 8 to 10 hours a week. Each `##` is one week. In a hurry? Follow the
[shortest path to ML](#the-big-picture-roadmap) first (about 25 weeks).

```text
 WEEK                    1   3   5   7   9   11  13  15  17  19  21  23  25  27  29  31
                         |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
 00  Prerequisites       ##
 01  Sets and events       ##
 02  Counting                ##
 03  Axioms                    ##
 04  Conditional + Bayes         ####
 05  Discrete RVs                    ##
 06  E[X], Var                         ###
 07  Discrete dists                       ###
 08  Continuous RVs                          ##
 09  Continuous dists                          ####
 10  Joint dists                                   ###
 11  Covariance                                       ##
 12  Multivar. Gaussian                                 ###
 13  Functions of RVs                                      ##
 14  Cond. expectation                                       ##
 15  Generating fns                                            #
 16  Inequalities                                               ##
 17  LLN and CLT                                                  ###
 18  Inference                                                       ######
 19  Information theory                                                    ###
 20  Markov chains                                                            ####
 21  Sampling, MCMC                                                               ####
 22  AI/ML map            ===== use alongside your ML study from week 5 onward =====
 23  Probability for life ===== practice it every day, starting now ==============
```

**Weekly rhythm (about 8 to 10 hours a week)**

```text
  +-----------+-----------------------------------------------+
  | Mon-Tue   | Lectures / reading, take notes                |
  | Wed       | Derive key formulas by hand                   |
  | Thu-Fri   | Problem sets (10 to 15 problems)              |
  | Sat       | Python simulation of the week's ideas         |
  | Sun       | Review, write a summary in this repo, rest    |
  +-----------+-----------------------------------------------+
```

---

## Appendix A: Notation Cheat Sheet

```text
  Symbol            Meaning
  ----------------  ---------------------------------------------------------
  Ω                 sample space (all possible outcomes)
  ω                 one outcome
  A, B              events (subsets of Ω)
  Aᶜ                complement of A ("not A")
  A ∪ B, A ∩ B      union ("or"), intersection ("and")
  P(A)              probability of event A
  P(A | B)          probability of A given B
  X, Y, Z           random variables (capital letters)
  x, y, z           specific values (lowercase letters)
  p(x), f(x)        PMF / PDF
  F(x)              CDF, P(X ≤ x)
  X ~ D             "X has distribution D"
  iid               independent and identically distributed
  E[X], μ           expected value / mean
  Var(X), σ²        variance
  σ                 standard deviation
  Cov(X, Y)         covariance
  ρ                 correlation coefficient
  Σ (matrix)        covariance matrix
  X̄                 sample mean
  θ                 model parameters
  θ̂                 an estimate of θ
  L(θ), ℓ(θ)        likelihood, log-likelihood
  H(X)              entropy
  D_KL(p || q)      KL divergence from q to p
  N(μ, σ²)          normal distribution
  ∝                 "proportional to"
  ->d, ->p, ->a.s.  convergence in distribution / probability / almost surely
```

---

## Appendix B: Distribution Cheat Sheet

| Distribution | Type | Support | Parameters | Mean | Variance | Story / ML use |
|---|---|---|---|---|---|---|
| Bernoulli | Discrete | {0, 1} | p | p | p(1-p) | One yes/no trial; binary labels, dropout |
| Binomial | Discrete | {0..n} | n, p | np | np(1-p) | Successes in n trials; test accuracy |
| Geometric | Discrete | {1, 2, ...} | p | 1/p | (1-p)/p² | Trials until first success |
| Negative Binomial | Discrete | {0, 1, ...} | r, p | r(1-p)/p | r(1-p)/p² | Failures before r-th success; overdispersed counts |
| Poisson | Discrete | {0, 1, ...} | λ | λ | λ | Rare event counts; clicks, arrivals |
| Hypergeometric | Discrete | {0..n} | N, K, n | nK/N | n(K/N)(1-K/N)(N-n)/(N-1) | Draws without replacement |
| Categorical | Discrete | {1..k} | p₁..pₖ | - | - | One k-way choice; softmax, next token |
| Multinomial | Discrete | counts | n, p₁..pₖ | npᵢ | npᵢ(1-pᵢ) | Counts of k outcomes; bag of words |
| Uniform | Continuous | [a, b] | a, b | (a+b)/2 | (b-a)²/12 | Total ignorance; random init |
| Normal | Continuous | ℝ | μ, σ² | μ | σ² | Sums of many effects; noise, VAEs |
| Exponential | Continuous | [0, ∞) | λ | 1/λ | 1/λ² | Waiting time; memoryless |
| Gamma | Continuous | (0, ∞) | α, β | α/β | α/β² | Sum of exponentials; prior on rates |
| Beta | Continuous | (0, 1) | α, β | α/(α+β) | αβ/((α+β)²(α+β+1)) | Prior on a probability; Thompson sampling |
| Dirichlet | Continuous | simplex | α₁..αₖ | αᵢ/Σα | - | Prior on probability vectors; topic models |
| Laplace | Continuous | ℝ | μ, b | μ | 2b² | Sharp peak; L1 regularization |
| Student-t | Continuous | ℝ | ν | 0 | ν/(ν-2) | Heavy tails; robust models, t-SNE |
| Chi-square | Continuous | (0, ∞) | k | k | 2k | Sum of k squared normals; tests |
| Log-normal | Continuous | (0, ∞) | μ, σ² | e^(μ+σ²/2) | (e^σ²-1)e^(2μ+σ²) | Products of effects; incomes, prices |
| Cauchy | Continuous | ℝ | x₀, γ | undefined | undefined | Counterexample: CLT fails |
| Gumbel | Continuous | ℝ | μ, β | μ + βγ | π²β²/6 | Maximum of samples; Gumbel-softmax |

(γ ≈ 0.5772 is the Euler-Mascheroni constant.)

---

## Appendix C: The One-Page Formula Sheet

```text
+==============================================================================+
|                        PROBABILITY ON ONE PAGE                               |
+==============================================================================+
|  BASICS                                                                      |
|   P(Aᶜ) = 1 - P(A)            P(A ∪ B) = P(A) + P(B) - P(A ∩ B)              |
|   P(A | B) = P(A ∩ B) / P(B)  P(A) = Σ P(A | Bᵢ) P(Bᵢ)                       |
|   Bayes:  P(H | E) = P(E | H) P(H) / P(E)                                    |
|   Independent:  P(A ∩ B) = P(A) P(B)                                         |
+------------------------------------------------------------------------------+
|  EXPECTATION AND VARIANCE                                                    |
|   E[aX + bY + c] = aE[X] + bE[Y] + c       (always)                          |
|   Var(X) = E[X²] - E[X]²       Var(aX + b) = a² Var(X)                       |
|   Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X, Y)                                 |
|   Cov(X, Y) = E[XY] - E[X]E[Y]      ρ = Cov / (σ_X σ_Y)                      |
|   E[E[Y | X]] = E[Y]       Var(Y) = E[Var(Y | X)] + Var(E[Y | X])            |
+------------------------------------------------------------------------------+
|  GAUSSIAN                                                                    |
|   N(μ, σ²):  (1/√(2πσ²)) exp(-(x - μ)² / (2σ²))      Z = (X - μ) / σ         |
|   AX + b ~ N(Aμ + b, AΣAᵀ)        68 / 95 / 99.7 within 1 / 2 / 3 σ          |
+------------------------------------------------------------------------------+
|  LIMITS AND BOUNDS                                                           |
|   LLN: X̄ -> μ          CLT: X̄ ≈ N(μ, σ²/n)          SE = σ / √n              |
|   Markov: P(X ≥ a) ≤ E[X]/a       Chebyshev: P(|X - μ| ≥ kσ) ≤ 1/k²          |
|   Jensen (convex f): f(E[X]) ≤ E[f(X)]                                       |
+------------------------------------------------------------------------------+
|  INFERENCE                                                                   |
|   MLE: argmax Σ log p(xᵢ | θ)       MAP: argmax [Σ log p(xᵢ | θ) + log p(θ)] |
|   posterior ∝ likelihood x prior    MSE = Bias² + Variance                   |
+------------------------------------------------------------------------------+
|  INFORMATION                                                                 |
|   H(p) = -Σ p log p        H(p, q) = -Σ p log q = H(p) + D_KL(p || q)        |
|   D_KL(p || q) = Σ p log(p / q) ≥ 0        I(X;Y) = H(X) - H(X | Y)          |
+==============================================================================+
```

---

## Appendix D: Resources

**Main textbooks (pick one to follow)**

| Book | Level | Why |
|---|---|---|
| Blitzstein and Hwang, *Introduction to Probability* (2nd ed.) | Beginner to intermediate | Best intuition and story proofs. Free PDF from the authors. |
| Bertsekas and Tsitsiklis, *Introduction to Probability* | Beginner to intermediate | Very clear, engineering-friendly. |
| Sheldon Ross, *A First Course in Probability* | Beginner | Lots of worked examples and exercises. |

**For the statistics and ML parts**

| Book | Covers |
|---|---|
| Wasserman, *All of Statistics* | Fast, complete tour of inference for CS people |
| Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Ch. 6) | Probability exactly as ML uses it. Free online. |
| Bishop, *Pattern Recognition and Machine Learning* | Probabilistic ML classic |
| Murphy, *Probabilistic Machine Learning: An Introduction* | Modern, complete. Free online. |
| MacKay, *Information Theory, Inference, and Learning Algorithms* | Information theory + Bayesian ML. Free online. |
| Cover and Thomas, *Elements of Information Theory* | The standard information theory text |
| Grimmett and Stirzaker, *Probability and Random Processes* | Rigorous, for later |

**Courses and videos**

- Harvard **Stat 110** (Joe Blitzstein): full lectures on YouTube, problem sets online.
- MIT **6.041 / RES.6-012** Probabilistic Systems Analysis (John Tsitsiklis): MIT OpenCourseWare.
- Stanford **CS109** Probability for Computer Scientists.
- **3Blue1Brown**: Bayes' theorem, the Central Limit Theorem, and convolutions.
- **Seeing Theory** (Brown University): interactive visual probability.

**Python tools**

```text
  numpy           random sampling, linear algebra
  scipy.stats     every distribution: pdf, cdf, ppf, rvs, fit
  matplotlib      plotting histograms and densities
  seaborn         nicer statistical plots
  pandas          working with real datasets
  PyMC / NumPyro  Bayesian modeling and MCMC
  torch.distributions   distributions inside deep learning models
```

---

## Appendix E: Progress Tracker

```text
  MODULE                                   READ  DERIVE  CODE  EXPLAIN  DONE
  ---------------------------------------  ----  ------  ----  -------  ----
  00  Prerequisites                        [ ]   [ ]     [ ]   [ ]      [ ]
  01  Sets, sample spaces, events          [ ]   [ ]     [ ]   [ ]      [ ]
  02  Counting                             [ ]   [ ]     [ ]   [ ]      [ ]
  03  Axioms of probability                [ ]   [ ]     [ ]   [ ]      [ ]
  04  Conditional probability and Bayes    [ ]   [ ]     [ ]   [ ]      [ ]
  05  Discrete random variables            [ ]   [ ]     [ ]   [ ]      [ ]
  06  Expectation, variance, moments       [ ]   [ ]     [ ]   [ ]      [ ]
  07  Discrete distributions               [ ]   [ ]     [ ]   [ ]      [ ]
  08  Continuous random variables          [ ]   [ ]     [ ]   [ ]      [ ]
  09  Continuous distributions             [ ]   [ ]     [ ]   [ ]      [ ]
  10  Joint distributions                  [ ]   [ ]     [ ]   [ ]      [ ]
  11  Covariance and correlation           [ ]   [ ]     [ ]   [ ]      [ ]
  12  Multivariate Gaussian                [ ]   [ ]     [ ]   [ ]      [ ]
  13  Functions of random variables        [ ]   [ ]     [ ]   [ ]      [ ]
  14  Conditional expectation              [ ]   [ ]     [ ]   [ ]      [ ]
  15  Generating functions                 [ ]   [ ]     [ ]   [ ]      [ ]
  16  Inequalities and concentration       [ ]   [ ]     [ ]   [ ]      [ ]
  17  Limit theorems                       [ ]   [ ]     [ ]   [ ]      [ ]
  18  Statistical inference                [ ]   [ ]     [ ]   [ ]      [ ]
  19  Information theory                   [ ]   [ ]     [ ]   [ ]      [ ]
  20  Stochastic processes                 [ ]   [ ]     [ ]   [ ]      [ ]
  21  Sampling and Monte Carlo             [ ]   [ ]     [ ]   [ ]      [ ]
  22  Probability in AI/ML                 [ ]   [ ]     [ ]   [ ]      [ ]
  23  Probability for life                 [ ]   [ ]     [ ]   [ ]      [ ]
```

```text
   "Probability theory is nothing but common sense reduced to calculation."
                                                   -- Pierre-Simon Laplace
```
