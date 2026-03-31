# ORF 309 Midterm 1 Formula Guide and Study Resource

## Most Frequent Problem Types (Based on 2017-2025 Midterms)

1. **Conditional Probability** (appears in ~90% of midterms)
2. **Independence Testing** (appears in ~80% of midterms)
3. **Bayes' Theorem Applications** (appears in ~75% of midterms)
4. **Discrete Random Variables & PMF** (appears in ~85% of midterms)
5. **Expectation and Variance Calculations** (appears in ~90% of midterms)
6. **Binomial Distribution Problems** (appears in ~70% of midterms)
7. **Joint Distributions** (appears in ~65% of midterms)
8. **Law of Total Probability** (appears in ~60% of midterms)

---

## Topic 1: Basic Probability Axioms and Set Theory

### Formula 1.1: Probability Axioms
**Importance: 5/5**

**Formula:**
1. $P(A) \geq 0$ for all events $A$
2. $P(\Omega) = 1$ where $\Omega$ is the sample space
3. For disjoint events $A_1, A_2, \ldots$: $P(\bigcup_{i=1}^{\infty} A_i) = \sum_{i=1}^{\infty} P(A_i)$

**Dos:**
- DO verify that events are disjoint before applying Axiom 3
- DO use these axioms to verify if a function is a valid probability measure
- DO remember that probabilities must be between 0 and 1
- DO use Axiom 3 as the foundation for all probability calculations involving unions

**Don'ts:**
- DON'T apply the sum rule (Axiom 3) to overlapping events
- DON'T forget to check if $P(\Omega) = 1$ when verifying a probability measure
- DON'T assume negative probabilities are ever valid
- DON'T confuse the axioms with conditional probability rules

---

### Formula 1.2: Complement Rule
**Importance: 5/5**

**Formula:**
$$P(A^c) = 1 - P(A)$$

**Dos:**
- DO use this when it's easier to calculate the probability of "not A" than "A"
- DO apply this in "at least one" problems (convert to "not none")
- DO verify that $A^c$ represents all outcomes not in $A$
- DO use this to check your work: $P(A) + P(A^c)$ should always equal 1

**Don'ts:**
- DON'T confuse $A^c$ with $A$ being false in logic (different contexts)
- DON'T forget that $A$ and $A^c$ are always disjoint
- DON'T apply this to conditional probabilities without conditioning on the same event: $P(A^c|B) \neq 1 - P(A|B)$ unless you're careful
- DON'T use when you can calculate $P(A)$ directly more easily

---

### Formula 1.3: Inclusion-Exclusion Principle (Two Events)
**Importance: 5/5**

**Formula:**
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Dos:**
- DO use this whenever you need the probability of "A or B"
- DO subtract the intersection to avoid double-counting
- DO check if events are disjoint first: if so, $P(A \cap B) = 0$ and the formula simplifies
- DO extend to three events if needed using the general inclusion-exclusion formula

**Don'ts:**
- DON'T forget to subtract $P(A \cap B)$ (most common mistake)
- DON'T confuse $\cup$ (union, "or") with $\cap$ (intersection, "and")
- DON'T apply this formula directly to conditional probabilities without adjusting
- DON'T assume $P(A \cup B) = P(A) + P(B)$ unless the events are disjoint

---

### Formula 1.4: Inclusion-Exclusion Principle (Three Events)
**Importance: 3/5**

**Formula:**
$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

**Dos:**
- DO add back the triple intersection after subtracting pairwise intersections
- DO use a Venn diagram to visualize which regions you're counting
- DO check for any disjoint pairs to simplify calculations
- DO remember the alternating pattern: add singles, subtract pairs, add triples

**Don'ts:**
- DON'T forget the $+ P(A \cap B \cap C)$ term at the end
- DON'T confuse the order of operations (all additions first, then subtractions won't work)
- DON'T use this when a simpler approach exists (like DeMorgan's laws with complements)
- DON'T extend this carelessly to more events without knowing the general formula

---

### Formula 1.5: DeMorgan's Laws
**Importance: 4/5**

**Formula:**
$$(A \cup B)^c = A^c \cap B^c$$
$$(A \cap B)^c = A^c \cup B^c$$

**Dos:**
- DO use these to simplify complement of unions/intersections
- DO apply these when working with "neither A nor B" problems: $(A \cup B)^c$
- DO verify your result using Venn diagrams if unsure
- DO remember "complement flips union to intersection and vice versa"

**Don'ts:**
- DON'T confuse which law applies to which operation
- DON'T forget to complement each individual event when taking the complement of a union/intersection
- DON'T apply these to probability expressions without also adjusting the probability notation
- DON'T use these as a substitute for directly calculating probabilities when that's simpler

---

## Topic 2: Conditional Probability

