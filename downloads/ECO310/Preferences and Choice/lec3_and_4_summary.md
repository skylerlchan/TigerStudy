# ECO 310 - Lectures 3 & 4: Preferences and Choice

## 1. Consumption Set

**Definition:** The *consumption set* X is the set of all possible consumption bundles the consumer could conceivably consume (whether or not they are affordable).

- Standard assumption: **X = R_+^L** (the non-negative orthant of L-dimensional real space), where L is the number of commodities.
- A consumption bundle is a vector **x = (x_1, x_2, ..., x_L)** where x_l >= 0 for each good l.

---

## 2. Preference Relations

### 2.1 The Weak Preference Relation

**Notation:** x >= y (read "x is weakly preferred to y") means "x is at least as good as y."

- This is the primitive (foundational) relation from which others are derived.

### 2.2 Derived Relations

**Strict Preference:**
x > y (x is strictly preferred to y) if and only if x >= y and NOT y >= x.

**Indifference:**
x ~ y (x is indifferent to y) if and only if x >= y AND y >= x.

---

## 3. Axioms (Properties) of Rational Preferences

### 3.1 Completeness (Axiom 1)

**Definition:** For all x, y in X: x >= y or y >= x (or both).

- The consumer can always compare any two bundles.
- Rules out the possibility that the consumer "doesn't know" how to rank two bundles.

### 3.2 Transitivity (Axiom 2)

**Definition:** For all x, y, z in X: if x >= y and y >= z, then x >= z.

- Ensures internal consistency of rankings.
- If violated, preferences would cycle and no "best" choice could exist.

### 3.3 Rationality

**Definition:** A preference relation is **rational** if it is both complete and transitive.

**Result:** If preferences are rational, then:
- Strict preference (>) is **transitive** and **irreflexive** (never x > x).
- Indifference (~) is **transitive**, **reflexive** (x ~ x), and **symmetric** (x ~ y implies y ~ x) -- i.e., it is an equivalence relation.

---

## 4. Desirability Assumptions

### 4.1 Monotonicity (More is Better)

**Definition:** Preferences are **monotone** if x >= y (i.e., x has at least as much of every good) and x != y implies x > y (strictly preferred).

- Increasing the amount of any good (holding others fixed) makes the consumer strictly better off.

### 4.2 Strong Monotonicity

**Definition:** Preferences are **strongly monotone** if x >= y (x_l >= y_l for all l) and x != y implies x > y.

- Same as monotonicity in the standard formulation; sometimes stated as: if x has more of at least one good and no less of any good, x is strictly preferred.

### 4.3 Local Non-Satiation (LNS)

**Definition:** For every x in X and every epsilon > 0, there exists a bundle y in X with ||x - y|| < epsilon such that y > x.

- Within any (arbitrarily small) neighborhood of any bundle, there is always a strictly preferred bundle.
- **Weaker** than monotonicity. It does NOT require that more of a good is better -- only that the consumer is never perfectly satisfied in any neighborhood.
- **Key implication:** Indifference curves cannot be "thick" (cannot contain open sets).

---

## 5. Indifference Curves and Indifference Sets

### 5.1 Upper Contour Set

**Definition:** The *upper contour set* of bundle y is:
UCS(y) = {x in X : x >= y}
(the set of all bundles at least as good as y)

### 5.2 Lower Contour Set

**Definition:** The *lower contour set* of bundle y is:
LCS(y) = {x in X : y >= x}
(the set of all bundles that y is at least as good as)

### 5.3 Indifference Set (Indifference Curve)

**Definition:** The *indifference set* containing y is:
I(y) = {x in X : x ~ y} = UCS(y) intersection LCS(y)

### Properties under rational, monotone preferences:
- Indifference curves are **downward-sloping** (with monotonicity).
- Indifference curves corresponding to **different** preference levels **cannot cross**.
- Higher indifference curves (further from the origin, to the northeast) represent higher satisfaction.

---

## 6. Convexity of Preferences

### 6.1 Convexity

**Definition:** Preferences are **convex** if for every x in X, the upper contour set UCS(x) = {y : y >= x} is a convex set.

Equivalently: if y >= x and z >= x, then for all alpha in [0, 1]:
**alpha * y + (1 - alpha) * z >= x**

