# ECO 310 - Lectures 5 & 6: Preferences and Choice - Comprehensive Summary

---

## 1. Preference Relations

### Definitions

**Consumption Set (X):** The set of all conceivable consumption bundles. Typically X = R+^L (the non-negative orthant of L-dimensional real space), where L is the number of commodities.

**Consumption Bundle:** A vector x = (x_1, x_2, ..., x_L) specifying quantities of each commodity.

**Preference Relation (>=, "weakly preferred to"):** A binary relation on X. We write x >= y to mean "x is at least as good as y."

**Strict Preference (>):** x > y if and only if x >= y and NOT y >= x. Meaning: "x is strictly preferred to y."

**Indifference (~):** x ~ y if and only if x >= y AND y >= x. Meaning: "x is exactly as good as y."

---

## 2. Axioms (Properties) of Rational Preferences

### Completeness
For all x, y in X: either x >= y or y >= x (or both).

Meaning: The consumer can always compare any two bundles. No "I don't know" is allowed.

### Transitivity
For all x, y, z in X: if x >= y and y >= z, then x >= z.

Meaning: Preferences are consistent -- no cycles.

### Definition of Rationality
A preference relation is **rational** if it is both **complete** and **transitive**.

---

## 3. Additional Properties of Preferences

### Monotonicity (More is Better)

**Monotonicity:** If x >= y (meaning x_i >= y_i for every component i), then x >= y (weakly preferred). If x >= y and x != y, then x > y.

**Strong Monotonicity:** If x >= y and x != y, then x > y (strictly preferred).

Implication: Indifference curves slope downward under monotonicity.

### Local Non-Satiation (LNS)
For every x in X and every epsilon > 0, there exists y in X such that ||y - x|| < epsilon and y > x.

Meaning: In any neighborhood of any bundle, there is always a strictly preferred bundle. There are no "thick" indifference curves and no bliss points.

Note: Monotonicity implies LNS, but LNS does NOT imply monotonicity.

### Convexity
For all x, y, z in X: if x >= z and y >= z, then tx + (1-t)y >= z for all t in [0, 1].

Meaning: Mixtures (averages) of equally good bundles are at least as good. Consumers prefer diversification. The upper contour set {y : y >= x} is a convex set.

### Strict Convexity
For all x, y, z in X: if x >= z and y >= z, and x != y, then tx + (1-t)y > z for all t in (0, 1).

Meaning: Mixtures of distinct but equally good bundles are strictly preferred. Guarantees unique optimal bundles.

### Continuity
For all x in X, the upper contour set {y in X : y >= x} and the lower contour set {y in X : x >= y} are both closed sets.

Equivalently: If {x_n} -> x and {y_n} -> y, and x_n >= y_n for all n, then x >= y.

Meaning: Preferences don't exhibit "jumps." Small changes in bundles lead to small changes in preference ordering.

---

## 4. Indifference Curves

### Definition
An **indifference curve** through bundle x is the set of all bundles indifferent to x:
IC(x) = {y in X : y ~ x}

### Properties (under rational, monotone preferences)
- Indifference curves are **downward sloping** (monotonicity).
- Indifference curves **cannot cross** (transitivity).
- Every bundle lies on exactly one indifference curve (completeness).
- Higher indifference curves represent higher utility/preference.

### Proof: Indifference Curves Cannot Cross
Suppose IC_1 and IC_2 cross at bundle B. Take A on IC_1 and C on IC_2. Then A ~ B (both on IC_1), B ~ C (both on IC_2). By transitivity, A ~ C. But if A is above IC_2 (or C above IC_1), monotonicity implies one is strictly preferred -- contradiction.

---

## 5. Utility Functions

### Definition
A function u: X -> R is a **utility function representing preference relation >=** if, for all x, y in X:

**x >= y if and only if u(x) >= u(y)**

