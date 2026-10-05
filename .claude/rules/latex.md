---
paths:
  - "**/*.md"
---

# Math and LaTeX Rules

Every formula in this repo must render correctly in **two** places:

| Where | Engine | What it supports |
|---|---|---|
| GitHub (web) | MathJax, but only **after** GitHub's Markdown parser has edited the text | `$...$`, `$$...$$`, ```` ```math ````, `` $`...`$ `` |
| VS Code preview | KaTeX | `$...$`, `$$...$$` only |

The rules below are not guesses. Every rule was tested on 2026-10-05 by rendering
real files through GitHub's renderer, VS Code's markdown-it + KaTeX pipeline, and
MathJax. `tools/check_math.py` enforces all of them. **Run it after every edit:**

```bash
python3 tools/check_math.py path/to/file.md
```

Zero errors is required. A warning means "this command was not tested yet".

---

## 1. Delimiters

| Use | Write | Never write |
|---|---|---|
| Math inside a sentence | `$x^2$` | `\( x^2 \)`, `` $`x^2`$ `` |
| Math on its own line | `$$` on its own line, formula, `$$` on its own line | `\[ ... \]`, ```` ```math ````, `$$` in the middle of a sentence |

**Inline math**

- No space just inside the dollars: `$x$`, not `$ x $`.
- **Before** the opening `$`, only: a space, the start of the line, `(`, or `**`
  (bold). These do **not** render: `variance$\sigma^2$`, `{$x$}`, `[$x$]`, `"$x$"`,
  `_$x$_`, `x/$y$`.
- **After** the closing `$`, only: a space, the end of the line, or one of
  `. , ; : ? ! ) - **`. **Never a letter or a digit:** `the $n$th term` and
  `$x$2` do not render. Write `the $n$-th term`.
- **No `\begin{...}` in inline math** (no matrices or `cases` in a sentence).
  Use a display block.

**Display math (top level)**

```markdown
The expected value is:

$$
E[X] = \sum_{x} x \thinspace p(x)
$$

Here $p(x)$ is the PMF.
```

- A blank line before the opening `$$` and after the closing `$$`. Without it,
  GitHub shows the raw dollars.
- No blank lines inside the block.
- No `$` inside the block.

**Display math inside a list item or `<details>`: ONE line, no environments.**
GitHub does not render a multi-line `$$` block there, and it does not render a
one-line `$$` that contains `\begin{...}` (`aligned`, `cases`, matrices) there
either. So, inside lists and `<details>`:

- write each formula on **one line**, with a blank line before and after it;
- write a derivation as **one chain** (`a = b = c`) or as **several one-line formulas**;
- keep `aligned`, `cases` and matrices for top-level `$$` blocks only.

```markdown
<details>
<summary>Answer</summary>

$$E[X] = 0 \cdot \tfrac{1}{2} + 1 \cdot \tfrac{1}{2} = \tfrac{1}{2}$$

$$\operatorname{Var}(X) = E[X^2] - (E[X])^2 = \tfrac{1}{2} - \tfrac{1}{4} = \tfrac{1}{4}$$

