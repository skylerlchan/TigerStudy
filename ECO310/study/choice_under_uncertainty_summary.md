# ECO 310 -- Choice Under Uncertainty: Comprehensive Summary

*Source: Lectures 7 & 8 (intermediate_lec7 and 8 math26.pdf)*

---

## 1. Lotteries and Probability

### Definition: Simple Lottery
A **simple lottery** is defined as:

$$L = (p_1, p_2, \ldots, p_N)$$

where outcome $n$ occurs with probability $p_n$, with:
- $p_n \geq 0$ for all $n$
- $\sum_{n=1}^{N} p_n = 1$

The set of all simple lotteries over $N$ outcomes is:

$$\mathscr{L} = \left\{ (p_1, \ldots, p_N) \in \mathbb{R}^N_+ : \sum_{n=1}^N p_n = 1 \right\}$$

This is the **(N-1)-dimensional simplex**.

### Definition: Compound Lottery
A **compound lottery** is a lottery over lotteries. Given $K$ simple lotteries $L_1, \ldots, L_K$ and probabilities $\alpha_1, \ldots, \alpha_K \geq 0$ with $\sum_k \alpha_k = 1$, the compound lottery is:

$$(L_1, \ldots, L_K; \alpha_1, \ldots, \alpha_K)$$

### Reduced Lottery
The **reduced lottery** is the simple lottery that yields the same ultimate distribution over outcomes as a compound lottery:

$$L = \alpha_1 L_1 + \alpha_2 L_2 + \cdots + \alpha_K L_K$$

Explicitly, the probability of outcome $n$ in the reduced lottery is:

$$p_n = \alpha_1 p_n^1 + \alpha_2 p_n^2 + \cdots + \alpha_K p_n^K$$

### Consequentialist Premise
The decision-maker only cares about the **reduced (simple) lottery** over final outcomes, not about the structure of the compound lottery that generates it.

---

## 2. Preferences Over Lotteries

### Continuity Axiom (L1)
$\succsim$ on $\mathscr{L}$ is **continuous** if for all $L, L', L'' \in \mathscr{L}$, the sets:

