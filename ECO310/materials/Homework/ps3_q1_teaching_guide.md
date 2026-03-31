# ECO310 Problem Set 3, Question 1 Teaching Guide
## Cost Functions & Monopoly Pricing - Comprehensive Lecture Review

**Date:** March 28, 2026

---

# Table of Contents

1. Overview: What You Need to Know
2. Part 1: Production Functions and Cost Functions (Question 1A)
3. Part 2: Monopoly and Profit Maximization (Question 1B)
4. Additional Concepts: Full Context
5. Common Mistakes and How to Avoid Them
6. Practice Problems
7. Quick Reference: Formulas You Need

---

# 1. Overview: What You Need to Know

This guide covers **two major topics** from Lectures 11 & 12 that you missed:

1. **Question 1A**: Deriving cost functions from production technology
2. **Question 1B**: Monopoly profit maximization

## Big Picture

We're transitioning from **consumer theory** (how consumers make choices) to **producer theory** (how firms make production decisions). This involves:

- Understanding how firms produce goods (production functions)
- How much it costs to produce goods (cost functions)
- How firms price their products (perfect competition vs. monopoly)

---

# 2. Part 1: Production Functions and Cost Functions (Question 1A)

## 2.1 What is a Production Function?

**Definition:** A **production function** shows the relationship between inputs (like labor, capital) and outputs (goods produced).

**General form:** q = f(L, K)

Where:
- q = quantity of output produced
- L = labor input (number of workers or hours)
- K = capital input (machines, equipment)

## 2.2 Common Production Functions You'll See

1. **Linear**: q = aL + bK (constant returns, each input adds constant amount)

2. **Square root**: q = √L or q = 1 + √L (**this is Question 1A!**)

3. **Cobb-Douglas**: q = L^α K^β (most common in economics)

4. **Quadratic**: q = L² or q = K²

## 2.3 From Production to Cost: The Key Steps

### The Process for Deriving Cost Functions

**Step 1:** Start with production function q = f(L, K)

**Step 2:** **Invert** to get input in terms of output
- Solve for L or K as a function of q
- Example: If q = √L, then L = q²

**Step 3:** Multiply by input prices
- If labor costs w per unit: Cost = w · L
- If capital costs r per unit: Cost = r · K
- Total cost: C(q) = wL(q) + rK(q)

**Step 4:** Identify fixed vs. variable costs
- Fixed costs (F): Don't change with q (rent, overhead)
- Variable costs (VC(q)): Change with q (labor, materials)
- C(q) = F + VC(q)

<!-- pagebreak -->

## 2.4 Worked Example: Similar to Question 1A

**Setup:** A firm has production function q = √L where L is labor. Each unit of labor costs w = $4.

**Question:** Find the cost function C(q).

### Solution:

**Step 1:** Production function is q = √L

**Step 2:** Invert to get L in terms of q:
- q = √L
- q² = L (square both sides)

So we need L = q² units of labor to produce q units of output.

**Step 3:** Multiply by wage rate:
- C(q) = w · L
- C(q) = 4 · q²
- C(q) = 4q²

**Answer:** C(q) = 4q²

**Interpretation:** To produce 1 unit costs $4. To produce 2 units costs $16. To produce 3 units costs $36. Costs increase *quadratically* with output!

## 2.5 Important Cost Function Terminology

Once you have C(q), you can derive several important concepts:

### Cost Function Components

1. **Total Cost:** C(q) = F + VC(q)
   - F = fixed costs (constant, independent of q)
   - VC(q) = variable costs (depends on q)

2. **Marginal Cost:** MC(q) = C'(q) = dC/dq
   - Cost of producing one more unit
   - **Key for profit maximization!**

3. **Average Cost:** AC(q) = C(q)/q
   - Cost per unit

4. **Average Variable Cost:** AVC(q) = VC(q)/q
   - Variable cost per unit
   - Important for shutdown decisions (firms shut down if p < min AVC)

<!-- pagebreak -->

## 2.6 Question 1A: Step-by-Step Approach

### Problem 1A

A firm produces output according to q = 1 + √L where q is output and L is labor. Each labor unit costs $2. Find the cost function C(q).

### Your Turn - Follow These Steps:

**Step 1:** Write down the production function
```
q = 1 + √L
```

