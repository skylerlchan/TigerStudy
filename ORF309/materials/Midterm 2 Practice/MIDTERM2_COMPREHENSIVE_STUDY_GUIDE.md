# ORF309 Midterm 2 - Comprehensive Study Guide

**Created:** March 31, 2026

## Overview

This guide analyzes **7 past Midterm 2 exams** (F2025, S2025, F2022, S2022, 2021, 2019, 2017) to identify the most important topics and create a strategic study plan.

**Exam Coverage:** Slides 7-23 (Post-Midterm 1 material)
- **Slides 7-10:** Bernoulli Processes & Continuous Time Limit
- **Slides 11-15:** Continuous Random Variables & Lifetimes
- **Slides 16-19:** Poisson Processes
- **Slides 20-22:** Random Walks
- **Slide 23:** Brownian Motion

---

## ⭐ HIGH PRIORITY TOPICS (Appear in 80%+ of exams)

### 1. **POISSON PROCESSES** 🔥🔥🔥
**Frequency:** Appears in **7/7 exams (100%)**
**Lecture Slides:** 16-19
**Average weight:** ~40% of exam

#### Key Concepts:
- **Thinning Property** (appears in 6/7 exams)
  - When customers arrive at rate λ and each has probability p of type A
  - Type A arrivals form a Poisson process with rate λp

- **Conditional Expectations Given Poisson Arrivals** (appears in 5/7 exams)
  - E[time | N arrivals occurred] = N/(rate)
  - Common setup: "Given that exactly k events happened, what's the expected time?"

- **Superposition/Merging** (appears in 4/7 exams)
  - Multiple independent Poisson processes merge into one
  - If rates are λ₁, λ₂, ..., λₙ, merged rate is λ₁ + λ₂ + ... + λₙ

- **Competing Poisson Processes** (appears in 5/7 exams)
  - "What's the probability A happens before B?"
  - P(A before B) = λ_A / (λ_A + λ_B)

#### Example Question Types:
- F2025 Q3: Coffee shop with multiple product types (thinning + conditional expectation)
- S2025 Q3: Taxi arrivals vs passenger arrivals (competing processes)
- 2022F Q1: Turkey arrivals with weight thresholds (thinning)
- 2022S Q1: Chicken crossing road (conditional expectation with exponential)
- 2019 Q1: Plagues arriving (thinning with acceptance probability)

---

### 2. **RANDOM WALKS & FIRST-STEP ANALYSIS** 🔥🔥🔥
**Frequency:** Appears in **7/7 exams (100%)**
**Lecture Slides:** 20-22
**Average weight:** ~35% of exam

#### Key Concepts:
- **First-Step Analysis for Hitting Probabilities**
  - Let p(i) = P(hit b before a | start at i)
  - Recursive formula: p(i) = (prob_up)·p(i+1) + (prob_down)·p(i-1) + (prob_stay)·p(i)
  - Boundary conditions: p(a) = 0, p(b) = 1

- **First-Step Analysis for Expected Hitting Times**
  - Let μ(i) = E[time to hit boundary | start at i]
  - Recursive formula: μ(i) = 1 + (prob_up)·μ(i+1) + (prob_down)·μ(i-1) + (prob_stay)·μ(i)
  - Boundary conditions: μ(a) = 0, μ(b) = 0

- **Gambler's Ruin**
  - Symmetric random walk: p(i) = i/(b-a) when starting between a and b
  - Fair game: E[time] = (i-a)(b-i)
  - Biased walk: use characteristic equation r² = pr + q where p = prob(+1), q = prob(-1)

- **Biased Random Walks** (appears in 4/7 exams)
  - When P(+1) ≠ P(-1)
  - Solve using characteristic equation method
  - If p > q: higher probability of reaching upper boundary
  - If p < q: higher probability of reaching lower boundary

#### Example Question Types:
- F2025 Q2: Gambler with laziness parameter (modified random walk)
- S2025 Q1: Flight price movement (biased walk with first-step analysis)
- 2022F Q3: Indigestion problem (hitting time analysis)
- 2022S Q2: Easter bunny with 2-step jumps (modified random walk)
- 2021 Q3: Time warp dance (asymmetric steps)
- 2019 Q3: Israelites in desert (biased walk with drift)
- 2017 Q3: Asymmetric casino game (biased walk)

