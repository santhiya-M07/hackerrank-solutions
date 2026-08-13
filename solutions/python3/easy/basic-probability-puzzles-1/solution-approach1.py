# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/basic-probability-puzzles-1/problem?isFullScreen=true
# Problem     Day 2: Basic Probability Puzzles #1 
# Difficulty  Easy
# Subdomain   Probability & Statistics - Foundations
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:07 a.m.
# ──────────────────────────────────────────────────

from fractions import Fraction

favorable = 0
total = 0

for i in range(1, 7):
    for j in range(1, 7):
        total += 1
        if i + j <= 9:
            favorable += 1

print(Fraction(favorable, total))