**Step 2:** Solve for L in terms of q (invert the function)
```
q = 1 + √L
q - 1 = √L          (subtract 1 from both sides)
(q-1)² = L          (square both sides)
```

So L(q) = (q-1)²

**Step 3:** Multiply by wage rate (w = 2)
```
C(q) = w · L(q)
C(q) = 2 · (q-1)²
C(q) = 2(q² - 2q + 1)
C(q) = 2q² - 4q + 2
```

### Answer to 1A

C(q) = 2q² - 4q + 2 or equivalently C(q) = 2(q-1)²

**Components:**
- Fixed cost: F = 2 (the constant term when q = 0, though technically C(0) = 2)
- Variable cost: VC(q) = 2q² - 4q (the part that depends on q)
- Marginal cost: MC(q) = C'(q) = 4q - 4 = 4(q-1)

### ⚠️ Common Mistake

Don't forget to square **both terms** when you have (q-1)²:

✓ **Correct:** (q-1)² = q² - 2q + 1

✗ **Wrong:** (q-1)² = q² - 1 or q² + 1

<!-- pagebreak -->

# 3. Part 2: Monopoly and Profit Maximization (Question 1B)

## 3.1 Perfect Competition vs. Monopoly: The Big Difference

| Feature | Perfect Competition | Monopoly |
|---------|---------------------|----------|
| Number of firms | Many small firms | One firm (the monopolist) |
| Price-taking? | Yes - firms take price as given | No - firm sets price |
| Demand curve | Horizontal (perfectly elastic) at market price p | Downward-sloping market demand P^D(Q) |
| Marginal Revenue | MR = p (constant) | MR = P^D(Q) + Q · dP^D/dQ (decreasing) |
| Profit max | p = MC | MR = MC |

## 3.2 Why Does Market Structure Matter?

### Perfect Competition Example

Imagine you're selling pencils at a farmer's market. There are 100 other vendors selling identical pencils.

- If everyone sells at $1, you must also sell at $1
- If you charge $1.10, nobody buys from you
- You're a **price-taker** - you take the market price as given
- Your revenue from selling q units: R(q) = p · q = 1 · q
- Marginal revenue: MR = dR/dq = 1 (constant!)

### Monopoly Example

Now imagine you're Apple in 2010, the only company selling tablets.

- You control the entire market
- If you want to sell more units, you must **lower the price**
- The market demand curve tells you: at price P, consumers want Q^D(P) units
- You must decide: high price + low quantity, or low price + high quantity?
- Your revenue: R(Q) = P^D(Q) · Q (price depends on quantity!)

<!-- pagebreak -->

## 3.3 Understanding Demand Curves

### Two Ways to Express the Same Relationship

**Demand curve:** Q^D(P) tells you quantity demanded at price P

- Example: Q^D(P) = 200 - 5P
- "At price P = 10, consumers demand Q = 200 - 50 = 150 units"

**Inverse demand curve:** P^D(Q) tells you the price at which you can sell Q units

- Solve for P: Q = 200 - 5P ⟹ 5P = 200 - Q ⟹ P = 40 - Q/5
- Example: P^D(Q) = 40 - Q/5
- "To sell Q = 150 units, you must charge price P = 40 - 30 = 10"

**For monopoly problems, we typically use inverse demand** P^D(Q) because the monopolist chooses quantity Q and the price is determined by the demand curve.

## 3.4 Monopolist's Revenue and Marginal Revenue

### Monopolist's Revenue

**Total Revenue:**
```
R(Q) = P^D(Q) · Q
```

The monopolist sells Q units at price P^D(Q).

### Marginal Revenue

Revenue from selling one more unit:
```
MR(Q) = dR/dQ = d/dQ[P^D(Q) · Q]
```

Using the product rule:
```
MR(Q) = P^D(Q) + Q · dP^D/dQ
```

Since demand is downward-sloping, dP^D/dQ < 0, so:

**MR(Q) < P^D(Q) for a monopolist**

### ⚠️ Critical Insight: Why is MR < P for a monopolist?

When a monopolist sells one more unit:

1. **Gain:** Revenue from selling that unit at price P (+P)
2. **Loss:** To sell more, price must drop, reducing revenue on *all previous units* (-Q · ΔP)