---

### 3. **CONTINUOUS RANDOM VARIABLES: JOINT & CONDITIONAL DENSITIES** 🔥🔥
**Frequency:** Appears in **6/7 exams (86%)**
**Lecture Slides:** 11-13
**Average weight:** ~25% of exam

#### Key Concepts:
- **Joint PDF of (X,Y)**
  - Finding f_{X,Y}(x,y) from conditional distributions
  - f_{X,Y}(x,y) = f_{X|Y}(x|y) · f_Y(y) = f_{Y|X}(y|x) · f_X(x)

- **Conditional Densities**
  - f_{X|Y}(x|y) = f_{X,Y}(x,y) / f_Y(y)
  - Be careful with the range/support!

- **Law of Total Expectation (Tower Property)**
  - E[Y] = E[E[Y|X]]
  - Extremely useful for computing expectations

- **Transformations of Random Variables**
  - If Y = g(X), find density of Y
  - Common: Y = UX where U ~ Uniform[0,1]

#### Example Question Types:
- F2025 Q1: Insurance payments Y = UX (joint density, conditional probability)
- S2025 Q2: Flight delay with weather index (joint density, conditional probabilities)
- 2022F Q2: Pie eaten by dog (conditional expectation)
- 2022S Q3: Stock price as e^{Bt} (probability calculations)
- 2021 Q2: Customer drinking sanitizer (expectations with Poisson)

---

## 🔴 MEDIUM-HIGH PRIORITY TOPICS (Appear in 40-80% of exams)

### 4. **EXPONENTIAL DISTRIBUTION & LIFETIMES** 🔥
**Frequency:** Appears in **5/7 exams (71%)**
**Lecture Slides:** 11, 14-15
**Average weight:** ~15% of exam

#### Key Concepts:
- **Memoryless Property**
  - P(T > s+t | T > s) = P(T > t)
  - Exponential is the ONLY continuous distribution with this property

- **Hazard Rate & Hazard Function**
  - h(t) = f(t) / (1 - F(t))
  - For exponential: h(t) = λ (constant)
  - Related to lifetime: f(t) = h(t)·e^{-∫h(s)ds}

- **Min/Max of Exponentials**
  - Min(T₁, T₂) where T₁ ~ Exp(λ₁), T₂ ~ Exp(λ₂): min ~ Exp(λ₁ + λ₂)
  - P(T₁ < T₂) = λ₁/(λ₁ + λ₂)
  - E[Max(T₁,T₂)] = 1/λ₁ + 1/λ₂ - 1/(λ₁+λ₂)

- **Series vs Parallel Systems**
  - Series (both must work): L = min(L₁, L₂)
  - Parallel (at least one works): L = max(L₁, L₂)

#### Example Question Types:
- 2022S Q1: Chicken crossing with exponential wait time
- 2019 Q2: Bread rising and proofing (max of exponentials)
- 2017 Q2: Smoker vs non-smoker lifetimes (hazard rates)
- S2025 Q2: Weather index with exponential delay

---

### 5. **BROWNIAN MOTION** 🔥
**Frequency:** Appears in **3/7 exams (43%)**
**Lecture Slides:** 23
**Average weight:** ~20% of exam when it appears

#### Key Concepts:
- **Definition: B(t) is Standard Brownian Motion if:**
  - B(0) = 0
  - B(t) - B(s) ~ Normal(0, t-s) for t > s
  - Independent increments

- **Properties:**
  - E[B(t)] = 0
  - Var(B(t)) = t
  - E[B(t)²] = t
  - B(t) ~ N(0,t)

- **Conditional Expectations**
  - E[B(t)² | B(s) = x] = x² + (t-s) for t > s
  - Distance between two independent BMs at time t has special distribution

- **Functions of Brownian Motion**
  - Common: S(t) = e^{B(t)} (geometric Brownian motion)
  - Stock price modeling

#### Example Question Types:
- 2022S Q3: Stock price S(t) = e^{B(t)}
- 2021 Q1: Two ants doing independent Brownian motion
- Recent exams tend to include BM more often!

---

## 📊 TOPIC FREQUENCY ANALYSIS

