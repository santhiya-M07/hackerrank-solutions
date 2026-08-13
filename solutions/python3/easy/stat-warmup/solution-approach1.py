# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/stat-warmup/problem?isFullScreen=true
# Problem     Basic Statistics Warmup
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:33 a.m.
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