**Example:** If you sell 100 tablets at $500 each (R = $50,000), and to sell 101 tablets you must drop price to $499:

- Gain from 101st tablet: +$499
- Loss on first 100 tablets: -100 × $1 = -$100
- Net marginal revenue: $499 - $100 = $399 < $499 (the price!)

<!-- pagebreak -->

## 3.5 Monopoly Profit Maximization

### The Monopolist's Problem

The monopolist wants to maximize profit:
```
Π(Q) = R(Q) - C(Q) = P^D(Q) · Q - C(Q)
```

**First Order Condition:**
```
dΠ/dQ = 0  ⟹  MR(Q) = MC(Q)
```

### Steps to Solve:

1. Write out profit function: Π(Q) = P^D(Q) · Q - C(Q)
2. Take derivative with respect to Q: dΠ/dQ = MR - MC
3. Set equal to zero: MR = MC
4. Solve for optimal quantity Q*
5. Plug Q* into inverse demand to find price: P* = P^D(Q*)

## 3.6 Calculating Marginal Revenue: The Formula

### MR Formula for Linear Demand

If inverse demand is **linear:** P^D(Q) = a - bQ

Then marginal revenue is: **MR(Q) = a - 2bQ**

**Rule of thumb:** MR has the **same intercept** but **twice the slope** of inverse demand!

**Why?**
```
R(Q) = P^D(Q) · Q = (a - bQ) · Q = aQ - bQ²
MR(Q) = dR/dQ = a - 2bQ
```

### Example: Computing MR

**Inverse demand:** P^D(Q) = 200 - 5Q

**Marginal revenue:**
```
R(Q) = P^D(Q) · Q = (200 - 5Q) · Q = 200Q - 5Q²
MR(Q) = dR/dQ = 200 - 10Q
```

Or use the shortcut: P = 200 - 5Q ⟹ MR = 200 - 10Q (same intercept, double the slope!)

<!-- pagebreak -->

## 3.7 Worked Example: Monopoly Profit Maximization

### Full Monopoly Problem

**Setup:** A monopolist has cost function C(Q) = Q² + 1 and faces inverse demand P^D(Q) = 400 - Q.

**Question:** Find the profit-maximizing quantity and price.

### Solution:

**Step 1:** Write profit function
```
Π(Q) = R(Q) - C(Q)
     = P^D(Q) · Q - C(Q)
     = (400 - Q) · Q - (Q² + 1)
     = 400Q - Q² - Q² - 1
     = 400Q - 2Q² - 1
```

**Step 2:** Find marginal revenue and marginal cost
```
MR(Q) = dR/dQ = d/dQ[(400-Q) · Q] = 400 - 2Q
MC(Q) = dC/dQ = 2Q
```

**Step 3:** Set MR = MC
```
400 - 2Q = 2Q
400 = 4Q
Q* = 100
```

**Step 4:** Find price by plugging into demand
```
P* = P^D(Q*) = 400 - 100 = 300
```

**Answer:** The monopolist sells Q* = 100 units at price P* = $300.

**Profit check:**
```
Π(100) = 300 · 100 - (100² + 1)
       = 30,000 - 10,001
       = 19,999
```

The monopolist makes $19,999 in profit!

<!-- pagebreak -->

## 3.8 Question 1B: Step-by-Step Approach

### Problem 1B

Suppose the firm is a monopolist and faces demand curve Q^D(P) = 200 - 5P. The cost function is C(q) = 2(q-1)² from part (a). How much will the monopolist sell, and at what price?

### Your Turn - Follow These Steps:

**Step 1:** Convert demand to inverse demand
```
Q^D(P) = 200 - 5P
5P = 200 - Q
P^D(Q) = 40 - Q/5
```

**Step 2:** Write profit function
```
Π(Q) = P^D(Q) · Q - C(Q)
     = (40 - Q/5) · Q - 2(Q-1)²
     = 40Q - Q²/5 - 2(Q² - 2Q + 1)
     = 40Q - Q²/5 - 2Q² + 4Q - 2
     = 44Q - Q²/5 - 2Q² - 2
```

Simplify the Q² terms:
```
-Q²/5 - 2Q² = -Q²/5 - 10Q²/5 = -11Q²/5
```

So:
```
Π(Q) = 44Q - 11Q²/5 - 2
```

