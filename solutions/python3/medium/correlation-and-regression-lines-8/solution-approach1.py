# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/correlation-and-regression-lines-8/problem?isFullScreen=true
# Problem     Correlation and Regression Lines - A quick recap #3
# Difficulty  Medium
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:19 a.m.
# Technique   least-squares-linear-regression
# Time        O(n)
# Space       O(n)
# Insight     The implementation calculates the linear regression line y = mx + c by determining the slope m as the covariance of x and y divided by the variance of x.
# Interview   Before: "How do you predict a dependent variable given an independent one?" After: "You compute the least-squares regression line using the means of both datasets to find the slope and intercept, resulting in an O(n) time complexity for the calculation."
# Pitfalls    (1) Failing to calculate the mean of the datasets correctly before computing the covariance and variance.  (2) Rounding the final prediction prematurely before the final output format requirement.  (3) Confusing the independent variable x with the dependent variable y in the regression formula.
# ──────────────────────────────────────────────────

# Given data
physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

# Calculate means
x_mean = sum(physics) / len(physics)
y_mean = sum(history) / len(history)

# Calculate slope (m)
numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(physics, history))
denominator = sum((x - x_mean) ** 2 for x in physics)

m = numerator / denominator

# Calculate intercept (c)
c = y_mean - m * x_mean

# Predict History score when Physics = 10
x = 10
prediction = m * x + c

print(f"{prediction:.1f}")
