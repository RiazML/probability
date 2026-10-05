# LaTeX render test, round 3

D1

<details>
<summary>Solution (single-line $$)</summary>

$$x = \frac{1}{2}$$

</details>

D2

<details>
<summary>Solution (blank line after summary, $$ block, blank lines)</summary>

Some text first.

$$
x = \frac{1}{2}
$$

More text.

</details>

D3

<details>
<summary>Solution (math fence)</summary>

```math
x = \frac{1}{2}
```

</details>

D4

<details>
<summary><b>Solution</b></summary>
<br>

$$
x = \frac{1}{2}
$$

</details>

L1

1. Step one:

   $$E[X] = \mu$$

2. Step two.

L2

- Bullet with block:

  $$
  E[X] = \mu
  $$

L3 After list, top-level block works:

$$
E[X] = \mu
$$

Q1

> [!TIP]
> Block inside an alert:
>
> $$
> E[X] = \mu
> $$
