# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/correlation-and-regression-lines-8/problem?isFullScreen=true
# Problem     Correlation and Regression Lines - A quick recap #3
# Difficulty  Medium
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:19 a.m.
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