- **Economic interpretation:** Mixtures (averages) of equally-good bundles are at least as good as the extremes. The consumer has a taste for diversification/balance.
- Implies indifference curves are **convex to the origin** (bowed inward).

### 6.2 Strict Convexity

**Definition:** Preferences are **strictly convex** if for every x, whenever y >= x, z >= x, and y != z, then for all alpha in (0, 1):
**alpha * y + (1 - alpha) * z > x**

- Strict mixtures of two distinct, equally-good bundles are **strictly better**.
- Implies indifference curves are **strictly** convex to the origin (no flat segments).

---

## 7. Utility Functions

### 7.1 Definition

**Definition:** A function u: X -> R is a **utility function representing preference relation >=** if, for all x, y in X:

**x >= y if and only if u(x) >= u(y)**

- A utility function assigns a numerical value to each bundle such that the numerical ranking reproduces the preference ranking.

### 7.2 Ordinal Nature of Utility

**Key result:** Utility is **ordinal**, not cardinal. Only the ranking (ordering) of utility values matters, not their magnitudes or differences.

**Proposition (Monotonic Transformations):** If u(x) represents preferences >= and f: R -> R is a **strictly increasing** function, then **v(x) = f(u(x))** also represents the same preferences >=.

- Examples: if u(x) represents preferences, so do u(x) + 5, 3u(x), u(x)^3 (when u > 0), ln(u(x)) (when u > 0), e^{u(x)}, etc.
- The converse is also true: if both u and v represent the same preferences, then v = f(u) for some strictly increasing f.

### 7.3 Existence of a Utility Representation

**Theorem (Existence):** If the preference relation >= on X = R_+^L is **complete, transitive, and continuous**, then there exists a **continuous** utility function u: X -> R that represents >=.

**Continuity of preferences (Axiom 3):**
For all x in X, the upper contour set {y : y >= x} and lower contour set {y : x >= y} are both **closed sets**.

Equivalently: if {x_n} -> x and {y_n} -> y, and x_n >= y_n for all n, then x >= y.

- Continuity rules out "jumps" or sudden reversals in preference.
- **Lexicographic preferences** are an example of complete and transitive preferences that are NOT continuous and therefore have no utility representation.

---

## 8. Common Utility Functions (Two-Good Case)

### 8.1 Cobb-Douglas

**u(x_1, x_2) = x_1^a * x_2^b** where a, b > 0.

- Equivalent monotonic transformation: v(x_1, x_2) = a*ln(x_1) + b*ln(x_2).
- Can normalize: alpha = a/(a+b), so u = x_1^alpha * x_2^(1-alpha).
- Indifference curves: smooth, strictly convex, asymptotic to both axes.
- Represents a preference for balanced/diversified bundles.

### 8.2 Perfect Substitutes

**u(x_1, x_2) = a*x_1 + b*x_2** where a, b > 0.

- Indifference curves: **straight lines** with slope **-a/b**.
- The consumer is willing to substitute good 1 for good 2 at a **constant rate** (a/b units of good 2 per unit of good 1).
- Convex but NOT strictly convex.

### 8.3 Perfect Complements (Leontief)

**u(x_1, x_2) = min{a*x_1, b*x_2}** where a, b > 0.

- Indifference curves: **L-shaped**, with kink along the ray where a*x_1 = b*x_2 (i.e., x_2/x_1 = a/b).
- The consumer always wants goods in fixed proportions; extra units of one good alone provide no additional utility.
- Convex but NOT strictly convex.

### 8.4 Quasilinear Utility

**u(x_1, x_2) = v(x_1) + x_2** where v is increasing and concave.

- Linear in good 2, nonlinear in good 1.
- Indifference curves are **parallel vertical shifts** of one another (same shape, shifted up/down).
- Example: v(x_1) = ln(x_1), so u = ln(x_1) + x_2.

---

## 9. Marginal Rate of Substitution (MRS)

### 9.1 Definition

**Definition:** The *marginal rate of substitution* of good 2 for good 1 at bundle (x_1, x_2) is:

**MRS_{12}(x_1, x_2) = dx_2/dx_1 |_{along indifference curve}**

This is the **slope of the indifference curve** at that point.

Using the utility function (via implicit differentiation of u(x_1, x_2) = constant):

