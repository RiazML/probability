# Probability: Zero to Hero

```text
 ____            _           _     _ _ _ _
|  _ \ _ __ ___ | |__   __ _| |__ (_) (_) |_ _   _
| |_) | '__/ _ \| '_ \ / _` | '_ \| | | | __| | | |
|  __/| | | (_) | |_) | (_| | |_) | | | | |_| |_| |
|_|   |_|  \___/|_.__/ \__,_|_.__/|_|_|_|\__|\__, |
                                             |___/

   ZERO  -->  coin flips  -->  Bayes  -->  distributions  -->  CLT  -->  HERO
```

> A complete self-study path through **probability and nothing else**:
> from "what is a sample space?" to Markov chains, martingales and
> measure-theoretic probability, plus where probability is used in the
> real world.
>
> 1. **Understand it.** Know why each result is true, not just the formula.
> 2. **Use it.** Know where it shows up: AI/ML, computer science, finance,
>    medicine, games and more.
> 3. **Live it.** Make better decisions under uncertainty.

---

## Table of Contents

- [How to Use This Syllabus](#how-to-use-this-syllabus)
- [Zero to Hero: The Five Levels](#zero-to-hero-the-five-levels)
- **Level 1: Zero (Foundations)**
  - [Module 01: Sets, Sample Spaces and Events](#module-01-sets-sample-spaces-and-events)
  - [Module 02: Counting](#module-02-counting)
  - [Module 03: Axioms of Probability](#module-03-axioms-of-probability)
  - [Module 04: Conditional Probability, Independence and Bayes](#module-04-conditional-probability-independence-and-bayes)
- **Level 2: Random Variables**
  - [Module 05: Discrete Random Variables](#module-05-discrete-random-variables)
  - [Module 06: Expectation, Variance and Moments](#module-06-expectation-variance-and-moments)
  - [Module 07: Discrete Distributions](#module-07-discrete-distributions)
  - [Module 08: Continuous Random Variables](#module-08-continuous-random-variables)
  - [Module 09: Continuous Distributions](#module-09-continuous-distributions)
- **Level 3: Many Random Variables**
  - [Module 10: Joint Distributions](#module-10-joint-distributions)
  - [Module 11: Covariance and Correlation](#module-11-covariance-and-correlation)
  - [Module 12: The Multivariate Gaussian](#module-12-the-multivariate-gaussian)
  - [Module 13: Functions of Random Variables](#module-13-functions-of-random-variables)
  - [Module 14: Conditional Expectation](#module-14-conditional-expectation)
- **Level 4: The Big Theorems**
  - [Module 15: Generating Functions](#module-15-generating-functions)
  - [Module 16: Inequalities and Concentration](#module-16-inequalities-and-concentration)
  - [Module 17: Limit Theorems (LLN and CLT)](#module-17-limit-theorems-lln-and-clt)
- **Level 5: Hero**
  - [Module 18: Stochastic Processes](#module-18-stochastic-processes)
  - [Module 19: Simulation and Monte Carlo](#module-19-simulation-and-monte-carlo)
  - [Module 20: Advanced Probability (Measure Theory)](#module-20-advanced-probability-measure-theory)
- **Uses of Probability**
  - [Module 21: Applications of Probability](#module-21-applications-of-probability)
  - [Module 22: Probability for Life](#module-22-probability-for-life)
- [Study Plan](#study-plan)
- [Appendix A: Notation Cheat Sheet](#appendix-a-notation-cheat-sheet)
- [Appendix B: Distribution Cheat Sheet](#appendix-b-distribution-cheat-sheet)
- [Appendix C: The One-Page Formula Sheet](#appendix-c-the-one-page-formula-sheet)
- [Appendix D: Resources](#appendix-d-resources)
- [Appendix E: Progress Tracker](#appendix-e-progress-tracker)

---

## How to Use This Syllabus

Every module folder in this repo matches a module below, and every file in
the folder matches one topic in the module's checklist.

Every module has the same layout:

```text
+-----------------------------------------------------------------+
|  MODULE NN  ::  TITLE                                           |
+-----------------------------------------------------------------+
|  Why it matters   -> the one-line reason to care                |
|  Topics           -> checklist of everything to learn           |
|  Key formulas     -> the results you must know by heart         |
|  Where it's used  -> real uses of the ideas                     |
|  Practice         -> pen-and-paper + simulation exercises       |
+-----------------------------------------------------------------+
```

**Importance markers**

```text
  [*****]  Core. Used everywhere. Master it.
  [**** ]  Very important.
  [***  ]  Important. Learn it well.
  [**   ]  Good to know. Come back later if short on time.
```

**The study loop for every module**

```text
     +--------+      +---------+      +----------+      +---------+
     |  READ  | ---> | DERIVE  | ---> | SIMULATE | ---> | EXPLAIN |
     | theory |      | by hand |      | in code  |      | in own  |
     +--------+      +---------+      +----------+      |  words  |
          ^                                             +---------+
          |                                                  |
          +-------------------- repeat ----------------------+
