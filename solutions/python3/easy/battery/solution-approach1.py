# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/battery/problem?isFullScreen=true
# Problem     Laptop Battery Life
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:25 a.m.
# Technique   linear-regression-threshold-clipping
# Time        O(1)
# Space       O(1)
# Insight     The model assumes a linear relationship between charging time and battery life up to a saturation point of four hours, after which the battery life remains constant at eight hours.
# Interview   Before: "I should train a complex regression model on the provided dataset." After: "Since the data shows a linear trend that plateaus at four hours, a simple O(1) conditional check is sufficient to predict battery life accurately while minimizing error."
# Pitfalls    (1) Failing to account for the saturation point where battery life caps at eight hours.  (2) Assuming a strictly linear relationship for all input values regardless of the training data distribution.
# ──────────────────────────────────────────────────

x = float(input())

if x <= 4:
    result = 2 * x
else:
    result = 8

print(f"{result:.2f}")
