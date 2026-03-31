# Law of Total Expectation

---

## What it says in plain English

> If you don't know E[Y] directly,
> **break the situation into cases**, compute E[Y] in each case,
> then average those results weighted by how likely each case is.

---

## The formula

```
E[Y]  =  E[Y | case 1] · P(case 1)
       +  E[Y | case 2] · P(case 2)
       +  E[Y | case 3] · P(case 3)
       +  ...
```

The cases must be:
- **exhaustive** — they cover every possibility
- **mutually exclusive** — they don't overlap

---

## Why it's true — the proof (simple version)

Let's prove it for the coin + die problem, then generalize.

---

### Setup

Y is a number that depends on the coin C and die D.
The coin is either H or T. Those are the two cases.

E[Y] means: if you played this game infinitely many times and averaged all the Y values, what would you get?

---

### Think about it as a long-run average

```
Out of 1000 games:
    ~500 games: coin = Heads  → Y = D  (die value)
    ~500 games: coin = Tails  → Y = 2D (die doubled)
```

The overall average Y is:

```
E[Y]  =  (sum of all Y values) / 1000

      =  (sum of Y values when H  +  sum of Y values when T) / 1000
```

Split the fraction:

```
      =  (sum of Y when H)/1000   +   (sum of Y when T)/1000
```

Multiply top and bottom of each piece by 500:

```
      =  (sum of Y when H)/500  · (500/1000)
       + (sum of Y when T)/500  · (500/1000)
```

But `(sum of Y when H)/500` = average of Y when H = **E[Y | H]**
And `500/1000 = 1/2 = P(H)`

So:

```
E[Y]  =  E[Y | H] · P(H)  +  E[Y | T] · P(T)
```

That's the law. The proof is just: split a big average into group averages, weighted by group size.

---

### General proof (any cases C1, C2, ..., Cn)

```
E[Y]  =  sum over ALL outcomes of  [Y(outcome) · P(outcome)]

       =  sum over cases Ci of
               sum over outcomes in Ci of  [Y(outcome) · P(outcome)]

       =  sum over cases Ci of
               P(Ci) · sum over outcomes in Ci of  [Y(outcome) · P(outcome|Ci)]

       =  sum over cases Ci of   E[Y | Ci] · P(Ci)
```

The key step: inside each case, `P(outcome) = P(Ci) · P(outcome | Ci)`
(that's just the definition of conditional probability)

---

## How it's actually used — the pattern

You use it when Y is **hard to compute directly** but **easy to compute given some extra info**.

```
Ask yourself: "Is there something, that if I knew it,
               would make Y easy to calculate?"
                        ↓
If yes → that thing is your conditioning variable
                        ↓
Split into cases based on that variable
Compute E[Y | each case]
Weight by probabilities
Add up
```

---

## Example: Q2a

Y = number reported. Hard to get E[Y] directly because Y depends on two things.

> "If I knew the coin outcome, Y would be easy."
> → condition on C (the coin)

```
E[Y | Heads] = E[D]   = 7/2     (easy — just the die average)
E[Y | Tails] = E[2D]  = 7       (easy — just double the die average)

E[Y] = (7/2)(1/2)  +  7(1/2)  =  21/4
```

---

## Another example to build intuition

> You pick a bag at random: bag A or bag B (50/50).
> Bag A has balls labeled 1, 2, 3.
> Bag B has balls labeled 10, 20.
> You draw one ball. What is E[ball value]?

Direct calculation is messy. But:

```
E[value | bag A] = (1+2+3)/3 = 2
E[value | bag B] = (10+20)/2 = 15

E[value] = 2 · P(A)  +  15 · P(B)
         = 2 · (1/2) + 15 · (1/2)
         = 1 + 7.5
         = 8.5
```

Same structure every time.

---

## Summary

| Question | Answer |
|----------|--------|
| What does it do? | Splits E[Y] into cases |
| When do you use it? | When Y is complex but simple given extra info |
| What are the cases? | Whatever variable makes Y easiest to work with |
| What's the formula? | E[Y] = sum of E[Y given case] · P(case) |
| Why is it true? | A big average = weighted sum of group averages |
