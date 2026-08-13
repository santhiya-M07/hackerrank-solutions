# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/computing-the-correlation/problem?isFullScreen=true
# Problem     Day 5: Computing the Correlation
# Difficulty  Expert
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:35 a.m.
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
