# ECO 310 - Choice Under Uncertainty (Lecture 9)

## Comprehensive Summary

---

## 1. Lotteries and Expected Value

### Definition: Lottery
A **lottery** is a list of outcomes and associated probabilities:

$$L = (p_1 \circ c_1, \; p_2 \circ c_2, \; \ldots, \; p_n \circ c_n)$$

where:
- $c_1, c_2, \ldots, c_n$ are the possible **outcomes** (consequences)
- $p_1, p_2, \ldots, p_n$ are the associated **probabilities**
- $p_i \geq 0$ for all $i$, and $\sum_{i=1}^n p_i = 1$

### Definition: Expected Value (Expected Monetary Value)
The **expected value** of a lottery is:

$$EV(L) = \sum_{i=1}^n p_i \cdot c_i = p_1 c_1 + p_2 c_2 + \cdots + p_n c_n$$

### Example from Lecture
Lottery: win \$10 with probability 1/2, win \$0 with probability 1/2.

$$EV = \frac{1}{2}(10) + \frac{1}{2}(0) = 5$$

---

## 2. Preferences Over Lotteries and Expected Utility

### Key Question
Should a rational decision-maker simply maximize expected monetary value? **No** -- people's attitudes toward risk matter.

### The St. Petersburg Paradox
A coin is flipped repeatedly. If the first head appears on flip $n$, you win $2^n$ dollars. The expected value is:

$$EV = \sum_{n=1}^{\infty} \frac{1}{2^n} \cdot 2^n = \sum_{n=1}^{\infty} 1 = \infty$$

Yet most people would only pay a small finite amount to play this game. This demonstrates that people do **not** simply maximize expected monetary value.

### Definition: Von Neumann-Morgenstern (vNM) Expected Utility
Given a utility function $u$ defined over outcomes, the **expected utility** of a lottery $L = (p_1 \circ c_1, \ldots, p_n \circ c_n)$ is:

$$EU(L) = \sum_{i=1}^n p_i \cdot u(c_i) = p_1 \, u(c_1) + p_2 \, u(c_2) + \cdots + p_n \, u(c_n)$$

A rational agent maximizes **expected utility**, not expected monetary value.

### Key Property
The vNM utility function $u$ is defined over **certain outcomes** (e.g., dollar amounts). The expected utility function $EU$ is defined over **lotteries**.

---

## 3. Axioms of Expected Utility Theory

The expected utility representation relies on the following axioms over preferences on lotteries:

### Axiom 1: Completeness
For any two lotteries $L_1$ and $L_2$, either $L_1 \succsim L_2$, or $L_2 \succsim L_1$, or both (indifference).

### Axiom 2: Transitivity
If $L_1 \succsim L_2$ and $L_2 \succsim L_3$, then $L_1 \succsim L_3$.

### Axiom 3: Continuity (Archimedean Property)
If $L_1 \succsim L_2 \succsim L_3$, then there exists some probability $\alpha \in [0,1]$ such that:

$$L_2 \sim \alpha \circ L_1 + (1-\alpha) \circ L_3$$

(Every lottery is indifferent to some compound lottery mixing the best and worst.)

### Axiom 4: Independence
If $L_1 \succsim L_2$, then for any lottery $L_3$ and any $\alpha \in (0,1]$:

$$\alpha \circ L_1 + (1-\alpha) \circ L_3 \succsim \alpha \circ L_2 + (1-\alpha) \circ L_3$$

Mixing each of two lotteries with a common third lottery does not change the preference ordering between them.

### Expected Utility Theorem
If preferences satisfy completeness, transitivity, continuity, and independence, then there exists a utility function $u$ over outcomes such that:

$$L_1 \succsim L_2 \iff EU(L_1) \geq EU(L_2)$$

---

## 4. Properties of vNM Utility Functions

### Uniqueness up to Positive Affine Transformation
If $u$ represents preferences, then $v = a \cdot u + b$ (where $a > 0$) represents the **same** preferences. That is, vNM utility is an **interval scale** (like temperature in Celsius vs. Fahrenheit).

- You **can** apply positive affine transformations: $v(x) = au(x) + b$, $a > 0$
- You **cannot** apply arbitrary monotone transformations (unlike ordinal utility in consumer theory)

### Cardinal vs. Ordinal Utility
- **Ordinal utility** (standard consumer theory): only the ranking matters; any monotone transformation preserves preferences.
- **Cardinal utility** (expected utility): the **shape** of $u$ matters (concavity, convexity); only positive affine transformations preserve expected utility rankings.

