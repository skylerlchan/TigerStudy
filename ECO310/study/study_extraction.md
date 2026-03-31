# ECO 310 -- Problems, Solutions, Formulas & Concepts Extraction

---

## Source 1: Extra Practice Questions on Optimization

### Problem 1 -- Cobb-Douglas Utility Maximization (Interior Solution)

**Concept Tested:** Lagrangian optimization / bang-per-buck with Cobb-Douglas utility; interior solutions.

**Setup:** Utility function u(x, y) = x^(1/2) * y^(1/2). Prices p_x = 2, p_y = 1. Income m = 12.

**Key Formulas Used:**
- MU_x = (1/2) x^(-1/2) y^(1/2)
- MU_y = (1/2) x^(1/2) y^(-1/2)
- Bang-per-buck condition: MU_x / p_x = MU_y / p_y => y/x = 2 => y = 2x
- Budget constraint: 2x + y = 12

**Solution:** Substituting y = 2x into budget: 2x + 2x = 12 => x* = 3, y* = 6. Utility = 3^(1/2) * 6^(1/2) = 18^(1/2).

---

### Problem 2 -- Perfect Substitutes Utility Maximization (Corner Solution)

**Concept Tested:** Corner solutions with linear (perfect substitutes) utility; comparing bang-per-buck across goods.

**Setup:** u(x, y) = 2x + y. Prices p_x = 2, p_y = 1. Income m = 12.

**Key Formulas Used:**
- MU_x / p_x = 2/2 = 1
- MU_y / p_y = 1/1 = 1
- Since bang-per-buck is equal, any bundle on the budget line is optimal.

**Solution:** The consumer is indifferent among all bundles on the budget line 2x + y = 12. Any combination satisfying this is optimal (e.g., (0,12), (6,0), (3,6), etc.).

---

### Problem 3 -- Perfect Substitutes with Strict Corner

**Concept Tested:** Corner solution when one good strictly dominates in bang-per-buck.

**Setup:** u(x, y) = 4x + y. Prices p_x = 2, p_y = 1. Income m = 12.

**Key Formulas Used:**
- MU_x / p_x = 4/2 = 2
- MU_y / p_y = 1/1 = 1
- Good x has strictly higher bang-per-buck, so spend all income on x.

**Solution:** x* = 12/2 = 6, y* = 0. Bundle = (6, 0).

---

### Problem 4 -- Cobb-Douglas with Different Exponents

**Concept Tested:** Cobb-Douglas optimization with unequal exponents; the "magic rule" for Cobb-Douglas spending shares.

**Setup:** u(x, y) = x^(1/3) * y^(2/3). Prices p_x = 2, p_y = 1. Income m = 12.

**Key Formulas Used:**
- MU_x = (1/3) x^(-2/3) y^(2/3)
- MU_y = (2/3) x^(1/3) y^(-1/3)
- Bang-per-buck: MU_x / p_x = MU_y / p_y => y/(2x) = 2 => y = 4x
- Budget: 2x + y = 12

**Solution:** 2x + 4x = 12 => x* = 2, y* = 8.

**Magic Rule shortcut:** Exponents are 1/3 and 2/3. Spend 1/3 of income on x: p_x * x = (1/3)(12) = 4 => x = 2. Spend 2/3 on y: p_y * y = (2/3)(12) = 8 => y = 8.

---

### Problem 5 -- Quasilinear Utility (Potential Corner Solution)

**Concept Tested:** Quasilinear preferences (u = x_2 + f(x_1)); checking for corner solutions when interior solution is infeasible.

**Setup:** u(x, y) = y + 24x^(1/2). Prices p_x = 8, p_y = 1. Income m = 12.

**Key Formulas Used:**
- MU_x = 12 / x^(1/2), MU_y = 1
- Bang-per-buck: 12 / x^(1/2) = 8 => x^(1/2) = 3/2 => x = 9/4
- Budget: 8(9/4) + y = 12 => 18 + y = 12 => y = -6

**Solution:** Interior solution gives y = -6, which is infeasible. Corner solution: y* = 0, spend all on x => x* = 12/8 = 3/2. Bundle = (3/2, 0).

**Key Insight:** With quasilinear utility, the interior demand for x_1 depends only on p_1 (not income). If income is too low to afford the interior x_1 while keeping x_2 >= 0, the consumer goes to the corner: all income on x_1, zero x_2.

---

### Problem 6 -- Perfect Complements (Leontief Preferences)

**Concept Tested:** Optimization with perfect complements (min function); no substitution, consume in fixed proportions.

**Setup:** u(x, y) = min(2x, y). Prices p_x = 2, p_y = 1. Income m = 12.