### Existence Theorem
If the preference relation >= is **rational**, **continuous**, and **monotone**, then there exists a continuous utility function u: X -> R that represents >=.

### Ordinal Nature of Utility
Utility is **ordinal**, not cardinal. Only the ranking matters, not the numerical values.

**Proposition:** If u(x) represents >= and f: R -> R is any strictly increasing function, then v(x) = f(u(x)) also represents >=.

Examples of valid transformations:
- v(x) = 2u(x) + 7
- v(x) = u(x)^3
- v(x) = ln(u(x)) (if u > 0)
- v(x) = e^{u(x)}

---

## 6. Common Utility Functions and Indifference Curves

### Perfect Substitutes
**u(x_1, x_2) = ax_1 + bx_2** (where a, b > 0)

- Indifference curves: straight lines with slope = -a/b.
- MRS = a/b (constant).
- Consumer views goods as interchangeable at a fixed rate.

### Perfect Complements (Leontief)
**u(x_1, x_2) = min{ax_1, bx_2}** (where a, b > 0)

- Indifference curves: L-shaped, with kink along the line ax_1 = bx_2 (i.e., x_2/x_1 = a/b).
- Goods are consumed in fixed proportions.
- No substitution between goods.

### Cobb-Douglas
**u(x_1, x_2) = x_1^a * x_2^b** (where a, b > 0)

Equivalent representations (monotonic transformations):
- v(x_1, x_2) = a*ln(x_1) + b*ln(x_2)
- w(x_1, x_2) = x_1^{a/(a+b)} * x_2^{b/(a+b)}

- Indifference curves: smooth, convex, downward sloping.
- Well-behaved preferences (monotone, convex, continuous).

### Quasilinear Preferences
**u(x_1, x_2) = v(x_1) + x_2** (where v is concave, e.g., v(x_1) = sqrt(x_1) or ln(x_1))

- Indifference curves are **vertically parallel** (same shape, shifted up/down).
- MRS depends only on x_1, not on x_2.
- No income effect for good 1 (at interior solutions).

---

## 7. Marginal Rate of Substitution (MRS)

### Definition
The **MRS at bundle (x_1, x_2)** is the rate at which the consumer is willing to trade good 2 for good 1 while remaining indifferent:

**MRS_{12} = dx_2/dx_1 |_{along IC} = - (MU_1 / MU_2) = -(partial u / partial x_1) / (partial u / partial x_2)**

Convention: MRS is often reported as a positive number (the absolute value of the slope of the indifference curve).

### Marginal Utility
**MU_1 = partial u / partial x_1** (the partial derivative of utility with respect to good 1)

**MU_2 = partial u / partial x_2** (the partial derivative of utility with respect to good 2)

### Derivation (using total differential)
Along an indifference curve, du = 0:

du = (partial u / partial x_1)dx_1 + (partial u / partial x_2)dx_2 = 0

Solving: dx_2/dx_1 = -(partial u / partial x_1) / (partial u / partial x_2) = -MU_1/MU_2

### Key Property: MRS is Invariant to Monotonic Transformations
If v(x) = f(u(x)) where f is strictly increasing, then MRS computed from v equals MRS computed from u. This is because the f'(u) terms cancel in the ratio of partial derivatives.

### Diminishing MRS
Under **strict convexity**, the MRS is diminishing (in absolute value) as we move along an indifference curve from left to right (increasing x_1). The consumer is willing to give up less and less of good 2 for each additional unit of good 1.

---

## 8. MRS Examples

### Perfect Substitutes: u = ax_1 + bx_2
- MU_1 = a, MU_2 = b
- **MRS = a/b** (constant everywhere)

### Cobb-Douglas: u = x_1^a * x_2^b
- MU_1 = a * x_1^{a-1} * x_2^b
- MU_2 = b * x_1^a * x_2^{b-1}
- **MRS = (a * x_2) / (b * x_1)**
- MRS is diminishing (decreases as x_1 increases along an IC).

