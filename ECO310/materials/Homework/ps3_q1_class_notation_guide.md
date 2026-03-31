# Problem Set 3, Question 1 - Class Notation Guide

## Your Understanding is CORRECT! ✓

You nailed the setup. Here's how to solve it using the **exact notation from class** (Lectures 10b, 11-12).

---

## Part (a): Finding the Cost Function C(q)

**Given:**
- Production function: q = 1 + √L
- Wage rate: w = $2 per labor unit

**Step 1: Invert the production function** (Lecture 11-12, slide 23)

The class teaches: "use the production function to figure out how many labor units L(q) are needed to produce q output units"

```
q = 1 + √L
√L = q - 1
L(q) = (q - 1)²
```

**Step 2: Calculate the cost** (Lecture 11-12, slide 23)

Since there's no capital (K = 0) and only labor, the cost function is:

```
C(q) = wL(q) = 2(q - 1)²
```

**Class notation used:**
- C(q) = total cost of producing q units
- L(q) = labor needed to produce q units
- w = wage rate

---

## Part (b): Monopoly Problem

**Given:**
- Cost function from part (a): C(Q) = 2(Q - 1)²
- Demand curve: Q^D(P) = 200 - 5P

### Class Notation (Lecture 10b, slides 3-4):

- **Demand curve**: Q^D(P) tells you quantity demanded at price P
- **Inverse demand curve**: P^D(Q) tells you the price at which you can sell Q units

**Key insight:** Monopolists work with the **inverse demand curve** P^D(Q), not the regular demand curve!

### Step 1: Invert the demand curve

From Lecture 10b: to get inverse demand, solve for P as a function of Q:

```
Q^D(P) = 200 - 5P
5P = 200 - Q
P^D(Q) = 40 - Q/5
```

### Step 2: Write the profit function (Lecture 11-12, slide 47)

The monopolist maximizes:

```
Π(Q) = Q · P^D(Q) - C(Q)
     = Q(40 - Q/5) - 2(Q - 1)²
     = 40Q - Q²/5 - 2(Q² - 2Q + 1)
     = 40Q - Q²/5 - 2Q² + 4Q - 2
     = 44Q - Q²/5 - 2Q² - 2
     = 44Q - Q²/5 - 10Q²/5 - 2
     = 44Q - 11Q²/5 - 2
```

### Step 3: First-order condition (Lecture 11-12, slide 48)

Take the derivative and set equal to zero:

```
Π'(Q) = 44 - 22Q/5 = 0
22Q/5 = 44
Q* = 10
```

### Step 4: Find the price (use inverse demand)

```
P* = P^D(Q*) = 40 - 10/5 = 40 - 2 = 38
```

### Step 5: Second-order condition check (Lecture 11-12, slide 49)

```
Π''(Q) = -22/5 < 0 ✓
```

This confirms we found a maximum, not a minimum.

---

## Summary of Class Notation:

| Symbol | Meaning | From Lecture |
|--------|---------|--------------|
| C(q) | Total cost of producing q units | Lec 11-12, slide 7 |
| L(q) | Labor needed to produce q units | Lec 11-12, slide 23 |
| w | Wage rate (price per labor unit) | Lec 11-12, slide 23 |
| Q^D(P) | Demand curve: quantity demanded at price P | Lec 10b, slide 2 |
| P^D(Q) | Inverse demand: price at which Q units sell | Lec 10b, slide 3 |
| Π(Q) | Profit as a function of quantity | Lec 11-12, slide 7 |
| MC(q) | Marginal cost = C'(q) | Lec 11-12, slide 7 |

---

## Final Answer:

**(a)** C(q) = 2(q - 1)²

**(b)** The monopolist will:
- Sell Q* = 10 units
- At price P* = $38 per unit
