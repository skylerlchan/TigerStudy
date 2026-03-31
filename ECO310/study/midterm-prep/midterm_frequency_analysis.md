# ECO 310 Midterm Frequency Analysis

All 4 exams (Spring 2022, 2023, 2024, 2025) plus the 2019 review sheet analyzed.

---

## FREQUENCY TABLE: Concept Appearance Across 4 Exams

### EVERY EXAM (4/4)

| Concept | 2022 | 2023 | 2024 | 2025 |
|---------|------|------|------|------|
| **Marshallian demand derivation** (set MRS = price ratio + budget constraint) | Q2a | Q3c | Q3c | SA1a |
| **Expected utility: write out EU expression** | Q3a | Q4a | Q2b(i) | SA3a |
| **Optimal investment/allocation under uncertainty** (FOC of EU) | Q3c | Q4b | Q2b(ii) | SA3b |
| **Risk aversion definition/application** (u(E[W]) > EU, concave u) | Q1c | Q1-6, Q2a | Q1-6, Q1-8, Q2a | SA2a |
| **Cobb-Douglas "magic rule"** (spend fraction alpha/(alpha+beta) on each good) | -- (implicit) | Q1-2 | Q1-3 | MC1, MC6 |
| **Perfect complements** (min{x1,x2}) demand/behavior | Q2 (all parts) | Q1-4 | Q1-5 | MC3 |

### MOST EXAMS (3/4)

| Concept | Exams |
|---------|-------|
| **WARP / Revealed Preference** (checking if choices violate WARP) | 2023 (Q2b), 2024 (MC9), 2025 (MC2) |
| **Substitution effect & income effect decomposition** | 2023 (MC4), 2024 (MC5), 2025 (MC6) |
| **Perfect substitutes** (corner solutions, bang-per-buck comparison) | 2024 (MC2, MC10), 2025 (MC5), 2023 (implicit in Q1-6) |
| **Certainty equivalent / risk premium** | 2023 (Q2a), 2024 (Q2a), 2025 (SA2b) |
| **Rationality of preferences** (completeness and transitivity) | 2022 (Q1a), 2023 (MC1), 2024 (MC1) |
| **Convexity of preferences** (MRS declining check) | 2022 (Q1a), 2023 (Q3a), 2024 (Q3b) |
| **Corner solutions / non-negativity constraints** | 2023 (Q3c), 2024 (MC2, MC10), 2025 (MC5) |
| **Consequentialism / EU paradoxes** (framing effects) | 2023 (MC5), 2024 (MC7) -- same question reused |
| **Risk-averse preference for mean-preserving contractions** | 2023 (MC6), 2024 (MC8), 2025 (SA2a) |
| **Expenditure function / Hicksian (compensated) demand** | 2022 (Q2c), 2024 (Q3d), 2025 (SA1c) |
| **Tax + subsidy: can consumer afford original bundle?** | 2023 (MC3), 2024 (MC4) -- identical question |
| **Asset allocation** (risky + risk-free, portfolio std dev) | 2023 (Q4), 2024 (Q2b), 2025 (MC4, SA3) |

### SOME EXAMS (2/4)

| Concept | Exams |
|---------|-------|
| **CES utility** (nests Cobb-Douglas, complements, substitutes as limits) | 2025 (SA1a-c) -- tested exhaustively; 2019 review sheet covers the component pieces |
| **Compensating variation** | 2022 (Q2b), 2025 (MC6 implicitly) |
| **IIA (Independence of Irrelevant Alternatives)** | 2022 (Q1b), 2019 review sheet |
| **Labor-leisure tradeoff** (endowment budget constraint) | 2022 (Q2), 2023 (Q3d -- time constraint variant) |
| **Proving EU inequalities** (weighted sums of concavity inequalities) | 2022 (Q1c), 2025 (SA2a-ii) |
| **Optimal x given binary/discrete outcomes** (invest x, keep rest safe) | 2023 (Q4), 2024 (Q2b) |
| **Log utility wealth threshold** (when does DM accept/reject gamble?) | 2024 (Q2a), 2025 (SA2b) |
| **CRRA utility** u(w) = w^(1-alpha) | 2024 (Q2), 2025 (implicitly in risk aversion discussion) |

### RARE (1/4)

