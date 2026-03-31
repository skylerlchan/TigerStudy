# Q2a — Stupid Game

---

## Step 0 · What even is a random variable?

A **random variable** is just a number that you don't know yet — because it depends on something random happening.

You give it a letter so you can write math about it before you know what it is.

> Think of it like a blank on a form.
> The blank has a name ("D", "C", "Y") and a list of things it *could* be filled in with.
> The randomness is just: which value actually gets filled in?

---

### How to find your variables — read the problem, circle the unknowns

The problem says:

> *"You roll a die... flip a coin... if heads you tell me the number... if tails you tell me the number times two."*

Read it and ask: **what things are uncertain / could go differently each time?**

```
Thing 1: the die roll        → could be 1, 2, 3, 4, 5, or 6  → call it D
Thing 2: the coin flip       → could be H or T                → call it C
Thing 3: the number reported → depends on D and C             → call it Y
```

That's it. You're just naming the unknowns so you can do math on them.

---

### Why those letters?

No deep reason — D for Die, C for Coin, Y for "the answer we want."
You could call them anything. The math works the same.

---

### What does "uniform on {1,2,3,4,5,6}" mean?

It means each of the 6 values is equally likely:

```
P(D = 1) = 1/6
P(D = 2) = 1/6
...
P(D = 6) = 1/6
```

"Uniform" = every option has the same probability.

---

### Why is Y defined in terms of D and C?

Because Y isn't independent — what you report **depends on** the die AND the coin.
So Y can't be defined without referencing both:

```
if C = Heads → Y = D        (just report the die)
if C = Tails → Y = 2 × D   (report the die doubled)
```

Y is not new randomness — it's a **function** of the randomness that already happened.

---

## Step 1 · Name everything

| Symbol | Meaning |
|--------|---------|
| **D** | die roll — uniform on {1, 2, 3, 4, 5, 6} |
| **C** | coin flip — H or T, each prob 1/2 |
| **Y** | the number you tell me ← this is what we want E[Y] |

---

## Step 2 · Write Y explicitly

```
         D      if coin = Heads
Y =  {
         2D     if coin = Tails
```

---

## Step 3 · Condition on the coin flip

**Law of Total Expectation:**

> **E[Y]  =  E[Y | H] · P(H)  +  E[Y | T] · P(T)**

---

### E[Y | Heads]

the die is just reported as-is, so...

```
= E[D]
= (1 + 2 + 3 + 4 + 5 + 6) / 6
= 21/6
= 7/2
```

---

### E[Y | Tails]

the die is doubled, so...

```
= E[2D]
= 2 · E[D]       ← linearity of expectation
= 2 · (7/2)
= 7
```

---

## Step 4 · Plug in

```
E[Y] = E[Y|H] · P(H)   +   E[Y|T] · P(T)

     = (7/2) · (1/2)   +   7 · (1/2)

     =   7/4            +   14/4

     =   21/4
```

---

## ★ Answer

> ## E[Y] = 21/4 = 5.25

---

## The recipe (reuse this pattern)

```
1.  Define your random variables clearly
           ↓
2.  Write Y as a cases formula  (what are the scenarios?)
           ↓
3.  Pick the variable to condition on
    → pick whichever one makes Y simplest in each case
           ↓
4.  Compute E[Y | each case]
    → use linearity:  E[aX] = a · E[X]
           ↓
5.  Total expectation:
    E[Y] = Σ  E[Y | case_i] · P(case_i)
```