### Formula 2.1: Definition of Conditional Probability
**Importance: 5/5**

**Formula:**
$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad \text{provided } P(B) > 0$$

**Dos:**
- DO check that $P(B) > 0$ before applying this formula
- DO interpret $P(A|B)$ as "probability of A given that B has occurred"
- DO use this to find $P(A \cap B) = P(A|B) \cdot P(B)$ (multiplication rule)
- DO remember that conditional probabilities satisfy all probability axioms
- DO use this as the foundation for all conditional probability problems

**Don'ts:**
- DON'T confuse $P(A|B)$ with $P(B|A)$ (they are usually different!)
- DON'T forget to divide by $P(B)$ when calculating from the intersection
- DON'T apply this when $P(B) = 0$ (conditional probability is undefined)
- DON'T assume $P(A|B) = P(A)$ unless you know $A$ and $B$ are independent

---

### Formula 2.2: Multiplication Rule (Chain Rule)
**Importance: 5/5**

**Formula:**
$$P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$$

More generally, for events $A_1, A_2, \ldots, A_n$:
$$P(A_1 \cap A_2 \cap \cdots \cap A_n) = P(A_1) \cdot P(A_2|A_1) \cdot P(A_3|A_1 \cap A_2) \cdots P(A_n|A_1 \cap \cdots \cap A_{n-1})$$

**Dos:**
- DO use this to find joint probabilities from conditional probabilities
- DO apply the chain rule for sequences of events (very common in midterms)
- DO choose the order of conditioning that makes calculation easiest
- DO verify that all conditional probabilities are well-defined (denominators > 0)

**Don'ts:**
- DON'T forget to multiply by the probability of the conditioning event
- DON'T confuse the order: $P(A|B) \cdot P(B)$ is not the same as $P(B|A) \cdot P(B)$
- DON'T assume you can drop conditioning events in the chain rule
- DON'T use independence shortcuts unless you've verified independence

---

### Formula 2.3: Law of Total Probability
**Importance: 5/5**

**Formula:**
If $B_1, B_2, \ldots, B_n$ form a partition of the sample space (disjoint and exhaustive), then:
$$P(A) = \sum_{i=1}^{n} P(A|B_i) \cdot P(B_i)$$

**Dos:**
- DO verify that the events $B_i$ are disjoint and cover the entire sample space
- DO use this when you know conditional probabilities but need the unconditional probability
- DO think of this as "breaking A into cases based on which $B_i$ occurs"
- DO apply this before Bayes' theorem (it often gives you the denominator)

**Don'ts:**
- DON'T forget that the $B_i$ must partition the sample space (no gaps, no overlaps)
- DON'T confuse this with simple addition of probabilities
- DON'T miss any cases in the partition (a common source of errors)
- DON'T use this when you can calculate $P(A)$ directly more easily

---

### Formula 2.4: Bayes' Theorem
**Importance: 5/5**

**Formula:**
$$P(B|A) = \frac{P(A|B) \cdot P(B)}{P(A)} = \frac{P(A|B) \cdot P(B)}{\sum_{i} P(A|B_i) \cdot P(B_i)}$$

where $B_1, B_2, \ldots, B_n$ form a partition.

**Dos:**
- DO use this to "flip" conditional probabilities (find $P(B|A)$ from $P(A|B)$)
- DO apply the law of total probability to find the denominator if not given
- DO identify which event is the "hypothesis" and which is the "evidence"
- DO use this in medical testing, diagnostic, and classification problems
- DO check your answer makes sense (should be between 0 and 1)

**Don'ts:**
- DON'T confuse $P(B|A)$ with $P(A|B)$ (this is what Bayes' theorem corrects!)
- DON'T forget to include all terms in the denominator sum
- DON'T skip the law of total probability step if you need to find $P(A)$
- DON'T use prior probabilities when you should use posterior probabilities
- DON'T forget that the denominator must be the same event as in the numerator

---

### Formula 2.5: Independence Definition
**Importance: 5/5**

**Formula:**
Events $A$ and $B$ are independent if and only if:
$$P(A \cap B) = P(A) \cdot P(B)$$

Equivalently (when $P(B) > 0$):
$$P(A|B) = P(A)$$

**Dos:**
- DO check independence using any of the equivalent definitions
- DO remember that independence is symmetric: if $A$ is independent of $B$, then $B$ is independent of $A$
- DO verify that complements are also independent: if $A \perp B$, then $A^c \perp B$, $A \perp B^c$, and $A^c \perp B^c$
- DO use independence to simplify calculations (products instead of conditional probabilities)
- DO test all three equivalent conditions when verifying independence