### Quasilinear: u = v(x_1) + x_2
- MU_1 = v'(x_1), MU_2 = 1
- **MRS = v'(x_1)** (depends only on x_1)

---

## 9. Choice: The Consumer's Problem (Utility Maximization)

### Setup
The consumer chooses bundle x = (x_1, x_2) to:

**Maximize u(x_1, x_2)**
**Subject to: p_1*x_1 + p_2*x_2 <= m** (budget constraint)
**and x_1 >= 0, x_2 >= 0** (non-negativity)

Where:
- p_1, p_2 = prices of goods 1 and 2
- m = income (wealth)

### Budget Set
**B = {(x_1, x_2) in R+^2 : p_1*x_1 + p_2*x_2 <= m}**

### Budget Line
**p_1*x_1 + p_2*x_2 = m**

Slope of budget line: **dx_2/dx_1 = -p_1/p_2**

Intercepts: x_1 = m/p_1 (horizontal), x_2 = m/p_2 (vertical).

---

## 10. Optimal Choice (Interior Solution)

### Tangency Condition
At an interior optimum (x_1* > 0, x_2* > 0), the indifference curve is tangent to the budget line:

**MRS = p_1/p_2**

Equivalently:

**MU_1/MU_2 = p_1/p_2**

Or rearranged:

**MU_1/p_1 = MU_2/p_2**

This says: the marginal utility per dollar spent must be equalized across goods.

### Lagrangian Method
**L = u(x_1, x_2) + lambda[m - p_1*x_1 - p_2*x_2]**

First-order conditions:
- partial L / partial x_1 = MU_1 - lambda*p_1 = 0 --> MU_1 = lambda*p_1
- partial L / partial x_2 = MU_2 - lambda*p_2 = 0 --> MU_2 = lambda*p_2
- partial L / partial lambda = m - p_1*x_1 - p_2*x_2 = 0

Dividing the first two: **MU_1/MU_2 = p_1/p_2** (tangency condition)

**lambda** = the **marginal utility of income** (shadow price of relaxing the budget constraint by one dollar).

### Sufficient Conditions
The tangency condition is sufficient for a maximum when:
- The utility function is **quasiconcave** (equivalently, preferences are convex).
- Under **strict quasiconcavity** (strict convexity of preferences), the optimum is **unique**.

---

## 11. Solving Specific Cases

### Cobb-Douglas: u = x_1^a * x_2^b

**Tangency:** (a*x_2)/(b*x_1) = p_1/p_2

**Budget:** p_1*x_1 + p_2*x_2 = m

Solving yields **Marshallian (ordinary) demand functions:**

**x_1* = (a/(a+b)) * (m/p_1)**

**x_2* = (b/(a+b)) * (m/p_2)**

Key property: The consumer spends a **fixed fraction** of income on each good:
- Fraction on good 1 = a/(a+b)
- Fraction on good 2 = b/(a+b)

### Perfect Substitutes: u = ax_1 + bx_2

No tangency -- compare MRS = a/b to price ratio p_1/p_2:

- If a/b > p_1/p_2: **x_1* = m/p_1, x_2* = 0** (all income on good 1)
- If a/b < p_1/p_2: **x_1* = 0, x_2* = m/p_2** (all income on good 2)
- If a/b = p_1/p_2: any bundle on the budget line is optimal

### Perfect Complements: u = min{ax_1, bx_2}

Optimal at the kink: **ax_1 = bx_2**

Combined with budget constraint:

**x_1* = bm/(bp_1 + ap_2)**

**x_2* = am/(bp_1 + ap_2)**

---

## 12. Corner Solutions

A **corner solution** occurs when the consumer buys zero of one (or more) goods. This happens when:

**MRS > p_1/p_2 at x_2 = 0** --> consume only good 1.

**MRS < p_1/p_2 at x_1 = 0** --> consume only good 2.

The tangency condition MRS = p_1/p_2 is replaced by an inequality at the boundary.