**Key Formulas Used:**
- Optimal condition: consume where 2x = y (the "kink" of the L-shaped indifference curves)
- Budget: 2x + y = 12
- Substitute y = 2x: 2x + 2x = 12

**Solution:** x* = 3, y* = 6. Utility = min(6, 6) = 6.

---

### Problem 7 -- Lagrangian with Cobb-Douglas

**Concept Tested:** Full Lagrangian method (setting up L, FOCs, solving system); verifying same answer as bang-per-buck.

**Setup:** Same as Problem 1: u(x, y) = x^(1/2) y^(1/2), p_x = 2, p_y = 1, m = 12.

**Lagrangian:**
L = x^(1/2) y^(1/2) - lambda(2x + y - 12)

**FOCs:**
- dL/dx = (1/2) x^(-1/2) y^(1/2) - 2*lambda = 0
- dL/dy = (1/2) x^(1/2) y^(-1/2) - lambda = 0
- dL/d(lambda) = -(2x + y - 12) = 0

**Solution:** Dividing FOC1 by FOC2: y/(2x) = 2 => y = 2x (same condition as bang-per-buck). Then x* = 3, y* = 6. lambda* = (1/2)(3)^(-1/2)(6)^(1/2) / 2 = sqrt(2)/4 (approximately 0.354).

**Interpretation of lambda:** The marginal utility of an additional dollar of income. If income increases from 12 to 13, utility increases by approximately lambda = sqrt(2)/4.

---

### Problem 8 -- Lagrangian with Cobb-Douglas (Different Exponents)

**Concept Tested:** Same Lagrangian technique with different exponents; confirming magic rule.

**Setup:** Same as Problem 4: u(x, y) = x^(1/3) y^(2/3), p_x = 2, p_y = 1, m = 12.

**Lagrangian:**
L = x^(1/3) y^(2/3) - lambda(2x + y - 12)

**FOCs:**
- (1/3) x^(-2/3) y^(2/3) = 2*lambda
- (2/3) x^(1/3) y^(-1/3) = lambda

**Solution:** Dividing: y/(4x) = 1 => y = 4x. Then x* = 2, y* = 8. lambda = (1/3)(2)^(-2/3)(8)^(2/3) / 2 = (2/3) * 2^(-2/3) (approximately 0.42).

---

### Problem 9 -- Three-Good Cobb-Douglas Optimization

**Concept Tested:** Extending Cobb-Douglas optimization to three goods; magic rule generalization.

**Setup:** u(x, y, z) = x^(1/4) y^(1/4) z^(1/2). Prices p_x = 2, p_y = 4, p_z = 1. Income m = 12.

**Key Formulas Used (Magic Rule for 3 goods):**
- Exponents: 1/4, 1/4, 1/2 (sum to 1 already).
- Spend fraction equal to exponent share: spend (1/4) of income on x, (1/4) on y, (1/2) on z.
- p_x * x = (1/4)(12) = 3 => x = 3/2
- p_y * y = (1/4)(12) = 3 => y = 3/4
- p_z * z = (1/2)(12) = 6 => z = 6

**Solution:** x* = 3/2, y* = 3/4, z* = 6.

---

### Problem 10 -- Three-Good Lagrangian

**Concept Tested:** Full Lagrangian with three goods; system of 4 equations and 4 unknowns.

**Setup:** Same as Problem 9.

**Lagrangian:**
L = x^(1/4) y^(1/4) z^(1/2) - lambda(2x + 4y + z - 12)

**FOCs:**
- (1/4) x^(-3/4) y^(1/4) z^(1/2) = 2*lambda
- (1/4) x^(1/4) y^(-3/4) z^(1/2) = 4*lambda
- (1/2) x^(1/4) y^(1/4) z^(-1/2) = lambda

**Solution:** From FOC1/FOC2: y/x = 1/2 => x = 2y. From FOC2/FOC3: 2z/(4y) = 1 => z = 8y. Budget: 2(2y) + 4y + 8y = 12 => 16y = 12 => y = 3/4. Then x = 3/2, z = 6.

---

### Problem 11 -- Quasilinear with Square Root

**Concept Tested:** Quasilinear optimization with potential corner; square root sub-utility.

**Setup:** u(x, y) = y + 12x^(1/2). Prices p_x = 2, p_y = 1. Income m = 24.

**Key Formulas Used:**
- MU_x / p_x = MU_y / p_y => 6/x^(1/2) = 2 => x^(1/2) = 3 => x = 9
- Budget: 2(9) + y = 24 => y = 6