| Topic | Frequency | Slides | Priority |
|-------|-----------|--------|----------|
| **Poisson Processes** | 7/7 (100%) | 16-19 | ⭐⭐⭐ CRITICAL |
| **Random Walks** | 7/7 (100%) | 20-22 | ⭐⭐⭐ CRITICAL |
| **Joint/Conditional Densities** | 6/7 (86%) | 11-13 | ⭐⭐⭐ CRITICAL |
| **Exponential/Lifetimes** | 5/7 (71%) | 11, 14-15 | ⭐⭐ HIGH |
| **Brownian Motion** | 3/7 (43%) | 23 | ⭐⭐ HIGH |
| **Law of Total Expectation** | 6/7 (86%) | 11-12 | ⭐⭐⭐ CRITICAL |
| **Thinning** | 6/7 (86%) | 17 | ⭐⭐⭐ CRITICAL |
| **Competing Processes** | 5/7 (71%) | 16-17 | ⭐⭐ HIGH |
| **First-Step Analysis** | 7/7 (100%) | 20-21 | ⭐⭐⭐ CRITICAL |
| **Biased Random Walks** | 4/7 (57%) | 22 | ⭐⭐ HIGH |
| **Conditional Probability** | 7/7 (100%) | All | ⭐⭐⭐ CRITICAL |

---

## 📚 DETAILED EXAM BREAKDOWN

### **Fall 2025 Midterm**
**Q1 (Insurance - 30 pts):** Joint/Conditional Densities, Transformations (Y = UX)
- *Topics:* Continuous RVs, conditional probability, tail distributions
- *Slides:* 11-13

**Q2 (Sleepy Gambler - 30 pts):** Modified Random Walk with laziness parameter
- *Topics:* First-step analysis, hitting probabilities, expected hitting times
- *Slides:* 20-21

**Q3 (Coffee Shop - 30 pts):** Poisson with Thinning, Conditional Expectation
- *Topics:* Thinning property, conditional expectations, Poisson processes
- *Slides:* 16-18

---

### **Spring 2025 Midterm**
**Q1 (Flight Prices - 30 pts):** Biased Random Walk with barriers
- *Topics:* First-step analysis, hitting probabilities, expected times
- *Slides:* 20-22

**Q2 (Weather Index - 30 pts):** Joint Density, Exponential conditioning
- *Topics:* Joint PDFs, conditional probabilities with continuous RVs
- *Slides:* 11-13, 14-15

**Q3 (Taxi Stop - 30 pts):** Competing Poisson Processes
- *Topics:* Poisson processes, conditional expectations, competing processes
- *Slides:* 16-18

---

### **Fall 2022 Midterm**
**Q1 (Turkeys - 30 pts):** Poisson with Thinning, Competing Processes
- *Topics:* Thinning (exponential threshold), competing Poisson vs customer arrivals
- *Slides:* 16-18

**Q2 (Pie - 30 pts):** Conditional Expectation, Gamma Distribution
- *Topics:* Law of total expectation, conditional expectations with continuous RVs
- *Slides:* 11-13

**Q3 (Indigestion - 30 pts):** Random Walk, Hitting Time
- *Topics:* Discrete random walk, probability of never hitting barrier
- *Slides:* 20-21

---

### **Spring 2022 Midterm**
**Q1 (Chicken Crossing - 30 pts):** Poisson + Exponential, Conditional Expectation
- *Topics:* Poisson count, conditional expectation given count
- *Slides:* 16-18, 11

**Q2 (Easter Bunny - 30 pts):** Random Walk with jumps of ±1, ±2
- *Topics:* Modified random walk, first-step analysis
- *Slides:* 20-22

**Q3 (Stock Price - 30 pts):** Brownian Motion, e^{B(t)}
- *Topics:* Brownian motion properties, probabilities with BM
- *Slides:* 23

---

### **2021 Midterm**
**Q1 (Tiger-ants - 30 pts):** Two Independent Brownian Motions
- *Topics:* Conditional expectations with BM, distance between BMs
- *Slides:* 23

**Q2 (Fruity Yogurt - 30 pts):** Poisson with Thinning (two-stage)
- *Topics:* Thinning with multiple probabilities, conditional expectations
- *Slides:* 16-18

