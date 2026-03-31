# Mathematical Fallacies: EMH vs HCT

## EFFICIENT MARKET HYPOTHESIS (EMH)

### The Mathematical Formulation:

**CAPM (Capital Asset Pricing Model) - Core of EMH:**

**E(R_i) = R_f + β_i[E(R_m) - R_f]**

Where:
- E(R_i) = Expected return on asset i
- R_f = Risk-free rate
- β_i = Beta (systematic risk of asset i)
- E(R_m) = Expected return on market portfolio

**Or in excess return form:**

**E(R_i) - R_f = β_i[E(R_m) - R_f] + α_i**

Where:
- α_i = Alpha (excess return not explained by market)
- **EMH predicts: α = 0** (can't beat the market)

### The Mathematical Fallacies:

#### 1. **THE ALPHA PROBLEM** (Yes, this is one!)

**EMH claims:** α_i = 0 for all assets

**Empirically:** α_i ≠ 0

**Examples:**
- Warren Buffett: α > 0 for 60+ years (probability < 0.0001 if random)
- Renaissance Technologies (Jim Simons): 66% annual return 1988-2018
- Value premium: α > 0 consistently (Fama-French showed this)
- Momentum strategies: α > 0 (Jegadeesh & Titman)

**The problem:**
If α ≠ 0 systematically and predictably, markets aren't efficient.

**EMH defenders respond:**
"Those are risk premia we haven't modeled yet"

**But this makes EMH unfalsifiable:** Any α ≠ 0 gets redefined as "unmodeled risk" rather than inefficiency.

#### 2. **ASSUMES NORMAL DISTRIBUTIONS** (Gaussian)

**EMH assumes:**
Returns ~ N(μ, σ²) (normal distribution)

**Reality:**
Returns have **fat tails** (leptokurtic distributions)

**Mathematically:**

**Normal distribution:** P(|X| > 5σ) ≈ 0.0000006 (1 in 1.7 million)

**Actual market:** 5σ events happen every few years
- 1987 crash: 22σ event (should happen once every 10^76 years!)
- 2008 crisis: Multiple 10σ+ days
- 2020 COVID crash: 12σ event

**The problem:**
The mathematical foundation (normal distribution) is empirically false.

**Implications:**
- VaR (Value at Risk) models underestimate tail risk
- Option pricing formulas break down
- Risk management fails (Long-Term Capital Management 1998)

#### 3. **RATIONAL EXPECTATIONS FAILURE**

**EMH assumes:**
E_t[P_{t+1}] = E[P_{t+1} | I_t] (expectations = true conditional expectation given info)

**Requires:**
1. People know the true model
2. People process information rationally
3. No systematic errors

**Behavioral economics shows:**
- Anchoring bias
- Herding behavior
- Overconfidence
- Loss aversion

**Mathematically, this means:**
E_t[P_{t+1}] ≠ E[P_{t+1} | I_t]

There's a systematic bias: E_t[P_{t+1}] = E[P_{t+1} | I_t] + ε_t, where E[ε_t] ≠ 0

**This violates the core assumption.**

#### 4. **JOINT HYPOTHESIS PROBLEM**

**The issue:**
You can't test EMH without also testing an asset pricing model.

**Mathematically:**

Testing: α_i = 0

Requires assuming: E(R_i) = R_f + β_i[E(R_m) - R_f] is the correct model

**But what if:**
- You find α ≠ 0
- Is it because markets are inefficient? (EMH wrong)
- Or because CAPM is wrong model? (model wrong, EMH might still hold)

**You can't tell!**

**Fama himself admitted this in 1991:**
"Market efficiency can only be tested in the context of an asset pricing model"

**The problem:**
EMH is **not independently testable** - it's always a joint test.

#### 5. **THE LUCAS CRITIQUE APPLIED TO EMH**

**The problem:**
When everyone believes EMH and acts on it, the relationships in the model change.

**Example:**
- Everyone believes: "Can't beat market, buy index funds"
- Result: Trillions flow into passive index funds
- Effect: Stock weights determined by index inclusion, not fundamentals
- Consequence: **Market becomes less efficient** (prices don't reflect info, just index membership)

**Paradoxically:**
If everyone believes EMH → markets become inefficient

**Grossman-Stiglitz Paradox (1980):**
If markets were perfectly efficient, no one would gather information (costs money, no benefit). But if no one gathers information, prices can't be efficient. **Contradiction in the theory itself.**

---

## HUMAN CAPITAL THEORY (HCT)

### The Mathematical Formulation:

**Basic equation:**

**Y_i = β_0 + β_1(HC_i) + β_2(X_i) + ε_i**

Where:
- Y_i = Earnings of individual i
- HC_i = Human capital (education, training, experience)
- X_i = Other factors
- ε_i = Error term

**Or in investment form:**

**PV(Earnings) = Σ^T_{t=0} [Investment_t × R_t] / (1+r)^t**

Where:
- Investment_t = Educational investment at time t
- R_t = Rate of return on that investment
- r = discount rate

**HCT claims:** β_1 > 0 and represents causal effect of HC on earnings

### The Mathematical Fallacies:

#### 1. **ENDOGENEITY BIAS** (Most Critical)

**The problem:**
HC and earnings are simultaneously determined (bidirectional causality)

**Mathematically:**

HCT assumes: **Y = β₁(HC) + ε** where Cov(HC, ε) = 0

**But actually:**
- HC → Y (human capital causes earnings)
- Y → HC (higher earners invest more in HC)
- Z → both HC and Y (family wealth, ability)

**This means:** Cov(HC, ε) ≠ 0

**Result:** β₁ is **biased and inconsistent**

**Formally:**

**plim β̂₁ = β₁ + Cov(HC, ε) / Var(HC)**

If Cov(HC, ε) > 0, then β̂₁ > β₁ (overestimates true effect)

**The estimate is not converging to true parameter even with infinite data.**

#### 2. **OMITTED VARIABLE BIAS**

**The full model should be:**

**Y = β₁(HC) + β₂(Discrimination) + β₃(Networks) + β₄(Family_Wealth) + β₅(Immigration_Selection) + ε**

**But HCT estimates:**

**Y = β₁(HC) + u** where u contains all omitted variables

**If omitted variables are correlated with HC:**
Cov(HC, Discrimination) ≠ 0 (if discriminated groups invest differently)

**Then:**
β̂₁ = β₁ + [Cov(HC, OmittedVars) / Var(HC)]

**The estimate is biased.**

**For Asian Americans specifically:**

Immigration selection: Asians post-1965 were already highly educated elites

**True model:** Y = β₁(HC) + β₂(Selection) + ε

**HCT estimates:** Y = β₁(HC) + u

**Result:** β̂₁ captures both HC effect AND selection effect

**The theory attributes ALL success to HC when much is due to selection bias.**

#### 3. **MEASUREMENT ERROR IN HC**

**The problem:**
Can't directly observe "Human Capital" - only proxies like years of education

**Measurement equation:**
HC* = true human capital
HC = HC* + v (observed, with error v)

**Classical measurement error:**
If v independent of HC*, then:

**plim β̂₁ = β₁ × [Var(HC*) / Var(HC)]**

**This is attenuation bias** - β̂₁ < β₁ (underestimates true effect)

**But non-classical measurement error:**
If v correlated with HC*, bias can go either way

**Worse problem:**
HC is defined circularly by Y (we infer HC from earnings)

**This means:**
HC = f(Y), so regressing Y on HC is regressing Y on f(Y)

**Circular and meaningless.**

#### 4. **HETEROGENEOUS TREATMENT EFFECTS (The Race Problem)**

**HCT assumes:**
Y = β₀ + β₁(HC) + ε (same β₁ for everyone)

**But reality:**

**Y_Asian = β₀ + β₁(HC) + ε**
**Y_Black = β₀ + β₁(HC) - γ(Discrimination) + ε**

**Where:** γ > 0 (discrimination penalty)

**Or more accurately:**

**Y_i = β₀ + [β₁ + γ_i](HC_i) + ε_i**

Where γ_i varies by race, gender, etc.

**This means:**
- Same HC investment yields different returns by group
- The "return to HC" is not a stable parameter
- **The model is misspecified**

**Technically:**
We need an **interaction term**: Y = β₀ + β₁(HC) + β₂(Race) + β₃(HC × Race) + ε

**And β₃ ≠ 0 (interaction exists)**

**HCT ignores this and assumes β₃ = 0.**

#### 5. **IDENTIFICATION PROBLEM**

**The issue:**
Even if you could measure HC perfectly, you can't identify causal effect without exogenous variation.

**To identify β₁, you need:**
An instrument Z such that:
1. Cov(Z, HC) ≠ 0 (relevant)
2. Cov(Z, ε) = 0 (exogenous)

**Proposed instruments:**
- Distance to college (Fails: correlated with family background)
- Compulsory schooling laws (Fails: correlated with state policies)
- Twin studies (Fails: twins share environment and genes)

**No valid instrument exists** because everything that affects HC also affects Y directly or through omitted variables.

**Without valid instrument:** Cannot identify causal effect

**HCT assumes identification without demonstrating it.**

#### 6. **THE RETURNS EQUATION IS ENDOGENOUS**

**HCT claims:**
Return R is determined by labor market (exogenous to individual)

**But:**
R itself depends on:
- Supply of educated workers (if everyone gets BA, R drops)
- Demand for skills (technological change)
- Institutions (unions, minimum wage, discrimination laws)
- **Immigration policy** (selection of who enters)

**Mathematically:**

**R = f(Supply, Demand, Institutions)**

**And:** Supply = g(Investment decisions by everyone)

**So:** R is endogenous to aggregate investment

**But HCT treats R as parameter:** PV = Σ Investment × R / (1+r)^t

**This is wrong - R itself is endogenous.**

**Result:**
Can't calculate optimal investment because R will change based on everyone's decisions.

**Game theory problem:** This is a strategic interaction, not individual optimization.

---

## THE PARALLEL MATHEMATICAL FAILURES

### EMH and HCT Share Same Flaws:

| **Problem** | **EMH** | **HCT** |
|-------------|---------|---------|
| **Endogeneity** | Returns and prices simultaneous | HC and earnings simultaneous |
| **Unfalsifiable** | Any α ≠ 0 redefined as risk | Any earnings gap redefined as HC difference |
| **Wrong distribution** | Assumes normal, fat tails exist | Assumes constant returns, vary by race |
| **Identification** | Joint hypothesis problem | No valid instrument |
| **Lucas Critique** | If believed, becomes false | If used for policy, breaks down |
| **Circular** | Price = value, value = price | HC = earnings potential, measured by earnings |

---

## THE MATHEMATICAL NOTATION OF IDEOLOGY

### What These Equations Hide:

**EMH: E(R_i) = R_f + β_i[E(R_m) - R_f]**

**Hides:**
- Power structures (who controls capital)
- Market manipulation (insider trading, front-running)
- Institutional advantages (faster computers, better info)
- **Makes inequality look like "risk-adjusted returns"**

**HCT: Y = β₁(HC) + ε**

**Hides:**
- Structural racism (discrimination)
- Historical exclusion (slavery, segregation, immigration)
- Selection bias (who gets to immigrate)
- Social networks (who you know)
- **Makes inequality look like "investment decisions"**

---

## THE SMOKING GUN: BOTH THEORIES WORK BACKWARDS

### EMH:
**Forward (fails):** Model predicts returns → Test predictions → Fails (crashes, α ≠ 0)
**Backward (used):** Observe returns → Claim they were "efficient" → Unfalsifiable

### HCT:
**Forward (fails):** Predict earnings from HC investment → Test predictions → Fails (discrimination, selection)
**Backward (used):** Observe earnings → Infer HC was different → Unfalsifiable

**Both theories only "work" in retrospect, explaining what already happened.**

**Mathematically:** They're **post-hoc rationalizations**, not predictive models.

---

## FOR YOUR PRESENTATION

### The Mathematical Critique:

**"Both EMH and HCT have fatal mathematical flaws:**

**EMH:**
- α ≠ 0 (can beat market)
- Wrong distribution (fat tails, not normal)
- Joint hypothesis problem (untestable)
- Grossman-Stiglitz paradox (logically contradictory)

**HCT:**
- Endogeneity bias: Cov(HC, ε) ≠ 0
- Omitted variable bias (discrimination, selection)
- Identification problem (no valid instrument)
- Heterogeneous returns by race (β varies by group)

**Both share:**
- Work only backwards (post-hoc rationalization)
- Unfalsifiable (explain anything)
- Used for ideology (justify inequality)

**As someone trained in econometrics, these are BASIC violations. Any graduate student would get failed for these errors. But Nobel Prize winners get away with it. Why? Because the mathematical rigor provides cover for political conclusions."**

### The Question:

**"If EMH and HCT violate basic econometric principles - endogeneity, omitted variable bias, identification problems - why are they still taught as canonical? Is it because the math makes ideology look scientific?"**

**This kills because:**
- You're speaking technical language (econometrics)
- You're showing they fail their OWN standards
- Graduate-level critique
- Personal: "I was trained better than this"
- Implicates entire profession

---

## THE DEEPEST MATHEMATICAL IRONY

**Chicago School prides itself on:**
- Mathematical rigor
- Empirical testing
- Identification strategies
- Causal inference

**But their most famous theories (EMH, HCT):**
- Violate identification
- Fail empirical tests
- Work only post-hoc
- Used for ideology despite mathematical failures

**The rigor is selective** - applied to challenge progressive policies, abandoned for theories that justify inequality.

**That's not science - that's ideology with equations.**