**Solution:** x* = 9, y* = 6. This is feasible (both non-negative), so interior solution holds.

**Verification:** Checked convexity: MU_x/MU_y = 6/x^(1/2) is decreasing in x, confirming diminishing MRS and thus convex preferences.

---

### Problem 12 -- Quasilinear Corner Solution Case

**Concept Tested:** Same utility form but income too low for interior solution.

**Setup:** u(x, y) = y + 12x^(1/2). Prices p_x = 2, p_y = 1. Income m = 8.

**Solution:** Interior would require x = 9 (same as above, independent of income for quasilinear), costing 18 > 8. Corner solution: y* = 0, x* = 8/2 = 4. Bundle = (4, 0).

---

## Source 2: ECO 310 Solutions 1 (Spring 2026)

### Problem 1 -- Revealed Preference and WARP

**Concept Tested:** Revealed preference theory; Weak Axiom of Revealed Preference (WARP); comparing bundles at different price regimes.

**Setup:**
- Year 1: p1 = p2 = $10, buys (10, 10)
- Year 2: p1 = $10, p2 = $7, buys (12, x)

**(a) When is the year-1 bundle revealed weakly/strictly preferred to year-2?**

**Formula:** At year-1 prices, cost of year-1 bundle >= cost of year-2 bundle:
- 10(10) + 10(10) >= 10(12) + 10(x)
- 200 >= 120 + 10x
- x <= 8 (weak preference); x < 8 (strict preference)

**(b) When is the year-2 bundle revealed weakly/strictly preferred to year-1?**

**Formula:** At year-2 prices, cost of year-2 bundle >= cost of year-1 bundle:
- 10(12) + 7x >= 10(10) + 7(10)
- 120 + 7x >= 170
- x >= 50/7 (weak preference); x > 50/7 (strict preference)

**(c) When does behavior violate WARP?**

**Answer:** WARP is violated when both (a) and (b) hold with at least one strict. This occurs when 50/7 <= x <= 8 (note 50/7 ~ 7.14 < 8, so this range is valid).

---

### Problem 2 -- Choice Functions, Rationalizability, and IIA

**Concept Tested:** Independence of Irrelevant Alternatives (IIA); transitivity; rationalizability of choice functions.

**Setup:** Melsi the puppy has three toys: F (frisbee), B (ball), S (stuffed squirrel).
- C({F, B}) = {F}
- C({B, S}) = {B}
- C({F, S}) = {S}

**(a) Why can't these choices be rationalized?**

From choices: F > B, B > S, S > F. This is an intransitive cycle. Transitivity requires F > B and B > S => F > S, but we observe S > F. Contradiction.

**(b) Prove WARP/IIA is violated regardless of C({F, B, S}).**

Three cases:
1. If she chooses F from {F,B,S}: violates IIA because F is not chosen from {F,S} (C({F,S}) = {S}).
2. If she chooses B from {F,B,S}: violates IIA because B is not chosen from {F,B} (C({F,B}) = {F}).
3. If she chooses S from {F,B,S}: violates IIA because S is not chosen from {B,S} (C({B,S}) = {B}).

All cases lead to a violation. IIA requires: if an item is chosen from a larger set, it must also be chosen from any subset containing it.

---

### Problem 3 -- Quasilinear Preferences with Logarithm

**Concept Tested:** Quasilinear utility optimization (u = x2 + ln(x1)); interior vs. corner solutions.

**Setup:** u(x1, x2) = x2 + ln(x1). Income m = 2.

**(a) Optimal bundle when p1 = p2 = 1.**

**Formulas:**
- MU1 = 1/x1, MU2 = 1
- Bang-per-buck: 1/x1 = 1/1 => x1 = 1
- Budget: x1 + x2 = 2 => x2 = 1

**Solution:** (x1, x2) = (1, 1).

**(b) Optimal bundle when p1 = 1, p2 = 3.**

- Bang-per-buck: 1/x1 = 1/3 => x1 = 3
- Budget: 3 + 3*x2 = 2 => x2 = -1/3

Infeasible (negative). Corner solution: x2 = 0, x1 = m/p1 = 2/1 = 2.

**Solution:** (x1, x2) = (2, 0).

**Key Insight:** When income is too low relative to the quasilinear "ideal" demand for x1, the consumer hits a corner. Here, at m = 2 she can afford at most x1 = 2, so MU1/MU2 = 1/2, and whenever p1/p2 < 1/2 (i.e., p2 > 2), good 1 always has higher bang-per-buck, pushing to the corner.

---

### Problem 4 -- Leisure-Consumption (Cobb-Douglas Labor Supply)