```

1. **Read** the theory from a book or lecture (see [Resources](#appendix-d-resources)).
2. **Derive** the key results yourself on paper.
3. **Simulate** it with a few lines of Python and check it matches.
4. **Explain** it in your own words in the matching file in this repo.

**What you need before starting:** school algebra is enough for Level 1.
From Module 08 on you need basic calculus (derivatives and integrals).
Modules 11 and 12 use a little matrix algebra. Learn those bits as you meet
them; this syllabus stays focused on probability.

---

## Zero to Hero: The Five Levels

```text
  LEVEL 5  HERO              +--------------------------------------------+
                             | 18 Stochastic processes   19 Simulation    |
                             | 20 Advanced (measure-theoretic) probability|
                             +---------------------^----------------------+
                                                   |
  LEVEL 4  BIG THEOREMS      +---------------------+----------------------+
                             | 15 Generating fns  16 Inequalities  17 CLT |
                             +---------------------^----------------------+
                                                   |
  LEVEL 3  MANY VARIABLES    +---------------------+----------------------+
                             | 10 Joint  11 Covariance  12 Multivar. Gauss|
                             | 13 Functions of RVs  14 Cond. expectation  |
                             +---------------------^----------------------+
                                                   |
  LEVEL 2  RANDOM VARIABLES  +---------------------+----------------------+
                             | 05 Discrete RV  06 E[X],Var  07 Discrete   |
                             | 08 Continuous RV  09 Continuous dists      |
                             +---------------------^----------------------+
                                                   |
  LEVEL 1  ZERO              +---------------------+----------------------+
                             | 01 Sets/Events  02 Counting  03 Axioms     |
                             | 04 Conditional probability and Bayes       |
                             +--------------------------------------------+

  USES (alongside every level)
     21 Applications: AI/ML, CS, finance, medicine, games, ...
     22 Probability for life: better decisions every day
```

---

# Level 1: Zero (Foundations)

## Module 01: Sets, Sample Spaces and Events

```text
+-----------------------------------------------------------------+
|  MODULE 01  ::  SETS, SAMPLE SPACES AND EVENTS   [*****]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Before you can measure uncertainty, you must describe
exactly what can happen.

**Topics**

- [ ] What probability is: a number between 0 and 1 measuring how likely something is
- [ ] Random experiment, outcome, sample space Ω
- [ ] Events as subsets of Ω
- [ ] Set operations on events: union (OR), intersection (AND), complement (NOT)
- [ ] Venn diagrams
- [ ] Mutually exclusive (disjoint) events
- [ ] Partitions of the sample space
- [ ] De Morgan's laws
- [ ] Finite, countably infinite and uncountable sample spaces

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

**Where it's used:** Every probability problem starts here: listing the
possible outcomes of a game, a test, a network packet, or the next word a
language model can output.

**Practice**

1. Write the sample space for rolling two dice. How many outcomes?
2. For two dice, write the event "sum is 7" as a set.
3. Prove both De Morgan laws.

---

## Module 02: Counting

```text
+-----------------------------------------------------------------+
|  MODULE 02  ::  COUNTING                         [**** ]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** When all outcomes are equally likely,
probability = (favorable outcomes) / (total outcomes). Counting gets you
both numbers.

**Topics**

- [ ] Multiplication rule and addition rule
- [ ] Permutations: ordered, without replacement
- [ ] Combinations: unordered, without replacement
- [ ] Sampling with replacement (ordered and unordered)
- [ ] Stars and bars
- [ ] Multinomial coefficients
- [ ] Binomial theorem and Pascal's triangle
- [ ] Inclusion-exclusion principle
- [ ] Pigeonhole principle
- [ ] Story proofs (proving identities by counting two ways)
- [ ] Classic problems: birthday problem, derangements (matching), poker hands

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

**Where it's used:** Lottery and poker odds, password strength, hash
collisions (the birthday problem), counting possible DNA sequences, and
estimating how fast a brute-force search blows up.

**Practice**

1. How many 5-card poker hands are a full house?
2. Birthday problem: find P(at least two share a birthday) for n people.
   Where does it cross 50%? (Answer: n = 23.)
3. Derangements: what is the probability nobody gets their own hat back
   among n people? Show that it tends to 1/e.
4. Simulate the birthday problem and compare with your formula.

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

**Where it's used:** Any system that outputs probabilities must obey these
rules; that is why a classifier's output probabilities are non-negative and
sum to 1. The union bound is used to bound failure rates of systems with many
parts.

**Practice**

1. Prove the complement rule and the addition rule from the axioms only.
2. A stick is broken at two uniform random points. What is the probability
   the three pieces form a triangle? (Answer: 1/4.) Verify by simulation.
3. Estimate π by throwing random points into a square.

---

## Module 04: Conditional Probability, Independence and Bayes

```text
+-----------------------------------------------------------------+
|  MODULE 04  ::  CONDITIONAL PROB. AND BAYES      [*****]  2 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** The single most important module. Conditional
probability is how you update what you believe when you learn something new.

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
     100 sick    -->  99 test positive
   9,900 healthy --> 495 test positive
   Positive tests = 594, of which only 99 are sick.