**Q3 (Time Warp - 30 pts):** Modified Random Walk
- *Topics:* First-step analysis with asymmetric steps
- *Slides:* 20-22

---

### **2019 Midterm**
**Q1 (Plagues - 30 pts):** Poisson with Thinning/Acceptance
- *Topics:* Thinning with acceptance probability, types of events
- *Slides:* 16-18

**Q2 (Matzot - 30 pts):** Max of Two Exponentials
- *Topics:* Expected max, probability calculations with exponentials
- *Slides:* 11, 14-15

**Q3 (Desert - 30 pts):** Random Walk with Drift
- *Topics:* Biased random walk, first-step analysis
- *Slides:* 20-22

---

### **2017 Midterm**
**Q1 (Twitter - 30 pts):** Multiple Competing Poisson Processes
- *Topics:* Superposition, competing processes, conditional expectations
- *Slides:* 16-18

**Q2 (Smoking - 30 pts):** Hazard Functions, Lifetimes
- *Topics:* Hazard rate, probability one outlasts another
- *Slides:* 14-15

**Q3 (Asymmetric Game - 30 pts):** Biased Random Walk (+1/-2)
- *Topics:* First-step analysis with asymmetric steps
- *Slides:* 20-22

---

## 🎯 STUDY STRATEGY

### Phase 1: Master the Fundamentals (Days 1-2)
**Focus on these slides in order:**
1. **Slides 16-19: Poisson Processes**
   - Master thinning, superposition, conditional expectations
   - Work through F2025 Q3, S2025 Q3, 2022F Q1, 2022S Q1

2. **Slides 20-22: Random Walks**
   - Master first-step analysis technique
   - Practice writing recursive formulas
   - Work through F2025 Q2, S2025 Q1, 2017 Q3

3. **Slides 11-13: Continuous Random Variables**
   - Joint and conditional densities
   - Law of total expectation
   - Work through F2025 Q1, S2025 Q2

### Phase 2: Practice Mixed Problems (Day 3)
**Complete full exams under timed conditions:**
- Start with F2025 or S2025 (most recent)
- Then do 2022 Spring and Fall
- Check solutions carefully, understand every step

### Phase 3: Advanced Topics (Day 4)
**If you have time:**
1. **Slides 14-15: Lifetimes** (for 2017 Q2, 2019 Q2)
2. **Slide 23: Brownian Motion** (for 2022S Q3, 2021 Q1)

### Phase 4: Final Review (Day before exam)
- Review your cheat sheet
- Redo problems you got wrong
- Focus on pattern recognition (which technique to use when)

---

## 🔑 KEY FORMULAS & TECHNIQUES

### Poisson Processes
```
If N(t) ~ Poisson(λt):
- P(N(t) = k) = (λt)^k · e^(-λt) / k!
- E[N(t)] = λt
- Var(N(t)) = λt

Thinning: If arrivals are rate λ, each type A with prob p
→ Type A arrivals are Poisson(λp)

Competing: P(A before B) = λ_A / (λ_A + λ_B)

Conditional: E[T | N(T) = n] = n/λ
```

### Random Walk First-Step Analysis
```
For hitting probability p(i):
p(i) = p_up · p(i+1) + p_down · p(i-1) + p_stay · p(i)
Boundaries: p(a) = 0, p(b) = 1

For expected hitting time μ(i):
μ(i) = 1 + p_up · μ(i+1) + p_down · μ(i-1) + p_stay · μ(i)
Boundaries: μ(a) = 0, μ(b) = 0

For symmetric walk (p = q = 1/2):
p(i) = (i-a)/(b-a)
μ(i) = (i-a)(b-i)
```

### Exponential Distribution
```
If T ~ Exp(λ):
- f(t) = λe^(-λt)
- E[T] = 1/λ
- P(T > t) = e^(-λt)
- Memoryless: P(T > s+t | T > s) = P(T > t)

Min of exponentials:
min(T₁, T₂) ~ Exp(λ₁ + λ₂)
P(T₁ < T₂) = λ₁/(λ₁ + λ₂)
```