**Step 3:** Find MR and MC
```
MR(Q) = d/dQ[(40 - Q/5) · Q] = 40 - 2Q/5
MC(Q) = dC/dQ = d/dQ[2(Q-1)²] = 2 · 2(Q-1) = 4(Q-1) = 4Q - 4
```

**Step 4:** Set MR = MC
```
40 - 2Q/5 = 4Q - 4
40 + 4 = 4Q + 2Q/5
44 = 20Q/5 + 2Q/5
44 = 22Q/5
220 = 22Q
Q* = 10
```

**Step 5:** Find price
```
P* = P^D(Q*) = 40 - 10/5 = 40 - 2 = 38
```

### Answer to 1B

Q* = 10 units, P* = $38

The monopolist will produce and sell 10 units at a price of $38 per unit.

**Check:**
- Revenue = 38 × 10 = $380
- Cost = C(10) = 2(10-1)² = 2(81) = $162
- Profit = 380 - 162 = $218

<!-- pagebreak -->

# 4. Additional Concepts: Full Context

## 4.1 Why Do We Care About Market Structure?

### Economic Efficiency

**Perfect competition** leads to efficient outcomes:
- Price = Marginal cost (P = MC)
- Consumer surplus + Producer surplus is maximized
- No deadweight loss

**Monopoly** creates inefficiency:
- Price > Marginal cost (P > MC)
- Monopolist restricts quantity to raise price
- Creates **deadweight loss** (lost welfare)
- Transfers surplus from consumers to the monopolist

## 4.2 Types of Costs: Complete Summary

| Cost Type | Formula | Meaning |
|-----------|---------|---------|
| Total Cost | C(q) = F + VC(q) | Total cost of producing q units |
| Fixed Cost | F | Costs that don't change with output (rent, machines) |
| Variable Cost | VC(q) | Costs that change with output (labor, materials) |
| Marginal Cost | MC(q) = C'(q) | Cost of producing one more unit |
| Average Total Cost | AC(q) = C(q)/q | Cost per unit |
| Average Variable Cost | AVC(q) = VC(q)/q | Variable cost per unit |
| Average Fixed Cost | AFC(q) = F/q | Fixed cost per unit (decreases as q increases) |

## 4.3 Profit Maximization: All Market Structures

### Universal Profit Maximization Rule

**All firms** (competitive or monopolist) maximize profit by producing where:
```
MR(Q) = MC(Q)
```

The difference is **what MR equals**:
- **Perfect competition:** MR = P (constant)
- **Monopoly:** MR = P^D(Q) + Q · dP^D/dQ < P (decreasing)

<!-- pagebreak -->

# 5. Common Mistakes and How to Avoid Them

## Mistake 1: Forgetting to Invert Production Function

### ❌ Don't Do This

**Wrong:** q = 1 + √L ⟹ C(q) = 2(1 + √q)

You can't just replace L with q! You must **solve for L first**.

### ✓ Correct Approach

```
q = 1 + √L  ⟹  L = (q-1)²  ⟹  C(q) = 2(q-1)²
```

## Mistake 2: Using Price Instead of MR for Monopolist

### ❌ Don't Do This

**Wrong:** "Monopolist maximizes profit where P = MC"

This is the **perfect competition** rule! For monopolists, MR ≠ P.

### ✓ Correct Approach

Monopolist maximizes where MR = MC, where:
```
MR = P^D(Q) + Q · dP^D/dQ < P^D(Q)
```

## Mistake 3: Confusing Demand and Inverse Demand

### ❌ Don't Do This

Given Q^D(P) = 200 - 5P:

**Wrong:** "Revenue = (200 - 5P) · P"

This mixes up the variable! If you're using Q as your choice variable (which monopolists do), you need inverse demand.

### ✓ Correct Approach

1. Convert to inverse demand: P^D(Q) = 40 - Q/5
2. Revenue: R(Q) = P^D(Q) · Q = (40 - Q/5) · Q

## Mistake 4: Not Simplifying Before Taking Derivatives

### ❌ Don't Do This

**Wrong:** Taking derivative of Π(Q) = (40 - Q/5) · Q - 2(Q-1)² directly without expanding.

This leads to messy product rule and chain rule applications.

### ✓ Correct Approach

