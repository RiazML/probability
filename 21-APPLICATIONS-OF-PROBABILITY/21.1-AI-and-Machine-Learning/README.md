# 21.1 AI and Machine Learning

[Probability](../../README.md) / [Module 21: Applications of Probability](../README.md) / 21.1 AI and Machine Learning

> **Big idea:** Almost every part of modern AI is a probability model with a name: a classifier outputs a categorical distribution, a loss function is a negative log-likelihood, a language model is the chain rule, a generative model is a sampler, and a learning agent is a Markov chain that collects rewards.

Machine learning looks like a pile of tricks, but under the tricks the same few ideas repeat. A model states a probability. The data are scored by how probable the model says they are. The model is changed to make them more probable. This section shows that pattern six times, with small examples that you can run in a few lines of numpy. It is not a machine learning course: there is no training of neural networks here. The focus is the **probability** behind each method, and each file links back to the module where that idea is taught.

Read the files in order. 21.1.1 and 21.1.2 are the base: Bayes' theorem for classifiers, and the likelihood behind every loss. 21.1.3 and 21.1.4 build on them (sequences, and sampling new data). 21.1.5 adds rewards and Markov chains. 21.1.6 asks the last question: when a model says "80%", is it right 80% of the time?

## Topics

| # | Topic | What it is about |
|---|---|---|
| 21.1.1 | [Probabilistic Classifiers and Naive Bayes](21.1.1-Probabilistic-Classifiers-and-Naive-Bayes.md) | Bayes' theorem plus conditional independence: a tiny spam filter from counts |
| 21.1.2 | [Loss Functions as Probability](21.1.2-Loss-Functions-as-Probability.md) | Cross-entropy is the negative log-likelihood of a categorical; squared error is a Gaussian one |
| 21.1.3 | [Language Models](21.1.3-Language-Models.md) | The chain rule, next-token sampling, temperature, and a bigram Markov chain |
| 21.1.4 | [Generative Models](21.1.4-Generative-Models.md) | Latent variables, Gaussian mixtures, and how to sample and invert a simple model |
| 21.1.5 | [Reinforcement Learning](21.1.5-Reinforcement-Learning.md) | Returns, value functions as conditional expectations, and Thompson sampling |
| 21.1.6 | [Uncertainty and Calibration](21.1.6-Uncertainty-and-Calibration.md) | Do predicted probabilities match frequencies? Reliability, Brier score, and Eve's law for ensembles |

---

[↑ Module 21: Applications of Probability](../README.md)