| Concept | Exam |
|---------|------|
| **Non-standard utility** (u = C^alpha + 2CN, polynomial) | 2023 (Q3) |
| **IIA formal proof** | 2022 (Q1b) |
| **Intertemporal consumption** (save today, consume tomorrow) | 2024 (Q3) |
| **Comparing two gambles** (playing once vs. twice) | 2025 (SA2a-ii) |
| **More risk-averse => lower CE proof** | 2023 (Q2a) |
| **Correlated assets** (state-dependent returns) | 2025 (SA3) |
| **Expenditure function limit behavior** | 2025 (SA1c) |

---

## FULL PROBLEM-BY-PROBLEM BREAKDOWN

---

## SPRING 2022

### Q1: Proofs and General Concepts (30 pts, 10 each)

**Q1a: u(x1,x2) = max{x1,x2} -- rational? convex?**
- **Concept tested:** Rationality (completeness + transitivity) from utility representation; convexity of preferences
- **Problem type:** Proof/conceptual
- **Solution:** (i) Rational -- existence of a utility function guarantees completeness and transitivity. (ii) NOT convex -- counterexample: u(1,3) = u(3,1) = 3, but the 50-50 mix u(2,2) = 2 < 3.
- **Trap:** Students often confuse "convex preferences" with "convex utility function." Convex preferences mean mixtures are weakly preferred to the worst bundle, which fails for max{} since it rewards extremes.

**Q1b: Sally minimizes utility from menus. Do choices satisfy IIA?**
- **Concept tested:** IIA / choice theory
- **Problem type:** Proof
- **Solution:** Yes. If a = argmin u(x) in A, then for any B subset of A containing a, a still minimizes u in B. Alternatively, minimizing u is the same as maximizing v = -u, and utility-maximizing choices satisfy IIA.
- **Trap:** Students think "minimizing utility" must violate rationality axioms, but it is still rationalizable (just with a different preference ordering).

**Q1c: Prove 50-50 win/lose $100 gamble preferred to 50-50 win/lose $200**
- **Concept tested:** Risk aversion proof via Jensen's inequality
- **Problem type:** Formal proof
- **Solution:** Apply risk aversion (u(E[W]) > EU) twice: u(w0 - 100) > (1/2)u(w0 - 200) + (1/2)u(w0) and u(w0 + 100) > (1/2)u(w0) + (1/2)u(w0 + 200). Adding these halved gives the result.
- **Trap:** Must use concavity of u applied at the right wealth levels. Cannot just say "lower variance is better" without proof.

### Q2: Demand -- Homer Simpson, u(B,L) = min{B,L} (30 pts)

**Q2a: Find optimal labor supply l(w)**
- **Concept tested:** Perfect complements demand with endowment budget constraint (labor-leisure)
- **Problem type:** Demand derivation with non-standard budget
- **Solution:** Budget: B = w(16-L) + N. Optimal: B = L. Solve to get L = (16w+N)/(1+w), so labor = 16 - L = (16-N)/(1+w).
- **Trap:** The budget constraint here is NOT the standard p1x1 + p2x2 = m. Students must recognize that leisure is "purchased" by forgoing wages. Also must check corner: if N > 16, Homer doesn't work at all.

**Q2b: Compensating variation if beer price doubles**
- **Concept tested:** Compensating variation with perfect complements
- **Problem type:** CV calculation
- **Solution:** With perfect complements, no substitution effect -- the cheapest way to maintain original utility is to buy the exact original bundle. So CV = extra cost of original beer quantity = B0 (since price doubles from 1 to 2). B0 = (16w+N)/(1+w).
- **Trap:** Students try to re-derive Hicksian demand when with perfect complements the compensated bundle IS the original bundle (no reoptimization).

**Q2c: Expenditure function -- how much allowance N needed for utility u*?**
- **Concept tested:** Expenditure function / Hicksian demand
- **Solution:** Need B = L = u* (perfect complements). Budget: pB * u* = w(16 - u*) + N. Solve: N = (pB + w)u* - 16w.
- **Trap:** Must correctly account for the wage income when writing the budget constraint.

### Q3: Expected Utility -- Sam's midterm time allocation (30 pts)

**Q3a: Write out EU from spending x minutes on hard question**
- **Concept tested:** Setting up EU expression
- **Problem type:** EU formulation
- **Solution:** EU = p * sqrt(60+x) + (1-p) * sqrt(60-x). With probability p, gets 2x from hard + (60-x) from easy = 60+x total. With probability (1-p), gets 0 from hard + (60-x) from easy.
- **Trap:** Students mess up the point totals. The hard question yields 2x points (not x), so total if successful is 60-x+2x = 60+x.

