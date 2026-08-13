# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/stat-warmup/problem?isFullScreen=true
# Problem     Basic Statistics Warmup
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:33 a.m.
# Technique   sorting-and-frequency-counting
# Time        O(N log N)
# Space       O(N)
# Insight     The implementation calculates descriptive statistics by sorting the array for median determination and using a hash map to identify the smallest mode among those with maximum frequency.
# Interview   Before: "How would you calculate the confidence interval for a sample mean?" After: "I would use the standard deviation and the sample size with the 1.96 z-score constant, resulting in O(N log N) time complexity due to the initial sorting required for the median."
# Pitfalls    (1) Failing to select the numerically smallest integer when multiple elements share the maximum frequency as required by the mode definition.  (2) Incorrectly calculating the median for even-sized arrays by failing to average the two middle elements.  (3) Using the wrong standard deviation formula by omitting the division by N before taking the square root.
# ──────────────────────────────────────────────────

import math
from collections import Counter

# Input
N = int(input())
arr = list(map(int, input().split()))

# Mean
mean = sum(arr) / N

# Median
arr.sort()

if N % 2 == 1:
    median = arr[N // 2]
else:
    median = (arr[N // 2 - 1] + arr[N // 2]) / 2

# Mode
count = Counter(arr)
max_freq = max(count.values())

# Smallest value among modes
mode = min(x for x in count if count[x] == max_freq)

# Standard Deviation
variance = sum((x - mean) ** 2 for x in arr) / N
sd = math.sqrt(variance)

# 95% Confidence Interval
margin = 1.96 * sd / math.sqrt(N)

lower = mean - margin
upper = mean + margin

# Output
print(f"{mean:.1f}")
print(f"{median:.1f}")
print(mode)
print(f"{sd:.1f}")
print(f"{lower:.1f} {upper:.1f}")
