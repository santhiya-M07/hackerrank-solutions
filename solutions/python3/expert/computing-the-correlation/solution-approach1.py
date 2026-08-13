# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/computing-the-correlation/problem?isFullScreen=true
# Problem     Day 5: Computing the Correlation
# Difficulty  Expert
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:35 a.m.
# Technique   pearson-correlation-coefficient-calculation
# Time        O(N)
# Space       O(N)
# Insight     The Pearson correlation coefficient is computed by calculating the sums of products and squares of two vectors in linear time.
# Interview   Before: "How do I calculate the correlation between two large datasets without external libraries?" After: "I implement the Pearson formula using single-pass summation, achieving O(N) time complexity, which is efficient for the 500,000 student constraint."
# Pitfalls    (1) Floating point precision errors may occur if the denominator is extremely close to zero.  (2) The formula requires exactly two decimal places, so failing to use formatted output will result in incorrect answers.  (3) Input reading must handle tab-separated values correctly to avoid parsing errors.
# ──────────────────────────────────────────────────

import math

n = int(input())

m = []
p = []
c = []

for _ in range(n):
    a, b, d = map(int, input().split())
    m.append(a)
    p.append(b)
    c.append(d)

def correlation(x, y):
    sx = sum(x)
    sy = sum(y)
    sxx = sum(v * v for v in x)
    syy = sum(v * v for v in y)
    sxy = sum(x[i] * y[i] for i in range(n))

    numerator = n * sxy - sx * sy
    denominator = math.sqrt((n * sxx - sx * sx) * (n * syy - sy * sy))

    return numerator / denominator

print(f"{correlation(m, p):.2f}")
print(f"{correlation(p, c):.2f}")
print(f"{correlation(c, m):.2f}")