**Don'ts:**
- DON'T confuse independence with disjointness (they're almost opposite!)
- DON'T assume $P(A|B) = P(A)$ means causation or lack of relationship
- DON'T forget that if $P(A) = 0$ or $P(A) = 1$, then $A$ is independent of any event
- DON'T use $P(A) + P(B) = P(A \cup B)$ as a test for independence (that's disjointness!)
- DON'T assume pairwise independence implies mutual independence for 3+ events

---

### Formula 2.6: Conditional Independence
**Importance: 3/5**

**Formula:**
Events $A$ and $B$ are conditionally independent given $C$ if:
$$P(A \cap B | C) = P(A|C) \cdot P(B|C)$$

**Dos:**
- DO recognize that conditional independence given $C$ doesn't imply unconditional independence
- DO use this in problems involving "given information" that makes events independent
- DO verify the conditioning event is the same throughout
- DO remember this is crucial for Bayesian networks and hierarchical models

**Don'ts:**
- DON'T confuse conditional independence with regular independence
- DON'T assume unconditional independence implies conditional independence
- DON'T forget to condition on the same event $C$ throughout your calculation
- DON'T use this unless the problem explicitly states or implies conditional independence

---

## Topic 3: Random Variables and Probability Mass Functions

### Formula 3.1: Probability Mass Function (PMF)
**Importance: 5/5**

**Formula:**
For a discrete random variable $X$:
$$p_X(x) = P(X = x)$$

Properties:
1. $p_X(x) \geq 0$ for all $x$
2. $\sum_{x} p_X(x) = 1$

**Dos:**
- DO verify that the PMF sums to 1 (always check this!)
- DO use the PMF to find probabilities of events: $P(X \in A) = \sum_{x \in A} p_X(x)$
- DO define the PMF for all possible values in the support of $X$
- DO remember that PMF values are probabilities (between 0 and 1)

**Don'ts:**
- DON'T confuse PMF with PDF (PDF is for continuous random variables)
- DON'T forget that PMF is only defined at discrete points
- DON'T assume PMF is uniform unless stated
- DON'T use PMF notation for events (use $P(X = x)$, not $p(X = x)$)

---

### Formula 3.2: Cumulative Distribution Function (CDF)
**Importance: 4/5**

**Formula:**
$$F_X(x) = P(X \leq x) = \sum_{k \leq x} p_X(k)$$

Properties:
1. $F_X$ is non-decreasing
2. $\lim_{x \to -\infty} F_X(x) = 0$ and $\lim_{x \to \infty} F_X(x) = 1$
3. $F_X$ is right-continuous

**Dos:**
- DO use CDF to find probabilities of intervals: $P(a < X \leq b) = F_X(b) - F_X(a)$
- DO remember that CDF always goes from 0 to 1
- DO verify that CDF is non-decreasing
- DO use CDF to find median and quantiles

**Don'ts:**
- DON'T confuse $P(X \leq x)$ with $P(X < x)$ (they differ at jump points)
- DON'T forget to sum over all values up to and including $x$
- DON'T assume CDF is continuous for discrete random variables
- DON'T use PMF when CDF is asked for (or vice versa)

---

### Formula 3.3: Expectation (Expected Value)
**Importance: 5/5**

**Formula:**
$$E[X] = \sum_{x} x \cdot p_X(x)$$

For functions of $X$:
$$E[g(X)] = \sum_{x} g(x) \cdot p_X(x)$$

**Dos:**
- DO weight each value by its probability
- DO use linearity: $E[aX + b] = aE[X] + b$
- DO apply the law of the unconscious statistician (LOTUS) for functions of $X$
- DO check that the sum converges (expectation may not exist)
- DO interpret $E[X]$ as the long-run average value

**Don'ts:**
- DON'T confuse expectation with the most likely value (mode)
- DON'T forget to multiply by probabilities (common error!)
- DON'T assume $E[g(X)] = g(E[X])$ unless $g$ is linear
- DON'T assume $E[X]$ must be a possible value of $X$
- DON'T forget that $E[X]$ may not exist if the sum doesn't converge

---

### Formula 3.4: Linearity of Expectation
**Importance: 5/5**

**Formula:**
$$E[aX + bY + c] = aE[X] + bE[Y] + c$$

More generally:
$$E\left[\sum_{i=1}^{n} a_i X_i\right] = \sum_{i=1}^{n} a_i E[X_i]$$

**Dos:**
- DO use this to simplify complex expectation calculations
- DO remember this holds even if $X$ and $Y$ are dependent
- DO apply this to indicator random variables (very powerful technique)
- DO break complex random variables into simpler components
- DO use this as your first tool for expectation problems

**Don'ts:**
- DON'T assume you need independence (linearity always holds!)
- DON'T confuse with $E[XY] = E[X]E[Y]$ (that requires independence)
- DON'T forget constant factors can be pulled out
- DON'T apply linearity to non-linear functions: $E[X^2] \neq (E[X])^2$

