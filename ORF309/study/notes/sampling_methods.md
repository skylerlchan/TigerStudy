# Sampling Methods Cheat Sheet

## The Core Question

Every time you pick things from a group, ask yourself two questions:

1. **Does order matter?** (Is 1-2-3 different from 3-2-1?)
2. **Can you pick the same thing twice?** (Replacement?)

Your answers determine which formula to use.

---

## The Four Cases

### 1. Permutations — Order YES, Replacement NO

> You're picking items and **the sequence matters**, and you **can't reuse** items.

**Formula:** `n! / (n-r)!`

**Example:** 12 horses in a race. How many ways can they finish 1st, 2nd, 3rd?

- n = 12, r = 3
- `12! / (12-3)! = 12 × 11 × 10 = 1320`

The horse that wins 1st place can't also come in 2nd. Order matters (gold ≠ silver ≠ bronze).

---

### 2. Combinations — Order NO, Replacement NO

> You're picking a **group**, sequence doesn't matter, and you **can't reuse** items.

**Formula:** `C(n, r) = n! / (r! × (n-r)!)`

**Example:** Pick 6 lottery numbers from 1–49. How many possible tickets?

- n = 49, r = 6
- `C(49, 6) = 13,983,816`

It doesn't matter what order you picked the numbers — if you have the right 6, you win.

---

### 3. Ordered with Replacement — Order YES, Replacement YES

> You're picking a sequence and **can reuse** items.

**Formula:** `n^r`

**Example:** Create a 4-digit PIN from digits 0–9.

- n = 10, r = 4
- `10^4 = 10,000`

You can repeat digits (like 1-1-1-1), and 1-2-3-4 is a different PIN than 4-3-2-1.

---

### 4. Unordered with Replacement — Order NO, Replacement YES

> You're picking a **group**, sequence doesn't matter, and you **can pick the same item multiple times**.

**Formula:** `C(n+r-1, r)`

**Example:** An ice cream shop has 5 flavors. You buy 3 scoops. How many combinations?

- n = 5, r = 3
- `C(5+3-1, 3) = C(7, 3) = 35`

Getting two chocolate + one vanilla is the same as vanilla + two chocolate (order doesn't matter), but you *can* pick the same flavor more than once.

---

## Summary Table

| Method                    | Order? | Replacement? | Formula          | Classic Example      |
|---------------------------|--------|--------------|------------------|----------------------|
| Permutations              | YES    | NO           | n! / (n-r)!      | Race podium          |
| Combinations              | NO     | NO           | C(n, r)          | Lottery ticket       |
| Ordered w/ replacement    | YES    | YES          | n^r              | PIN / password       |
| Unordered w/ replacement  | NO     | YES          | C(n+r-1, r)      | Ice cream scoops     |

---

## Quick Decision Tree

```
Does order matter?
├── YES → Can you reuse items?
│         ├── YES → n^r
│         └── NO  → n! / (n-r)!
└── NO  → Can you reuse items?
          ├── YES → C(n+r-1, r)
          └── NO  → C(n, r)
```