```

**Where it's used:** Medical diagnosis, spam filters (Naive Bayes), court
evidence, search and rescue, language models (the chain rule writes a
sentence's probability as a product of next-word probabilities), and every
time you change your mind because of new evidence.

**Practice**

1. Solve Monty Hall with Bayes' theorem, then simulate 100,000 games.
2. Rework the medical example with prevalence 0.1. What changes, and why?
3. Find three events that are pairwise independent but not mutually independent.
4. Gambler's ruin: start with k taka, bet 1 taka on each fair coin flip, and stop
   at 0 or N taka. Show P(reach N) = k/N.

---

# Level 2: Random Variables

## Module 05: Discrete Random Variables

```text
+-----------------------------------------------------------------+
|  MODULE 05  ::  DISCRETE RANDOM VARIABLES        [*****]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** A random variable turns outcomes into numbers so we can
do math with them.

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

**Where it's used:** Number of defective items in a batch, number of
customers in a shop, the class a classifier picks, the score of a dice game.

**Practice**

1. Write the PMF and draw the CDF for the sum of two dice.
2. Show that the CDF of a discrete variable is a step function.
3. Simulate the sum of two dice 100,000 times and compare with the PMF.

---

## Module 06: Expectation, Variance and Moments

```text
+-----------------------------------------------------------------+
|  MODULE 06  ::  EXPECTATION, VARIANCE, MOMENTS   [*****]  1.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** Expectation is the long-run average and the center of a
distribution. Variance measures spread, which is risk.

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
- [ ] Expectation as the best guess under squared error

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
  Best guess      argmin_c E[(X - c)²] = E[X]
                  argmin_c E[|X - c|]  = median(X)
```

**Where it's used:** Fair prices of bets and insurance, average running time
of algorithms, expected profit in business, and the loss functions that
machine learning models minimize (they are expectations).

**Practice**

1. Use indicators to find the expected number of fixed points in a random
   permutation of n items. (Answer: 1, for every n.)
2. Prove E[X²] ≥ (E[X])².
3. Prove that E[X] minimizes E[(X - c)²] over c.
4. A game costs 5 taka. You roll a die and win (2 x roll) taka. Should you play?

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

**Where it's used:** Quality control (binomial), calls arriving at a call
center and website hits (Poisson), card games and lotteries
(hypergeometric), surveys and elections (binomial/multinomial), and every
classifier's output (categorical).

**Practice**

1. Derive the mean and variance of the binomial using indicators.
2. Show Binomial(n, λ/n) -> Poisson(λ) as n -> ∞.
3. Prove the geometric distribution is memoryless.
4. Plot every PMF above for a few parameter values.

---

## Module 08: Continuous Random Variables

```text
+-----------------------------------------------------------------+
|  MODULE 08  ::  CONTINUOUS RANDOM VARIABLES      [*****]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Time, height, temperature and prices are continuous.
Probability becomes area under a curve.

**Topics**

- [ ] Probability density function (PDF)
- [ ] Why P(X = x) = 0 for a continuous variable
- [ ] A density can be greater than 1 (it is not a probability)
- [ ] CDF and its relationship with the PDF
- [ ] Expectation and variance using integrals
- [ ] LOTUS for continuous variables
- [ ] Quantile function (inverse CDF), median, percentiles
- [ ] Change of variables for one variable (monotonic g)
- [ ] Mixed discrete-continuous distributions

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

**Where it's used:** Measurement errors in science, waiting times, lifetimes
of machines, percentiles in exam scores and medicine (growth charts).

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

**Why it matters:** The normal distribution is the most important
distribution in all of science. The others model waiting times,
proportions, lifetimes and extremes.

**Topics**

- [ ] Uniform
- [ ] Normal (Gaussian): standardization, z-scores, 68-95-99.7 rule
- [ ] Exponential: waiting times, memoryless
- [ ] Gamma: sum of exponentials; the Gamma function
- [ ] Beta: a distribution over probabilities
- [ ] Chi-square, Student's t and F
- [ ] Laplace (double exponential)
- [ ] Log-normal
- [ ] Cauchy (a distribution with no mean)
- [ ] Logistic and Gumbel
- [ ] Weibull (lifetimes and failure)
- [ ] Dirichlet: a distribution over probability vectors
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

**Where it's used:** Heights, test scores and measurement noise (normal);
time until the next earthquake or server failure (exponential, Weibull);
stock prices and incomes (log-normal); click-through rates (beta); largest
flood in 100 years (Gumbel); and weight initialization and noise in deep
learning (normal, uniform).

**Practice**

1. Show that the exponential distribution is memoryless.
2. Prove that the sum of n independent Exponential(λ) is Gamma(n, λ).
3. Show that Beta(1, 1) is Uniform(0, 1).
4. Simulate the Cauchy distribution and watch the running mean never settle.

---

# Level 3: Many Random Variables

## Module 10: Joint Distributions

```text
+-----------------------------------------------------------------+
|  MODULE 10  ::  JOINT DISTRIBUTIONS              [*****]  1.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** Real situations involve several uncertain quantities at
once, and how they relate is often what matters most.

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

**Where it's used:** Height and weight together, rainfall and crop yield,
symptoms and diseases, features and labels in a dataset.

**Practice**

1. For the table above, are X and Y independent? Show why.
2. If (X, Y) is uniform on the unit disk, find the marginal of X.
3. Write the joint, marginal and conditional for a 3x3 table of your choice.

---

## Module 11: Covariance and Correlation