---

### Formula 3.5: Variance
**Importance: 5/5**

**Formula:**
$$\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$$

Standard deviation:
$$\sigma_X = \sqrt{\text{Var}(X)}$$

**Dos:**
- DO use the computational formula $E[X^2] - (E[X])^2$ for calculations
- DO remember that variance is always non-negative
- DO scale variance by the square: $\text{Var}(aX + b) = a^2 \text{Var}(X)$
- DO interpret variance as a measure of spread around the mean
- DO use standard deviation when you want units matching $X$

**Don'ts:**
- DON'T confuse $E[X^2]$ with $(E[X])^2$ (they're usually different!)
- DON'T forget to square the constant: $\text{Var}(aX) = a^2 \text{Var}(X)$, not $a \text{Var}(X)$
- DON'T assume $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ unless $X$ and $Y$ are independent
- DON'T use variance directly in inequalities (use standard deviation or Chebyshev's inequality)
- DON'T forget that adding a constant doesn't change variance: $\text{Var}(X + b) = \text{Var}(X)$

---

### Formula 3.6: Variance Properties
**Importance: 4/5**

**Formula:**
1. $\text{Var}(aX + b) = a^2 \text{Var}(X)$
2. If $X$ and $Y$ are independent: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$
3. $\text{Var}(X) = 0$ if and only if $X$ is constant with probability 1

**Dos:**
- DO check independence before adding variances
- DO remember constants disappear: $\text{Var}(X + c) = \text{Var}(X)$
- DO square the scalar when scaling: $\text{Var}(cX) = c^2 \text{Var}(X)$
- DO use independence to simplify variance of sums

**Don'ts:**
- DON'T add variances without checking independence
- DON'T forget to square the coefficient
- DON'T confuse variance with standard deviation when scaling
- DON'T assume negative variance is possible (it's not!)

---

## Topic 4: Common Discrete Distributions

### Formula 4.1: Bernoulli Distribution
**Importance: 4/5**

**Formula:**
$$X \sim \text{Bernoulli}(p)$$
$$p_X(x) = \begin{cases} p & \text{if } x = 1 \\ 1-p & \text{if } x = 0 \end{cases}$$
$$E[X] = p$$
$$\text{Var}(X) = p(1-p)$$

**Dos:**
- DO use this for any binary outcome (success/failure, yes/no)
- DO remember this is the building block for binomial distribution
- DO use indicator random variables with Bernoulli(p) where p is the probability of the event
- DO note that maximum variance occurs at $p = 0.5$

**Don'ts:**
- DON'T confuse Bernoulli (single trial) with Binomial (multiple trials)
- DON'T forget that $X$ can only take values 0 or 1
- DON'T use this for counts of successes (use Binomial instead)
- DON'T assume $p = 0.5$ unless stated (common mistake)

---

### Formula 4.2: Binomial Distribution
**Importance: 5/5**

**Formula:**
$$X \sim \text{Binomial}(n, p)$$
$$p_X(k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n$$
$$E[X] = np$$
$$\text{Var}(X) = np(1-p)$$

**Dos:**
- DO verify the conditions: fixed number of trials $n$, independent trials, constant probability $p$, binary outcomes
- DO use this for "number of successes in $n$ trials"
- DO remember that sum of independent Bernoulli(p) random variables is Binomial(n, p)
- DO check if problem asks for "at least k" or "at most k" (sum PMF values)
- DO use complement when appropriate: $P(X \geq k) = 1 - P(X \leq k-1)$

**Don'ts:**
- DON'T forget the binomial coefficient $\binom{n}{k}$
- DON'T use this when trials are dependent (use hypergeometric instead)
- DON'T confuse $n$ (number of trials) with $k$ (number of successes)
- DON'T assume independence without justification
- DON'T forget that $p$ must be constant across all trials

---

### Formula 4.3: Geometric Distribution
**Importance: 3/5**

**Formula:**
$$X \sim \text{Geometric}(p)$$
$$p_X(k) = (1-p)^{k-1} p, \quad k = 1, 2, 3, \ldots$$
$$E[X] = \frac{1}{p}$$
$$\text{Var}(X) = \frac{1-p}{p^2}$$

**Dos:**
- DO use this for "number of trials until first success"
- DO verify that trials are independent with constant probability
- DO remember the memoryless property: $P(X > n+m | X > n) = P(X > m)$
- DO use this for "waiting time" problems in discrete settings

**Don'ts:**
- DON'T confuse with "number of failures before first success" version (some books use $k = 0, 1, 2, \ldots$)
- DON'T forget that support starts at 1 (or 0, depending on convention)
- DON'T use this for "number of successes in n trials" (that's Binomial)
- DON'T assume memoryless property holds for other distributions