**Q3b: If p < 1/2, show Sam should spend all 60 min on easy question**
- **Concept tested:** Combining expected return argument with risk aversion
- **Solution:** Expected points from hard = 2px < x per minute when p < 1/2. Easy question gives 1 guaranteed point per minute. Since easy has BOTH higher expected return AND no risk, a risk-averse Sam strictly prefers easy.
- **Trap:** Must make BOTH arguments: (1) lower expected return AND (2) risk aversion. Either alone is not sufficient for a definitive answer without the other.

**Q3c: Find optimal x when p > 1/2**
- **Concept tested:** FOC optimization of EU
- **Solution:** FOC: p/(2*sqrt(60+x)) = (1-p)/(2*sqrt(60-x)). Solve: x = 60 * [p^2 - (1-p)^2] / [p^2 + (1-p)^2].
- **Trap:** Algebra-heavy. Students must square both sides correctly after cross-multiplying.

**Q3d: If must choose ONLY hard or ONLY easy, for what p choose hard?**
- **Concept tested:** Comparing two EU values (discrete choice)
- **Solution:** All easy: EU = sqrt(60). All hard: EU = p*sqrt(120). Choose hard if p > sqrt(60)/sqrt(120) = 1/sqrt(2).
- **Trap:** This is NOT the same threshold as in (c). The discrete choice is simpler but students try to reuse the FOC.

---

## SPRING 2023

### Q1: Multiple Choice (24 pts, 4 each)

**MC1: Jake prefers a iff a >= b+1. Rational?**
- **Concept:** Completeness and transitivity
- **Answer:** B -- Incomplete (cannot compare a and b when |a-b| < 1), but transitive.
- **Trap:** Students assume "irrational" = "intransitive." Here it's incomplete but transitive.

**MC2: u(x1,x2) = x1^(1/2) * x2. Optimal spending?**
- **Concept:** Cobb-Douglas magic rule
- **Answer:** C -- Exponents are 1/2 and 1. Normalize: spend fraction (1)/(1/2+1) = 2/3 on good 2.
- **Trap:** Must normalize exponents. Ratio of exponents determines spending shares.

**MC3: Apple tax + fruit subsidy. Better or worse off?**
- **Concept:** Slutsky compensation / revealed preference
- **Answer:** A -- The $5 subsidy exactly covers the increased cost of the original bundle (10 apples x $0.50). So original bundle is still affordable, but consumer can likely reoptimize and do better.
- **Trap:** Students think the consumer is "definitely indifferent" because the original bundle is affordable. But reoptimization at new prices typically makes them strictly better off.

**MC4: min{L,R}, m=10, pR rises from 1 to 4. Substitution effect on R?**
- **Concept:** Substitution effect with perfect complements
- **Answer:** A (zero) -- With perfect complements, compensated bundle = original bundle (no reoptimization possible).
- **Trap:** Students compute the total change and call it the substitution effect. With min{}, the entire change is income effect, substitution effect is zero.

**MC5: Framing paradox (saving lives vs. killing). What's violated?**
- **Concept:** Consequentialism, EU maximization
- **Answer:** D -- Violates both consequentialism AND EU maximization (but NOT independence, since these are the same two lotteries described differently, not different lotteries).
- **Trap:** Students pick "all of these." Independence is about combining lotteries with a common third option -- not relevant here since the lotteries are identical, just reframed.

**MC6: Risk-averse consumer, what's preferred to 50-50 $0 or $200?**
- **Concept:** Risk aversion implications
- **Answer:** D (both b and c) -- $110 lump-sum is better (higher expected value, no risk). 50-50 $50/$150 is better (same EV=$100, less spread). $90 lump-sum is ambiguous.
- **Trap:** $90 is below the $100 EV, so it's not guaranteed to be preferred despite being risk-free. Must compare both dimensions (return and risk).

### Q2: Proofs and General Concepts (20 pts)

**Q2a: More risk-averse => if Mavi accepts bet, so does Melsi (12 pts)**
- **Concept tested:** Certainty equivalent, risk premium, comparative risk aversion
- **Problem type:** Step-by-step proof
- **Solution:**
  - Part i: Accept bet iff CE > w0 (by definition, EU = u(CE), and accepting means EU > u(w0), so CE > w0).
  - Part ii: Higher risk premium means lower CE (since CE = E[W] - risk_premium). If Mavi (more risk-averse) accepts, her CE > w0, so Melsi's CE is even higher => Melsi also accepts.
- **Trap:** Students forget that CE = E[W] - pi, linking risk premium to certainty equivalent directly.