```text
+-----------------------------------------------------------------+
|  MODULE 11  ::  COVARIANCE AND CORRELATION       [*****]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Covariance measures how two variables move together.
The covariance matrix describes a whole random vector's spread.

**Topics**

- [ ] Covariance and its properties
- [ ] Correlation coefficient and why it is between -1 and 1
- [ ] Variance of a sum
- [ ] Uncorrelated does NOT imply independent
- [ ] Random vectors, mean vector, covariance matrix
- [ ] The covariance matrix is symmetric and positive semi-definite
- [ ] Linear transformations of random vectors

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
  Var of aᵀX       Var(aᵀX) = aᵀ Σ a ≥ 0      (so Σ is positive semi-definite)
```

**Where it's used:** Portfolio risk in finance (diversification works
because of the covariance term), PCA in data science, and sensor fusion.

**Practice**

1. Let X ~ Uniform(-1, 1) and Y = X². Show Cov(X, Y) = 0 but they are dependent.
2. Prove Var(aᵀX) = aᵀ Σ a.
3. Two stocks each have variance 1 and correlation ρ. Find the variance of
   a 50/50 portfolio. When is diversification most useful?

---

## Module 12: The Multivariate Gaussian

```text
+-----------------------------------------------------------------+
|  MODULE 12  ::  THE MULTIVARIATE GAUSSIAN        [**** ]  1.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** The most important multi-dimensional distribution. It
stays Gaussian under linear maps, marginalizing and conditioning, so many
problems have exact answers.

**Topics**

- [ ] PDF of the multivariate normal
- [ ] Geometry: contours are ellipses set by the eigenvectors of Σ
- [ ] Mahalanobis distance
- [ ] Standard normal vectors and the Cholesky trick
- [ ] Affine transformations stay Gaussian
- [ ] Marginals are Gaussian
- [ ] Conditionals are Gaussian (formula below)
- [ ] For jointly Gaussian variables, uncorrelated <=> independent
- [ ] Sums of independent Gaussians
- [ ] The bivariate normal in detail

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
  Bivariate     E[Y | X = x] = μ_Y + ρ (σ_Y / σ_X)(x - μ_X)
```

**Where it's used:** GPS and robot tracking (Kalman filters), weather
models, Gaussian processes, generative AI models (VAEs, diffusion), and
finance risk models.

**Practice**

1. Derive the 1-D normal PDF as a special case of the multivariate one.
2. Sample from a 2-D Gaussian with a given Σ using Cholesky. Plot the cloud
   and its contour ellipses.
3. Derive the conditional mean formula for the bivariate case.
4. Show by simulation that the squared Mahalanobis distance of x ~ N(μ, Σ) in
   d dimensions follows a chi-square(d) distribution.

---

## Module 13: Functions of Random Variables

```text
+-----------------------------------------------------------------+
|  MODULE 13  ::  FUNCTIONS OF RANDOM VARIABLES    [***  ]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** If you know the distribution of X, what is the
distribution of X², X + Y, or max(X, Y)? This module answers that.

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
  Convolution      f_{X+Y}(z) = ∫ f_X(x) f_Y(z - x) dx
  Poisson sum      Pois(λ₁) + Pois(λ₂) = Pois(λ₁ + λ₂)        (independent)
  Max of n iid     F_max(x) = F(x)^n
  Min of n iid     F_min(x) = 1 - (1 - F(x))^n
  Order stat.      k-th smallest of n iid U(0,1) ~ Beta(k, n - k + 1)
  Box-Muller       U₁, U₂ ~ U(0,1):  Z = √(-2 ln U₁) cos(2π U₂) ~ N(0, 1)
```

**Where it's used:** System reliability (a chain fails at its weakest link:
the minimum), auctions (the highest bid: the maximum), flood levels, total
waiting times, and generating random numbers.

**Practice**

1. If X, Y ~ Uniform(0,1) independent, find the PDF of X + Y (a triangle).
2. Find the distribution of the minimum of n independent Exponential(λ).
3. Implement Box-Muller and check the result with a histogram.

---

## Module 14: Conditional Expectation

```text
+-----------------------------------------------------------------+
|  MODULE 14  ::  CONDITIONAL EXPECTATION          [**** ]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** E[Y | X] is the best possible prediction of Y once you
know X. It also breaks hard problems into easy steps.

**Topics**

- [ ] Conditional expectation E[Y | X = x] as a number
- [ ] E[Y | X] as a random variable
- [ ] Law of total expectation (tower property)
- [ ] Law of total variance (Eve's law)
- [ ] E[Y | X] is the best predictor under squared error
- [ ] Taking out what is known: E[g(X) Y | X] = g(X) E[Y | X]
- [ ] Random sums (sum of a random number of variables)

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

**Where it's used:** Insurance (total claims = random number of random
amounts), prediction and regression, expected time to finish a game, and
value functions in reinforcement learning.

**Practice**

1. Prove the tower property for discrete variables.
2. Prove that E[Y | X] minimizes mean squared error.
3. A store has N ~ Poisson(λ) customers a day, each spending X with mean μ.
   Find the expected total revenue.
4. How many coin flips on average until you see HH? Until HT? (6 and 4.)

---

# Level 4: The Big Theorems

## Module 15: Generating Functions

```text
+-----------------------------------------------------------------+
|  MODULE 15  ::  GENERATING FUNCTIONS             [***  ]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Generating functions turn hard problems (sums of
variables, moments) into easy algebra. They are the tool used to prove the
Central Limit Theorem.