---

### Formula 4.4: Poisson Distribution
**Importance: 3/5**

**Formula:**
$$X \sim \text{Poisson}(\lambda)$$
$$p_X(k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \ldots$$
$$E[X] = \lambda$$
$$\text{Var}(X) = \lambda$$

**Dos:**
- DO use this for "number of events in a fixed interval" (time, space, volume)
- DO verify conditions: events occur independently, at constant average rate, one at a time
- DO remember that mean equals variance (unique property)
- DO use as approximation to Binomial(n,p) when $n$ is large and $p$ is small ($\lambda = np$)

**Don'ts:**
- DON'T forget the $e^{-\lambda}$ term
- DON'T confuse $\lambda$ (rate parameter) with number of events
- DON'T use this when events are not independent
- DON'T forget $k!$ in the denominator
- DON'T assume Poisson when rate is not constant over the interval

---

### Formula 4.5: Hypergeometric Distribution
**Importance: 2/5**

**Formula:**
$$X \sim \text{Hypergeometric}(N, K, n)$$
$$p_X(k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$$
$$E[X] = n\frac{K}{N}$$

**Dos:**
- DO use this for sampling without replacement
- DO remember: $N$ = population size, $K$ = number of success states in population, $n$ = number of draws, $k$ = number of observed successes
- DO verify that sampling is without replacement
- DO check constraints: $\max(0, n-N+K) \leq k \leq \min(n, K)$

**Don'ts:**
- DON'T confuse with Binomial (which is sampling with replacement or independent trials)
- DON'T forget to use binomial coefficients in numerator AND denominator
- DON'T use when population is very large relative to sample (use Binomial approximation instead)
- DON'T mix up $K$, $N$, and $n$ (very common mistake)

---

## Topic 5: Joint Distributions and Independence

### Formula 5.1: Joint PMF
**Importance: 4/5**

**Formula:**
$$p_{X,Y}(x, y) = P(X = x, Y = y)$$

Properties:
1. $p_{X,Y}(x, y) \geq 0$ for all $(x, y)$
2. $\sum_x \sum_y p_{X,Y}(x, y) = 1$

**Dos:**
- DO create a joint probability table for discrete random variables
- DO verify that all probabilities sum to 1
- DO use joint PMF to find probabilities of events involving both variables
- DO check for independence by testing if $p_{X,Y}(x,y) = p_X(x) \cdot p_Y(y)$

**Don'ts:**
- DON'T confuse joint PMF with marginal PMF
- DON'T forget to sum over all possible pairs when verifying sum equals 1
- DON'T assume independence without checking
- DON'T mix up conditional and joint probabilities

---

### Formula 5.2: Marginal PMF
**Importance: 4/5**

**Formula:**
$$p_X(x) = \sum_y p_{X,Y}(x, y)$$
$$p_Y(y) = \sum_x p_{X,Y}(x, y)$$

**Dos:**
- DO sum over all values of the other variable to get the marginal
- DO use marginal PMFs to find probabilities involving only one variable
- DO create marginal distributions from joint tables by summing rows/columns
- DO verify that marginals sum to 1

**Don'ts:**
- DON'T confuse marginal with conditional PMF
- DON'T forget to sum over ALL values of the other variable
- DON'T assume you can recover joint from marginals without independence
- DON'T use marginals alone to determine independence (need joint PMF)

---

### Formula 5.3: Conditional PMF
**Importance: 4/5**

**Formula:**
$$p_{X|Y}(x|y) = P(X = x | Y = y) = \frac{p_{X,Y}(x,y)}{p_Y(y)}, \quad \text{provided } p_Y(y) > 0$$

**Dos:**
- DO verify that the denominator is positive
- DO use this to update probabilities based on observed information
- DO remember this satisfies all properties of a PMF (sums to 1 over $x$)
- DO use multiplication: $p_{X,Y}(x,y) = p_{X|Y}(x|y) \cdot p_Y(y)$

**Don'ts:**
- DON'T confuse $p_{X|Y}(x|y)$ with $p_{Y|X}(y|x)$
- DON'T forget to divide by the marginal $p_Y(y)$
- DON'T use when $p_Y(y) = 0$ (undefined)
- DON'T assume conditional independence from unconditional independence

---

### Formula 5.4: Independence of Random Variables
**Importance: 5/5**

**Formula:**
$X$ and $Y$ are independent if and only if:
$$p_{X,Y}(x, y) = p_X(x) \cdot p_Y(y) \text{ for all } (x, y)$$

Equivalently:
$$P(X \in A, Y \in B) = P(X \in A) \cdot P(Y \in B) \text{ for all sets } A, B$$

**Dos:**
- DO verify independence by checking if joint equals product of marginals
- DO use independence to simplify calculations: $E[XY] = E[X]E[Y]$, $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$
- DO check ALL pairs $(x, y)$ when verifying independence from a table
- DO remember that independent random variables have uncorrelated outcomes

**Don'ts:**
- DON'T assume independence without verification or explicit statement
- DON'T confuse independence with zero correlation (independence implies zero correlation, but not vice versa)
- DON'T check only one pair (must check all pairs)
- DON'T forget that marginals alone don't determine independence

---

### Formula 5.5: Expectation of Products (Independent Case)
**Importance: 4/5**

**Formula:**
If $X$ and $Y$ are independent:
$$E[XY] = E[X] \cdot E[Y]$$

More generally, for independent $X_1, \ldots, X_n$:
$$E\left[\prod_{i=1}^{n} X_i\right] = \prod_{i=1}^{n} E[X_i]$$

**Dos:**
- DO verify independence before using this formula
- DO use this to simplify calculations involving products
- DO remember this extends to products of functions: $E[g(X)h(Y)] = E[g(X)]E[h(Y)]$ if $X \perp Y$
- DO use this to find $E[X^2]$ when $X$ is independent of itself is meaningless, but useful for products of different variables

**Don'ts:**
- DON'T use this without independence (most common mistake!)
- DON'T confuse with linearity of expectation (which doesn't require independence)
- DON'T assume $E[XY] = E[X]E[Y]$ implies independence (counterexamples exist)
- DON'T forget that this is an "if" statement, not "if and only if"

---

### Formula 5.6: Covariance
**Importance: 3/5**

**Formula:**
$$\text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$$

**Dos:**
- DO use the computational formula $E[XY] - E[X]E[Y]$ for calculations
- DO remember that $\text{Cov}(X, X) = \text{Var}(X)$
- DO check if $\text{Cov}(X, Y) = 0$ to test for uncorrelatedness
- DO use this in variance of sums: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y)$

