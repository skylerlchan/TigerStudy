# ECO 310 Lecture 10b: Markets -- Comprehensive Summary

---

## 1. Exchange Economy (Edgeworth Box)

### Setup

- **Two consumers** (1 and 2), **two goods** (x and y).
- Each consumer has an **endowment**: consumer 1 has `(e_1^x, e_1^y)`, consumer 2 has `(e_2^x, e_2^y)`.
- **Total endowment** in the economy:
  - `E^x = e_1^x + e_2^x`
  - `E^y = e_1^y + e_2^y`
- The **Edgeworth box** has dimensions `E^x` (width) by `E^y` (height).
- Consumer 1's origin is at the **bottom-left**; consumer 2's origin is at the **top-right**.

### Definition: Feasible Allocation

An allocation `((x_1, y_1), (x_2, y_2))` is **feasible** if:

```
x_1 + x_2 = E^x
y_1 + y_2 = E^y
```

Every point inside the Edgeworth box represents a feasible allocation.

### Definition: Pareto Improvement

An allocation `((x_1', y_1'), (x_2', y_2'))` is a **Pareto improvement** over `((x_1, y_1), (x_2, y_2))` if:

- `u_1(x_1', y_1') >= u_1(x_1, y_1)` and `u_2(x_2', y_2') >= u_2(x_2, y_2)`
- with **at least one strict inequality**.

### Definition: Pareto Efficient (Pareto Optimal)

A feasible allocation is **Pareto efficient** if there is **no feasible Pareto improvement** over it. Equivalently, it is impossible to make one person better off without making the other worse off.

### Key Result: Characterizing Pareto Efficiency (Interior Allocations)

At an interior Pareto efficient allocation (with smooth, strictly convex preferences):

```
MRS_1(x_1, y_1) = MRS_2(x_2, y_2)
```

The **marginal rates of substitution** of both consumers must be **equal**.

**Intuition:** If MRS_1 != MRS_2, there exist mutually beneficial trades. E.g., if consumer 1 values x more (in terms of y) than consumer 2, they can trade and both be better off.

### Definition: Contract Curve

The **contract curve** is the set of all Pareto efficient allocations in the Edgeworth box. It is the locus of tangency points between the two consumers' indifference curves.

---

## 2. Competitive (Walrasian) Equilibrium

### Setup

- A **price vector** `(p_x, p_y)` is announced (or equivalently, a relative price `p = p_x / p_y`).
- Each consumer **maximizes utility** subject to their **budget constraint**.

### Definition: Budget Constraint

Consumer `i`'s budget constraint:

```
p_x * x_i + p_y * y_i = p_x * e_i^x + p_y * e_i^y
```

The right-hand side is the **value of consumer i's endowment** (their "income").

The budget line passes through the endowment point `(e_i^x, e_i^y)` for each consumer.

### Definition: Competitive (Walrasian) Equilibrium

A competitive equilibrium consists of a price vector `(p_x*, p_y*)` and an allocation `((x_1*, y_1*), (x_2*, y_2*))` such that:

1. Each consumer **maximizes utility** given prices:
   - `(x_i*, y_i*)` solves `max u_i(x_i, y_i)` subject to `p_x* x_i + p_y* y_i = p_x* e_i^x + p_y* e_i^y` for `i = 1, 2`.

2. **Markets clear** (supply = demand):
   - `x_1* + x_2* = E^x`
   - `y_1* + y_2* = E^y`

### Key Property: Only Relative Prices Matter

If `(p_x*, p_y*)` is an equilibrium price vector, then so is `(t * p_x*, t * p_y*)` for any `t > 0`. We can **normalize** by setting `p_y = 1` (making y the numeraire) and solving for `p_x / p_y`.

### Walras' Law

**If each consumer satisfies their budget constraint with equality**, then if one market clears, the other market clears automatically.

Formally: Summing the budget constraints:

```
p_x(x_1 + x_2) + p_y(y_1 + y_2) = p_x(e_1^x + e_2^x) + p_y(e_1^y + e_2^y)
```

This implies:

```
p_x(x_1 + x_2 - E^x) + p_y(y_1 + y_2 - E^y) = 0
```

So if excess demand in one market is zero, excess demand in the other must also be zero (as long as prices are positive).

**Implication:** With `n` goods, you only need to clear `n - 1` markets.

---

## 3. Solving for Competitive Equilibrium (Method)

### Step-by-Step Procedure