**Q2b: WARP violation -- which bundles get the elderly man committed? (8 pts)**
- **Concept tested:** WARP with prices
- **Solution:** Old bundle (4,2) at prices (1,3) cost 10. New prices (3,5). WARP violated if: (1) old bundle revealed preferred: 1*4 + 3*2 >= 1*x1 + 3*x2, i.e., 10 >= x1 + 3x2, AND (2) new bundle revealed preferred: 3*x1 + 5*x2 <= 3*4 + 5*2 = 22, i.e., 3x1 + 5x2 >= 22 (with at least one strict).
- **Trap:** Must get the direction of inequalities right. "Revealed preferred" means the chosen bundle costs at least as much as the alternative at those prices.

### Q3: Demand -- Harry, u(N,C) = C^alpha + 2CN (37 pts)

**Q3a: Show preferences are convex if alpha <= 2 (8 pts)**
- **Concept tested:** Convexity test via declining MRS
- **Solution:** MUC/MUN = (alpha*C^(alpha-1) + 2N) / (2C). Show this falls as C rises and N falls. The N/C term falls. The C^(alpha-2) term falls when alpha <= 2.
- **Trap:** Non-standard utility function. Students used to Cobb-Douglas may not know how to handle polynomial utility.

**Q3b: Indifference curve through (1,1) (5 pts)**
- **Concept:** Indifference curves
- **Solution:** C^alpha + 2CN = 1 + 2 = 3.

**Q3c: Marshallian demand when alpha = 2 (12 pts)**
- **Concept tested:** Demand derivation with non-standard utility
- **Solution:** MUC/MUN = (2C + 2N)/(2C) = 1 + N/C = pC/pN. So N/C = (pC-pN)/pN. Substitute into budget: C = m/(2pC - pN), N = m(pC-pN)/[pN(2pC-pN)]. Corner: if pC < pN, then N = 0, C = m/pC.
- **Trap:** Must check non-negativity. If pC < pN, the "interior" solution gives negative N, so must go to corner.

**Q3d: Time constraint instead of money; how much time T for utility u*? (12 pts)**
- **Concept tested:** Expenditure function / cost minimization with non-monetary constraint
- **Solution:** Budget: C + N <= T (prices both 1). Bang-per-buck: 1 + N/C = 1 => N = 0. Utility with N=0: C^2 = u* => C = sqrt(u*). So T = sqrt(u*).
- **Trap:** When prices are equal for this utility function, corner solution N=0 emerges. Students who don't check this get stuck.

### Q4: Expected Utility -- Investment with 3 return rates (31 pts)

**Q4a: Write out EU from investing $x (12 pts)**
- **Concept tested:** EU formulation with multiple states
- **Solution:** EU = q*u(100-x) + q*u(100+x) + (1-2q)*u(100+2x). Three states: r=-1 (lose x), r=1 (gain x), r=2 (gain 2x).
- **Trap:** Many students failed to correctly identify final wealth in each state. Must use: final wealth = 100 + x*r for each return rate r. The "sock drawer" portion (100-x) earns zero return.

**Q4b-i: At q=0, invest everything (5 pts)**
- **Concept tested:** Corner solution reasoning
- **Solution:** At q=0, EU = u(100+2x), which is increasing in x. So invest maximum x=100.

**Q4b-ii: For what q is x=0 optimal? (9 pts)**
- **Concept tested:** FOC at boundary, corner solution analysis
- **Solution:** EU'(x) evaluated at x=0: EU'(0) = 2(1-2q)*u'(100). This is zero only at q=1/2. For q < 1/2, EU'(0) > 0, so invest positive amount. Only at q = 1/2 is zero investment optimal.
- **Trap:** Students try to solve FOC = 0 for general x rather than evaluating at x = 0. The question asks WHEN x=0 is optimal, which means checking the sign of EU'(0).

**Q4c: Invest $20 or $80 -- how to decide? (5 pts)**
- **Concept tested:** Comparing EU at discrete options
- **Solution:** Plug x=20 and x=80 into the EU expression. Pick whichever gives higher EU.

---

## SPRING 2024

### Q1: Multiple Choice (40 pts, 4 each)

**MC1: Jake prefers car better in 2 of 3 attributes. Rational?**
- **Concept:** Transitivity (Condorcet paradox)
- **Answer:** C -- Complete (one car always wins 2+ attributes) but intransitive (cycling possible, like voting paradox).
- **Trap:** Opposite of 2023's Jake question. Here preferences ARE complete but NOT transitive. Students must carefully check both properties.

