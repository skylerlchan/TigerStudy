# ECO 310 Lecture 2: Preferences and Choice -- Comprehensive Summary

**Intermediate Micro (Mathematical) | January 28, 2026**

---

## 1. Bundles and Utility Functions

- Focus on two goods (good 1 and good 2).
- A **bundle** is a pair (x_1, x_2) specifying the quantity of each good.
- A **utility function** u(x_1, x_2) assigns a number (utility) to every possible bundle.

---

## 2. Indifference Curves

**Definition:** An indifference curve traces out all points (bundles) that give a particular utility level -- i.e., bundles among which you are *indifferent*.

- If two points A, B lie on the same indifference curve, then A ~ B.
- Indifference curves are a 2D representation of preferences (since graphing utility directly would require 3D).

### Properties of Indifference Curves

1. **Rational preferences imply indifference curves cannot cross.**
   - Proof sketch: If two curves cross at a point, take A on curve 1, B at the intersection, C on curve 2. Then A ~ B (same curve) and B ~ C (same curve), so by transitivity A ~ C -- but A and C are on different curves, a contradiction.

2. **If preferences are monotonic, indifference curves cannot be thick.**

3. **For two "good" goods, indifference curves are downward sloping.**
   - Moving down (losing good 2) requires moving right (gaining good 1) to stay indifferent.

**Definition -- Monotonic Preferences:** Preferences are monotonic if getting more of some good, without losing anything, makes you strictly better off.

---

## 3. Special Types of Preferences

### Perfect Substitutes

**Definition:** Two goods are perfect substitutes when the individual is willing to substitute one for another at a *constant rate*.

- Indifference curves are **straight lines**.
- Example: Trading 1 coffee for 4 teas at any consumption level.
- **Utility representation (1:1 substitution):** u(x_1, x_2) = x_1 + x_2
- Any positive linear transformation also works, e.g., u(x_1, x_2) = 2x_1 + 2x_2.
- An indifference curve for utility level u-bar is given by u(x_1, x_2) = u-bar, yielding a straight line with slope -1 (for the 1:1 case).

### Perfect Complements

**Definition:** Two goods are perfect complements when the individual wants to consume them in *fixed proportions*.

- Examples: Left and right shoes (1:1), sugar and coffee (2 teaspoons per 1 coffee).
- Indifference curves are **L-shaped** (right angles).
- For the 1:1 case, all pairs (1, x) or (x, 1) with x > 1 are on the same indifference curve as (1,1). Increasing only one good beyond the fixed ratio provides no additional utility.
- **Utility representation:** u(x_1, x_2) = min{x_1, x_2}

---

## 4. Marginal Rate of Substitution (MRS)

**Definition:** The MRS (of good 2 for good 1) is the negative of the slope of the indifference curve at a point:

$$MRS \text{ at } (x_1, x_2) = -\frac{\Delta x_2}{\Delta x_1}\bigg|_{\text{indifference curve}}$$

**Interpretation:** The MRS tells you how many units of good 2 you're willing to give up (-Delta x_2) to get Delta x_1 more units of good 1.

### MRS and Marginal Utility

For nonlinear indifference curves, use the derivative:

$$MRS = -\frac{dx_2}{dx_1}\bigg|_{\text{indifference curve}} = \frac{MU_1}{MU_2}$$

where MU_i is the **marginal utility** with respect to good i (i = 1, 2), i.e., the partial derivative of u with respect to x_i.

**Proof:** Along an indifference curve, u(x_1, x_2) = constant, so the total differential is:

$$MU_1 \, dx_1 + MU_2 \, dx_2 = 0$$

Rearranging: dx_2/dx_1 = -MU_1/MU_2.

### Marginal Utility Defined

**Definition:** *Marginal utility of good 1 (or 2)* is the change in your utility resulting from a small change in the amount of good 1 (or 2).

- A "good" good has **positive marginal utility**.
- A steep indifference curve (large MRS) means MU_1 is large relative to MU_2 -- you'd give up a lot of good 2 for a bit more good 1.

### Worked Example

Given u(x_1, x_2) = log(x_1) + x_1^2 * x_2 + x_2:

$$MU_1 = \frac{1}{x_1} + 2x_1 x_2$$

$$MU_2 = x_1^2 + 1$$

$$MRS = \frac{MU_1}{MU_2} = \frac{\frac{1}{x_1} + 2x_1 x_2}{x_1^2 + 1}$$

At (1, 2): MRS = (1 + 4) / (1 + 1) = 5/2 = 2.5, meaning the consumer is willing to trade 2.5 units of good 2 for one extra unit of good 1.

