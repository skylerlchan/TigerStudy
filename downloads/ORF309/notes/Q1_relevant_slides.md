# ORF309 — Slides Relevant to HW3 Q1

**Source:** Slides 05 (pp. 6–10) and Slides 06 (pp. 3–8)

**Q1 goal:** Prove that for a non-negative integer-valued RV $X$:
$$E(X) = \sum_{k=1}^{\infty} P(X \geq k)$$

---

## Slides 05 — Discrete Random Variables I: Expectations & Distributions

### Definition of Expectation

**Definition:** If $X: \Omega \to S$ is a discrete random variable (DRV) and $g: S \to \mathbb{R}$ is a value function, then the expectation of $g(X)$ is:
$$E[g(X)] = \sum_{x \in S} g(x) \cdot P(X = x)$$

**Special case:** Choosing $g(x) = x$:
$$E[X] = \sum_{x \in S} x \cdot P(X = x)$$

> **Note:** This definition only makes sense for DRVs. For continuous RVs, $P(X = x) = 0$ for all $x \in S$.

---

### Example 1 — Card Suit

- DRV: $X$ = suit of a card. Each suit equally likely, so $P(X = \text{any suit}) = 1/4$.
- Value function $g: S \to \{1, 2, 3, 4\}$ (value in dollars per suit).

$$E[g(X)] = \frac{1}{4}(1) + \frac{1}{4}(2) + \frac{1}{4}(3) + \frac{1}{4}(4) = \frac{10}{4} = \frac{5}{2}$$

---

### Indicator Function — **VERY IMPORTANT**

**Definition:** For an event $A$, define the indicator RV:
$$\mathbf{1}_A(\omega) = \begin{cases} 1 & \text{if } \omega \in A \\ 0 & \text{if } \omega \notin A \end{cases}$$

**Key result:**
$$E[\mathbf{1}_A] = 1 \cdot P(\mathbf{1}_A = 1) + 0 \cdot P(\mathbf{1}_A = 0) = P(A)$$

> **The expectation of an indicator equals the probability of the event.**

---

### Indicator Function — Usefulness

The indicator function lets you express a count as a sum of simple 0/1 variables.

**Example:** Let $X$ = number of heads in $n$ coin flips.

- Define events $A_i$ = "the $i$-th flip is heads", for $i = 1, 2, \ldots, n$.
- Define indicator $\mathbf{1}_{A_i}$ for each flip.
- Then:

$$X = \mathbf{1}_{A_1} + \mathbf{1}_{A_2} + \cdots + \mathbf{1}_{A_n}$$

---

## Slides 06 — Expectations, Linearity, and Indicator Functions

### Recap of Key Definitions

| Concept | Definition |
|---|---|
| Expectation | $E[g(X)] = \sum_{x \in S} g(x) \cdot P(X = x)$ |
| Distribution of $X$ | The set of probabilities $P(X = x)$ for all $x \in S$ |
| Joint distribution of $X, Y$ | All probabilities $P(X = x, Y = y)$ |
| Marginal distribution | $P(X = x) = \sum_{y \in S_Y} P(X = x, Y = y)$ |

---

### Linearity of Expectation

**Result:** $E[X + Y] = E[X] + E[Y]$

**Proof sketch:**
$$E[X + Y] = \sum_{x, y} (x + y) \cdot P(X = x, Y = y)$$
$$= \sum_{x,y} x \cdot P(X=x, Y=y) + \sum_{x,y} y \cdot P(X=x, Y=y)$$
$$= \sum_x x \cdot P(X = x) + \sum_y y \cdot P(Y = y) = E[X] + E[Y]$$

> (The last step uses marginal distributions to collapse the double sums.)

---

### Indicator Function + Linearity — Coin Flip Example

**Setup:** Flip $n$ coins with $P(\text{heads}) = p$. Let $X$ = total number of heads.

**Step 1:** Write $X$ as a sum of indicators:
$$X = \mathbf{1}_{A_1} + \mathbf{1}_{A_2} + \cdots + \mathbf{1}_{A_n}$$

**Step 2:** Apply linearity of expectation:
$$E[X] = E[\mathbf{1}_{A_1}] + E[\mathbf{1}_{A_2}] + \cdots + E[\mathbf{1}_{A_n}]$$

**Step 3:** Each indicator has $E[\mathbf{1}_{A_i}] = P(A_i) = p$:
$$E[X] = p + p + \cdots + p = np$$

> **Key remark:** Independence was never assumed. Even if the coins were colluded, linearity of expectation still holds. $E[X] = np$ regardless.

---

## How These Apply to Q1

To prove $E(X) = \sum_{k=1}^{\infty} P(X \geq k)$:

1. **Write** $X$ as a sum of indicators: $X = \sum_{k=1}^{\infty} \mathbf{1}_{X \geq k}$
   - This works because for a non-negative integer $X = n$, exactly $n$ of the events $\{X \geq 1\}, \{X \geq 2\}, \ldots$ are true.

2. **Take expectation** and apply linearity:
$$E[X] = E\left[\sum_{k=1}^{\infty} \mathbf{1}_{X \geq k}\right] = \sum_{k=1}^{\infty} E[\mathbf{1}_{X \geq k}]$$

3. **Use** $E[\mathbf{1}_A] = P(A)$:
$$= \sum_{k=1}^{\infty} P(X \geq k) \quad \blacksquare$$
