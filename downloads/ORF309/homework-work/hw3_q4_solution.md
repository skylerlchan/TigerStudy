# ORF 309 Homework 3 - Question 4: Love Triangles

## Detailed Step-by-Step Solution

---

## Problem Setup

A dating website has $n$ people signed up. For every pair of people, the website independently flips a coin that comes up heads with probability $p$. If heads, the pair is matched. A **love triangle** is a set of three people who are all mutually matched.

---

## Part (a): Expected Number of Hookups for a Given Individual

### Step 1: Identify the Random Experiment

Fix a particular person, call them Person 1. There are $n - 1$ other people on the site. For each of these $n - 1$ other people, the website independently flips a coin with probability $p$ of heads.

### Step 2: Define Indicator Variables

For each person $j \in \{2, 3, \ldots, n\}$, define an indicator random variable:

$$X_j = \begin{cases} 1 & \text{if Person 1 is matched with Person } j \\ 0 & \text{otherwise} \end{cases}$$

Each $X_j$ is a Bernoulli random variable with $P(X_j = 1) = p$.

### Step 3: Express the Total Hookups as a Sum

The total number of hookups Person 1 has is:

$$H = \sum_{j=2}^{n} X_j$$

### Step 4: Apply Linearity of Expectation

$$E[H] = E\left[\sum_{j=2}^{n} X_j\right] = \sum_{j=2}^{n} E[X_j] = \sum_{j=2}^{n} p = (n-1)p$$

### Answer

$$\boxed{E[\text{hookups}] = (n-1)p}$$

---

## Part (b): Probability That a Given Individual Has More Than One Hookup

### Step 1: Identify the Distribution

From Part (a), the number of hookups for Person 1 is $H = \sum_{j=2}^{n} X_j$, where each $X_j$ is an independent Bernoulli($p$) random variable.

The sum of $n - 1$ independent Bernoulli($p$) random variables follows a **Binomial distribution**:

$$H \sim \text{Binomial}(n-1, p)$$

### Step 2: Use the Complement

We want $P(H > 1)$. It is easier to compute this via the complement:

$$P(H > 1) = 1 - P(H \leq 1) = 1 - P(H = 0) - P(H = 1)$$

### Step 3: Compute $P(H = 0)$

Using the Binomial PMF:

$$P(H = 0) = \binom{n-1}{0} p^0 (1-p)^{n-1} = (1-p)^{n-1}$$

This is the probability that none of the $n - 1$ coin flips come up heads.

### Step 4: Compute $P(H = 1)$

$$P(H = 1) = \binom{n-1}{1} p^1 (1-p)^{n-2} = (n-1)p(1-p)^{n-2}$$

This is the probability that exactly one of the $n - 1$ flips comes up heads.

### Step 5: Combine

$$P(H > 1) = 1 - (1-p)^{n-1} - (n-1)p(1-p)^{n-2}$$

### Answer

$$\boxed{P(\text{more than one hookup}) = 1 - (1-p)^{n-1} - (n-1)p(1-p)^{n-2}}$$

---

## Part (c): Expected Number of Love Triangles on the Entire Site

### Step 1: Enumerate All Possible Triangles

A love triangle requires choosing 3 people out of $n$. The number of ways to choose 3 people is:

$$\binom{n}{3} = \frac{n(n-1)(n-2)}{6}$$

### Step 2: Define Indicator Variables for Each Triple

For each triple of people $\{i, j, k\}$, define:

$$T_{ijk} = \begin{cases} 1 & \text{if } \{i, j, k\} \text{ form a love triangle} \\ 0 & \text{otherwise} \end{cases}$$

The total number of love triangles on the site is:

$$L = \sum_{\{i,j,k\}} T_{ijk}$$

where the sum is over all $\binom{n}{3}$ triples.

### Step 3: Compute $P(T_{ijk} = 1)$ for a Given Triple

For $\{i, j, k\}$ to be a love triangle, **all three pairs** must be matched:

- Pair $(i, j)$ matched: probability $p$
- Pair $(i, k)$ matched: probability $p$
- Pair $(j, k)$ matched: probability $p$

Since the coin flips for different pairs are **independent**, the probability that all three pairs are matched is:

$$P(T_{ijk} = 1) = p \cdot p \cdot p = p^3$$

### Step 4: Apply Linearity of Expectation

$$E[L] = E\left[\sum_{\{i,j,k\}} T_{ijk}\right] = \sum_{\{i,j,k\}} E[T_{ijk}] = \sum_{\{i,j,k\}} p^3 = \binom{n}{3} \cdot p^3$$

Note: Linearity of expectation applies regardless of whether the $T_{ijk}$ are independent (and they are **not** independent, since triangles can share edges). This is precisely why linearity of expectation is so powerful here.

### Step 5: Simplify

$$E[L] = \frac{n(n-1)(n-2)}{6} \cdot p^3$$

### Answer

$$\boxed{E[\text{love triangles}] = \frac{n(n-1)(n-2)}{6} \, p^3}$$