**Topics**

- [ ] Moment generating function (MGF)
- [ ] Getting moments by differentiating the MGF
- [ ] MGF of a sum of independent variables = product of MGFs
- [ ] Uniqueness: same MGF => same distribution
- [ ] Probability generating function (PGF)
- [ ] Characteristic function (always exists)
- [ ] Cumulants

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

**Where it's used:** Proving limit theorems, branching processes
(population growth and extinction), and Chernoff bounds.

**Practice**

1. Use MGFs to prove that the sum of independent Poissons is Poisson.
2. Find the mean and variance of Exponential(λ) from its MGF.
3. Use the PGF to find the distribution of the sum of two dice.

---

## Module 16: Inequalities and Concentration

```text
+-----------------------------------------------------------------+
|  MODULE 16  ::  INEQUALITIES AND CONCENTRATION   [**** ]  1 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** Often you cannot compute a probability exactly, but you
can bound it. Concentration explains why averages of many random things
are so predictable.

**Topics**

- [ ] Markov's inequality
- [ ] Chebyshev's inequality
- [ ] Jensen's inequality (convex functions)
- [ ] Cauchy-Schwarz inequality
- [ ] Union bound (revisited)
- [ ] Chernoff bounds
- [ ] Hoeffding's inequality
- [ ] Concentration of measure (intuition)

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

**Where it's used:** How many people to poll before an election, how many
test cases to trust a system, guarantees for randomized algorithms, and
why machine learning models generalize from finite data.

**Practice**

1. Prove Markov's inequality, then derive Chebyshev from it.
2. Use Jensen to show E[log X] ≤ log E[X].
3. Using Hoeffding, how many coin flips do you need to estimate P(heads)
   within ±0.02 with 95% confidence?

---

## Module 17: Limit Theorems (LLN and CLT)

```text
+-----------------------------------------------------------------+
|  MODULE 17  ::  LIMIT THEOREMS                   [*****]  1.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** The Law of Large Numbers says averages settle down to the
true mean. The Central Limit Theorem says they look normal on the way. This
is why the normal distribution is everywhere.

**Topics**

- [ ] Modes of convergence: in probability, almost surely, in distribution,
      in mean square
- [ ] How the modes relate to each other
- [ ] Weak Law of Large Numbers (WLLN)
- [ ] Strong Law of Large Numbers (SLLN)
- [ ] Central Limit Theorem (CLT)
- [ ] Normal approximation to the binomial; continuity correction
- [ ] Delta method
- [ ] Slutsky's theorem
- [ ] When the CLT fails (infinite variance, e.g. Cauchy)
- [ ] Poisson limit theorem (law of rare events)

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
  Spread of average   SD(X̄ₙ) = σ / √n       (100x more data = 10x more precise)
  Delta method        √n (g(X̄ₙ) - g(μ))  ->  N(0, g'(μ)² σ²)
  Poisson limit       Binomial(n, λ/n) -> Poisson(λ)
```

**Where it's used:** Casinos and insurance companies (they rely on the LLN
to make steady profits), opinion polls, quality control, Monte Carlo
simulation, and averaging in machine learning.

**Practice**

1. Prove the WLLN using Chebyshev's inequality.
2. Simulate the CLT: averages of n draws from Exponential(1) for
   n = 1, 2, 5, 30, 100. Plot histograms.
3. Use the normal approximation to find P(more than 60 heads in 100 flips).
4. Show by simulation that the running average of Cauchy samples does not
   converge.

---

# Level 5: Hero

## Module 18: Stochastic Processes

```text
+-----------------------------------------------------------------+
|  MODULE 18  ::  STOCHASTIC PROCESSES             [**** ]  2.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** Many things change randomly over time: prices, queues,
populations, text. A stochastic process is a random variable that evolves.

**Topics**

- [ ] What a stochastic process is
- [ ] Random walks: simple random walk, gambler's ruin, reflection
      principle, recurrence and transience
- [ ] Markov chains: Markov property, transition matrix, n-step
      transitions, classification of states, irreducible and aperiodic
      chains, stationary distribution, detailed balance, absorbing chains,
      convergence to equilibrium
- [ ] Continuous-time Markov chains
- [ ] Poisson process: arrivals, exponential inter-arrival times, splitting
      and merging
- [ ] Branching processes: extinction probability
- [ ] Queues (intuition): arrivals, service, waiting times
- [ ] Brownian motion

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
  Gambler's ruin    fair game, start k, stop at 0 or N:  P(reach N) = k / N
  Poisson process   N(t) ~ Poisson(λt),   inter-arrival times ~ Exponential(λ)
  Branching         extinction prob. q = smallest root of q = G(q)   (G = PGF)
  Brownian motion   B(t) - B(s) ~ N(0, t - s),  independent increments
```

**Where it's used:** Google PageRank (stationary distribution of a random
web surfer), queues at banks and servers, stock price models (Brownian
motion), genetics and population models, board games like Snakes and
Ladders (absorbing chains), reinforcement learning, and text generators.

**Practice**

1. Find the stationary distribution of the weather chain by hand and by
   computing Pⁿ for large n.
2. Simulate gambler's ruin and check P(reach N) = k/N.
3. Expected number of moves to finish Snakes and Ladders (absorbing chain).
4. Implement PageRank on a 5-page toy web.
5. Simulate a Poisson process and check the inter-arrival times are exponential.

---

## Module 19: Simulation and Monte Carlo

```text
+-----------------------------------------------------------------+
|  MODULE 19  ::  SIMULATION AND MONTE CARLO       [**** ]  1.5wk |
+-----------------------------------------------------------------+
```

**Why it matters:** When the math gets too hard, simulate. Simulation also
lets you check every result in this syllabus with a few lines of code.

**Topics**

- [ ] Why simulate
- [ ] Pseudo-random numbers and seeds
- [ ] Monte Carlo estimation and its error
- [ ] Inverse transform sampling
- [ ] Rejection sampling
- [ ] Importance sampling
- [ ] Markov Chain Monte Carlo (MCMC): Metropolis-Hastings, Gibbs sampling,
      burn-in, mixing and diagnostics
- [ ] Verifying theory by simulation

**Key formulas**

```text
  Monte Carlo       E[f(X)] ≈ (1/n) Σᵢ f(xᵢ),   xᵢ ~ p,   error ≈ σ_f / √n
  Inverse transform U ~ Uniform(0,1)  =>  X = F⁻¹(U) has CDF F
  Rejection         sample x ~ q, accept with prob. p(x) / (M q(x)),  p ≤ Mq
  Importance        E_p[f(X)] = E_q[ f(X) p(X) / q(X) ]
  Metropolis-H.     accept x' with prob. min(1, p(x') q(x | x') / (p(x) q(x' | x)))
