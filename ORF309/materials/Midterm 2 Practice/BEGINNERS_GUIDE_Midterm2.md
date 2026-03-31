# ORF309 Midterm 2 - Complete Beginner's Guide
## Learning Everything From Scratch

**For:** Students learning this material for the first time
**Style:** Simple explanations, lots of examples, step-by-step

---

## Part 1: POISSON PROCESSES (The Most Important Topic!)

### What's the Big Idea?

Imagine you're sitting at a coffee shop watching customers walk in. Sometimes 3 people come in 5 minutes, sometimes nobody comes for 10 minutes. It seems random, right? **Poisson processes** are a mathematical way to model these random arrivals.

### The Basic Setup

A **Poisson process** is when:
- Events (like customers arriving) happen randomly over time
- Events happen at some average rate (like "2 customers per minute on average")
- Each event is independent (one customer arriving doesn't affect when the next one arrives)

**Example:** Starbucks gets an average of 3 customers per minute.

### The Math (Don't Panic!)

If customers arrive at rate λ = 3 per minute, then:
- The **expected** number of customers in time t is: **λt**
- In 5 minutes, you'd expect: 3 × 5 = 15 customers

**The probability of exactly k arrivals in time t:**
```
P(N(t) = k) = (λt)^k · e^(-λt) / k!
```

Don't memorize this yet! Just understand: there's a formula to calculate the probability of getting exactly k events.

### Real Example

**Question:** At Starbucks (λ = 3 per minute), what's the expected number of customers in 10 minutes?

**Answer:** E[N(10)] = λt = 3 × 10 = **30 customers**

---

### THINNING: The Game-Changer 🔥

This is the **#1 most tested concept** on Midterm 2. Let me explain it super clearly.

#### The Scenario

Imagine customers arrive at Starbucks at rate 3 per minute. But not everyone orders the same thing:
- 40% order coffee
- 30% order tea
- 30% order food

**Question:** How often do coffee orders happen?

#### The Intuition

If 3 customers arrive per minute, and 40% of them order coffee:
- Coffee orders happen at rate: 3 × 0.4 = **1.2 per minute**

That's thinning! You "thin out" the arrival process by the probability.

#### The Formal Statement

If arrivals happen at rate λ, and each arrival is "type A" with probability p, then:
```
Type A arrivals form a Poisson process with rate λp
```

#### Practice Example

**Q:** Emails arrive at your inbox at rate 20 per hour. 15% are important. What's the rate of important emails?

**A:** λ_important = 20 × 0.15 = **3 per hour**

So important emails arrive as a Poisson(3 per hour) process!

---

### COMPETING PROCESSES: Which Happens First?

#### The Scenario

You're waiting for either:
- Your Uber (arrives at rate λ_Uber = 1 per 10 min = 0.1 per min)
- The bus (arrives at rate λ_bus = 1 per 15 min ≈ 0.067 per min)

Whichever comes first, you'll take it.

#### The Question

What's the probability your Uber arrives before the bus?

#### The Answer

```
P(Uber first) = λ_Uber / (λ_Uber + λ_bus)
               = 0.1 / (0.1 + 0.067)
               = 0.1 / 0.167
               ≈ 0.60 = 60%
```

**General Formula:**
```
P(A before B) = λ_A / (λ_A + λ_B)
```

#### How Long Until Something Happens?

Expected time until *either* arrives:
```
E[time] = 1 / (λ_A + λ_B)
        = 1 / (0.1 + 0.067)
        = 1 / 0.167
        ≈ 6 minutes
```

---

### CONDITIONAL EXPECTATION: Given Something Happened

This sounds complicated but it's actually simple!

#### The Scenario

Customers arrive at rate λ = 2 per minute. You check your watch and see that exactly 10 customers arrived.

**Question:** How much time passed?

#### The Intuition

If customers arrive at rate 2 per minute, then:
- 10 customers should take: 10 / 2 = **5 minutes**

#### The Formula

```
E[Time | N(T) = n] = n / λ
```

Where:
- n = number of arrivals that happened
- λ = arrival rate

#### Practice Example

**Q:** Texts arrive at rate 5 per hour. Given that exactly 20 texts arrived, what's the expected time?

**A:** E[T | N = 20] = 20 / 5 = **4 hours**

---

### POISSON CHEAT SHEET

**Basic Facts:**
- Arrivals at rate λ → Expected number in time t is λt
- Thinning: If arrivals are λ and p% are type A → Type A is Poisson(λp)
- Competing: P(A before B) = λ_A / (λ_A + λ_B)
- Conditional: E[T | n arrivals] = n / λ

**When to Use What:**
- See "types of customers/events"? → Use THINNING
- See "which happens first"? → Use COMPETING PROCESSES
- See "given that n events happened"? → Use CONDITIONAL EXPECTATION

---

## Part 2: RANDOM WALKS & FIRST-STEP ANALYSIS

### What's a Random Walk?

Imagine you're playing a game:
- You start with $50
- You flip a coin each round
- Heads: you win $1
- Tails: you lose $1
- Game ends when you hit $0 (bankrupt) or $100 (rich!)

Your money goes up and down randomly - that's a **random walk**!

### The Setup

- **States:** Different positions (like $0, $1, $2, ..., $100)
- **Barriers:** Boundaries where the game ends (like $0 and $100)
- **Starting position:** Where you begin (like $50)
- **Transition probabilities:** Chances of moving (like 50% up, 50% down)

### The Two Main Questions

1. **What's the probability I reach $100 before $0?**
   → This is asking for the "hitting probability"

2. **How long will the game take on average?**
   → This is asking for the "expected hitting time"

---

### FIRST-STEP ANALYSIS: The Magic Technique

This is the **key method** for solving random walk problems. Let me explain it simply.

#### The Idea

To figure out what happens starting from position i, think about:
- What happens on the **first step**?
- Then use what you know about the **next position**

It's like saying: "If I'm at $50, I'll be at either $51 or $49 after one flip. So my chances of reaching $100 depend on my chances from those positions."

---

### Finding HITTING PROBABILITIES

Let's say p(i) = probability of reaching the upper barrier starting from position i.

#### The First-Step Formula

```
p(i) = (prob of moving up) × p(i+1) + (prob of moving down) × p(i-1)
```

#### Example: Simple Coin Flip Game

- Start at position 2 (out of 0, 1, 2, 3, 4)
- Each round: 50% chance move up, 50% chance move down
- Win at 4, lose at 0

**What's the probability of winning starting from position 2?**

**Step 1:** Set up boundary conditions
```
p(0) = 0  (if you're at 0, you already lost - 0% chance of winning)
p(4) = 1  (if you're at 4, you already won - 100% chance)
```

**Step 2:** Write first-step equations for middle positions

From position 1:
```
p(1) = 0.5 × p(2) + 0.5 × p(0)
p(1) = 0.5 × p(2) + 0.5 × 0
p(1) = 0.5 × p(2)
```

From position 2:
```
p(2) = 0.5 × p(3) + 0.5 × p(1)
```

From position 3:
```
p(3) = 0.5 × p(4) + 0.5 × p(2)
p(3) = 0.5 × 1 + 0.5 × p(2)
p(3) = 0.5 + 0.5 × p(2)
```

**Step 3:** Solve the system

From position 1: p(1) = 0.5p(2)
From position 3: p(3) = 0.5 + 0.5p(2)

Substitute into position 2:
```
p(2) = 0.5 × p(3) + 0.5 × p(1)
p(2) = 0.5 × (0.5 + 0.5p(2)) + 0.5 × (0.5p(2))
p(2) = 0.25 + 0.25p(2) + 0.25p(2)
p(2) = 0.25 + 0.5p(2)
0.5p(2) = 0.25
p(2) = 0.5
```

**Answer: 50% chance of winning starting from position 2**

For a symmetric random walk, there's actually a shortcut:
```
p(i) = i / (upper barrier)
p(2) = 2/4 = 0.5 ✓
```

---

### Finding EXPECTED TIME

Now let's find how long the game takes on average.

Let μ(i) = expected number of rounds starting from position i.

#### The First-Step Formula (IMPORTANT!)

```
μ(i) = 1 + (prob of moving up) × μ(i+1) + (prob of moving down) × μ(i-1)
```

**DON'T FORGET THE "+1"!** This is the most common mistake. The "+1" represents the current round.

#### Example: Same Game

Starting from position 2, how many rounds on average?

**Step 1:** Boundaries
```
μ(0) = 0  (game is over)
μ(4) = 0  (game is over)
```

**Step 2:** First-step equations

From position 1:
```
μ(1) = 1 + 0.5 × μ(2) + 0.5 × μ(0)
μ(1) = 1 + 0.5μ(2)
```

From position 2:
```
μ(2) = 1 + 0.5 × μ(3) + 0.5 × μ(1)
```

From position 3:
```
μ(3) = 1 + 0.5 × μ(4) + 0.5 × μ(2)
μ(3) = 1 + 0.5μ(2)
```

**Step 3:** Notice μ(1) = μ(3) by symmetry

```
μ(1) = 1 + 0.5μ(2)
μ(3) = 1 + 0.5μ(2)

So: μ(2) = 1 + 0.5μ(3) + 0.5μ(1)
         = 1 + 0.5(1 + 0.5μ(2)) + 0.5(1 + 0.5μ(2))
         = 1 + 0.5 + 0.25μ(2) + 0.5 + 0.25μ(2)
         = 2 + 0.5μ(2)

0.5μ(2) = 2
μ(2) = 4
```

**Answer: Takes 4 rounds on average**

For symmetric walk, the shortcut is:
```
μ(i) = i × (upper barrier - i)
μ(2) = 2 × (4-2) = 2 × 2 = 4 ✓
```

---

### RANDOM WALK CHEAT SHEET

**First-Step Analysis Templates:**

For hitting probability p(i):
```
p(i) = p_up × p(i+1) + p_down × p(i-1) + p_stay × p(i)
Boundaries: p(lower) = 0, p(upper) = 1
```

For expected time μ(i):
```
μ(i) = 1 + p_up × μ(i+1) + p_down × μ(i-1) + p_stay × μ(i)
Boundaries: μ(lower) = 0, μ(upper) = 0
DON'T FORGET THE "+1"!
```

**Symmetric Walk Shortcuts** (when prob up = prob down = 0.5):
```
p(i) = (i - lower) / (upper - lower)
μ(i) = (i - lower) × (upper - i)
```

---

## Part 3: JOINT & CONDITIONAL DENSITIES

### What's This About?

So far we've dealt with single random variables (like X = "arrival time"). But often we have **two** random variables that are related:
- X = total bill amount
- Y = amount you pay (some fraction of X)

We need to understand how they relate!

### Continuous Random Variables Review

A **continuous random variable** can take any value in a range (like any number between 0 and 10).

We describe it with a **PDF (probability density function)** f(x).

**Key facts:**
- Area under the PDF = probability
- Total area = 1 (something has to happen!)
- P(a < X < b) = ∫[a to b] f(x) dx

---

### Joint PDF: Two Variables Together

The **joint PDF** f_{X,Y}(x,y) describes two random variables together.

Think of it like a heat map: dark areas = high probability, light areas = low probability.

**Key property:**
```
∫∫ f_{X,Y}(x,y) dx dy = 1
```
(Total probability = 1)

---

### Marginal PDF: One Variable Alone

If you have the joint PDF but only care about X (ignoring Y), you get the **marginal PDF**:

```
f_X(x) = ∫ f_{X,Y}(x,y) dy
```

You're "integrating out" Y (summing over all possible values of Y).

**Analogy:** Imagine a table of (height, weight) data. The marginal distribution of height ignores weight - it just shows the distribution of heights.

---

### Conditional PDF: One Given the Other

**Conditional PDF** f_{X|Y}(x|y) means: "What does X look like if I know Y = y?"

Formula:
```
f_{X|Y}(x|y) = f_{X,Y}(x,y) / f_Y(y)
```

#### Example: Bill Payment

- X = total restaurant bill (say, exponentially distributed with mean $50)
- U = fraction you pay, Uniform[0,1] (your friend covers the rest randomly)
- Y = UX = amount you pay

**Question:** Given X = 100, what's the distribution of Y?

**Answer:**
- Given X = 100, Y = U × 100
- U is uniform on [0,1]
- So Y is uniform on [0, 100]
- f_{Y|X}(y|100) = 1/100 for 0 < y < 100

---

### Law of Total Expectation (SUPER USEFUL!)

This is one of the most powerful tools.

**The idea:** To find E[Y], you can:
1. First find E[Y | X = x] for each value of x
2. Then average those over all x values

**Formula:**
```
E[Y] = E[E[Y|X]]
```

Or in integral form:
```
E[Y] = ∫ E[Y|X=x] × f_X(x) dx
```

#### Example: Bill Payment (continued)

X ~ Exp(λ), Y = UX where U ~ Uniform[0,1]

**Find E[Y]:**

Step 1: Find E[Y | X = x]
```
Given X = x, Y = Ux is uniform on [0, x]
E[Y | X = x] = x/2  (average of uniform [0,x])
```

Step 2: Average over X
```
E[Y] = E[E[Y|X]]
     = E[X/2]
     = (1/2) E[X]
     = (1/2) × (1/λ)
     = 1/(2λ)
```

**Answer: E[Y] = 1/(2λ)** - you pay half the expected bill on average!

---

### Building Joint PDF from Conditional

Often you're given:
- The marginal f_X(x)
- The conditional f_{Y|X}(y|x)

To get the joint:
```
f_{X,Y}(x,y) = f_{Y|X}(y|x) × f_X(x)
```

#### Example Problem (EXAM STYLE!)

- X = loss amount, with P(X > x) = 1/x² for x ≥ 1
- U ~ Uniform[0,1], independent of X
- Y = UX = amount you pay

**Find joint PDF of (X,Y):**

Step 1: Find f_X(x)
```
P(X > x) = 1/x²
F_X(x) = 1 - 1/x² for x ≥ 1
f_X(x) = dF/dx = 2/x³ for x ≥ 1
```

Step 2: Find f_{Y|X}(y|x)
```
Given X = x, Y = Ux is uniform on [0, x]
f_{Y|X}(y|x) = 1/x for 0 < y < x
```

Step 3: Combine
```
f_{X,Y}(x,y) = f_{Y|X}(y|x) × f_X(x)
             = (1/x) × (2/x³)
             = 2/x⁴ for 0 < y < x, x ≥ 1
```

**IMPORTANT:** Always specify the range! Here it's "0 < y < x, x ≥ 1"

---

### JOINT DENSITY CHEAT SHEET

**Key Relationships:**
```
Joint to Marginal:
f_X(x) = ∫ f_{X,Y}(x,y) dy

Conditional:
f_{X|Y}(x|y) = f_{X,Y}(x,y) / f_Y(y)

Building Joint:
f_{X,Y}(x,y) = f_{Y|X}(y|x) × f_X(x)

Law of Total Expectation:
E[Y] = E[E[Y|X]]
```

**Problem-Solving Steps:**
1. Identify what's given (marginal? conditional?)
2. Find what you need using formulas above
3. **Always specify the range where f > 0!**
4. Check: does it integrate to 1?

---

## Part 4: EXPONENTIAL DISTRIBUTION

### What Is It?

Exponential distribution models **waiting times**.

Examples:
- Time until next customer arrives
- Time until a light bulb burns out
- Time until your phone gets a text

**Key parameter:** λ = rate (like "2 customers per minute")

### The PDF

```
f(t) = λe^(-λt) for t > 0
```

Looks like an exponentially decaying curve (starts high, drops fast).

### Important Facts

```
Mean: E[T] = 1/λ
Variance: Var(T) = 1/λ²
P(T > t) = e^(-λt)
```

**Common mistake:** Mixing up λ and 1/λ!
- If λ = 2 per minute, then E[T] = 1/2 = 0.5 minutes

---

### Memoryless Property (SUPER IMPORTANT!)

This is the most important property of exponential distribution.

**Statement:**
```
P(T > s + t | T > s) = P(T > t)
```

**What does this mean?**

If you've already waited s minutes, the probability you have to wait t more minutes is the same as if you hadn't waited at all!

#### Example

You're waiting for a bus. Buses arrive exponentially with rate λ = 1/10 min⁻¹ (average 10 min between buses).

You've already waited 5 minutes. What's the probability you have to wait 5 more minutes?

**Answer:** Same as the probability from the start: P(T > 5) = e^(-5/10) = e^(-0.5) ≈ 0.606

The bus "doesn't remember" you've been waiting!

**Key fact:** Exponential is the ONLY continuous distribution with this property!

---

### Minimum of Exponentials

This connects to competing Poisson processes!

If T₁ ~ Exp(λ₁) and T₂ ~ Exp(λ₂) are independent:

```
min(T₁, T₂) ~ Exp(λ₁ + λ₂)
P(T₁ < T₂) = λ₁ / (λ₁ + λ₂)
```

#### Example

- Time until Uber arrives: T₁ ~ Exp(0.1 per min) = Exp(6 per hour)
- Time until bus arrives: T₂ ~ Exp(4 per hour)

**What's the distribution of whichever comes first?**

```
min(T₁, T₂) ~ Exp(6 + 4) = Exp(10 per hour)
E[min] = 1/10 hour = 6 minutes
```

**Which is more likely to arrive first?**

```
P(Uber first) = 6/(6+4) = 6/10 = 60%
P(Bus first) = 4/(6+4) = 4/10 = 40%
```

---

### Maximum of Exponentials

Less common but still shows up.

```
E[max(T₁, T₂)] = 1/λ₁ + 1/λ₂ - 1/(λ₁+λ₂)
```

No simple form for the full distribution!

#### Example (Exam-Style)

Two processes: rising time (mean 8 hours) and proofing time (mean 4 hours), happening simultaneously.

What's the expected time until both are done (i.e., the max)?

```
λ₁ = 1/8, λ₂ = 1/4
E[max] = 8 + 4 - 1/(1/8 + 1/4)
       = 12 - 1/(3/8)
       = 12 - 8/3
       = 12 - 2.67
       ≈ 9.33 hours
```

---

### EXPONENTIAL CHEAT SHEET

```
T ~ Exp(λ):
- PDF: f(t) = λe^(-λt)
- Mean: E[T] = 1/λ  (NOT λ!)
- P(T > t) = e^(-λt)
- Memoryless: P(T > s+t | T > s) = P(T > t)

Min of exponentials:
- min(T₁, T₂) ~ Exp(λ₁ + λ₂)
- P(T₁ < T₂) = λ₁/(λ₁ + λ₂)

Max of exponentials:
- E[max(T₁, T₂)] = 1/λ₁ + 1/λ₂ - 1/(λ₁+λ₂)
```

---

## Part 5: BROWNIAN MOTION (Optional but appears more recently!)

### What Is It?

Brownian motion B(t) models **continuous random movement**.

Think of:
- A particle jiggling around in water
- Stock prices moving up and down
- Position of a drunk person walking randomly

It's like a random walk, but in continuous time with tiny steps.

---

### Standard Brownian Motion Definition

B(t) is **standard Brownian motion** if:

1. B(0) = 0 (starts at origin)
2. B(t) - B(s) ~ Normal(0, t-s) for t > s (increments are normal)
3. Independent increments (future doesn't depend on past, given present)
4. Continuous paths (no jumps)

---

### Key Properties

```
E[B(t)] = 0  (expected position is still at origin)
Var(B(t)) = t  (variance grows with time)
B(t) ~ Normal(0, t)

E[B(t)²] = t  (since Var = E[X²] - (E[X])² = E[X²])
```

**Intuition:** The longer you wait, the farther away you'll drift (on average), but you're equally likely to be above or below 0.

---

### Conditional Properties

For t > s:

```
E[B(t) | B(s) = x] = x
E[B(t)² | B(s) = x] = x² + (t-s)
```

**Intuition:** If you're at position x at time s, your expected position at time t is still x, but you'll have drifted around.

---

### Applications

**Geometric Brownian Motion** (Stock prices):
```
S(t) = S₀ × e^(B(t))
```

The stock price is always positive (since e^x > 0) and moves randomly.

#### Example Problem

Stock price S(t) = e^(B(t)), starting at S(0) = 1.

**What's the probability that S(2) ≥ S(1)²?**

```
S(2) ≥ S(1)²
e^(B(2)) ≥ (e^(B(1)))²
e^(B(2)) ≥ e^(2B(1))
B(2) ≥ 2B(1)
B(2) - 2B(1) ≥ 0
```

Now, B(2) - 2B(1) = [B(2) - B(1)] - B(1) ~ Normal(?, ?)

Need to find mean and variance:
- B(2) - B(1) ~ Normal(0, 1), independent of B(1)
- B(1) ~ Normal(0, 1)
- So B(2) - 2B(1) ~ Normal(0, 1 + 1) = Normal(0, 2)

```
P(B(2) - 2B(1) ≥ 0) = P(Z ≥ 0) where Z ~ Normal(0, 1) = 0.5
```

**Answer: 50%**

---

### BROWNIAN MOTION CHEAT SHEET

```
Standard BM B(t):
- B(0) = 0
- E[B(t)] = 0
- Var(B(t)) = t
- B(t) ~ N(0, t)
- B(t) - B(s) ~ N(0, t-s) for t > s

Conditional:
- E[B(t) | B(s) = x] = x
- E[B(t)² | B(s) = x] = x² + (t-s)

Geometric BM:
- S(t) = S₀e^(B(t)) (stock prices)
```

---

## PUTTING IT ALL TOGETHER: Pattern Recognition

When you see a problem, ask yourself:

### 1. Is it about ARRIVALS/EVENTS over time?
- Keywords: "customers arrive", "events happen", "rate of"
- → Use **POISSON PROCESSES**
- Sub-questions:
  - Different types? → **THINNING**
  - Which happens first? → **COMPETING**
  - Given n arrivals? → **CONDITIONAL EXPECTATION**

### 2. Is it about a WALK/GAME with states?
- Keywords: "position", "move up/down", "reaching", "game ends at"
- → Use **RANDOM WALK** with **FIRST-STEP ANALYSIS**
- Sub-questions:
  - Probability of reaching? → Set up p(i) equations
  - Expected time? → Set up μ(i) equations (DON'T FORGET +1!)

### 3. Is it about TWO RELATED random variables?
- Keywords: "joint", "given X", "conditional", "Y depends on X"
- → Use **JOINT/CONDITIONAL DENSITIES**
- Sub-questions:
  - Find joint PDF? → f(x,y) = f(y|x) × f_X(x)
  - Find expectation? → Use **LAW OF TOTAL EXPECTATION**
  - Always specify the **RANGE**!

### 4. Is it about WAITING TIMES?
- Keywords: "time until", "waiting time", "lifetime"
- → Usually **EXPONENTIAL**
- Sub-questions:
  - Min of waiting times? → Sum the rates
  - Which happens first? → λ₁/(λ₁+λ₂)

### 5. Is it about CONTINUOUS RANDOM MOVEMENT?
- Keywords: "Brownian motion", "B(t)", "stock price"
- → Use **BROWNIAN MOTION** properties
- Key facts: E[B(t)] = 0, Var(B(t)) = t

---

## STUDY PLAN FOR COMPLETE BEGINNERS

### Day 1: Master Poisson (8 hours)

**Morning (4 hours):**
1. Read the Poisson section above slowly (2 hours)
2. Make your own examples for thinning (1 hour)
3. Do practice problems from slides 16-19 (1 hour)

**Afternoon (4 hours):**
1. Try F2025 Q3 yourself (30 min)
2. Check solution, understand each step (30 min)
3. Try S2025 Q3 (30 min)
4. Check solution (30 min)
5. Do one more practice problem (2 hours)

**Evening:**
- Explain thinning to yourself out loud
- Test: Can you solve a competing process problem from memory?

### Day 2: Master Random Walks (8 hours)

**Morning (4 hours):**
1. Read the Random Walk section above (2 hours)
2. Work through the example step-by-step (1 hour)
3. Do a simple example yourself (1 hour)

**Afternoon (4 hours):**
1. Try F2025 Q2 (1 hour)
2. Check solution (30 min)
3. Try S2025 Q1 (1 hour)
4. Check solution (30 min)
5. Practice one more (1 hour)

**Evening:**
- Write the first-step formulas from memory
- Check: Do you remember the +1 for expected time?

### Day 3: Joint Densities + Mixed Practice (8 hours)

**Morning (3 hours):**
1. Read Joint/Conditional Density section (2 hours)
2. Work through the Y = UX example carefully (1 hour)

**Afternoon (5 hours):**
1. Try F2025 Q1 (1 hour)
2. Check solution (30 min)
3. Do a FULL practice exam (F2025 or S2025) timed (2 hours)
4. Check all solutions carefully (1.5 hours)

### Day 4: Review + Weak Spots (6 hours)

**Morning (3 hours):**
- Do another full practice exam
- Identify your 2-3 weakest areas

**Afternoon (3 hours):**
- Focus ONLY on your weak areas
- Redo problems you got wrong
- Make your cheat sheet

**Evening:**
- Light review
- Get good sleep!

---

## FINAL TIPS FOR BEGINNERS

1. **Don't memorize, understand**
   - Can you explain WHY the formula works?
   - Make up your own simple examples

2. **Draw pictures**
   - Random walks: draw the states
   - Poisson: draw a timeline of arrivals
   - Joint PDFs: sketch the region where f > 0

3. **Check your work**
   - Does the probability add to 1?
   - Does the answer make intuitive sense?
   - Are the units right?

4. **Start simple**
   - Master the basic examples first
   - Then move to harder problems
   - Don't jump to exam problems immediately

5. **Ask yourself questions**
   - What technique should I use?
   - What am I given?
   - What do I need to find?
   - Have I seen something similar?

6. **Practice writing solutions**
   - Show your work step-by-step
   - Explain what you're doing
   - Partial credit is huge on exams!

---

## YOU CAN DO THIS!

I know it seems like a lot, but:
- These are just 3-4 main techniques
- Each technique has a clear pattern
- With practice, you'll recognize problems instantly
- Thousands of students have learned this before you

**The key:** Focused, deliberate practice. Don't just read - DO problems!

Start with Poisson (it's the most common). Once you get thinning, you'll feel so much better.

Good luck! 🍀