**MRS_{12} = - (partial u / partial x_1) / (partial u / partial x_2) = - MU_1 / MU_2**

where MU_l = partial u / partial x_l is the **marginal utility** of good l.

### 9.2 Economic Interpretation

- The MRS gives the rate at which the consumer is willing to **trade** good 2 for good 1 while remaining on the same indifference curve.
- |MRS_{12}| = MU_1 / MU_2 tells you how many units of good 2 the consumer is willing to give up for one additional unit of good 1.

### 9.3 Invariance to Monotonic Transformations

**Key result:** The MRS is invariant to monotonic transformations of the utility function.

If v(x_1, x_2) = f(u(x_1, x_2)) where f' > 0, then:
MRS under v = - (f' * MU_1) / (f' * MU_2) = - MU_1 / MU_2 = MRS under u.

### 9.4 Diminishing MRS

**Definition:** Preferences exhibit a **diminishing marginal rate of substitution** if |MRS_{12}| decreases as x_1 increases along an indifference curve (the indifference curve becomes flatter).

- This is equivalent to **convexity** of preferences.
- Intuition: The more of good 1 you have (relative to good 2), the less good 2 you are willing to sacrifice for yet another unit of good 1.

### 9.5 MRS for Common Utility Functions

**Cobb-Douglas** u = x_1^a * x_2^b:
MRS_{12} = -(a * x_2) / (b * x_1)

**Perfect Substitutes** u = a*x_1 + b*x_2:
MRS_{12} = -a/b (constant everywhere)

**Perfect Complements** u = min{a*x_1, b*x_2}:
MRS is undefined at the kink (where a*x_1 = b*x_2); it is 0 on the horizontal segment and negative infinity on the vertical segment.

**Quasilinear** u = v(x_1) + x_2:
MRS_{12} = -v'(x_1) (depends only on x_1, not on x_2)

---

## 10. Choice Rules and Revealed Preference

### 10.1 Choice Structure

**Definition:** A *choice structure* (B, C(.)) consists of:
- **B**: a family of nonempty subsets of X (the "budget sets" or feasible sets the decision-maker might face).
- **C(B)**: a *choice rule* that assigns to each B in B a nonempty set C(B) subset of B (the chosen elements from B).

### 10.2 Weak Axiom of Revealed Preference (WARP)

**Definition (WARP):** A choice structure (B, C(.)) satisfies WARP if:

For any B, B' in B, if x, y are in B and x, y are in B', and x is in C(B), then y is NOT in C(B') unless x is also in C(B').

**Equivalent statement:** If x is "revealed preferred" to y (i.e., both are available and x is chosen), then there is no situation where y is chosen and x is available but not chosen.

- WARP ensures consistency: if x was chosen over y when both were available, then y should never be chosen in a way that contradicts x's superiority.

### 10.3 Revealed Preference Relation

**Definition:** Given a choice structure (B, C(.)), the *revealed preference relation* >=* is defined by:

**x >=* y if there exists some B in B such that x, y are in B and x is in C(B).**

(x is revealed at least as good as y.)

### 10.4 Relationship Between Preference-Based Choice and WARP

**Result:** If preferences >= are rational (complete + transitive) and the choice rule is generated by maximizing >=, i.e., C(B, >=) = {x in B : x >= y for all y in B}, then the resulting choice structure satisfies WARP.

**Important caveat:** The converse does NOT fully hold. WARP does not guarantee that the revealed preference relation is transitive (hence fully rational). WARP is a necessary but not sufficient condition for rationality of the underlying preferences. The **Strong Axiom of Revealed Preference (SARP)**, which requires transitivity of revealed preference, is needed for full rationality.

---

## 11. Summary of Key Relationships

| Property | Implication |
|---|---|
| Completeness + Transitivity | Rational preferences |
| Rational + Continuous | Utility representation exists |
| Monotonicity | Indifference curves slope downward |
| Convexity | Diminishing MRS; upper contour sets are convex |
| Strict Convexity | Strictly diminishing MRS; unique optimum in convex budget sets |
| Monotonic transformation of u | Same preferences, same MRS, same indifference map |
| LNS (Local Non-Satiation) | No thick indifference curves; consumer spends full budget at optimum |