**MC2: Which utility functions might have corner solutions?**
- **Concept:** Corner solutions, concavity
- **Answer:** D -- u = x1 + x2^2 (concave in one variable) and u = x1^2 + x2 (concave in one variable) both can have corners. u = x1^2 * x2 cannot (zero of either good = zero utility).
- **Trap:** Cobb-Douglas with multiplication never has a corner (both goods needed). Additive forms can.

**MC3: u(x1,x2) = x1 * x2^3. Optimal spending?**
- **Concept:** Cobb-Douglas magic rule
- **Answer:** D -- Spends 3/(1+3) = 3/4 of income on good 2, i.e., SPENDS 3 times as much (not BUYS 3 times as much). Option (a) says "buy 3 times as much" which conflates spending with quantity.
- **Trap:** "Spend 3 times as much" != "buy 3 times as much" unless prices are equal. Option (c) says "spend 4 times" which is also wrong (it's 3 times).

**MC4: Apple tax + subsidy (identical to 2023 MC3)**
- **Answer:** A -- Same reasoning as 2023.

**MC5: min{L,R}, pR rises 1->4. Income effect on R?**
- **Concept:** Income effect with perfect complements
- **Answer:** D (-3) -- Total change: R goes from 5 to 2 (drop of 3). With perfect complements, substitution effect = 0, so entire drop is income effect.
- **Trap:** This is the COMPLEMENT to 2023's question which asked for substitution effect (answer: 0). Students must distinguish which effect is being asked for.

**MC6: EU of gamble = 100. What implies risk aversion?**
- **Concept:** Definition of risk aversion: u(E[W]) > EU
- **Answer:** A -- Expected wealth = w0 + 100 - 300p. Risk averse iff u(E[W]) > EU = 100, so u(w0 + 100 - 300p) > 100.
- **Trap:** Must correctly compute expected wealth. Students who confuse E[W] with w0 get the wrong answer.

**MC7: Framing paradox (identical to 2023 MC5)**
- **Answer:** D -- Same reasoning.

**MC8: Risk-averse, what's preferred to 50-50 $0/$200?**
- **Concept:** Mean-preserving contraction
- **Answer:** B, C, D -- $110 (more money, no risk); 50-50 $50/$150 (same EV, less spread); 50-50 $10/$190 (same EV, less spread). NOT $90 (less money, ambiguous).
- **Trap:** $10/$190 IS preferred because it's a mean-preserving contraction of $0/$200. Students think it's "almost as spread out" but mathematically it's strictly less risky with the same EV.

**MC9: Homer, Monday $100, Tuesday $80 (would cost $100 Monday). WARP?**
- **Concept:** WARP with prices
- **Answer:** B -- Monday bundle costs $100, Tuesday bundle also costs $100 at Monday prices => Monday weakly revealed preferred. WARP violated if Tuesday strictly revealed preferred, i.e., Monday bundle costs LESS than $80 at Tuesday prices.
- **Trap:** Direction of inequality. "Strictly revealed preferred" on Tuesday means the Monday bundle was available for less but not chosen.

**MC10: Perfect substitutes, pens cheaper. Which non-negativity constraint binds?**
- **Concept:** Corner solutions with perfect substitutes, Lagrangian
- **Answer:** C -- Buys only pens (cheaper). Non-negativity binds for pencils (would want negative pencils if allowed), non-binding for pens.
- **Trap:** "Binding" means the constraint x >= 0 is active (i.e., x = 0). The constraint on pens is non-binding because she buys positive pens.

### Q2: Expected Utility -- u(w) = w^(1-alpha) (30 pts)

**Q2a: Certainty equivalent for 50-50 $0 or $200 (10 pts)**
- **Concept tested:** Certainty equivalent computation, CRRA
- **Solution:** CE^(1-alpha) = (1/2)*0 + (1/2)*200^(1-alpha). CE = (1/2)^(1/(1-alpha)) * 200. As alpha increases (more risk-averse), CE decreases.
- **Trap:** Must handle the 0^(1-alpha) term carefully. Also, showing the comparative static on alpha requires understanding how the exponent 1/(1-alpha) behaves.

**Q2b: Double-or-nothing asset. Write EU and find optimal x (20 pts)**
- **Concept tested:** Portfolio optimization with binary outcome
- **Solution:**
  - EU = p*(w0+x)^(1-alpha) + (1-p)*(w0-x)^(1-alpha)
  - FOC: p(w0+x)^(-alpha) = (1-p)(w0-x)^(-alpha)
  - Solve: x = [(p/(1-p))^(1/alpha) - 1] / [(p/(1-p))^(1/alpha) + 1] * w0
  - Interior solution requires alpha > 0 and p >= 1/2. If p < 1/2, invest x = 0.
- **Trap:** Must check corners. If alpha <= 0 (risk-loving), invest everything or nothing. If p < 1/2, the FOC gives negative x, so corner x = 0 applies. Many students lost points for not characterizing corners.

### Q3: Demand -- Melsi's intertemporal cookies, u = v(C1) + v(C2) (30 pts)

**Q3a: Budget constraint (5 pts)**
- **Concept tested:** Intertemporal budget constraint
- **Solution:** C2 = 2(w1 - C1), or equivalently 2C1 + C2 = 2w1. "Price" of C1 is 2, "price" of C2 is 1.
- **Trap:** The doubling of savings means the effective price of consuming today is 2 (opportunity cost of not saving).

**Q3b: Are preferences convex? (6 pts)**
- **Concept tested:** Convexity check
- **Solution:** MU1/MU2 = v'(C1)/v'(C2). Since v is concave, v' is decreasing. As C1 rises and C2 falls, v'(C1) falls and v'(C2) rises, so MRS falls. Convex.

**Q3c: Best affordable bundle (9 pts)**
- **Concept tested:** Marshallian demand setup (general)
- **Solution:** Two equations: (1) v'(C1)/v'(C2) = 2 (optimal spending), (2) C2 = 2(w1 - C1) (budget). Cannot solve without knowing v.

**Q3d: v(C) = ln C. Cheapest bundle for utility u*? (10 pts)**
- **Concept tested:** Expenditure minimization / Hicksian demand
- **Solution:** Optimal spending: C2/C1 = 2 => C2 = 2C1. Utility: ln(C1) + ln(C2) = u*. Plug in: ln(C1) + ln(2C1) = u* => 2C1^2 = e^(u*) => C1 = sqrt(e^(u*)/2), C2 = sqrt(2)*e^(u*/2).
- **Trap:** Many students computed Marshallian demand (maximizing utility given income) instead of Hicksian demand (minimizing cost given utility target). This was a major grading deduction.

---

## SPRING 2025

### Multiple Choice (24 pts, 4 each)

**MC1: u = x1^0.2 * x2^0.4. How many units of good 2? (p1=1, p2=2, m=15)**
- **Concept:** Cobb-Douglas magic rule
- **Answer:** C (5) -- Exponent ratio: spend 0.4/(0.2+0.4) = 2/3 of income on good 2. That's $10 on good 2, at $2/unit = 5 units.
- **Trap:** Must normalize exponents to get spending shares. Don't just use the raw exponents.

**MC2: Homer buys $90 Monday, $100 Tuesday (costs $80 at Monday prices). WARP?**
- **Concept:** WARP
- **Answer:** A -- Monday: chose $90 bundle over Tuesday bundle (which cost $80, strictly less). Monday bundle strictly revealed preferred. WARP violated if Tuesday choice also reveals preference for Tuesday bundle, i.e., Monday bundle costs <= $100 at Tuesday prices. Answer A ($100 exactly) works.
- **Trap:** Must get the "weak" vs "strict" right. One revelation must be strict, the other can be weak.

**MC3: u = min{4x1, x2}. Hicksian demand?**
- **Concept:** Hicksian demand with perfect complements
- **Answer:** B -- (u*/4, u*). Set 4x1 = x2 = u* => x1 = u*/4, x2 = u*.
- **Trap:** The coefficient 4 on x1 means x1 is the "more potent" good. To avoid waste: 4x1 = x2. Students who set x1 = x2 get it wrong.

**MC4: Risk-free 10%, risky 20% expected with variance 1/4. Overall std dev = 1/4. Expected return?**
- **Concept:** Portfolio risk/return with risky + risk-free assets
- **Answer:** A (0.15) -- Risky asset std dev = sqrt(1/4) = 1/2. Portfolio std dev = alpha * 1/2 = 1/4 => alpha = 1/2. Expected return = 0.5*10% + 0.5*20% = 15%.
- **Trap:** Must distinguish variance from standard deviation. Variance = 1/4 means std dev = 1/2, not 1/4.

**MC5: u = x1 + 2x2. When is non-negativity on good 1 NON-binding?**
- **Concept:** Perfect substitutes, corner solutions, Lagrangian
- **Answer:** A (p1=2, p2=5) -- Good 1 non-binding means consumer buys good 1, which happens when bang-per-buck of good 1 > good 2: MU1/p1 > MU2/p2 => 1/p1 > 2/p2 => p2 > 2p1. Only A satisfies: 5 > 4.
- **Trap:** Must compare bang-per-buck (MU/p), not just MRS to price ratio. With perfect substitutes, the consumer buys only the good with higher bang-per-buck.

**MC6: u = BT, Cobb-Douglas. Substitution effect when pB rises from $1 to $4?**
- **Concept:** Substitution effect decomposition
- **Answer:** B (-8) -- Original: B=16, T=4 (equal spending: pB*B = pT*T => B=16, T=4). New prices: pB=4, pT=4 => B=T. Compensated: B=T and BT=64 => B=T=8. Sub effect: 8-16 = -8.
- **Trap:** Must find the compensated bundle (same utility, new price ratio) not the new uncompensated bundle.

### SA1: CES Demand (32 pts)

**SA1a: Marshallian demand for CES utility (10 pts)**
- **Concept tested:** CES demand derivation via MRS = price ratio
- **Solution:** MRS = (T/B)^(1/s) = pB/pT. Solve with budget constraint to get B = m / [pB^s * (pB^(1-s) + pT^(1-s))], T = m / [pT^s * (pB^(1-s) + pT^(1-s))].
- **Trap:** Heavy algebra with exponents. The key is that MUB/MUT simplifies to (T/B)^(1/s) because the common X terms cancel.

**SA1b: Show CES demand approaches complements (s->0), substitutes (s->inf), Cobb-Douglas (s->1) (12 pts)**
- **Concept tested:** CES as a nesting family, limit analysis
- **Solution:**
  - s->0: B = T = m/(pB+pT) (perfect complements, B=T)
  - s->1: B = m/(2pB), T = m/(2pT) (Cobb-Douglas equal exponents, spend half on each)
  - s->inf: Spend all on cheaper good (perfect substitutes)
- **Trap:** The s->infinity limit requires careful analysis of (pB/pT)^(s-1) behavior depending on whether pB < or > pT.

**SA1c: Expenditure function limit as s->0 (10 pts)**
- **Concept tested:** Expenditure function, limit analysis, perfect complements intuition
- **Solution:** Plug s=0, u*=1: expenditure = pB*(1 + pT/pB) = pB + pT. This matches perfect complements: need B=T=1, costing pB + pT.

### SA2: Expected Utility -- Risk Aversion (28 pts)

**SA2a-i: Why reject zero-EV bet at any wealth? (5 pts)**
- **Concept tested:** Risk aversion definition
- **Solution:** EV = (1/3)(200) + (2/3)(-100) = 0. Risk-averse DM prefers certainty of $0 change over a zero-EV gamble with risk.

**SA2a-ii: Playing twice is worse than playing once (12 pts)**
- **Concept tested:** Proving EU inequality via weighted sums of concavity conditions
- **Solution:** Inequality (1): u(w0+200) > (1/3)u(w0+400) + (2/3)u(w0+100) [risk aversion applied to gaining $200 for sure vs. risky gain with same EV]. Inequality (2): u(w0-100) > (1/3)u(w0+100) + (2/3)u(w0-200) [same logic for losing $100]. Take (1/3)*(1) + (2/3)*(2) to get EU(play once) > EU(play twice).
- **Trap:** Must identify the correct weights alpha = 1/3 to make the weighted sum match the EU of playing once vs. twice. The probability tree for playing twice has outcomes: +400 (prob 1/9), +100 (prob 4/9), -200 (prob 4/9).

**SA2b: u = ln(w), equal chances win $200 or lose $100. Can poorer DM accept while richer rejects? (11 pts)**
- **Concept tested:** DARA (Decreasing Absolute Risk Aversion) with log utility
- **Solution:** Accept iff (1/2)ln(w0+200) + (1/2)ln(w0-100) > ln(w0). Simplifies to: (w0+200)(w0-100) > w0^2, i.e., 100w0 - 20000 > 0, i.e., w0 > 200. So everyone above $200 accepts. A poorer person who accepts must have w0 > 200, and any wealthier person also has w0 > 200, so NO, it cannot happen.
- **Trap:** The threshold w0 > 200 means acceptance is monotone in wealth. Log utility exhibits DARA, so wealthier people are (weakly) more willing to accept. Students who don't simplify the algebra may not see this clean threshold.

### SA3: Expected Utility -- Optimal Investment with Correlated Assets (26 pts)

**SA3a: Write EU from investing $x in asset 1, $100-x in asset 2 (8 pts)**
- **Concept tested:** EU with state-dependent returns
- **Solution:** EU = (1/3)u(w0 + rA1*x + rA2*(100-x)) + (1/3)u(w0 + 100*rB) + (1/3)u(w0 + rC1*x + rC2*(100-x)).

**SA3b: Show interior optimal x satisfies (rA1-rA2)/(rC2-rC1) = u'(wC)/u'(wA) (12 pts)**
- **Concept tested:** FOC of EU maximization, portfolio optimization
- **Solution:** Differentiate EU w.r.t. x, set to zero. The state B term drops out (no x dependence). Rearranges to the given equation. Corner: if RHS < LHS even at x=100, invest everything in asset 1.

**SA3c: When does DM prefer state C to state A? (6 pts)**
- **Concept tested:** Risk aversion and marginal utility comparison
- **Solution:** Prefer C iff wC > wA. By risk aversion, u' is declining, so wC > wA iff u'(wC) < u'(wA). From (*), this holds iff (rA1-rA2)/(rC2-rC1) < 1, i.e., rA1 - rA2 < rC2 - rC1.
- **Trap:** Must connect the preference for states to the marginal utility comparison via the optimality condition.

---

## 2019 REVIEW SHEET -- Key Topics Covered

The review sheet covers the same core topics but provides the theoretical framework:

1. **Choice theory:** Rationalizability, WARP, IIA, Sen's alpha/beta
2. **Marginal utility and MRS**
3. **Budget line**
4. **MRS vs. price ratio** (the "very important relationship")
5. **Marshallian demand** (3 methods: intuitive, substitution, Lagrangian)
6. **Corner solutions** (concave preferences, binding non-negativity)
7. **Hicksian/compensated demand**
8. **Income effect, substitution effect, compensating variation**
9. **Expenditure function and Shepard's Lemma**
10. **Expected value, variance, standard deviation**
11. **Asset allocation** (portfolio expected return and risk)
12. **Expected utility, risk aversion, certainty equivalent, risk premium**
13. **Normal/inferior, luxury/necessity, Giffen goods** (mentioned but rarely tested on exams)

---

## KEY PATTERNS AND STUDY PRIORITIES

### Absolute Must-Know (tested every single exam):
1. **Marshallian demand derivation** -- Be able to do this for Cobb-Douglas, perfect complements, perfect substitutes, CES, and non-standard utility functions
2. **Setting up an EU expression** -- Read the problem carefully, identify states/probabilities/wealth in each state
3. **Optimizing EU via FOC** -- Differentiate EU w.r.t. choice variable, solve FOC, check corners
4. **Cobb-Douglas magic rule** -- Spending shares = exponent ratios (after normalizing)
5. **Perfect complements** -- Set arguments of min{} equal, substitute into constraint

### High Priority (tested most exams):
6. **WARP** -- Know the definition cold; practice checking revealed preference with price data
7. **Substitution vs. income effect** -- Especially with perfect complements (sub effect = 0)
8. **Certainty equivalent** -- u(CE) = EU, and how it relates to risk premium
9. **Corner solutions / non-negativity** -- When to expect them, how to handle in Lagrangian
10. **Expenditure function / Hicksian demand** -- Know the difference from Marshallian (cost minimization vs. utility maximization)

### Common Traps Across All Exams:
- **Confusing Marshallian and Hicksian demand** (2024 grading note: major deduction)
- **Perfect complements: substitution effect = 0** (students compute total change instead)
- **WARP: getting inequality directions wrong** (which bundle is revealed preferred?)
- **EU setup: wrong wealth levels in each state** (follow the probability tree approach)
- **Corner solutions: forgetting to check non-negativity** (especially with perfect substitutes or when FOC gives negative quantities)
- **Cobb-Douglas: "spend X times as much" vs. "buy X times as much"** (different unless prices equal)
- **Variance vs. standard deviation** in portfolio problems
- **CES/limit problems: careful algebra with exponents**

### Repeated Questions (literally the same or near-identical):
- Apple tax + $5 subsidy: appeared in **both 2023 and 2024**
- Framing paradox (saving lives): appeared in **both 2023 and 2024**
- Risk-averse preference over gambles (50-50 $0/$200): appeared in **both 2023 and 2024**
- Perfect complements sub/income effect: appeared in **2023** (sub effect) and **2024** (income effect)
