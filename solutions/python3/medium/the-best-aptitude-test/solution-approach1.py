# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-best-aptitude-test/problem?isFullScreen=true
# Problem     The Best Aptitude Test
# Difficulty  Medium
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:43 a.m.
# ──────────────────────────────────────────────────

import math

T = int(input())

for _ in range(T):
    N = int(input())
    gpa = list(map(float, input().split()))

    tests = []
    for i in range(5):
        tests.append(list(map(float, input().split())))

    def correlation(x, y):
        n = len(x)
        mx = sum(x) / n
        my = sum(y) / n

        num = sum((x[i] - mx) * (y[i] - my) for i in range(n))
        dx = sum((x[i] - mx) ** 2 for i in range(n))
        dy = sum((y[i] - my) ** 2 for i in range(n))

        if dx == 0 or dy == 0:
            return 0

        return num / math.sqrt(dx * dy)

    best_test = 1
    best_corr = -1

    for i in range(5):
        corr = abs(correlation(gpa, tests[i]))

        if corr > best_corr:
            best_corr = corr
            best_test = i + 1

    print(best_test)
