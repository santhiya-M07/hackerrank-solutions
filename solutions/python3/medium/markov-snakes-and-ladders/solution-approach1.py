# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/markov-snakes-and-ladders/problem?isFullScreen=true
# Problem     Markov's Snakes And Ladders
# Difficulty  Medium
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:36 a.m.
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