---

## 5. Risk Attitudes

### Definition: Risk Averse
An agent is **risk averse** if for every lottery $L$:

$$u(EV(L)) \geq EU(L)$$

Equivalently, the agent prefers the **sure thing** of receiving $EV(L)$ to playing the lottery $L$.

**Characterization:** $u$ is **concave** ($u'' < 0$).

### Definition: Risk Neutral
An agent is **risk neutral** if for every lottery $L$:

$$u(EV(L)) = EU(L)$$

**Characterization:** $u$ is **linear** (affine): $u(x) = ax + b$.

### Definition: Risk Loving (Risk Seeking)
An agent is **risk loving** if for every lottery $L$:

$$EU(L) \geq u(EV(L))$$

Equivalently, the agent prefers the lottery to the sure thing of receiving $EV(L)$.

**Characterization:** $u$ is **convex** ($u'' > 0$).

### Graphical Intuition (Jensen's Inequality)
For a lottery $(p \circ x_1, (1-p) \circ x_2)$:

- **Risk averse (concave $u$):** The chord connecting $(x_1, u(x_1))$ and $(x_2, u(x_2))$ lies **below** the curve. So $EU = p \, u(x_1) + (1-p) \, u(x_2) \leq u(p \, x_1 + (1-p) \, x_2) = u(EV)$.
- **Risk loving (convex $u$):** The chord lies **above** the curve. So $EU \geq u(EV)$.
- **Risk neutral (linear $u$):** The chord coincides with the curve. So $EU = u(EV)$.

---

## 6. Certainty Equivalent and Risk Premium

### Definition: Certainty Equivalent (CE)
The **certainty equivalent** of a lottery $L$ is the sure amount of money $CE$ such that the agent is indifferent between receiving $CE$ for certain and playing the lottery:

$$u(CE) = EU(L)$$

$$CE = u^{-1}(EU(L))$$

### Definition: Risk Premium (RP)
The **risk premium** is the amount a risk-averse agent would be willing to give up (relative to the expected value) to eliminate risk:

$$RP = EV(L) - CE$$

### Risk Attitude Summary via CE and RP

| Risk Attitude | CE vs. EV | RP | $u$ shape |
|---|---|---|---|
| Risk Averse | $CE < EV$ | $RP > 0$ | Concave |
| Risk Neutral | $CE = EV$ | $RP = 0$ | Linear |
| Risk Loving | $CE > EV$ | $RP < 0$ | Convex |

---

## 7. Measures of Risk Aversion

### Arrow-Pratt Coefficient of Absolute Risk Aversion (ARA)

