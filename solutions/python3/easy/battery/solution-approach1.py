# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/battery/problem?isFullScreen=true
# Problem     Laptop Battery Life
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:25 a.m.
# ──────────────────────────────────────────────────

x = float(input())

if x <= 4:
    result = 2 * x
else:
    result = 8

print(f"{result:.2f}")