### Kuhn-Tucker Conditions (General)
- MU_1 - lambda*p_1 <= 0, with equality if x_1 > 0
- MU_2 - lambda*p_2 <= 0, with equality if x_2 > 0
- p_1*x_1 + p_2*x_2 = m

---

## 13. Demand Functions

### Marshallian (Ordinary) Demand
The solution to the utility maximization problem gives **Marshallian demand functions:**

**x_i* = x_i(p_1, p_2, m)** for i = 1, 2

These express optimal quantities as functions of prices and income.

### Properties
- **Homogeneous of degree zero** in (p_1, p_2, m): Scaling all prices and income by the same factor leaves demand unchanged.
  x_i(tp_1, tp_2, tm) = x_i(p_1, p_2, m) for all t > 0
- Satisfies **Walras' Law** (budget exhaustion): p_1*x_1* + p_2*x_2* = m (under LNS, the consumer spends all income).

---

## 14. Indirect Utility Function

### Definition
The **indirect utility function** gives the maximum utility achievable at given prices and income:

**v(p_1, p_2, m) = u(x_1*(p_1, p_2, m), x_2*(p_1, p_2, m))**

That is, substitute the Marshallian demands into the utility function.

### Properties
- **Decreasing** in each price p_i.
- **Increasing** in income m.
- **Homogeneous of degree zero** in (p, m).
- **Quasiconvex** in prices.

### Roy's Identity
**x_i*(p, m) = -(partial v / partial p_i) / (partial v / partial m)**

This allows recovery of Marshallian demand from the indirect utility function.

---

## 15. Expenditure Minimization Problem (EMP)

### Setup
Dual to utility maximization. The consumer chooses x to:

**Minimize p_1*x_1 + p_2*x_2**
**Subject to: u(x_1, x_2) >= u_bar** (must achieve at least utility level u_bar)

### Hicksian (Compensated) Demand
The solution gives **Hicksian demand functions:**

**h_i = h_i(p_1, p_2, u_bar)** for i = 1, 2

These express optimal quantities as functions of prices and a target utility level.

### Expenditure Function
**e(p_1, p_2, u_bar) = p_1*h_1(p_1, p_2, u_bar) + p_2*h_2(p_1, p_2, u_bar)**

The minimum expenditure needed to achieve utility u_bar at prices (p_1, p_2).

### Properties of the Expenditure Function
- **Increasing** in u_bar.
- **Increasing** in each price p_i.
- **Homogeneous of degree one** in prices.
- **Concave** in prices.

### Shephard's Lemma
**h_i(p, u_bar) = partial e(p, u_bar) / partial p_i**

The Hicksian demand for good i equals the partial derivative of the expenditure function with respect to p_i.

---

## 16. Duality Relations

The utility maximization problem (UMP) and expenditure minimization problem (EMP) are **duals** of each other:

1. **v(p, e(p, u_bar)) = u_bar** (spending the minimum expenditure to reach u_bar gives exactly u_bar utility)
2. **e(p, v(p, m)) = m** (the minimum cost to reach the utility from income m is exactly m)
3. **x_i(p, m) = h_i(p, v(p, m))** (Marshallian demand at income m equals Hicksian demand at the utility level achieved)
4. **h_i(p, u_bar) = x_i(p, e(p, u_bar))** (Hicksian demand at u_bar equals Marshallian demand when income equals minimum expenditure)

---

## 17. Key Relationships Summary

| Concept | UMP (Utility Max) | EMP (Expenditure Min) |
|---|---|---|
| Objective | Maximize u(x) | Minimize p*x |
| Constraint | p*x <= m | u(x) >= u_bar |
| Solution | Marshallian demand x(p,m) | Hicksian demand h(p,u_bar) |
| Value function | Indirect utility v(p,m) | Expenditure function e(p,u_bar) |
| Envelope result | Roy's Identity | Shephard's Lemma |
