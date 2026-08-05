# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
# Problem     Python If-Else
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-05, 02:51 p.m.
# Technique   conditional-branching-logic
# Time        O(1)
# Space       O(1)
# Insight     The code evaluates the parity and magnitude of the integer n to determine the output based on four mutually exclusive conditional branches.
# Interview   Before: "How would you handle multiple conditional ranges for an integer?" After: "I use a series of if-elif-else statements to check parity and range constraints, ensuring O(1) time complexity for any input n, including the boundary cases like 2, 5, 6, and 20."
# Pitfalls    (1) Failing to account for the inclusive nature of the ranges 2 to 5 and 6 to 20.  (2) Incorrectly ordering the conditional checks, which could lead to overlapping logic errors.  (3) Neglecting the requirement to print 'Not Weird' for even numbers greater than 20.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