</details>
```

At the top level (not in a list or `<details>`), a one-line `$$` with
`\begin{aligned} ... \cr ... \end{aligned}` is fine.

Blockquotes and alerts (`> [!NOTE]`) are fine with multi-line `$$` blocks
when every line starts with `>`.

## 2. The big one: never put a backslash before punctuation

GitHub's Markdown parser runs **before** MathJax. It treats `\` + punctuation as an
escape and deletes the backslash. So `\{` reaches MathJax as `{` and the braces
vanish. This was confirmed for every command in this table.

| Breaks on GitHub | Write instead | Why |
|---|---|---|
| `\{ \}` | `\lbrace \rbrace` | sets: `$A = \lbrace 1, 2, 3 \rbrace$` |
| `\left\{` | `\left\lbrace` | big braces |
| `\,` | `\thinspace` | small space, e.g. before `dx` |
| `\;` `\:` | `\ ` (backslash space) or `\quad` | medium space |
| `\!` | delete it | negative space is never needed |
| `\\|` | `\Vert` | norm |
| `\%` `\#` `\&` `\$` `\_` | put the symbol outside the math, or use words | `$0.25$ (25%)` |
| `\\` in the middle of a line | end the line right after `\\`, or use `\cr` | line breaks in `aligned`, `cases`, matrices |

`\\` is safe **only** as the last thing on a line inside a top-level `$$` block:

```markdown
$$
f(x) =
\begin{cases}
\lambda e^{-\lambda x} & \text{if } x \ge 0 \\
0 & \text{if } x \lt 0
\end{cases}
$$
```

## 3. Characters that Markdown also understands

| Character | Problem | Rule |
|---|---|---|
| `*` | `$f^*$ ... $g^*$` turns into italics | always `\ast`: `$f^{\ast}$` |
| `\|` | splits table cells; inconsistent elsewhere | conditioning and sets: `\mid`. Absolute value: `\lvert x \rvert`. Never a bare `\|` |
| `<` | `$x<y>z$` loses `<y>` (read as an HTML tag) | use `\lt` / `\gt`, or spaces: `$a < b$`. Prefer `\le` `\ge` for ≤ ≥ |
| `_` | safe inside `$...$` | but never `_` inside `\text{}` |
| `$` for money | starts math by accident | write money in words: "5 dollars", "Tk 500", "USD 20" |

## 4. Where math is not allowed

- **Headings.** `### The $\chi^2$ distribution` breaks the link anchor. Write
  `### The Chi-Square Distribution`, then use math in the text below.
- **Link text and image alt text.**
- **Code blocks.** Inside ```` ```text ```` and ```` ```python ```` blocks nothing
  renders, which is correct for diagrams and code.

## 5. Tested commands (whitelist)

All of these compile in KaTeX and in MathJax and survive GitHub's parser.

| Kind | Commands |
|---|---|
| Greek | `\alpha \beta \gamma \delta \epsilon \varepsilon \lambda \mu \sigma \rho \theta \phi \varphi \chi \omega \Omega \Gamma \Sigma \Phi` and the rest of the alphabet |
| Probability | `P(A)`, `P(A \mid B)`, `E[X]`, `\operatorname{Var}(X)`, `\operatorname{Cov}(X, Y)`, `\Pr` |
| Sets | `\Omega \omega \in \notin \subset \subseteq \cup \cap \setminus \varnothing \emptyset \lbrace \rbrace \mid A^c` |
| Big operators | `\sum \prod \int \lim \bigcup \bigcap \max \min \sup \inf \log \ln \exp` |
| Relations | `= \ne \lt \gt \le \ge \approx \sim \propto \equiv \to \implies \iff \perp` |
| Arithmetic | `\pm \times \cdot \div \ast \frac \dfrac \tfrac \binom \sqrt` |
| Dots | `\dots \ldots \cdots \vdots \ddots` |
| Fonts | `\mathbb{R} \mathbf{x} \mathcal{F} \mathrm{d} \boldsymbol{\mu} \text{...} \operatorname{...}` |
| Accents | `\bar{X} \overline{X} \hat{\theta} \tilde{X} \vec{v} \underbrace{...}_{...} \overbrace{...}^{...}` |
| Arrows | `\to \rightarrow \Rightarrow \mapsto \xrightarrow{d} \overset{\text{iid}}{\sim} \stackrel{p}{\to}` |
| Delimiters | `\left( \right) \big( \big) \Big[ \Big] \lvert \rvert \lVert \rVert \langle \rangle \lfloor \rfloor \lceil \rceil` |
| Spacing | `\thinspace \quad \qquad \enspace` and `\ ` (backslash space) |
| Layout | `\begin{aligned} \begin{cases} \begin{array} \begin{pmatrix} \begin{bmatrix} \cr \hline \boxed \displaystyle` |

**Banned** (break in at least one renderer): `\color \textcolor \cancel \medspace
\thickspace \mspace \tag \label \ref \eqref \newcommand \def \bm \over \choose`,
and the environments `align equation gather multline eqnarray`. Use
`\begin{aligned}` inside `$$` instead. Need an equation number? Write
`\qquad \text{(1)}` at the end of the line.

To use a new command, test it on GitHub and in VS Code, then add it to `ALLOWED`
in `tools/check_math.py` and to this table.

## 6. Notation used in this repo

Use exactly this notation in every file so the whole repo reads as one book.
It matches Appendix A of `SYLLABUS.md`.

| Idea | Write | Note |
|---|---|---|
| Sample space, outcome | `\Omega`, `\omega` | |
| Events | `A, B, C` | capital letters |
| Complement | `A^c` | not `\bar{A}` or `A'` |
| Probability | `P(A)` | not `\Pr(A)` or `\mathbb{P}(A)` |
| Conditional | `P(A \mid B)` | never `P(A \| B)` |
| Random variables | `X, Y, Z` | values are lowercase: `x, y, z` |
| PMF / PDF / CDF | `p_X(x)`, `f_X(x)`, `F_X(x)` | drop the subscript when it is clear |
| Expectation | `E[X]`, `E[X \mid Y]` | not `\mathbb{E}` |
| Variance, SD | `\operatorname{Var}(X)`, `\sigma^2`, `\sigma` | |
| Covariance, correlation | `\operatorname{Cov}(X, Y)`, `\rho` | |
| Has distribution | `X \sim \text{Bin}(n, p)` | |
| i.i.d. | `X_1, \dots, X_n \overset{\text{iid}}{\sim} F` | |
| Sample mean | `\bar{X}_n` | |
| Indicator | `I_A` | |
| Sets | `\lbrace 1, 2, 3 \rbrace`, `\lbrace x : x \gt 0 \rbrace` | never `\{ \}` |
| Choose | `\binom{n}{k}` | |
| Convergence | `\xrightarrow{p}`, `\xrightarrow{d}`, `\xrightarrow{\text{a.s.}}` | |
| Independence | `X \perp Y` | |

**Distribution names**, always upright with `\text{}`:

| Distribution | Write | Parameter meaning |
|---|---|---|
| Bernoulli | `\text{Bern}(p)` | p = success probability |
| Binomial | `\text{Bin}(n, p)` | |
| Geometric | `\text{Geom}(p)` | number of **trials** until the first success, support 1, 2, 3, ... |
| Negative binomial | `\text{NegBin}(r, p)` | number of **failures** before the r-th success |
| Poisson | `\text{Pois}(\lambda)` | λ = rate (mean) |
| Hypergeometric | `\text{HGeom}(N, K, n)` | |
| Discrete uniform | `\text{Unif}\lbrace a, \dots, b \rbrace` | whole numbers a to b, each equally likely |
| Categorical | `\text{Cat}(p_1, \dots, p_k)` | one draw from k categories |
| Multinomial | `\text{Mult}(n, p_1, \dots, p_k)` | counts from n draws |
| Uniform | `\text{Unif}(a, b)` | continuous, on the interval from a to b |
| Normal | `\mathcal{N}(\mu, \sigma^2)` | second parameter is the **variance** |
| Exponential | `\text{Exp}(\lambda)` | λ = **rate**, mean 1/λ |
| Gamma | `\text{Gamma}(\alpha, \beta)` | shape α, **rate** β |
| Beta | `\text{Beta}(\alpha, \beta)` | |

Always say the parameterization in words the first time a distribution
appears in a file (for example "here λ is the rate, so the mean is 1/λ").

## 7. Style of formulas

- Put every formula worth remembering in display math, not inline.
- Inline math only for short symbols and expressions, roughly under 40 characters.
- One idea per display block. For a derivation, use `aligned` with `&=` and put
  the reason on the right: `&= E[X^2] - \mu^2 && \text{(linearity)}`.
- After a formula, explain every symbol in words: "where $n$ is the number of trials
  and $p$ is the probability of success".
- Write multiplication as juxtaposition (`np`) or `\cdot`. Use `\times` only for numbers: `0.99 \times 0.01`.
- Write numbers in math: `$0.0594$`, `$\frac{1}{6}$`. Round to 3 or 4 significant
  digits and say "about" or use `\approx`.
- Use `\left( \right)` only around tall content such as fractions. Use plain `( )` otherwise.
