# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/markov-snakes-and-ladders/problem?isFullScreen=true
# Problem     Markov's Snakes And Ladders
# Difficulty  Medium
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:36 a.m.
# Technique   monte-carlo-simulation
# Time        O(T * games * max_rolls)
# Space       O(S + L)
# Insight     The simulation approximates the expected value by averaging the number of die rolls required to reach square 100 across 5000 independent game trials.
# Interview   Before: "How would you calculate the expected number of rolls for this board?" After: "I used a Monte Carlo simulation with 5000 trials to approximate the expected value, which runs in O(T * games * max_rolls) time, ensuring we handle the biased die and board transitions correctly."
# Pitfalls    (1) Failing to handle the rule where rolls resulting in a position greater than 100 are ignored and the player remains at their current square.  (2) Incorrectly assuming the game must terminate, ignoring the requirement to cap simulations at 1000 rolls per game.  (3) Misinterpreting the board input format when the number of snakes or ladders is zero, leading to incorrect input consumption.
# ──────────────────────────────────────────────────

import random

T = int(input())

for _ in range(T):
    prob = list(map(float, input().split(',')))

    ladders, snakes = map(int, input().split(','))

    board = {}

    if ladders > 0:
        for pair in input().split():
            a, b = map(int, pair.split(','))
            board[a] = b
    else:
        input()

    if snakes > 0:
        for pair in input().split():
            a, b = map(int, pair.split(','))
            board[a] = b
    else:
        input()

    rolls_total = 0
    games = 5000

    faces = [1, 2, 3, 4, 5, 6]

    for _ in range(games):
        pos = 1
        rolls = 0

        while pos != 100 and rolls < 1000:
            roll = random.choices(faces, weights=prob)[0]
            rolls += 1

            new_pos = pos + roll

            if new_pos <= 100:
                pos = board.get(new_pos, new_pos)

        if pos == 100:
            rolls_total += rolls

    print(round(rolls_total / games))
