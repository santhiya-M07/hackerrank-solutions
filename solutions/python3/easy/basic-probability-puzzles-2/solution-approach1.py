# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/basic-probability-puzzles-2/problem?isFullScreen=true
# Problem     Day 2: Basic Probability Puzzles #2
# Difficulty  Easy
# Subdomain   Probability & Statistics - Foundations
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:08 a.m.
# Technique   brute-force-nested-loops
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through all possible outcomes of two six-sided dice to count pairs that satisfy the distinctness and sum constraints.
# Interview   Before: "How would you calculate the probability of a specific sum with two dice?" After: "I iterate through all 36 possible outcomes in O(1) time, filtering for distinct values that sum to 6, then reduce the resulting fraction."
# Pitfalls    (1) Failing to exclude cases where the dice values are equal, as the problem explicitly requires the values to be different.  (2) Incorrectly calculating the total sample space size for two six-sided dice as 12 instead of 36.
# ──────────────────────────────────────────────────

from fractions import Fraction

count = 0

for i in range(1, 7):
    for j in range(1, 7):
        if i != j and i + j == 6:
            count += 1

print(Fraction(count, 36))
