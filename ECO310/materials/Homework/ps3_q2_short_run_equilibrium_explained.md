# Problem Set 3, Question 2(a) - Short-Run Equilibrium Explained

## What is Short-Run Equilibrium? (Lecture 11-12, slide 31)

**From the slides:**
> "In equilibrium, demand equals supply. Equilibrium price: the price p at which Q^S(p) = Q^D(p)"
>
> "This is the ONLY requirement for a SR equilibrium"

### In Plain English:

**Short-run equilibrium** is when the market clears:
- **Supply = Demand**
- The number of firms N is **fixed** (firms can't enter or exit in the short run)
- Each firm produces whatever maximizes their profit at the market price

---

## Problem 2(a) Setup:

**Given:**
- Market demand: Q^D(p) = 200 - 5p
- N = 10 firms (fixed in short run)
- Each firm has cost: C(q) = f(N) + αq²
  - For part (a): we're just told N = 10, and α > 0
  - f(N) is a "fixed cost" that depends on how many firms are in the market

**Find:** The short-run equilibrium price

---

## Solution Steps (Following Lecture 11-12, slides 17-21, 29-31):

### Step 1: Find each firm's supply curve

Each **price-taking firm** maximizes profit by producing where **p = MC** (Lecture 11-12, slide 7)

**Cost function:**
```
C(q) = f(N) + αq²
```

**Marginal cost:**
```
MC(q) = dC/dq = 2αq
```

**Each firm's supply curve** (Lecture 11-12, slide 20):
```
p = MC
p = 2αq
q = p/(2α)    ← This is each firm's supply curve q^S(p)
```

### Step 2: Find market supply (Lecture 11-12, slide 29-30)

**From the slides:** "To derive market supply, we add up the individual market supply curves across firms"

With N = 10 firms:
```
Q^S(p) = N × q^S(p) = 10 × p/(2α) = 5p/α
```

### Step 3: Set supply = demand (Lecture 11-12, slide 31)

**Equilibrium condition:**
```
Q^S(p) = Q^D(p)
5p/α = 200 - 5p
5p/α + 5p = 200
5p(1/α + 1) = 200
5p(1 + α)/α = 200
p = 40α/(1 + α)
```

---

## Final Answer:

**Short-run equilibrium price:** p* = 40α/(1 + α)

---

## Key Differences: Short Run vs. Long Run

| **Short Run (SR)** | **Long Run (LR)** |
|-------------------|-------------------|
| Number of firms N is **fixed** | Firms can **enter/exit** |
| Only condition: Supply = Demand | Additional condition: Firms make **zero profit** |
| Firms might make profit or loss | p = min AC (firms break even) |

**From slide 32:** "If firms currently in the market are making money, new firms will come in... if firms are losing money, some will exit"

In the **short run**, we don't worry about profits yet - we just find where supply meets demand with the current number of firms!

---

## Intuition Check:

Think of it like a farmers market:
- **Short run:** There are 10 farmers at the market today (can't change)
- Each farmer decides how much to produce based on the market price
- The price adjusts until the total amount farmers bring = total amount customers want
- Some farmers might make money, some might lose money, but they're stuck there for today

That's short-run equilibrium!