### Continuous Random Variables
```
Joint to Marginal:
f_X(x) = ∫ f_{X,Y}(x,y) dy

Conditional:
f_{X|Y}(x|y) = f_{X,Y}(x,y) / f_Y(y)

Law of Total Expectation:
E[Y] = E[E[Y|X]] = ∫ E[Y|X=x] · f_X(x) dx
```

### Brownian Motion
```
If B(t) is standard BM:
- B(0) = 0
- E[B(t)] = 0
- Var(B(t)) = t
- B(t) ~ N(0,t)
- B(t) - B(s) ~ N(0, t-s) for t > s
- E[B(t)² | B(s) = x] = x² + (t-s)
```

---

## ⚡ COMMON MISTAKES TO AVOID

1. **Poisson Processes:**
   - ❌ Forgetting to use thinning when events split into types
   - ❌ Not recognizing when to use conditional expectation E[T | N = n]
   - ✅ Always check if arrivals split by type → use thinning

2. **Random Walks:**
   - ❌ Forgetting the "+1" in the expected time formula: μ(i) = **1** + ...
   - ❌ Wrong boundary conditions (should be 0 at both barriers)
   - ✅ Write out the recursive formula carefully with all probabilities

3. **Joint Densities:**
   - ❌ Not checking the range/support of the distribution
   - ❌ Forgetting to normalize (density must integrate to 1)
   - ✅ Always specify the region where f(x,y) > 0

4. **Exponential:**
   - ❌ Confusing rate λ with mean (mean = 1/λ)
   - ❌ Not using memoryless property when applicable
   - ✅ Remember: min of exponentials → sum of rates

---

## 📝 PRACTICE PROBLEM RECOMMENDATIONS

### Must-Do Problems (Do these first!):
1. **F2025 Q3** (Poisson thinning + conditional expectation) ⭐⭐⭐
2. **F2025 Q2** (Random walk with modified probabilities) ⭐⭐⭐
3. **S2025 Q1** (Biased random walk first-step analysis) ⭐⭐⭐
4. **S2025 Q3** (Competing Poisson processes) ⭐⭐⭐
5. **2022F Q1** (Poisson with exponential threshold) ⭐⭐
6. **2022S Q1** (Poisson + exponential conditional) ⭐⭐

### Good Practice Problems:
7. **F2025 Q1** (Joint density Y = UX)
8. **S2025 Q2** (Joint density with exponentials)
9. **2021 Q2** (Poisson two-stage thinning)
10. **2019 Q3** (Biased random walk)

### Advanced/Optional:
11. **2022S Q3** (Brownian motion - stock prices)
12. **2021 Q1** (Two Brownian motions)
13. **2017 Q2** (Hazard functions)

---

## 🚨 EXAM DAY TIPS

1. **Read the problem carefully** - identify which technique to use
2. **Write down what you know** - given distributions, parameters, etc.
3. **Set up the problem** - define random variables clearly
4. **Show your work** - partial credit is awarded!
5. **Check boundary conditions** - especially for random walks
6. **Simplify your answer** - reduce fractions, combine terms
7. **Sanity check** - does your answer make intuitive sense?

---

## 📖 QUICK REFERENCE: Which Technique When?

**See "Poisson process" + "types/categories"** → Use **Thinning**

**See "random walk" + "probability of hitting"** → Use **First-Step Analysis (hitting prob)**

**See "random walk" + "expected time"** → Use **First-Step Analysis (expected time)**

**See "given that N(t) = n"** → Use **Conditional Expectation** with Poisson

**See "exponential" + "minimum" or "first to occur"** → Use **Min of Exponentials**

**See "joint density" or "f(x,y)"** → Set up **Joint PDF**, remember to check range

**See "given X = x, find E[Y]"** → Use **Conditional Expectation/Conditional Density**

**See "Brownian motion" or "B(t)"** → Use **BM properties** (E[B(t)] = 0, Var = t)

---

## 💪 YOU CAN DO THIS!

Don't panic! You have a clear roadmap now:
1. Focus on Poisson Processes + Random Walks first (100% appearance rate!)
2. Master the techniques, not just memorize formulas
3. Practice with past exams under timed conditions
4. Understand WHY each step works, not just HOW

**Key to success:** Pattern recognition + technique mastery

Good luck! 🍀