$$r_A(x) = -\frac{u''(x)}{u'(x)}$$

- Measures the degree of risk aversion at wealth level $x$.
- Higher $r_A$ means more risk averse.
- Useful for comparing risk attitudes across agents or across wealth levels.

### Decreasing / Constant / Increasing Absolute Risk Aversion (DARA / CARA / IARA)
- **DARA:** $r_A'(x) < 0$ -- as wealth increases, absolute risk aversion decreases (wealthier people take on more absolute risk). This is the empirically most common case.
- **CARA:** $r_A'(x) = 0$ -- absolute risk aversion is constant across wealth levels.
- **IARA:** $r_A'(x) > 0$ -- absolute risk aversion increases with wealth.

### Arrow-Pratt Coefficient of Relative Risk Aversion (RRA)

$$r_R(x) = -\frac{x \cdot u''(x)}{u'(x)} = x \cdot r_A(x)$$

- Measures risk aversion relative to the scale of wealth.
- Relevant when considering gambles that are proportional to wealth.

---

## 8. Common Utility Functions

### Logarithmic Utility
$$u(x) = \ln(x)$$

- $u'(x) = 1/x > 0$, $u''(x) = -1/x^2 < 0$ --> **risk averse**
- $r_A(x) = 1/x$ --> **DARA** (decreasing in $x$)
- $r_R(x) = 1$ --> **constant relative risk aversion (CRRA)**

### Exponential Utility (CARA Utility)
$$u(x) = -e^{-\alpha x}, \quad \alpha > 0$$

- $u'(x) = \alpha e^{-\alpha x} > 0$, $u''(x) = -\alpha^2 e^{-\alpha x} < 0$ --> **risk averse**
- $r_A(x) = \alpha$ --> **CARA** (constant absolute risk aversion)
- $r_R(x) = \alpha x$ --> increasing relative risk aversion

### Power Utility (CRRA Utility)
$$u(x) = \frac{x^{1-\rho}}{1-\rho}, \quad \rho > 0, \; \rho \neq 1$$

- For $\rho = 1$, this converges to $u(x) = \ln(x)$.
- $r_R(x) = \rho$ --> **constant relative risk aversion**
- $r_A(x) = \rho / x$ --> **DARA**

### Quadratic Utility
$$u(x) = x - \frac{b}{2}x^2, \quad b > 0$$

- $u'(x) = 1 - bx$ (only valid for $x < 1/b$ so that $u' > 0$)
- $u''(x) = -b < 0$ --> **risk averse** in the valid domain
- $r_A(x) = \frac{b}{1 - bx}$ --> **IARA** (increasing absolute risk aversion) -- generally considered unrealistic

---

## 9. Comparing Risk Aversion Across Agents

### Theorem: More Risk Averse Agent
Agent A is **more risk averse** than Agent B if and only if any of the following equivalent conditions hold:

1. $r_A^A(x) \geq r_A^B(x)$ for all $x$ (higher Arrow-Pratt ARA everywhere)
2. $u_A = g(u_B)$ where $g$ is a **concave** function (A's utility is a concave transformation of B's)
3. $CE_A(L) \leq CE_B(L)$ for every lottery $L$
4. $RP_A(L) \geq RP_B(L)$ for every lottery $L$

---

## 10. Insurance and Risk

### Setup
- Initial wealth: $w$
- Potential loss: $\ell$ (occurs with probability $p$)
- Insurance: pay premium $\gamma$ per dollar of coverage; buy $q$ dollars of coverage
- Premium cost: $\gamma q$

### Wealth in Each State
- **No loss:** $w - \gamma q$
- **Loss occurs:** $w - \ell - \gamma q + q = w - \ell + q(1 - \gamma)$

### Expected Utility with Insurance
$$EU = (1 - p) \cdot u(w - \gamma q) + p \cdot u(w - \ell + q(1 - \gamma))$$

### Optimal Insurance: First-Order Condition
Taking the derivative with respect to $q$ and setting it to zero:

$$-\gamma (1-p) \, u'(w - \gamma q) + p(1 - \gamma) \, u'(w - \ell + q(1 - \gamma)) = 0$$

### Actuarially Fair Insurance
Insurance is **actuarially fair** if $\gamma = p$ (the premium rate equals the probability of loss). The insurer's expected profit is zero.

**Key Result:** With actuarially fair insurance, a risk-averse agent purchases **full insurance** ($q^* = \ell$).

**Proof:** At full insurance ($q = \ell$), wealth is $w - p\ell$ in both states. The FOC becomes:
$$-p(1-p) \, u'(w - p\ell) + p(1-p) \, u'(w - p\ell) = 0$$
which is satisfied.

### Unfair Insurance ($\gamma > p$)
When the premium rate exceeds the probability of loss (insurer makes positive expected profit), a risk-averse agent purchases **partial insurance** ($q^* < \ell$).

---

## 11. Portfolio Choice / Asset Allocation

### Setup
- Initial wealth: $w$
- **Risk-free asset:** return $r_f$ per dollar
- **Risky asset:** random return $\tilde{r}$ with $E[\tilde{r}] > r_f$
- Agent invests $a$ dollars in the risky asset, $(w - a)$ in the risk-free asset

### Final Wealth
$$\tilde{W} = (w - a)(1 + r_f) + a(1 + \tilde{r}) = w(1 + r_f) + a(\tilde{r} - r_f)$$

### Optimization Problem
$$\max_{a} \; E[u(\tilde{W})] = E[u(w(1 + r_f) + a(\tilde{r} - r_f))]$$

### First-Order Condition
$$E[u'(\tilde{W}) \cdot (\tilde{r} - r_f)] = 0$$

### Key Result
If $E[\tilde{r}] > r_f$ (the risky asset has a positive risk premium), then:
- A risk-averse agent invests a **positive** amount in the risky asset ($a^* > 0$), but not all wealth.
- The **more risk-averse** the agent, the **less** they invest in the risky asset.

---

## 12. Stochastic Dominance

### First-Order Stochastic Dominance (FOSD)
**Definition:** Lottery $L_A$ **first-order stochastically dominates** $L_B$ if for every outcome $x$:

$$F_A(x) \leq F_B(x)$$

where $F_A$ and $F_B$ are the cumulative distribution functions (CDFs).

**Equivalently:** $L_A$ FOSD $L_B$ if and only if every agent with an **increasing** utility function ($u' > 0$) prefers $L_A$ to $L_B$:

$$EU_A(L_A) \geq EU_A(L_B) \quad \text{for all } u \text{ with } u' > 0$$

**Intuition:** $L_A$ puts more probability weight on higher outcomes. The CDF of $L_A$ is everywhere to the right of (or equal to) the CDF of $L_B$.

### Second-Order Stochastic Dominance (SOSD)
**Definition:** Lottery $L_A$ **second-order stochastically dominates** $L_B$ if for every outcome $x$:

$$\int_{-\infty}^{x} F_A(t) \, dt \leq \int_{-\infty}^{x} F_B(t) \, dt$$

**Equivalently:** $L_A$ SOSD $L_B$ if and only if every **risk-averse** agent (with $u' > 0$ and $u'' \leq 0$) prefers $L_A$:

$$EU_A(L_A) \geq EU_A(L_B) \quad \text{for all } u \text{ with } u' > 0, \; u'' \leq 0$$

**Key Relationship:**
- If $L_A$ and $L_B$ have the **same mean** but $L_B$ has greater variance/spread, then $L_A$ SOSD $L_B$ (all risk-averse agents prefer the less risky lottery).
- FOSD implies SOSD (but not vice versa).

### Mean-Preserving Spread
$L_B$ is a **mean-preserving spread** of $L_A$ if $L_B$ has the same mean as $L_A$ but is more dispersed. Equivalently, $L_A$ SOSD $L_B$.

---

## 13. State-Dependent Utility and Contingent Consumption

### Setup
- Two states of the world: state 1 (probability $\pi_1$) and state 2 (probability $\pi_2 = 1 - \pi_1$)
- Consumer chooses contingent consumption: $c_1$ in state 1, $c_2$ in state 2
- Expected utility: $EU = \pi_1 u(c_1) + \pi_2 u(c_2)$

### Indifference Curves in State-Contingent Space
Along an indifference curve ($EU$ constant):

$$\frac{dc_2}{dc_1} = -\frac{\pi_1 u'(c_1)}{\pi_2 u'(c_2)}$$

This is the **marginal rate of substitution** between consumption in state 1 and state 2.

### The 45-Degree Line (Certainty Line)
On the 45-degree line, $c_1 = c_2 = c$, meaning consumption is the same regardless of the state (no risk). At this point:

$$MRS = -\frac{\pi_1 u'(c)}{\pi_2 u'(c)} = -\frac{\pi_1}{\pi_2}$$

**Result:** A risk-averse consumer's indifference curves are **convex** in $(c_1, c_2)$ space, and the slope on the 45-degree line equals the negative ratio of probabilities.

---

## 14. Allais Paradox

### Description
The Allais Paradox demonstrates a systematic violation of the **Independence Axiom**.

**Choice 1:**
- Option A: \$1 million for certain
- Option B: (0.89: \$1M, 0.10: \$5M, 0.01: \$0)

Most people choose A.

**Choice 2:**
- Option C: (0.11: \$1M, 0.89: \$0)
- Option D: (0.10: \$5M, 0.90: \$0)

Most people choose D.

**The paradox:** Choosing A in Choice 1 **and** D in Choice 2 violates the Independence Axiom. Under expected utility, $A \succ B$ implies $C \succ D$ (or equivalently, $B \succ A$ implies $D \succ C$).

**Implication:** Real human preferences may violate expected utility theory, motivating alternative theories like **Prospect Theory**.

---

## 15. Key Formulas Reference

| Concept | Formula |
|---|---|
| Expected Value | $EV = \sum p_i c_i$ |
| Expected Utility | $EU = \sum p_i u(c_i)$ |
| Certainty Equivalent | $u(CE) = EU(L)$ |
| Risk Premium | $RP = EV - CE$ |
| Absolute Risk Aversion | $r_A(x) = -u''(x)/u'(x)$ |
| Relative Risk Aversion | $r_R(x) = -x \cdot u''(x)/u'(x)$ |
| Insurance FOC | $-\gamma(1-p)u'(w - \gamma q) + p(1-\gamma)u'(w - \ell + q(1-\gamma)) = 0$ |
| Portfolio FOC | $E[u'(\tilde{W})(\tilde{r} - r_f)] = 0$ |
| FOSD condition | $F_A(x) \leq F_B(x)$ for all $x$ |
| SOSD condition | $\int_{-\infty}^x F_A(t)dt \leq \int_{-\infty}^x F_B(t)dt$ for all $x$ |
| MRS (contingent claims) | $-\pi_1 u'(c_1) / [\pi_2 u'(c_2)]$ |