```

**Where it's used:** Risk analysis in finance, physics simulations, weather
forecasting, computer graphics (ray tracing), game AI, Bayesian statistics,
and testing your own probability answers.

**Practice**

1. Sample from Exponential(λ) using inverse transform. Check the histogram.
2. Estimate ∫₀¹ e^(-x²) dx with Monte Carlo and compare with the exact value.
3. Implement Metropolis-Hastings to sample from a 2-peaked 1-D distribution.
4. Pick three earlier practice problems and verify your answers by simulation.

---

## Module 20: Advanced Probability (Measure Theory)

```text
+-----------------------------------------------------------------+
|  MODULE 20  ::  ADVANCED PROBABILITY             [***  ]  3 wk  |
+-----------------------------------------------------------------+
```

**Why it matters:** This is the rigorous foundation that professional
probabilists use. It answers questions like "which events can have a
probability?" and makes the limit theorems fully precise. Optional, but it
is what turns you from user into hero.

**Topics**

- [ ] Why measure theory (paradoxes the naive approach cannot handle)
- [ ] σ-algebras and measurable spaces
- [ ] Probability measures and probability spaces (Ω, F, P)
- [ ] Random variables as measurable functions
- [ ] Lebesgue integral and expectation
- [ ] Borel-Cantelli lemmas
- [ ] Kolmogorov's zero-one law
- [ ] Martingales
- [ ] Stopping times and the optional stopping theorem
- [ ] Radon-Nikodym theorem and where densities come from

**Key formulas**

```text
  σ-algebra F       Ω ∈ F;  A ∈ F => Aᶜ ∈ F;  A₁, A₂, ... ∈ F => ∪ Aᵢ ∈ F
  Probability space (Ω, F, P)
  Borel-Cantelli 1  Σ P(Aₙ) < ∞  =>  P(Aₙ happens infinitely often) = 0
  Borel-Cantelli 2  Aₙ independent, Σ P(Aₙ) = ∞  =>  P(Aₙ i.o.) = 1
  Zero-one law      a tail event has probability 0 or 1
  Martingale        E[M_{n+1} | M_0, ..., M_n] = M_n
  Optional stopping E[M_T] = E[M_0]          (under suitable conditions)
  Density           f = dP / dλ               (Radon-Nikodym derivative)
