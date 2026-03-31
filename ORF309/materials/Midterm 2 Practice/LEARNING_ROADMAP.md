# ORF309 Midterm 2 - Learning Roadmap

**Your situation:** Haven't attended lectures, need to learn everything from scratch
**Time pressure:** High stress, but YOU CAN DO THIS! 💪
**Strategy:** Focus on high-frequency topics first, build understanding systematically

---

## 🎯 PRIORITY LEARNING PATH

### 📌 CRITICAL PRIORITY - Learn These FIRST (Day 1-2)

These 3 topics appear in **100%** of exams and make up **~75%** of exam content:

#### **1. POISSON PROCESSES** (Slides 16-19)
⏱️ **Time to Learn:** 4-6 hours
📊 **Exam Weight:** ~40% of exam
🔥 **Frequency:** 7/7 exams (100%)

**What you MUST know:**
1. Basic Poisson definition
   - Arrivals happen at rate λ (per unit time)
   - Number of arrivals N(t) ~ Poisson(λt)
   - P(N(t) = k) = (λt)^k · e^(-λt) / k!

2. **Thinning Property** (⭐ SUPER IMPORTANT)
   - If customers arrive at rate λ
   - Each customer is "type A" with probability p (independent)
   - Then type A arrivals form Poisson process with rate **λp**
   - Example: "Customers arrive at rate 2/min, 40% order coffee"
     → Coffee orders are Poisson(0.8/min)

3. **Superposition/Merging**
   - Multiple independent Poisson processes combine
   - Rates add: λ₁ + λ₂ + ... + λₙ

4. **Competing Processes**
   - Process A at rate λ_A, Process B at rate λ_B
   - P(A happens first) = λ_A / (λ_A + λ_B)
   - Expected time until first event: 1/(λ_A + λ_B)

5. **Conditional Expectations**
   - E[Time | N events occurred] = N/λ
   - Example: "Given 10 customers arrived, expected time = 10/λ"

**Learning Resources:**
- Read Slides 16-19 carefully
- Watch: Search "Poisson process thinning" on YouTube
- Practice: F2025 Q3, S2025 Q3, 2022F Q1, 2019 Q1

**Self-Test Questions:**
- Can you explain thinning in your own words?
- Can you set up P(A before B) for competing processes?
- Can you use E[T | N=n] = n/λ correctly?

---

#### **2. RANDOM WALKS & FIRST-STEP ANALYSIS** (Slides 20-22)
⏱️ **Time to Learn:** 4-6 hours
📊 **Exam Weight:** ~35% of exam
🔥 **Frequency:** 7/7 exams (100%)

**What you MUST know:**
1. **Random Walk Setup**
   - Start at position S₀ (usually between barriers a and b)
   - Each step: move +1, -1, or stay, with given probabilities
   - Continue until hitting a or b (boundaries)

2. **First-Step Analysis for HITTING PROBABILITY**
   - Define: p(i) = P(hit b before a | start at i)
   - **Recursive formula template:**
     ```
     p(i) = (prob move to i+1) · p(i+1)
          + (prob move to i-1) · p(i-1)
          + (prob stay at i) · p(i)
     ```
   - **Boundary conditions:** p(a) = 0, p(b) = 1
   - Solve the system of equations!

3. **First-Step Analysis for EXPECTED TIME**
   - Define: μ(i) = E[time to hit boundary | start at i]
   - **Recursive formula template:**
     ```
     μ(i) = 1 + (prob move to i+1) · μ(i+1)
              + (prob move to i-1) · μ(i-1)
              + (prob stay at i) · μ(i)
     ```
   - **DON'T FORGET THE "+1"!** (most common mistake)
   - **Boundary conditions:** μ(a) = 0, μ(b) = 0

4. **Special Case: Symmetric Random Walk**
   - When P(+1) = P(-1) = 1/2
   - Closed form: p(i) = (i-a)/(b-a)
   - Closed form: μ(i) = (i-a)(b-i)

5. **Biased Random Walk** (appears in ~60% of exams)
   - When P(+1) ≠ P(-1)
   - Use first-step analysis + solve system
   - OR use characteristic equation: r = p·r + q/r

**Step-by-Step Problem Solving:**
1. Draw a diagram with states a, i, b
2. Write what you're solving for: p(i) or μ(i)
3. Write the recursive formula
4. Write boundary conditions
5. Solve the system (usually 2-3 equations)

**Learning Resources:**
- Read Slides 20-22 carefully
- Focus on examples with first-step analysis
- Practice: F2025 Q2, S2025 Q1, 2017 Q3, 2019 Q3

**Self-Test Questions:**
- Can you write the first-step formula from scratch?
- Do you remember to include "+1" for expected time?
- Can you identify boundary conditions correctly?
- Can you solve a 3-equation system?

---

#### **3. CONTINUOUS RANDOM VARIABLES: JOINT & CONDITIONAL** (Slides 11-13)
⏱️ **Time to Learn:** 3-5 hours
📊 **Exam Weight:** ~25% of exam
🔥 **Frequency:** 6/7 exams (86%)

