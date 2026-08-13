# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/correlation-and-regression-lines-5/problem?isFullScreen=true
# Problem     Correlation and Regression Lines - A Quick Recap #5
# Difficulty  Medium
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:22 a.m.
# ──────────────────────────────────────────────────

import math

b_yx = 4 / 5
b_xy = 9 / 20

# r^2 = b_yx * b_xy
r = math.sqrt(b_yx * b_xy)

sigma_x = 3

# b_yx = r * (sigma_y / sigma_x)
sigma_y = (b_yx * sigma_x) / r

variance_y = sigma_y ** 2

print(f"{variance_y:.1f}")