```

**Where it's used:** Research in probability and statistics, mathematical
finance (fair prices are martingales), rigorous proofs in machine learning
theory, and proving "you cannot beat a fair game" with any betting system.

**Practice**

1. Show that the set of all subsets of a finite Ω is a σ-algebra.
2. Use Borel-Cantelli to show that a fair coin shows heads infinitely
   often with probability 1.
3. Show that your fortune in a fair betting game is a martingale.
4. Use optional stopping to re-derive the gambler's ruin probability k/N.

---

# Uses of Probability

## Module 21: Applications of Probability

```text
+-----------------------------------------------------------------+
|  MODULE 21  ::  APPLICATIONS OF PROBABILITY      [*****]  always|
+-----------------------------------------------------------------+
```

**Why it matters:** Probability is the language of uncertainty in almost
every field. Each file in this module collects how one field uses it.

**The map**

```text
+-----------------------------+----------------------------------------+---------+
| Field / use                 | Probability behind it                  | Modules |
+-----------------------------+----------------------------------------+---------+
| AI: classifiers, Naive Bayes| Bayes, conditional independence        | 04 10   |
| AI: loss functions          | Expectation, likelihood of data        | 06 07   |
| AI: language models         | Chain rule, categorical distribution   | 04 07   |
| AI: generative models       | Multivariate Gaussian, sampling        | 12 19   |
| AI: reinforcement learning  | Markov chains, conditional expectation | 14 18   |
| AI: uncertainty/calibration | Probabilities that match frequencies   | 03 17   |
| Statistics and data science | Distributions, LLN, CLT                | 07-09 17|
| Randomized algorithms       | Expectation, concentration             | 06 16   |
| Hashing, Bloom filters      | Counting, birthday problem             | 02 03   |
| Networks and queues         | Poisson process, Markov chains         | 18      |
| Cryptography and security   | Uniform randomness, counting           | 02 07   |
| Finance and insurance       | Expectation, covariance, Brownian mot. | 06 11 18|
| Medicine and testing        | Bayes, base rates                      | 04      |
| Engineering reliability     | Exponential, Weibull, min/max          | 09 13   |
| Physics                     | Distributions, random walks, MC        | 09 18 19|
| Biology and genetics        | Binomial, branching processes          | 07 18   |
| Games, gambling and sports  | Counting, expectation, LLN             | 02 06 17|
| Weather and forecasting     | Conditional probability, simulation    | 04 19   |
+-----------------------------+----------------------------------------+---------+
```

**Topics** (one file or subfolder each)

- [ ] AI and machine learning (subfolder): probabilistic classifiers and Naive
      Bayes, loss functions as probability, language models, generative
      models, reinforcement learning, uncertainty and calibration
- [ ] Statistics and data science
- [ ] Computer science (subfolder): randomized algorithms, hashing and Bloom
      filters, average-case analysis, networks and queues
- [ ] Cryptography and security
- [ ] Finance and insurance
- [ ] Medicine and diagnostic testing
- [ ] Engineering and reliability
- [ ] Physics
- [ ] Biology and genetics
- [ ] Games, gambling and sports
- [ ] Weather and forecasting

**Mini projects**

```text
  [ ] P1  Monte Carlo playground: π, birthday problem, Monty Hall
  [ ] P2  CLT visualizer for any distribution
  [ ] P3  Naive Bayes spam filter from scratch
  [ ] P4  Bayesian coin: watch beliefs update flip by flip
  [ ] P5  Markov chain text generator
  [ ] P6  Snakes and Ladders: expected game length via Markov chains
  [ ] P7  Casino simulator: why the house always wins (LLN)
  [ ] P8  Random walk and stock price simulator
```

---

## Module 22: Probability for Life

```text
+-----------------------------------------------------------------+
|  MODULE 22  ::  PROBABILITY FOR LIFE             [*****]  always|
+-----------------------------------------------------------------+
```

**Why it matters:** Every important decision (health, money, career,
relationships) is made under uncertainty. Probability is the logic of
uncertainty.

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

## Study Plan

About 8 to 10 hours a week. Each `##` is one week, about 28 weeks in total.
Modules 21 and 22 run alongside everything else.

```text
 WEEK                    1   3   5   7   9   11  13  15  17  19  21  23  25  27  29
                         |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
 01  Sets and events     ##
 02  Counting              ##
 03  Axioms                  ##
 04  Conditional + Bayes       ####
 05  Discrete RVs                  ##
 06  E[X], Var                       ###
 07  Discrete dists                     ###
 08  Continuous RVs                        ##
 09  Continuous dists                        ####
 10  Joint dists                                 ###
 11  Covariance                                     ##
 12  Multivar. Gaussian                               ###
 13  Functions of RVs                                    ##
 14  Cond. expectation                                     ##
 15  Generating fns                                          ##
 16  Inequalities                                              ##
 17  LLN and CLT                                                 ###
 18  Stochastic proc.                                               #####
 19  Simulation                                                          ###
 20  Advanced (measure)                                                     ######
 21  Applications         ===== read alongside every module =====
 22  Probability for life ===== practice it every day, starting now =====
```

**Weekly rhythm**

```text
  +-----------+-----------------------------------------------+
  | Mon-Tue   | Lectures / reading, take notes                |
  | Wed       | Derive key results by hand                    |
  | Thu-Fri   | Problem sets (10 to 15 problems)              |
  | Sat       | Simulate the week's ideas in Python           |
  | Sun       | Review, write your notes in this repo, rest   |
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
  X̄                 average of X₁, ..., Xₙ
  M_X(t)            moment generating function
  N(μ, σ²)          normal distribution
  ∝                 "proportional to"
  ->d, ->p, ->a.s.  convergence in distribution / probability / almost surely
  (Ω, F, P)         probability space (Module 20)
```

---

## Appendix B: Distribution Cheat Sheet