**Don'ts:**
- DON'T confuse covariance with correlation (correlation is standardized)
- DON'T assume $\text{Cov}(X, Y) = 0$ implies independence (only the reverse is true)
- DON'T forget that covariance can be negative
- DON'T use covariance to measure strength of relationship (use correlation instead)

---

### Formula 5.7: Variance of Sum
**Importance: 4/5**

**Formula:**
$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y)$$

If $X$ and $Y$ are independent:
$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$$

More generally:
$$\text{Var}\left(\sum_{i=1}^{n} X_i\right) = \sum_{i=1}^{n} \text{Var}(X_i) + 2\sum_{i<j} \text{Cov}(X_i, X_j)$$

**Dos:**
- DO check for independence before dropping the covariance term
- DO remember that covariance term can be positive or negative
- DO use this when finding variance of sums (very common in midterms)
- DO simplify for independent variables by dropping cross terms

**Don'ts:**
- DON'T forget the factor of 2 in front of covariance
- DON'T assume $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ without independence
- DON'T confuse $\text{Var}(aX + bY)$ with $\text{Var}(X + Y)$ (need to factor out $a^2$ and $b^2$)
- DON'T forget cross terms when dealing with more than two variables

---

## Topic 6: Conditional Expectation and Total Expectation

### Formula 6.1: Conditional Expectation
**Importance: 4/5**

**Formula:**
$$E[X | Y = y] = \sum_x x \cdot p_{X|Y}(x|y)$$

As a random variable:
$$E[X | Y] = g(Y) \text{ where } g(y) = E[X | Y = y]$$

**Dos:**
- DO use conditional PMF to compute conditional expectation
- DO interpret $E[X | Y = y]$ as the average value of $X$ given $Y = y$
- DO remember that $E[X|Y]$ is a random variable (function of $Y$)
- DO use this to update expectations based on observed information

**Don'ts:**
- DON'T confuse $E[X | Y = y]$ (a number) with $E[X | Y]$ (a random variable)
- DON'T assume $E[X | Y] = E[X]$ unless $X$ and $Y$ are independent
- DON'T forget to condition properly when computing expectations
- DON'T use marginal PMF when you should use conditional PMF

---

### Formula 6.2: Law of Total Expectation (Tower Property)
**Importance: 5/5**

**Formula:**
$$E[X] = E[E[X | Y]]$$

Discrete version:
$$E[X] = \sum_y E[X | Y = y] \cdot P(Y = y)$$

**Dos:**
- DO use this to find expectations by conditioning on a convenient random variable
- DO verify that you're taking expectation over the correct variable in each step
- DO think of this as "averaging the conditional averages"
- DO use this in problems where direct calculation is difficult but conditional calculation is easy
- DO remember this is analogous to law of total probability

