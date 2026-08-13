# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/correlation-and-regression-lines-5/problem?isFullScreen=true
# Problem     Correlation and Regression Lines - A Quick Recap #5
# Difficulty  Medium
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:22 a.m.
# Technique   algebraic-regression-coefficient-derivation
# Time        O(1)
# Space       O(1)
# Insight     The variance of y is derived by calculating the correlation coefficient from the product of the two regression slopes and applying the regression coefficient formula.
# Interview   Before: "How do you find the variance of y given two regression lines and the standard deviation of x?" After: "By isolating the slopes b_yx and b_xy, we compute the correlation r, then solve for sigma_y using the regression formula in O(1) time."
# Pitfalls    (1) Confusing the regression line of y on x with x on y when assigning slope values.  (2) Failing to square the standard deviation to obtain the variance as requested by the problem statement.
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