| Distribution | Type | Support | Parameters | Mean | Variance | Story / used for |
|---|---|---|---|---|---|---|
| Bernoulli | Discrete | {0, 1} | p | p | p(1-p) | One yes/no trial |
| Binomial | Discrete | {0..n} | n, p | np | np(1-p) | Successes in n trials; quality control, polls |
| Geometric | Discrete | {1, 2, ...} | p | 1/p | (1-p)/p² | Trials until first success |
| Negative Binomial | Discrete | {0, 1, ...} | r, p | r(1-p)/p | r(1-p)/p² | Failures before r-th success |
| Poisson | Discrete | {0, 1, ...} | λ | λ | λ | Rare event counts; calls, arrivals, typos |
| Hypergeometric | Discrete | {0..n} | N, K, n | nK/N | n(K/N)(1-K/N)(N-n)/(N-1) | Draws without replacement; cards |
| Categorical | Discrete | {1..k} | p₁..pₖ | - | - | One k-way choice; a die, a classifier |
| Multinomial | Discrete | counts | n, p₁..pₖ | npᵢ | npᵢ(1-pᵢ) | Counts of k outcomes; election votes |
| Uniform | Continuous | [a, b] | a, b | (a+b)/2 | (b-a)²/12 | Total ignorance; random numbers |
| Normal | Continuous | ℝ | μ, σ² | μ | σ² | Sums of many small effects; heights, errors |
| Exponential | Continuous | [0, ∞) | λ | 1/λ | 1/λ² | Waiting time; memoryless |
| Gamma | Continuous | (0, ∞) | α, β | α/β | α/β² | Sum of exponential waiting times |
| Beta | Continuous | (0, 1) | α, β | α/(α+β) | αβ/((α+β)²(α+β+1)) | Uncertainty about a probability |
| Dirichlet | Continuous | simplex | α₁..αₖ | αᵢ/Σα | - | Uncertainty about probability vectors |
| Laplace | Continuous | ℝ | μ, b | μ | 2b² | Sharp peak, heavier tails than normal |
| Student-t | Continuous | ℝ | ν | 0 | ν/(ν-2) | Heavy tails; small-sample averages |
| Chi-square | Continuous | (0, ∞) | k | k | 2k | Sum of k squared standard normals |
| Log-normal | Continuous | (0, ∞) | μ, σ² | e^(μ+σ²/2) | (e^σ²-1)e^(2μ+σ²) | Products of effects; incomes, prices |
| Weibull | Continuous | [0, ∞) | k, λ | λΓ(1+1/k) | λ²[Γ(1+2/k) - Γ(1+1/k)²] | Lifetimes and failure times |
| Cauchy | Continuous | ℝ | x₀, γ | undefined | undefined | Counterexample: LLN and CLT fail |
| Gumbel | Continuous | ℝ | μ, β | μ + βγ | π²β²/6 | Maximum of many samples; floods |

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
|  GENERATING FUNCTIONS                                                        |
|   M_X(t) = E[e^(tX)]     E[X^n] = M^(n)(0)     M_{X+Y} = M_X M_Y (indep.)    |
+------------------------------------------------------------------------------+
|  LIMITS AND BOUNDS                                                           |
|   LLN: X̄ -> μ          CLT: X̄ ≈ N(μ, σ²/n)          SD(X̄) = σ / √n           |
|   Markov: P(X ≥ a) ≤ E[X]/a       Chebyshev: P(|X - μ| ≥ kσ) ≤ 1/k²          |
|   Jensen (convex f): f(E[X]) ≤ E[f(X)]                                       |
+------------------------------------------------------------------------------+
|  PROCESSES                                                                   |
|   Markov chain: π = πP      Poisson process: N(t) ~ Poisson(λt)              |
|   Martingale: E[M_{n+1} | past] = M_n                                        |
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

**Going further (Level 5)**

| Book | Covers |
|---|---|
| Jim Pitman, *Probability* | Beautiful problems and intuition |
| Grimmett and Stirzaker, *Probability and Random Processes* | Rigorous, covers stochastic processes |
| Sheldon Ross, *Introduction to Probability Models* | Markov chains, Poisson processes, queues |
| William Feller, *An Introduction to Probability Theory and Its Applications, Vol. 1* | The classic |
| David Williams, *Probability with Martingales* | Measure theory and martingales, short and friendly |
| Rick Durrett, *Probability: Theory and Examples* | Graduate-level measure-theoretic probability. Free online. |

**Problem books**

| Book | Why |
|---|---|
| Frederick Mosteller, *Fifty Challenging Problems in Probability* | Short, famous puzzles with solutions |
| Grimmett and Stirzaker, *One Thousand Exercises in Probability* | Huge set of solved exercises |

**Courses and videos**

- Harvard **Stat 110** (Joe Blitzstein): full lectures on YouTube, problem sets online.
- MIT **6.041 / RES.6-012** Probabilistic Systems Analysis (John Tsitsiklis): MIT OpenCourseWare.
- Stanford **CS109** Probability for Computer Scientists.
- **3Blue1Brown**: Bayes' theorem and the Central Limit Theorem.
- **Seeing Theory** (Brown University): interactive visual probability.

**Python for simulation**

```text
  numpy           random sampling
  scipy.stats     every distribution: pdf, cdf, ppf, rvs
  matplotlib      histograms and density plots
```

---

## Appendix E: Progress Tracker

```text
  MODULE                                   READ  DERIVE  SIM.  EXPLAIN  DONE
  ---------------------------------------  ----  ------  ----  -------  ----
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
  18  Stochastic processes                 [ ]   [ ]     [ ]   [ ]      [ ]
  19  Simulation and Monte Carlo           [ ]   [ ]     [ ]   [ ]      [ ]
  20  Advanced probability                 [ ]   [ ]     [ ]   [ ]      [ ]
  21  Applications of probability          [ ]   [ ]     [ ]   [ ]      [ ]
  22  Probability for life                 [ ]   [ ]     [ ]   [ ]      [ ]
```

```text
   "Probability theory is nothing but common sense reduced to calculation."
                                                   -- Pierre-Simon Laplace
```