**What you MUST know:**
1. **Joint PDF f_{X,Y}(x,y)**
   - Probability density for two continuous RVs
   - Must integrate to 1: ∫∫ f(x,y) dx dy = 1
   - **Always specify the range!** (e.g., "for 0 < y < x < ∞")

2. **Marginal PDF from Joint**
   - f_X(x) = ∫ f_{X,Y}(x,y) dy (integrate over y)
   - f_Y(y) = ∫ f_{X,Y}(x,y) dx (integrate over x)

3. **Conditional PDF**
   - f_{X|Y}(x|y) = f_{X,Y}(x,y) / f_Y(y)
   - f_{Y|X}(y|x) = f_{X,Y}(x,y) / f_X(x)

4. **Building Joint PDF from Conditional**
   - f_{X,Y}(x,y) = f_{X|Y}(x|y) · f_Y(y)
   - f_{X,Y}(x,y) = f_{Y|X}(y|x) · f_X(x)

5. **Law of Total Expectation** (⭐ SUPER IMPORTANT)
   - E[Y] = E[E[Y|X]]
   - E[Y] = ∫ E[Y|X=x] · f_X(x) dx
   - Incredibly useful for computing expectations!

6. **Common Transformation: Y = UX**
   - U ~ Uniform[0,1], independent of X
   - Given X, Y is uniform on [0, X]
   - f_{Y|X}(y|x) = 1/x for 0 < y < x

**Problem-Solving Strategy:**
1. Identify what's given (conditional or marginal?)
2. Build joint PDF using f(x,y) = f(x|y)·f(y) or f(y|x)·f(x)
3. **Check the range carefully!** Draw a picture if needed
4. For expectations: use law of total expectation

**Learning Resources:**
- Read Slides 11-13
- Focus on examples with conditional densities
- Practice: F2025 Q1, S2025 Q2, 2022F Q2

**Self-Test Questions:**
- Can you go from conditional to joint PDF?
- Can you specify the correct range for the density?
- Can you use E[Y] = E[E[Y|X]]?
- Can you find marginal from joint?

---

### 📌 HIGH PRIORITY - Learn These NEXT (Day 3)

#### **4. EXPONENTIAL DISTRIBUTION & LIFETIMES** (Slides 11, 14-15)
⏱️ **Time to Learn:** 2-3 hours
📊 **Exam Weight:** ~15% of exam
🔥 **Frequency:** 5/7 exams (71%)

**What you MUST know:**
1. **Exponential Distribution Basics**
   - T ~ Exp(λ)
   - PDF: f(t) = λe^(-λt) for t > 0
   - CDF: F(t) = 1 - e^(-λt)
   - Mean: E[T] = 1/λ
   - P(T > t) = e^(-λt)

2. **Memoryless Property** (⭐ KEY!)
   - P(T > s+t | T > s) = P(T > t)
   - "Doesn't remember the past"
   - Only continuous distribution with this property

3. **Minimum of Independent Exponentials**
   - T₁ ~ Exp(λ₁), T₂ ~ Exp(λ₂)
   - min(T₁, T₂) ~ Exp(λ₁ + λ₂)
   - P(T₁ < T₂) = λ₁/(λ₁ + λ₂)
   - Connects to competing Poisson processes!

4. **Maximum of Exponentials**
   - E[max(T₁, T₂)] = 1/λ₁ + 1/λ₂ - 1/(λ₁+λ₂)
   - No simple closed form for distribution

5. **Hazard Function (optional but useful)**
   - h(t) = f(t) / (1 - F(t))
   - For exponential: h(t) = λ (constant)
   - Used in lifetime/reliability problems

**Learning Resources:**
- Read Slides 11, 14-15
- Focus on memoryless property examples
- Practice: 2022S Q1, 2019 Q2

---

#### **5. BROWNIAN MOTION** (Slide 23)
⏱️ **Time to Learn:** 2-3 hours
📊 **Exam Weight:** ~20% when it appears
🔥 **Frequency:** 3/7 exams (43%)

**What you MUST know:**
1. **Standard Brownian Motion B(t) Definition**
   - B(0) = 0 (starts at origin)
   - B(t) ~ Normal(0, t)
   - Independent increments
   - B(t) - B(s) ~ Normal(0, t-s) for t > s

2. **Key Properties**
   - E[B(t)] = 0
   - Var(B(t)) = t
   - E[B(t)²] = t (because Var = E[X²] - (E[X])² = E[X²] - 0)

3. **Conditional Expectations**
   - E[B(t) | B(s) = x] = x for t > s
   - E[B(t)² | B(s) = x] = x² + (t-s) for t > s
   - Distance between two independent BMs

4. **Common Application: Stock Prices**
   - S(t) = S₀ · e^{B(t)} (geometric Brownian motion)
   - Used in financial modeling

**Note:** This is less common but has appeared more in recent exams. If time is limited, focus on Poisson + Random Walks first!

**Learning Resources:**
- Read Slide 23
- Practice: 2022S Q3, 2021 Q1