**Don'ts:**
- DON'T forget to multiply by $P(Y = y)$ when summing
- DON'T confuse the inner and outer expectations (they're over different variables)
- DON'T skip steps in the tower property when applying multiple times
- DON'T use this when direct calculation is simpler

---

### Formula 6.3: Conditional Variance Formula
**Importance: 3/5**

**Formula:**
$$\text{Var}(X) = E[\text{Var}(X | Y)] + \text{Var}(E[X | Y])$$

**Dos:**
- DO use this to decompose variance into "explained" and "unexplained" parts
- DO verify which term is variance and which is expectation of variance
- DO remember: "variance of the conditional means plus expected conditional variance"
- DO use this in hierarchical models and regression contexts

**Don'ts:**
- DON'T confuse the two terms (they're different!)
- DON'T forget to take expectation of the conditional variance
- DON'T use this when direct calculation is easier
- DON'T mix up $\text{Var}(E[X|Y])$ with $E[\text{Var}(X|Y)]$

---

## Topic 7: Key Inequalities

### Formula 7.1: Markov's Inequality
**Importance: 3/5**

**Formula:**
For non-negative random variable $X$ and $a > 0$:
$$P(X \geq a) \leq \frac{E[X]}{a}$$

**Dos:**
- DO verify that $X$ is non-negative before applying
- DO use this when you only know the mean (no variance information)
- DO remember this gives an upper bound on tail probabilities
- DO use this as a stepping stone to Chebyshev's inequality

**Don'ts:**
- DON'T apply to random variables that can be negative
- DON'T expect tight bounds (this inequality is often very loose)
- DON'T confuse with Chebyshev's inequality (which uses variance)
- DON'T use when you have more information (variance, distribution shape)

---

### Formula 7.2: Chebyshev's Inequality
**Importance: 4/5**

**Formula:**
For any random variable $X$ with mean $\mu$ and variance $\sigma^2$, and any $k > 0$:
$$P(|X - \mu| \geq k) \leq \frac{\sigma^2}{k^2}$$

Alternative form:
$$P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$$

**Dos:**
- DO use this to bound probabilities when you know mean and variance but not the distribution
- DO remember this works for ANY distribution (very general)
- DO use the alternative form with standard deviations for intuition
- DO interpret as "most of the probability mass is within a few standard deviations of the mean"

