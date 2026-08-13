# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/basic-probability-puzzles-1/problem?isFullScreen=true
# Problem     Day 2: Basic Probability Puzzles #1 
# Difficulty  Easy
# Subdomain   Probability & Statistics - Foundations
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:07 a.m.
# Technique   nested-loop-brute-force
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through all possible outcomes of two six-sided dice to count the frequency of sums less than or equal to nine.
# Interview   Before: "How would you calculate the probability of a sum for two dice?" After: "I iterate through all 36 combinations in O(1) time, counting those where the sum is at most 9, then simplify the fraction."
# Pitfalls    (1) Misinterpreting the inclusive 'at most' condition as strictly less than.  (2) Assuming the sample space size is not 36 for two six-sided dice.
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
