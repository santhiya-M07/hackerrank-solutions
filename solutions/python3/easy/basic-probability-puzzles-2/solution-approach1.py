# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/basic-probability-puzzles-2/problem?isFullScreen=true
# Problem     Day 2: Basic Probability Puzzles #2
# Difficulty  Easy
# Subdomain   Probability & Statistics - Foundations
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:08 a.m.
# ──────────────────────────────────────────────────

from fractions import Fraction

count = 0

for i in range(1, 7):
    for j in range(1, 7):
        if i != j and i + j == 6:
            count += 1

print(Fraction(count, 36))