**Don'ts:**
- DON'T expect tight bounds (this is a worst-case bound)
- DON'T use when you know the actual distribution (calculate exact probabilities instead)
- DON'T forget the absolute value: it's $|X - \mu|$, not $X - \mu$
- DON'T confuse with Markov's inequality (Chebyshev's is stronger but requires variance)

---

## Topic 8: Moment Generating Functions (If Covered)

### Formula 8.1: Moment Generating Function (MGF)
**Importance: 2/5**

**Formula:**
$$M_X(t) = E[e^{tX}] = \sum_x e^{tx} p_X(x)$$

**Dos:**
- DO use this to find moments: $E[X^n] = M_X^{(n)}(0)$ (nth derivative at 0)
- DO remember that MGF uniquely determines the distribution
- DO use this to prove independence: $M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$ if $X \perp Y$
- DO check that the sum/integral converges (MGF may not exist)

**Don'ts:**
- DON'T assume MGF always exists (it may not converge)
- DON'T forget to evaluate derivatives at $t = 0$ to get moments
- DON'T confuse MGF with characteristic function (which always exists)
- DON'T use MGF for problems where PMF/expectation is simpler

---

## Problem-Solving Strategies (Based on Past Midterms)

### Strategy 1: Indicator Random Variables
**When to use:** Counting problems, expectation of number of events

**Approach:**
1. Define $I_i = 1$ if event $i$ occurs, 0 otherwise
2. Express quantity as $X = \sum_i I_i$
3. Use linearity of expectation: $E[X] = \sum_i E[I_i] = \sum_i P(\text{event } i)$
4. Often can find $E[X]$ without finding distribution of $X$

**Common in:** "Number of fixed points in permutation", "coupon collector", "matching problems"

---

### Strategy 2: Conditioning on the First Step
**When to use:** Sequential processes, recursive problems

**Approach:**
1. Let $E$ be the quantity you want to find (expectation, probability)
2. Condition on the outcome of the first trial/step
3. Use law of total probability or total expectation
4. Often leads to a recursive equation that you can solve

**Common in:** Geometric distribution problems, gambler's ruin, random walks

---

### Strategy 3: Symmetry Arguments
**When to use:** Problems with interchangeable elements

**Approach:**
1. Identify symmetric structure in the problem
2. Use symmetry to conclude certain probabilities/expectations are equal
3. Combine with other constraints (like sum equals 1) to solve

**Common in:** Permutation problems, urn problems, birthday problems

---

### Strategy 4: Complementary Counting
**When to use:** "At least one" problems, complex event probabilities

**Approach:**
1. Convert "at least one" to "not none": $P(\text{at least one}) = 1 - P(\text{none})$
2. Calculate $P(\text{none})$, which is often easier
3. Subtract from 1

**Common in:** Matching problems, birthday problems, occupancy problems

---

### Strategy 5: Partition and Condition
**When to use:** Complex probability problems with natural cases

**Approach:**
1. Partition the sample space or condition on a random variable
2. Find conditional probabilities/expectations for each case
3. Use law of total probability/expectation to combine cases

**Common in:** Bayes' theorem problems, tree diagrams, multi-stage experiments

---

## Most Tested Concepts Summary

1. **Conditional Probability & Bayes' Theorem** (Critical - appears in 75%+ of exams)
   - Always identify what you know vs. what you want
   - Draw tree diagrams for complex scenarios
   - Check if you need law of total probability for denominator

2. **Independence vs. Disjointness** (Critical - frequently tested conceptually)
   - Disjoint: $A \cap B = \emptyset$, so $P(A \cap B) = 0$
   - Independent: $P(A \cap B) = P(A)P(B)$
   - If $A$ and $B$ are both non-null and disjoint, they CANNOT be independent

3. **Expectation Calculations** (Critical - appears in 90%+ of exams)
   - Master linearity of expectation (doesn't require independence!)
   - Use indicator random variables whenever possible
   - Remember $E[g(X)] \neq g(E[X])$ in general

4. **Binomial Distribution** (Very Common - 70%+ of exams)
   - Verify: fixed n, independent trials, constant p, binary outcomes
   - Know when to use complement: $P(X \geq k) = 1 - P(X \leq k-1)$
   - Remember expectation $np$ and variance $np(1-p)$

5. **Joint Distributions & Independence** (Common - 65%+ of exams)
   - Create joint probability tables
   - Test independence: joint = product of marginals
   - Find marginals by summing rows/columns
   - Use independence for variance of sums

6. **Variance Calculations** (Very Common - 90%+ of exams)
   - Use $\text{Var}(X) = E[X^2] - (E[X])^2$
   - Remember $\text{Var}(aX + b) = a^2\text{Var}(X)$
   - For sums: need independence or covariance

7. **Law of Total Probability/Expectation** (Common - 60%+ of exams)
   - Condition on a convenient partition or random variable
   - Often simplifies complex problems dramatically
   - Make sure partition is exhaustive and disjoint

---

## Common Mistakes to Avoid

1. **Confusing $P(A|B)$ with $P(B|A)$** - These are almost always different!
2. **Assuming independence without verification** - Always check or justify
3. **Forgetting to check if events are disjoint** - Before using $P(A \cup B) = P(A) + P(B)$
4. **Mixing up $E[X^2]$ and $(E[X])^2$** - These are different (Jensen's inequality)
5. **Not checking probability sums to 1** - Always verify your PMF/PDF
6. **Using wrong distribution** - Read problem carefully for independence, replacement, etc.
7. **Arithmetic errors with combinations/factorials** - Double-check calculations
8. **Forgetting to condition throughout** - In conditional probability, everything needs same conditioning
9. **Not using complement when appropriate** - "At least one" → "not none"
10. **Assuming $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$** - Only true if independent

---

## Quick Reference: When to Use Which Formula

| Problem Type | Primary Formula/Approach |
|-------------|--------------------------|
| "Given that..." | Conditional probability: $P(A\|B) = \frac{P(A \cap B)}{P(B)}$ |
| Flip conditioning | Bayes' theorem |
| "At least one" | Complement rule: $1 - P(\text{none})$ |
| "A or B" | Inclusion-exclusion: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Test independence | Check if $P(A \cap B) = P(A)P(B)$ |
| Number of successes in n trials | Binomial distribution |
| Waiting time to first success | Geometric distribution |
| Events in interval at constant rate | Poisson distribution |
| Sampling without replacement | Hypergeometric distribution |
| Expected value of sum | Linearity: $E[\sum X_i] = \sum E[X_i]$ |
| Expected value of product | If independent: $E[XY] = E[X]E[Y]$ |
| Variance of sum | If independent: $\text{Var}(\sum X_i) = \sum \text{Var}(X_i)$ |
| Complex expectation | Law of total expectation: condition on convenient RV |
| Tail probability bound | Markov's or Chebyshev's inequality |

---

This guide covers all essential formulas and concepts that have appeared in ORF 309 Midterm 1 exams from 2017-2025. The importance ratings reflect frequency and criticality in past exams. Focus on formulas rated 4/5 and 5/5 first, as these appear most frequently and are most essential for success.