---

## 5. Preferences and Choices

### Revealed Preference (Motivation)

- If we *know* preferences and feasible choices, we assume consumers choose the best feasible option.
- If we *observe* choices (but don't know preferences), choosing an alternative **reveals** a preference for it over unchosen feasible alternatives. This defines a **revealed preference relation**.
- Key question: When are observed choices consistent with optimization by a "rational consumer" (one with a complete, transitive preference)?

---

## 6. Choice Rules

**Definition -- Choice Rule:** A choice rule on a finite set X is a correspondence C that maps each non-empty subset A of X onto a **non-empty** subset C(A) of A.

- C(A) is the set of all options the decision-maker would be willing to choose from A.
- Typically, A is the set of feasible (affordable) consumption bundles.

### Rationalizable Choice Rules

**Definition:** A choice rule is **rationalizable** if it could result from a rational consumer who always chooses the best (according to some complete and transitive preference) feasible option.

- Formally: C is rationalizable if there exists a complete and transitive preference relation (at least as good as) such that actual choices agree with the elements that are best according to that preference.

---

## 7. Axioms on Choice

### Two Necessary Conditions for Rationalizability

#### Sen's Axiom alpha -- Independence of Irrelevant Alternatives (IIA)

**Axiom IIA:** If x is in B, B is a subset of A, and x is in C(A), then x is in C(B).

**In words:** If you choose x from a "big" set A, then you should also choose it from any subset of A containing x. The other options in A\B are irrelevant to your feelings about x.

**Example:** "If Simone Biles is the best gymnast in the world, then she must also be the best gymnast in the USA."

**Theorem:** Rationalizability implies IIA.

*Proof:* Take x in B, B a subset of A, with x in C(A). If C is rationalizable, choices from any set are optimal according to some preference (at least as good as). So x in C(A) means x is most-preferred in A. Since B is a subset of A, x is also optimal in B, so x is in C(B).

**Key result:** IIA alone does NOT imply rationalizability.

*Counterexample:* Let X = {a, b, c} with C({a,b}) = {a}, C({a,c}) = {a,c}, C({b,c}) = {c}, C(X) = {a}, C({x}) = {x} for all x. This satisfies IIA but is not rationalizable because C({a,c}) = {a,c} implies a ~ c, while C(X) = {a} together with a ~ c implies a > c, a contradiction.

#### Sen's Axiom beta -- Consistency Axiom

**Sen's Axiom beta:** If {x, y} is a subset of C(B), B is a subset of A, and x is in C(A), then y is in C(A).

**In words:** If x and y are both chosen from B, and B is a subset of A, and x is chosen from A, then y must also be chosen from A.

**Example:** "If Simone Biles and Aly Raisman are tied for USA champions, and Simone is a world champion, then Aly Raisman must also be a world champion."

**Theorem:** Rationalizability implies Sen's beta.

*Proof:* Assume {x, y} is a subset of C(B), B is a subset of A, x in C(A), and choices are rationalizable. There is a preference (at least as good as) such that C = C_(at least as good as). So x, y are both optimal in B, implying x ~ y, while x is optimal in A. By transitivity, y must also be optimal in A, so y is in C(A).

**Key result:** Beta alone does NOT imply rationalizability.

*Reason:* Sen's axiom beta only has "bite" if the DM is willing to choose more than one alternative from some set. Any choice rule where C(A) is always a singleton satisfies beta trivially, yet could violate IIA and fail to be rationalizable.

---

## 8. The Combined Result: WARP

**Theorem (previewed for next lecture):** A choice rule satisfies both alpha and beta **if and only if** it is rationalizable.

- Together, alpha + beta are equivalent to the **Weak Axiom of Revealed Preference (WARP)**.
- WARP is a necessary and sufficient condition for choices to be rationalizable.

---

## Summary of Key Formulas

| Concept | Formula |
|---|---|
| Perfect substitutes utility | u(x_1, x_2) = x_1 + x_2 |
| Perfect complements utility | u(x_1, x_2) = min{x_1, x_2} |
| MRS (discrete) | MRS = -Delta x_2 / Delta x_1 along indifference curve |
| MRS (calculus) | MRS = MU_1 / MU_2 |
| Total differential on indifference curve | MU_1 dx_1 + MU_2 dx_2 = 0 |
| Axiom IIA (alpha) | x in B, B subset of A, x in C(A) implies x in C(B) |
| Axiom beta | {x,y} subset of C(B), B subset of A, x in C(A) implies y in C(A) |
| Rationalizability | Equivalent to alpha + beta (i.e., WARP) |