$$\{ \alpha \in [0,1] : \alpha L + (1-\alpha) L' \succsim L'' \}$$
$$\{ \alpha \in [0,1] : L'' \succsim \alpha L + (1-\alpha) L' \}$$

are both closed. Equivalently, if $L \succ L' \succ L''$, then there exist $\alpha, \beta \in (0,1)$ such that:

$$\alpha L + (1-\alpha) L'' \succ L' \succ \beta L + (1-\beta) L''$$

### Independence Axiom (L2)
For all $L, L', L'' \in \mathscr{L}$ and $\alpha \in (0,1)$:

$$L \succsim L' \iff \alpha L + (1-\alpha) L'' \succsim \alpha L' + (1-\alpha) L''$$

Mixing any lottery with a common third lottery does not change the ranking between the original two lotteries.

---

## 3. Expected Utility Theory

### Expected Utility (von Neumann-Morgenstern) Theorem
A rational preference relation $\succsim$ on $\mathscr{L}$ satisfies the **Continuity** and **Independence** axioms if and only if there exists a utility function $U: \mathscr{L} \to \mathbb{R}$ that:

1. Has the **expected utility form**:

$$U(L) = u_1 p_1 + u_2 p_2 + \cdots + u_N p_N = \sum_{n=1}^N u_n p_n$$

where $u_n$ is the utility of outcome $n$ (a Bernoulli utility value).

2. **Represents** $\succsim$: $L \succsim L'$ if and only if $U(L) \geq U(L')$.

### Definition: von Neumann-Morgenstern (vNM) Expected Utility Function
A utility function $U: \mathscr{L} \to \mathbb{R}$ has the **expected utility form** if there exist numbers $(u_1, \ldots, u_N)$ assigned to outcomes such that for every simple lottery $L = (p_1, \ldots, p_N)$:

$$U(L) = \sum_{n=1}^N u_n p_n = E[u]$$

The values $u_n$ are called **Bernoulli utilities**.

### Uniqueness (Cardinality) of vNM Utility
The vNM utility function is unique up to **positive affine transformations**. If $U(L) = \sum u_n p_n$ represents $\succsim$, then $\tilde{U}(L) = \sum \tilde{u}_n p_n$ also represents $\succsim$ if and only if:

$$\tilde{u}_n = a + b \cdot u_n \quad \text{for all } n$$

for some constants $a \in \mathbb{R}$ and $b > 0$.

This means the **ratios of utility differences** are preserved and behaviorally meaningful:

$$\frac{u_1 - u_2}{u_2 - u_3}$$

is invariant under positive affine transformations.

---

## 4. Money Lotteries and Risk Aversion

### Setup
Outcomes are amounts of money $x \in \mathbb{R}$. A lottery $F$ is a cumulative distribution function (CDF) over money outcomes. Expected utility becomes:

$$U(F) = \int u(x) \, dF(x)$$

where $u(\cdot)$ is the **Bernoulli utility function** (utility of money), assumed to be increasing and continuous.

For discrete lotteries with outcomes $x_1, \ldots, x_n$ and probabilities $p_1, \ldots, p_n$:

$$U = \sum_{i=1}^n p_i \, u(x_i)$$

### Definition: Expected Value of a Lottery
$$E[x] = \sum_{i=1}^n p_i x_i \quad \text{(discrete)}$$
$$E[x] = \int x \, dF(x) \quad \text{(continuous)}$$

### Definition: Fair Gamble / Actuarially Fair Lottery
A gamble/lottery is **fair** (actuarially fair) if its expected monetary value equals zero (or equivalently, the expected value of wealth after the gamble equals initial wealth).

---

## 5. Risk Attitudes

### Definition: Risk Averse
A decision-maker is **risk averse** if for every lottery $F$, the **degenerate lottery** that pays $E[x]$ for certain is at least as good as $F$ itself:

$$u(E[x]) \geq E[u(x)] = \int u(x) \, dF(x)$$

Equivalently: the agent always (weakly) prefers the expected value with certainty over the gamble.

**Characterization:** Risk aversion $\iff$ $u(\cdot)$ is **concave**.

### Definition: Risk Neutral
$$u(E[x]) = E[u(x)] \quad \text{for all } F$$

**Characterization:** Risk neutrality $\iff$ $u(\cdot)$ is **linear** (affine).

### Definition: Risk Loving (Risk Seeking)
$$u(E[x]) \leq E[u(x)] \quad \text{for all } F$$

**Characterization:** Risk loving $\iff$ $u(\cdot)$ is **convex**.

### Jensen's Inequality
- $u$ concave $\implies$ $u(E[x]) \geq E[u(x)]$ (risk aversion)
- $u$ convex $\implies$ $u(E[x]) \leq E[u(x)]$ (risk loving)
- $u$ linear $\implies$ $u(E[x]) = E[u(x)]$ (risk neutrality)

---

## 6. Certainty Equivalent and Risk Premium

### Definition: Certainty Equivalent (CE)
The **certainty equivalent** of a lottery $F$ is the guaranteed amount of money $c(F, u)$ such that the agent is indifferent between receiving $c$ for sure and facing the lottery:

$$u(c(F, u)) = E[u(x)] = \int u(x) \, dF(x)$$

Solving: $c(F, u) = u^{-1}\left( E[u(x)] \right)$

### Definition: Risk Premium
The **risk premium** $\rho$ is the amount of expected value the agent is willing to forgo to eliminate risk:

$$\rho(F, u) = E[x] - c(F, u)$$

**Key relationships:**
- Risk averse ($u$ concave): $c \leq E[x]$, so $\rho \geq 0$
- Risk neutral ($u$ linear): $c = E[x]$, so $\rho = 0$
- Risk loving ($u$ convex): $c \geq E[x]$, so $\rho \leq 0$

### Maximum Willingness to Pay for Insurance
For a risk-averse agent facing a potential loss, the **maximum insurance premium** they would pay equals the amount at which they are indifferent between buying insurance and not. This is directly related to the certainty equivalent.

---

## 7. Measures of Risk Aversion

### Arrow-Pratt Coefficient of Absolute Risk Aversion (ARA)
$$r_A(x) = -\frac{u''(x)}{u'(x)}$$

- Measures risk aversion at wealth level $x$
- Higher $r_A(x)$ = more risk averse
- Risk averse: $r_A(x) > 0$ (since $u'' < 0$ and $u' > 0$)
- Risk neutral: $r_A(x) = 0$
- Risk loving: $r_A(x) < 0$

### Comparing Risk Aversion Across Agents
Given two agents with Bernoulli utilities $u_1$ and $u_2$, the following are equivalent:
1. $r_A^{(2)}(x) \geq r_A^{(1)}(x)$ for all $x$ (agent 2 has higher ARA everywhere)
2. There exists an increasing, concave function $\psi$ such that $u_2(x) = \psi(u_1(x))$ for all $x$ (i.e., $u_2$ is a concave transformation of $u_1$)
3. $c_2(F, u_2) \leq c_1(F, u_1)$ for every lottery $F$ (agent 2 always has a lower certainty equivalent)
4. $\rho_2(F, u_2) \geq \rho_1(F, u_1)$ for every lottery $F$ (agent 2 always has a higher risk premium)

### Approximate Risk Premium (Arrow-Pratt Approximation)
For a "small" gamble with mean $\bar{x}$ and variance $\sigma^2$:

$$\rho \approx \frac{1}{2} r_A(\bar{x}) \cdot \sigma^2$$

The risk premium is approximately half the coefficient of absolute risk aversion times the variance of the gamble.

---

## 8. Common Bernoulli Utility Functions

### Constant Absolute Risk Aversion (CARA)
$$u(x) = -e^{-ax}, \quad a > 0$$

- $r_A(x) = a$ (constant, does not depend on wealth)
- Also called **exponential utility**

### Constant Relative Risk Aversion (CRRA)
The **coefficient of relative risk aversion** is:

$$r_R(x) = x \cdot r_A(x) = -\frac{x \, u''(x)}{u'(x)}$$

CRRA utility functions:

$$u(x) = \frac{x^{1-\rho}}{1-\rho}, \quad \rho \neq 1$$

$$u(x) = \ln(x), \quad \rho = 1$$

where $\rho$ is the constant coefficient of relative risk aversion.

---

## 9. Decreasing / Increasing / Constant Absolute Risk Aversion (DARA, IARA, CARA)

- **DARA** (Decreasing ARA): $r_A'(x) < 0$ -- as wealth increases, absolute risk aversion decreases. The agent becomes less averse to a fixed-dollar gamble as they get wealthier. Generally considered the most empirically realistic.
- **CARA**: $r_A'(x) = 0$ -- risk attitude toward a fixed-dollar gamble is independent of wealth level.
- **IARA**: $r_A'(x) > 0$ -- risk aversion increases with wealth (considered unrealistic).

---

## 10. Stochastic Dominance

### First-Order Stochastic Dominance (FOSD)
Distribution $F$ **first-order stochastically dominates** distribution $G$ (written $F \succsim_{FOSD} G$) if:

$$F(x) \leq G(x) \quad \text{for all } x$$

**Equivalently:** $\int u(x) \, dF(x) \geq \int u(x) \, dG(x)$ for every increasing function $u$.

**Interpretation:** Every expected-utility maximizer with an increasing utility function prefers $F$ to $G$. $F$ puts more probability weight on higher outcomes.

### Second-Order Stochastic Dominance (SOSD)
Distribution $F$ **second-order stochastically dominates** distribution $G$ (written $F \succsim_{SOSD} G$) if:

$$\int u(x) \, dF(x) \geq \int u(x) \, dG(x)$$

for every increasing **and concave** function $u$.

**Equivalently (integral condition):**

$$\int_{-\infty}^{t} F(x) \, dx \leq \int_{-\infty}^{t} G(x) \, dx \quad \text{for all } t$$

**Key result:** If $F$ and $G$ have the **same mean**, then $F$ SOSD $G$ if and only if $G$ is a **mean-preserving spread** of $F$ (i.e., $G$ has more risk/dispersion).

**Interpretation:** Every risk-averse expected-utility maximizer prefers $F$ to $G$.

### Mean-Preserving Spread
$G$ is a **mean-preserving spread** of $F$ if $G$ can be obtained from $F$ by adding noise (a zero-mean random variable) to each outcome. Formally, $G$ has the same mean as $F$ but more dispersion.

---

## 11. Insurance and Risk Sharing

### Insurance Model Setup
- Initial wealth: $w$
- Loss $D$ occurs with probability $\pi$
- Insurance contract: pay premium $q$ to receive payout $K$ if loss occurs
- Fair insurance: $q = \pi K$ (premium equals expected payout)

### Expected Utility with Insurance
$$EU = (1-\pi) \, u(w - q) + \pi \, u(w - q - D + K)$$

**Result (Full Insurance under Fair Pricing):** A risk-averse agent offered actuarially fair insurance will choose **full insurance** ($K = D$), equating wealth across states:

$$w - q = w - q - D + K \implies K = D$$

### Marginal Condition for Optimal Insurance
At interior optimum:

$$\frac{(1-\pi) \, u'(w - q)}{(1-\pi)} \cdot \frac{dq}{dK} = \frac{\pi \, u'(w - q - D + K)}{...}$$

More precisely, for fair insurance ($q = \pi K$):

$$u'(w - \pi K) \cdot \pi = u'(w - \pi K - D + K) \cdot (1-\pi) \cdot \frac{\pi}{1-\pi}$$

which simplifies at optimum to $u'$ equalized across states, confirming full insurance.

---

## 12. State-Dependent Utility and Contingent Commodities

### Contingent Commodity Framework
- **States of nature:** $s = 1, 2, \ldots, S$ with probabilities $\pi_1, \ldots, \pi_S$
- **Contingent consumption plan:** $(c_1, c_2, \ldots, c_S)$ where $c_s$ = consumption in state $s$
- Expected utility:

$$EU = \sum_{s=1}^S \pi_s \, u(c_s)$$

### Optimal Risk Sharing (MRS Condition)
With two states (good/bad) and expected utility, the marginal rate of substitution between state-contingent consumptions:

$$MRS_{1,2} = \frac{\pi_1 \, u'(c_1)}{\pi_2 \, u'(c_2)}$$

At an optimum with fair odds, a risk-averse agent sets $c_1 = c_2$ (full insurance / equal consumption across states).

### Budget Constraint with State Prices
If the price of a dollar in state $s$ is $q_s$:

$$\sum_s q_s \, c_s = \sum_s q_s \, \omega_s$$

where $\omega_s$ is the endowment in state $s$.

**Fair prices:** $q_s = \pi_s$ (state prices equal probabilities). Under fair prices, optimal choice for a risk-averse agent is $c_1 = c_2 = \cdots = c_S$.

---

## 13. Key Results and Theorems Summary

| Result | Statement |
|--------|-----------|
| **vNM Theorem** | Continuity + Independence $\implies$ expected utility representation |
| **Uniqueness** | vNM utility is unique up to positive affine transformations ($a + bu$) |
| **Risk aversion $\iff$ concavity** | Agent is risk averse iff Bernoulli utility $u$ is concave |
| **Jensen's Inequality** | $u$ concave $\implies$ $u(E[x]) \geq E[u(x)]$ |
| **Arrow-Pratt** | $r_A(x) = -u''(x)/u'(x)$ measures local risk aversion |
| **Risk premium approx.** | $\rho \approx \frac{1}{2} r_A(\bar{x}) \sigma^2$ |
| **FOSD** | $F(x) \leq G(x)$ for all $x$ $\iff$ all agents with $u' > 0$ prefer $F$ |
| **SOSD** | All risk-averse agents prefer $F$ $\iff$ $G$ is a mean-preserving spread of $F$ (when means are equal) |
| **Full insurance** | Under actuarially fair pricing, risk-averse agents fully insure |