**Concept Tested:** Labor supply model; Cobb-Douglas utility over leisure and spending; budget constraint derivation; monotone transformations of utility; Lagrangian method.

**Setup:** u(L, S) = L^(1/4) * S^(3/4). Wage = w per hour. Total hours = T.

**(a) Budget constraint:**

S <= w(T - L), i.e., spending cannot exceed wage income from hours worked. Rearranged: S + wL = wT.

**(b) Magic rule for Cobb-Douglas: L = T/5.**

- Normalize exponents: raise u to power 3/5 to get L^(1/5) * S^(4/5) (exponents now sum to 1 -- note: original exponents 1/4 + 3/4 = 1, but the document's problem uses L^(1/3)S^(4/3) with sum 5/3, requiring normalization).
- The exponent on L is 1/5, so spend 1/5 of "resource" on leisure.
- Using budget S + wL = wT (where "price" of L is w and "income" is wT): wL = (1/5)(wT) => L = T/5.

**Result is independent of wage w.**

**(c) Monotone transformation equivalence:**

u(L,S) = L^(1/3) S^(4/3) => raise to 3/5 power => L^(1/5) S^(4/5) => take log => (1/5)ln(L) + (4/5)ln(S) => multiply by 5 => ln(L) + 4ln(S) = v(L,S).

All steps are monotone transformations, so v represents the same preferences as u.

**(d) Full solution using v(L,S) = log(L) + 4log(S).**

**Bang-per-buck method:**
- MU_L / MU_S = (1/L) / (4/S) = S/(4L)
- Set equal to price ratio: S/(4L) = w => S = 4wL
- Budget: S + wL = wT => 5wL = wT => L = T/5
- S = 4w(T/5) = 4wT/5

**Solution:** (L*, S*) = (T/5, 4wT/5).

**Lagrangian method:**
- L = log(L) + 4log(S) + lambda_1 * L + lambda_2 * S + lambda_3 * (wT - wL - S)
- Assuming interior (lambda_1 = lambda_2 = 0):
  - FOC for L: 1/L = lambda_3 * w
  - FOC for S: 4/S = lambda_3
  - Dividing: S/(4L) = w => S = 4wL (same as above)
- lambda_3 = 5/(wT)

**Full solution:** (L, S, lambda_1, lambda_2, lambda_3) = (T/5, 4wT/5, 0, 0, 5/(wT)).

---

## Key Formulas and Concepts Summary

### Optimization Methods

| Method | When to Use | Key Equation |
|---|---|---|
| Bang-per-buck (MRS = price ratio) | Interior solutions with differentiable utility | MU_x / p_x = MU_y / p_y |
| Lagrangian | General constrained optimization; finding shadow value of constraint | Set up L, take FOCs, solve system |
| Cobb-Douglas Magic Rule | Any Cobb-Douglas u = x^a * y^b | Spend a/(a+b) of income on x, b/(a+b) on y |
| Corner solution check | Linear utility or when interior gives negative quantities | Compare bang-per-buck; if one good always dominates, spend all income on it |

### Utility Function Types and Solution Approaches

| Utility Type | Form | Solution Approach |
|---|---|---|
| Cobb-Douglas | x^a * y^b | Magic rule or bang-per-buck; always interior |
| Perfect Substitutes | ax + by | Compare MU_x/p_x vs MU_y/p_y; corner or entire budget line |
| Perfect Complements | min(ax, by) | Set ax = by and combine with budget |
| Quasilinear | y + f(x) | Bang-per-buck gives x independent of income; check for corner (y >= 0) |

### Revealed Preference

- **Revealed Weak Preference:** Bundle A is revealed weakly preferred to B if A is chosen when B is affordable (cost of A >= cost of B at the prices where A is chosen).
- **WARP Violation:** Both bundles are revealed preferred to each other, with at least one strict.

### Choice Theory

- **IIA (Independence of Irrelevant Alternatives):** If an item is chosen from a set, it must be chosen from every subset that contains it.
- **Rationalizability:** Choices can be rationalized by a utility function only if they satisfy transitivity and IIA.
- **Intransitive Cycle:** A > B, B > C, C > A -- cannot be represented by any utility function.

### Monotone Transformations

Any strictly increasing function applied to a utility function preserves the same preferences:
- Raising to a positive power
- Taking logarithm
- Multiplying by a positive constant

These do not change optimal bundles, only the numerical utility values.

### Lagrangian Interpretation

- **lambda (Lagrange multiplier):** The marginal value of relaxing the constraint by one unit. In consumer theory, it is the marginal utility of income -- how much utility increases per additional dollar of budget.