1. **Normalize prices**: Set `p_y = 1`, let `p = p_x`.
2. **Solve each consumer's optimization problem**: Given price `p`, find demand functions `x_i(p)` and `y_i(p)` using the tangency condition `MRS_i = p_x / p_y = p` and the budget constraint.
3. **Impose market clearing** in one market (by Walras' Law, the other clears automatically):
   - `x_1(p) + x_2(p) = E^x`  (or equivalently for good y)
4. **Solve for equilibrium price** `p*`.
5. **Plug `p*` back** into demand functions to get equilibrium allocation.

---

## 4. Worked Example: Cobb-Douglas Preferences

### Setup

- Consumer 1: `u_1(x_1, y_1) = x_1^a * y_1^(1-a)`, endowment `(e_1^x, e_1^y) = (1, 0)`
- Consumer 2: `u_2(x_2, y_2) = x_2^b * y_2^(1-b)`, endowment `(e_2^x, e_2^y) = (0, 1)`
- Normalize: `p_y = 1`, price of x is `p`.

### Cobb-Douglas Demand (Standard Result)

For Cobb-Douglas utility `u = x^a * y^(1-a)` with income `m`:

```
x = a * m / p_x
y = (1 - a) * m / p_y
```

The consumer spends **fraction `a`** of income on good x and **fraction `(1-a)`** on good y.

### Consumer 1's Demands

Income: `m_1 = p * 1 + 1 * 0 = p`

```
x_1(p) = a * p / p = a
y_1(p) = (1 - a) * p / 1 = (1 - a) * p
```

### Consumer 2's Demands

Income: `m_2 = p * 0 + 1 * 1 = 1`

```
x_2(p) = b * 1 / p = b / p
y_2(p) = (1 - b) * 1 / 1 = 1 - b
```

### Market Clearing (Good x)

```
x_1(p) + x_2(p) = E^x = 1
a + b / p = 1
b / p = 1 - a
p* = b / (1 - a)
```

### Equilibrium Allocation

```
x_1* = a,    y_1* = (1 - a) * b / (1 - a) = b
x_2* = 1 - a,    y_2* = 1 - b
```

### Verification: Market for y clears

```
y_1* + y_2* = b + (1 - b) = 1 = E^y  (check)
```

---

## 5. The First Welfare Theorem

### Theorem Statement

If preferences are **locally non-satiated** (more is weakly preferred), then every competitive (Walrasian) equilibrium allocation is **Pareto efficient**.

### Proof Sketch

Suppose the equilibrium allocation `(x_1*, x_2*)` is **not** Pareto efficient. Then there exists a feasible allocation `(x_1', x_2')` such that both are weakly better off and at least one is strictly better off.

- If consumer `i` **strictly prefers** `x_i'`, then `x_i'` must be **outside** their budget set (otherwise they would have chosen it): `p * x_i' > p * e_i`.
- If consumer `i` is **indifferent**, then by local non-satiation, there is a nearby bundle that is strictly preferred and also outside the budget set, implying `p * x_i' >= p * e_i`.
- With at least one strict inequality, summing: `p * (x_1' + x_2') > p * (e_1 + e_2)`.
- But feasibility requires `x_1' + x_2' = e_1 + e_2`, a **contradiction**.

### Interpretation

- Competitive markets achieve efficiency "automatically" through the price mechanism.
- **No central planner is needed** to coordinate an efficient outcome.
- This is the formal version of Adam Smith's "invisible hand."

### Limitations / What the First Welfare Theorem Does NOT Say

- It says nothing about **fairness or equity** -- an allocation where one person has everything is Pareto efficient.
- Requires **no externalities**, **no market power** (price-taking), and **complete markets**.
- Efficiency does not imply desirability from a social welfare perspective.

---

## 6. The Second Welfare Theorem

### Theorem Statement

If preferences are **convex**, **continuous**, and **locally non-satiated**, then for **any** Pareto efficient allocation, there exists a set of prices and a redistribution of endowments such that that allocation is a competitive equilibrium.

### Interpretation

- Any Pareto efficient outcome can be achieved through markets, provided we redistribute endowments appropriately first (e.g., via lump-sum transfers).
- **Separation of efficiency and equity**: Use lump-sum transfers to address equity concerns, then let markets achieve efficiency.
- The government's role is limited to redistribution; the market handles allocation.

### Key Caveat

- Requires **lump-sum transfers**, which are difficult to implement in practice (they require information about preferences/endowments that governments typically lack).

---

## 7. Production Economy

### Setup

- Extends the exchange economy by adding **firms** that transform inputs into outputs.
- A firm has a **production function** `y = f(x)` (or a production set `Y`).

### Definition: Production Set

The **production set** `Y` is the set of all technologically feasible production plans. A production plan specifies net outputs of each good (negative entries = inputs, positive entries = outputs).

### Definition: Profit Maximization

Given prices `(p_x, p_y)`, a firm chooses production plan `y in Y` to maximize profit:

```
pi = p * y = p_y * output - p_x * input
```

### Competitive Equilibrium with Production

A competitive equilibrium in a production economy consists of prices `p*`, consumption allocations `(x_i*)`, and production plans `(y_j*)` such that:

1. Each **consumer maximizes utility** subject to budget constraint (income now includes profit shares).
2. Each **firm maximizes profit** given prices.
3. **Markets clear**: total demand = total endowment + total net production for each good.

Consumer i's budget constraint now includes **profit income**:

```
p * x_i <= p * e_i + sum_j (theta_ij * pi_j)
```

where `theta_ij` is consumer i's ownership share of firm j, and `pi_j` is firm j's profit.

### Market Clearing with Production

```
sum_i x_i^k = sum_i e_i^k + sum_j y_j^k    for each good k
```

Total consumption = total endowment + total net output.

---

## 8. First and Second Welfare Theorems (with Production)

Both welfare theorems extend to production economies:

- **First Welfare Theorem**: Every competitive equilibrium (with production) is Pareto efficient.
- **Second Welfare Theorem**: Every Pareto efficient allocation can be decentralized as a competitive equilibrium with appropriate transfers (requires convex production sets in addition to convex preferences).

---

## 9. Robinson Crusoe Economy (One Consumer, One Firm)

### Setup

- One consumer (Robinson) with utility `u(x, y)`, endowment of labor `L_bar` (total hours).
- One firm with production function `y = f(L)` where `L` is labor input.
- Two "goods": leisure (`x = L_bar - L`) and output y (coconuts).
- Robinson owns the firm (gets all profits).

### Firm's Problem

```
max_L  p_y * f(L) - w * L
```

FOC: `p_y * f'(L) = w`, i.e., **value of marginal product = wage**.

Equivalently: `f'(L*) = w / p_y` (marginal product of labor = real wage).

### Consumer's Problem

Income = wage income + profit:

```
m = w * L_bar + pi
```

where `pi = p_y * f(L*) - w * L*`.

```
max u(x, y)  subject to  w * x + p_y * y = w * L_bar + pi
```

where `x` is leisure (so `w * x` is the opportunity cost of leisure).

### Equilibrium Condition

The equilibrium production point is where the **production possibilities frontier** (PPF) is tangent to the **highest achievable indifference curve**, which is also tangent to the budget line.

```
MRS(x, y) = w / p_y = f'(L)  (= MPL)
```

The marginal rate of substitution between leisure and output equals the marginal product of labor.

---

## 10. Key Definitions Summary

| Term | Definition |
|------|-----------|
| **Feasible allocation** | Total consumption = total endowment for each good |
| **Pareto improvement** | Makes at least one person strictly better off, no one worse off |
| **Pareto efficient** | No feasible Pareto improvement exists |
| **Contract curve** | Set of all Pareto efficient allocations in the Edgeworth box |
| **Competitive equilibrium** | Prices + allocation where all optimize and markets clear |
| **Walras' Law** | If n-1 markets clear, the n-th clears automatically |
| **First Welfare Theorem** | Competitive equilibrium => Pareto efficient |
| **Second Welfare Theorem** | Any Pareto efficient allocation can be supported as a competitive equilibrium with transfers |
| **Production set** | Set of technologically feasible production plans |
| **Profit maximization** | Firm chooses plan to maximize p * y over production set |

---

## 11. Key Formulas Reference

| Formula | Context |
|---------|---------|
| `MRS_1 = MRS_2` | Condition for Pareto efficiency (interior, 2 consumers) |
| `MRS_i = p_x / p_y` for all i | Condition at competitive equilibrium (interior) |
| `x = a * m / p_x` | Cobb-Douglas demand (exponent a on good x) |
| `p_x(ED_x) + p_y(ED_y) = 0` | Walras' Law (ED = excess demand) |
| `p_y * f'(L) = w` | Firm's optimality: value of MPL = wage |
| `MRS = w/p_y = MPL` | Robinson Crusoe equilibrium condition |
| `p * x_i <= p * e_i + sum_j theta_ij * pi_j` | Budget constraint with firm ownership |