Expand everything first:
```
Π(Q) = 40Q - Q²/5 - 2Q² + 4Q - 2
     = 44Q - 11Q²/5 - 2
```

Now taking the derivative is easy!

<!-- pagebreak -->

# 6. Practice Problems

## Practice Problem 1: Cost Functions

**Problem:** A firm has production function q = 2√L where labor costs $9 per unit. Find C(q).

### Solution Space
```
Step 1: Invert production function

Step 2: Multiply by wage

Answer:
```

## Practice Problem 2: Monopoly

**Problem:** A monopolist has C(Q) = 3Q² and faces demand Q^D(P) = 100 - 2P. Find optimal Q and P.

### Solution Space
```
Step 1: Convert to inverse demand

Step 2: Find MR and MC

Step 3: Set MR = MC and solve

Step 4: Find price

Answer:
```

## Practice Problem 3: Comparing Outcomes

**Problem:** Using the same demand and cost as Practice Problem 2, what would Q and P be under perfect competition?

### Solution Space
```
Perfect competition rule: P = MC

Answer:
```

<!-- pagebreak -->

# Solutions to Practice Problems

## Solution 1

**Given:** q = 2√L, w = 9

**Step 1:** Invert production function
```
q = 2√L
q/2 = √L
(q/2)² = L
L = q²/4
```

**Step 2:** Multiply by wage
```
C(q) = 9 · q²/4 = 9q²/4
```

**Answer:** C(q) = 9q²/4

## Solution 2

**Given:** C(Q) = 3Q², Q^D(P) = 100 - 2P

**Step 1:** Inverse demand
```
Q = 100 - 2P  ⟹  P^D(Q) = 50 - Q/2
```

**Step 2:** Find MR and MC
```
MR = 50 - Q     (double the slope)
MC = 6Q
```

**Step 3:** Set MR = MC
```
50 - Q = 6Q
50 = 7Q
Q* = 50/7 ≈ 7.14
```

**Step 4:** Find price
```
P* = 50 - (50/7)/2 = 50 - 25/7 = 325/7 ≈ 46.43
```

**Answer:** Q* ≈ 7.14 units, P* ≈ $46.43

## Solution 3

**Perfect competition:** Set P = MC

```
P = 50 - Q/2     (from inverse demand)
MC = 6Q
50 - Q/2 = 6Q
50 = 6Q + Q/2 = 13Q/2
Q_pc = 100/13 ≈ 7.69
P_pc = 6 · (100/13) = 600/13 ≈ 46.15
```

**Comparison:**
- Monopoly: Q = 7.14, P = 46.43
- Perfect competition: Q = 7.69, P = 46.15
- Monopolist produces less and charges more!

<!-- pagebreak -->

# 7. Quick Reference: Formulas You Need

## Essential Formulas Cheat Sheet

### Cost Functions
- C(q) = F + VC(q) (total = fixed + variable)
- MC(q) = C'(q) (marginal cost)
- AC(q) = C(q)/q (average cost)

### Revenue
- R(Q) = P · Q (revenue = price × quantity)
- For monopolist: R(Q) = P^D(Q) · Q (price depends on Q!)

### Marginal Revenue
- Perfect competition: MR = P (constant)
- Monopoly: MR = P^D(Q) + Q · dP^D/dQ
- For linear demand P = a - bQ: MR = a - 2bQ

### Profit
- Π(Q) = R(Q) - C(Q)
- Maximize: dΠ/dQ = 0 ⟹ MR = MC

### Inverse Demand
- Given Q^D(P) = a - bP, inverse is P^D(Q) = a/b - Q/b
- Example: Q = 200 - 5P ⟹ P = 40 - Q/5

---

# Final Checklist for Problem Set 3, Question 1

## ✓ Question 1A:
- Invert production function q = 1 + √L to get L = (q-1)²
- Multiply by wage: C(q) = 2(q-1)² = 2q² - 4q + 2
- Check by verifying MC = C'(q) = 4q - 4

## ✓ Question 1B:
- Convert demand to inverse: P^D(Q) = 40 - Q/5
- Find MR: MR = 40 - 2Q/5
- Find MC from part (a): MC = 4Q - 4
- Set MR = MC and solve: Q* = 10
- Find price: P* = 40 - 2 = 38

---

# You're ready to solve the problem!

**Good luck, and remember: take it step by step!**