---

## 📅 SUGGESTED 4-DAY STUDY PLAN

### **Day 1: Poisson Processes** (6-8 hours)
**Morning (3-4 hours):**
- Read Slides 16-19 carefully
- Take notes on thinning, superposition, competing processes
- Work through slide examples

**Afternoon (3-4 hours):**
- Practice F2025 Q3 (Coffee shop)
- Practice S2025 Q3 (Taxi stop)
- Practice 2019 Q1 (Plagues)
- Check solutions, understand every step

**Evening Review:**
- Can you explain thinning without looking at notes?
- Can you set up competing process problems?

---

### **Day 2: Random Walks** (6-8 hours)
**Morning (3-4 hours):**
- Read Slides 20-22 carefully
- Focus on first-step analysis technique
- Write out formula templates

**Afternoon (3-4 hours):**
- Practice F2025 Q2 (Sleepy gambler)
- Practice S2025 Q1 (Flight prices)
- Practice 2017 Q3 (Asymmetric game)

**Evening Review:**
- Write first-step formulas from memory
- Check: do you remember the "+1" for expected time?

---

### **Day 3: Joint Densities + Mixed Practice** (6-8 hours)
**Morning (2-3 hours):**
- Read Slides 11-13
- Focus on conditional densities and law of total expectation
- Work through examples

**Afternoon (3-4 hours):**
- Practice F2025 Q1 (Insurance)
- Practice S2025 Q2 (Weather index)
- Do a FULL timed practice exam (F2025 or S2025)

**Evening (1-2 hours):**
- Quick review of Exponential (Slides 11, 14-15)
- If time: Brownian Motion basics (Slide 23)

---

### **Day 4: Final Review + Weak Areas** (4-6 hours)
**Morning (2-3 hours):**
- Do another full timed practice exam
- Identify weak topics

**Afternoon (2-3 hours):**
- Focus on problems you got wrong
- Review key formulas
- Create/refine your cheat sheet

**Evening:**
- Light review, no new material
- Get good sleep before exam!

---

## 🎓 HOW TO LEARN EACH TOPIC EFFECTIVELY

### 1. **Read Slides First**
   - Don't rush, understand each example
   - Write down key formulas in your own notes
   - Try to explain concepts in your own words

### 2. **Practice Problems Immediately**
   - Don't just read solutions!
   - Attempt problem yourself first (even if you struggle)
   - Then check solution and understand each step

### 3. **Pattern Recognition**
   - Notice: "When I see X, I should use technique Y"
   - Example: "When I see 'types of customers' → Thinning!"
   - Example: "When I see 'hitting probability' → First-step analysis!"

### 4. **Active Recall**
   - After learning a topic, close your notes
   - Try to write key formulas from memory
   - Explain the technique out loud to yourself

### 5. **Interleaved Practice**
   - Don't do 10 Poisson problems in a row
   - Mix topics: Poisson → Random Walk → Joint Density
   - Helps you recognize which technique to use

---

## 🔥 EMERGENCY 2-DAY CRASH PLAN

If you only have 2 days:

### **Day 1: Poisson + Random Walks ONLY** (10-12 hours)
- These are 100% guaranteed to appear
- Master thinning and first-step analysis
- Do F2025 Q2, Q3 and S2025 Q1, Q3

### **Day 2: Joint Densities + Full Practice** (10-12 hours)
- Learn conditional density basics
- Do 2 full timed practice exams
- Focus on understanding solutions

Skip Brownian Motion if pressed for time. Focus on the big 3!

---

## ✅ KNOWLEDGE CHECK: Are You Ready?

Before the exam, you should be able to:

**Poisson Processes:**
- [ ] Explain what thinning means and when to use it
- [ ] Set up P(A before B) for competing processes
- [ ] Use E[T | N=n] correctly

**Random Walks:**
- [ ] Write first-step analysis formula from memory
- [ ] Remember to include "+1" for expected time formula
- [ ] Identify and write correct boundary conditions
- [ ] Solve a system of 2-3 linear equations

**Joint/Conditional Densities:**
- [ ] Build joint PDF from conditional + marginal
- [ ] Specify correct range for density
- [ ] Use law of total expectation E[Y] = E[E[Y|X]]
- [ ] Find marginal from joint PDF

**Exponential:**
- [ ] Know memoryless property
- [ ] Set up min of exponentials
- [ ] Remember E[T] = 1/λ (not λ!)

---

## 💪 MOTIVATION

**Remember:**
- You have a clear roadmap now!
- Topics are well-defined and learnable
- Focus on understanding, not memorizing
- Past students have done this successfully
- You can learn a lot in a focused few days

**Strategy for success:**
1. Don't try to learn everything perfectly
2. Focus on high-frequency topics first
3. Understand the TECHNIQUES, not just formulas
4. Practice with actual exam problems
5. Learn from mistakes

**You've got this! 🎯**

The fact that you're being proactive and strategic shows you have what it takes to succeed.

Now stop reading and start learning! 📚💪
