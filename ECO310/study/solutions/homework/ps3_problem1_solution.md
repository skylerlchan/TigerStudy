# ECO 310 Problem Set 3 - Problem 1 Solution
## Cost Functions and Monopoly

**Due: April 2, 2026**

---

## Part (a): Finding the Cost Function

**Given:**
- Production technology: q = 1 + √L
- Wage rate: w = $2 per labor unit

**Find:** The firm's cost function C(q)

### Solution:

To find the cost function, we need to:
1. Invert the production function to express L as a function of q
2. Multiply by the wage rate

**Step 1: Invert the production function**

Starting with the production function:
```
q = 1 + √L
```

Solving for L:
```
q - 1 = √L
(q - 1)² = L
```

So the labor demand function is: **L(q) = (q - 1)²**

**Step 2: Calculate the cost function**

Since each labor unit costs $2:
```
C(q) = w × L(q)
     = 2(q - 1)²
```

**Domain note:** Since √L ≥ 0, we have q ≥ 1. Notice that when L = 0, the firm produces q = 1 unit (this is like a "free" output from the production technology).

### **Answer: C(q) = 2(q - 1)² for q ≥ 1**

Equivalently, expanding: **C(q) = 2q² - 4q + 2**

---

## Part (b): Monopolist's Optimal Quantity and Price

**Given:**
- The firm is a monopolist
- Demand curve: Q^D(P) = 200 - 5P
- Cost function from part (a): C(q) = 2(q-1)²

**Find:** How much will the monopolist sell, and at what price?

### Solution:

**Step 1: Find the inverse demand curve**

From Q^D(P) = 200 - 5P, solve for P:
```
Q = 200 - 5P
5P = 200 - Q
P(q) = 40 - q/5
```

**Step 2: Write the profit function**

Revenue:
```
R(q) = P(q) × q = (40 - q/5) × q = 40q - q²/5
```

Expanding the cost:
```
C(q) = 2(q - 1)² = 2q² - 4q + 2
```

Profit:
```
π(q) = R(q) - C(q)
     = 40q - q²/5 - 2q² + 4q - 2
     = 44q - q²/5 - 10q²/5 - 2
     = 44q - 11q²/5 - 2
```

**Step 3: Maximize profit (first-order condition)**

```
dπ/dq = 44 - 22q/5 = 0
44 = 22q/5
220 = 22q
q* = 10
```

**Step 4: Find the optimal price**

```
P* = 40 - q*/5 = 40 - 10/5 = 40 - 2 = 38
```

**Verification:**
- Second-order condition: d²π/dq² = -22/5 < 0 ✓ (maximum)
- Demand check: Q^D(38) = 200 - 5(38) = 10 ✓

### **Answer:**
- **Quantity sold: q* = 10 units**
- **Price: P* = $38**

---

## Economic Interpretation

The monopolist restricts output to 10 units (compared to what would occur in perfect competition) and charges $38 per unit. The monopolist earns profit:

```
π* = R(10) - C(10)
   = 40(10) - 100/5 - 2(10-1)²
   = 400 - 20 - 162
   = $218
```

---

**Files:**
- LaTeX source: [_src/ps3_problem1_solution.tex](_src/ps3_problem1_solution.tex)
- This markdown: [ps3_problem1_solution.md](ps3_problem1_solution.md)
