# Bayes' Formula
*(from Slides03, pp. 12-19)*

---

## The one-line idea

> You know P(B|A) — the easy direction.
> Bayes flips it to give you P(A|B) — the direction you actually want.

---

## First: what is conditional probability?

> P(A | B) = "probability that A happens, **given that B already happened**"

The formula:

```
P(A | B)  =  P(A ∩ B) / P(B)
```

In words: out of all the times B happens, what fraction of those also have A?

---

## The Bayes Formula (derived step by step)

**Start from the definition of conditional probability — written two ways:**

```
P(A | B) = P(A ∩ B) / P(B)     ... (i)
P(B | A) = P(A ∩ B) / P(A)     ... (ii)
```

Both have P(A ∩ B) in the numerator.

**Set them equal:**

```
From (ii):   P(A ∩ B)  =  P(B|A) · P(A)

Plug into (i):

         P(A|B)  =  P(A) · P(B|A)
                    ---------------
                         P(B)
```

**That's Bayes' formula.**

---

## But what is P(B)?

Usually you don't know P(B) directly. Use the **total probability rule** to expand it:

```
P(B)  =  P(B ∩ A)  +  P(B ∩ A^c)

      =  P(B|A) · P(A)   +   P(B|A^c) · P(A^c)
```

(Split into: B happening when A is true, plus B happening when A is false)

---

## Full Bayes Formula (the version you use)

```
                    P(A) · P(B|A)
P(A|B)  =  ─────────────────────────────────────
             P(B|A)·P(A)  +  P(B|A^c)·P(A^c)
```

---

## The COVID example from the slides

**Setup:**
```
P(test positive | sick)      = 0.95   ← sensitivity
P(test positive | not sick)  = 0.02   ← false positive rate
P(sick)                      = 1/1000 ← disease is rare
```

**Question:** given that you test positive, what is P(actually sick)?

---

**Step 1 — name the events:**

```
S = event that person is sick
Q = event that test is positive
```

**Step 2 — identify what you know vs. want:**

```
Know:    P(S),  P(Q|S),  P(Q|S^c)
Want:    P(S|Q)
```

**Step 3 — apply Bayes:**

```
                   P(S) · P(Q|S)
P(S|Q)  =  ─────────────────────────────────────
             P(Q|S)·P(S)  +  P(Q|S^c)·P(S^c)
```

**Step 4 — plug in numbers:**

```
P(S^c)  =  1 - 1/1000  =  999/1000

Numerator:    0.001 × 0.95  =  0.00095

Denominator:  (0.95 × 0.001)  +  (0.02 × 0.999)
           =  0.00095  +  0.01998
           =  0.02093

P(S|Q)  =  0.00095 / 0.02093  ≈  4.5%
```

---

## The surprising result

> Only ~4.5% of people who test positive are actually sick.
> The test has 95% sensitivity — yet it's nearly useless for rare diseases.

**Why?**

The disease is rare (P(S) = 0.001).
The false positive rate (2%) seems small — but because almost everyone is healthy,
the false positives vastly outnumber the true positives.

```
Out of 1000 people:
    ~1 is sick          → test catches 0.95 of them   ≈ 1 true positive
    ~999 are healthy    → test falsely flags 2%        ≈ 20 false positives

So out of ~21 positives, only ~1 is real.
That's 1/21 ≈ 4.8%
```

---

## When to use Bayes

```
You want P(cause | effect)
but you know P(effect | cause)
             ↓
Use Bayes to flip the direction
```

| You know | You want |
|----------|----------|
| P(positive test given sick) | P(sick given positive test) |
| P(coin = Heads given you reported 6) | P(you reported 6 given Heads) |
| P(data given hypothesis) | P(hypothesis given data) |

---

## The recipe

```
1. Name your events clearly (what is A? what is B?)
         ↓
2. Write down what you know: P(A), P(B|A), P(B|A^c)
         ↓
3. Compute P(B) using total probability:
   P(B) = P(B|A)·P(A) + P(B|A^c)·P(A^c)
         ↓
4. Apply Bayes:
   P(A|B) = P(A)·P(B|A) / P(B)
```
