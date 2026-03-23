"""Generate a PDF solution for ORF 309 HW3 Q4 with properly rendered LaTeX math."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import textwrap

OUTPUT_PATH = r"c:\Users\skyle\OneDrive\Desktop\Canvas\downloads\ORF309\solutions\hw3_q4_solution.pdf"

# Enable matplotlib's built-in TeX rendering
plt.rcParams.update({
    'mathtext.fontset': 'cm',
    'font.family': 'serif',
    'font.size': 12,
})

def new_page(pdf, width=8.5, height=11):
    fig = plt.figure(figsize=(width, height))
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')
    return fig, ax

def text(ax, x, y, s, **kwargs):
    defaults = dict(fontsize=11, va='top', ha='left', wrap=False, family='serif')
    defaults.update(kwargs)
    ax.text(x, y, s, transform=ax.transData, **defaults)

def title_text(ax, x, y, s):
    text(ax, x, y, s, fontsize=14, fontweight='bold')

def section_text(ax, x, y, s):
    text(ax, x, y, s, fontsize=13, fontweight='bold')

def step_text(ax, x, y, s):
    text(ax, x, y, s, fontsize=11, fontweight='bold')

def math_text(ax, x, y, s, fontsize=13):
    text(ax, x, y, s, fontsize=fontsize, ha='center')

def body(ax, x, y, s, fontsize=11):
    text(ax, x, y, s, fontsize=fontsize)

def boxed_answer(ax, x, y, s, fontsize=12):
    ax.text(x, y, s, fontsize=fontsize, va='top', ha='center', family='serif',
            bbox=dict(boxstyle='round,pad=0.4', edgecolor='black', facecolor='#f0f0f0', linewidth=1.5))

with PdfPages(OUTPUT_PATH) as pdf:
    # ========== PAGE 1 ==========
    fig, ax = new_page(pdf)

    title_text(ax, 4.25, 10.2, 'ORF 309 Homework 3 — Question 4: Love Triangles')
    ax.plot([0.7, 7.8], [10.0, 10.0], 'k-', linewidth=1)

    section_text(ax, 0.7, 9.6, 'Problem Setup')
    body(ax, 0.7, 9.25, r'A dating website has $n$ people signed up. For every pair of people, the website')
    body(ax, 0.7, 8.95, r'independently flips a coin that comes up heads with probability $p$. If heads, the pair')
    body(ax, 0.7, 8.65, r'is matched. A love triangle is a set of three people who are all mutually matched.')

    ax.plot([0.7, 7.8], [8.3, 8.3], 'k-', linewidth=0.5)

    section_text(ax, 0.7, 8.0, 'Part (a): Expected Number of Hookups for a Given Individual')

    step_text(ax, 0.7, 7.55, 'Step 1: Identify the random experiment.')
    body(ax, 0.7, 7.25, r'Fix a particular person, call them Person 1. There are $n - 1$ other people on the site.')
    body(ax, 0.7, 6.95, r'For each of these $n - 1$ people, the website independently flips a coin with probability')
    body(ax, 0.7, 6.65, r'$p$ of heads.')

    step_text(ax, 0.7, 6.2, 'Step 2: Define indicator variables.')
    body(ax, 0.7, 5.9, r'For each person $j \in \{2, 3, \ldots, n\}$, define:')

    math_text(ax, 4.25, 5.45, r'$X_j = \begin{cases} 1 & \mathrm{if\ Person\ 1\ is\ matched\ with\ Person}\ j \\ 0 & \mathrm{otherwise} \end{cases}$', fontsize=14)

    body(ax, 0.7, 4.85, r'Each $X_j$ is a Bernoulli random variable with $P(X_j = 1) = p$, so $E[X_j] = p$.')

    step_text(ax, 0.7, 4.4, 'Step 3: Express total hookups as a sum.')
    body(ax, 0.7, 4.1, 'The total number of hookups Person 1 has is:')

    math_text(ax, 4.25, 3.7, r'$H = \sum_{j=2}^{n} X_j$', fontsize=14)

    step_text(ax, 0.7, 3.15, 'Step 4: Apply linearity of expectation.')

    math_text(ax, 4.25, 2.7, r'$E[H] = E\left[\sum_{j=2}^{n} X_j\right] = \sum_{j=2}^{n} E[X_j] = \sum_{j=2}^{n} p = (n-1)p$', fontsize=14)

    boxed_answer(ax, 4.25, 2.0, r'$\mathbf{Answer:}\ \ E[\mathrm{hookups}] = (n-1)p$', fontsize=13)

    pdf.savefig(fig)
    plt.close(fig)

    # ========== PAGE 2 ==========
    fig, ax = new_page(pdf)

    section_text(ax, 0.7, 10.2, 'Part (b): Probability of More Than One Hookup')
    ax.plot([0.7, 7.8], [10.0, 10.0], 'k-', linewidth=0.5)

    step_text(ax, 0.7, 9.65, 'Step 1: Identify the distribution.')
    body(ax, 0.7, 9.35, r'From Part (a), $H = \sum_{j=2}^{n} X_j$ where each $X_j$ is an independent Bernoulli($p$).')
    body(ax, 0.7, 9.05, r'The sum of $n-1$ independent Bernoulli($p$) variables follows a Binomial distribution:')

    math_text(ax, 4.25, 8.6, r'$H \sim \mathrm{Binomial}(n-1,\ p)$', fontsize=14)

    step_text(ax, 0.7, 8.1, 'Step 2: Use the complement.')

    math_text(ax, 4.25, 7.65, r'$P(H > 1) = 1 - P(H = 0) - P(H = 1)$', fontsize=14)

    step_text(ax, 0.7, 7.1, r'Step 3: Compute $P(H = 0)$.')

    math_text(ax, 4.25, 6.65, r'$P(H = 0) = \binom{n-1}{0}\, p^0\, (1-p)^{n-1} = (1-p)^{n-1}$', fontsize=14)

    body(ax, 0.7, 6.15, r'This is the probability that none of the $n - 1$ coin flips come up heads.')

    step_text(ax, 0.7, 5.7, r'Step 4: Compute $P(H = 1)$.')

    math_text(ax, 4.25, 5.25, r'$P(H = 1) = \binom{n-1}{1}\, p^1\, (1-p)^{n-2} = (n-1)\,p\,(1-p)^{n-2}$', fontsize=14)

    body(ax, 0.7, 4.75, r'This is the probability that exactly one of the $n - 1$ flips comes up heads.')

    step_text(ax, 0.7, 4.3, 'Step 5: Combine.')

    math_text(ax, 4.25, 3.85, r'$P(H > 1) = 1 - (1-p)^{n-1} - (n-1)\,p\,(1-p)^{n-2}$', fontsize=14)

    boxed_answer(ax, 4.25, 3.1, r'$\mathbf{Answer:}\ \ P(\mathrm{more\ than\ one\ hookup}) = 1 - (1-p)^{n-1} - (n-1)\,p\,(1-p)^{n-2}$', fontsize=12)

    pdf.savefig(fig)
    plt.close(fig)

    # ========== PAGE 3 ==========
    fig, ax = new_page(pdf)

    section_text(ax, 0.7, 10.2, 'Part (c): Expected Number of Love Triangles')
    ax.plot([0.7, 7.8], [10.0, 10.0], 'k-', linewidth=0.5)

    step_text(ax, 0.7, 9.65, 'Step 1: Enumerate all possible triangles.')
    body(ax, 0.7, 9.35, r'A love triangle requires choosing 3 people out of $n$. The number of ways to do this is:')

    math_text(ax, 4.25, 8.9, r'$\binom{n}{3} = \frac{n(n-1)(n-2)}{6}$', fontsize=14)

    step_text(ax, 0.7, 8.3, 'Step 2: Define indicator variables for each triple.')
    body(ax, 0.7, 8.0, r'For each triple of people $\{i, j, k\}$, define:')

    math_text(ax, 4.25, 7.5, r'$T_{ijk} = \begin{cases} 1 & \mathrm{if}\ \{i, j, k\}\ \mathrm{form\ a\ love\ triangle} \\ 0 & \mathrm{otherwise} \end{cases}$', fontsize=14)

    body(ax, 0.7, 6.85, 'The total number of love triangles on the site is:')

    math_text(ax, 4.25, 6.4, r'$L = \sum_{\{i,j,k\}} T_{ijk}$', fontsize=14)

    body(ax, 0.7, 5.9, r'where the sum is over all $\binom{n}{3}$ triples.')

    step_text(ax, 0.7, 5.45, r'Step 3: Compute $P(T_{ijk} = 1)$ for a given triple.')
    body(ax, 0.7, 5.15, r'For $\{i, j, k\}$ to be a love triangle, all three pairs must be matched:')
    body(ax, 1.1, 4.8, r'$\bullet$ Pair $(i, j)$ matched with probability $p$')
    body(ax, 1.1, 4.5, r'$\bullet$ Pair $(i, k)$ matched with probability $p$')
    body(ax, 1.1, 4.2, r'$\bullet$ Pair $(j, k)$ matched with probability $p$')
    body(ax, 0.7, 3.8, 'Since the coin flips for different pairs are independent:')

    math_text(ax, 4.25, 3.35, r'$P(T_{ijk} = 1) = p \cdot p \cdot p = p^3$', fontsize=14)

    step_text(ax, 0.7, 2.8, 'Step 4: Apply linearity of expectation.')

    math_text(ax, 4.25, 2.3, r'$E[L] = \sum_{\{i,j,k\}} E[T_{ijk}] = \sum_{\{i,j,k\}} p^3 = \binom{n}{3} \cdot p^3$', fontsize=14)

    body(ax, 0.7, 1.75, r'Note: Linearity of expectation works even though the $T_{ijk}$ are not independent')
    body(ax, 0.7, 1.45, r'(triangles can share edges). This is why linearity of expectation is so powerful.')

    pdf.savefig(fig)
    plt.close(fig)

    # ========== PAGE 4 ==========
    fig, ax = new_page(pdf)

    step_text(ax, 0.7, 10.2, 'Step 5: Simplify.')

    math_text(ax, 4.25, 9.6, r'$E[L] = \frac{n(n-1)(n-2)}{6} \cdot p^3$', fontsize=16)

    boxed_answer(ax, 4.25, 8.7, r'$\mathbf{Answer:}\ \ E[\mathrm{love\ triangles}] = \dfrac{n(n-1)(n-2)}{6}\, p^3$', fontsize=14)

    pdf.savefig(fig)
    plt.close(fig)

print(f"PDF generated: {OUTPUT_PATH}")
