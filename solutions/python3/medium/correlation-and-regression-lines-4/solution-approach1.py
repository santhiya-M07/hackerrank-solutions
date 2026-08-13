# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/correlation-and-regression-lines-4/problem?isFullScreen=true
# Problem     Correlation and Regression Lines - A Quick Recap #4
# Difficulty  Medium
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:20 a.m.
# Technique   linear-equation-substitution
# Time        O(1)
# Space       O(1)
# Insight     The solution calculates the value of x by rearranging the given regression line equation of x on y to isolate x and substituting the provided value of y.
# Interview   Before: "How would you find x given the regression line of x on y?" After: "I isolate x in the equation 20x - 9y - 107 = 0 to get x = (9y + 107) / 20, resulting in an O(1) time and space complexity calculation."
# Pitfalls    (1) Confusing the regression line of y on x with the regression line of x on y when substituting the given variable.  (2) Failing to format the output to exactly one decimal place as required by the problem statement.
# ──────────────────────────────────────────────────

y = 7

x = (9 * y + 107) / 20

print(f"{x:.1f}")
