# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/predicting-office-space-price/problem?isFullScreen=true
# Problem     Polynomial Regression: Office Prices
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 09:16 a.m.
# ──────────────────────────────────────────────────

import sys
import numpy as np

# Read input
data = sys.stdin.read().strip().split()
it = iter(data)

F = int(next(it))
N = int(next(it))

# Training data
X = []
Y = []

for _ in range(N):
    row = [float(next(it)) for _ in range(F + 1)]
    X.append(row[:F])
    Y.append(row[F])

# Convert to numpy arrays
X = np.array(X)
Y = np.array(Y)

# Create polynomial features up to degree 3
def polynomial_features(X):
    features = [np.ones(len(X))]

    # Degree 1
    for i in range(F):
        features.append(X[:, i])

    # Degree 2
    for i in range(F):
        for j in range(i, F):
            features.append(X[:, i] * X[:, j])

    # Degree 3
    for i in range(F):
        for j in range(i, F):
            for k in range(j, F):
                features.append(X[:, i] * X[:, j] * X[:, k])

    return np.column_stack(features)

# Generate polynomial training features
A = polynomial_features(X)

# Find regression coefficients
coefficients = np.linalg.lstsq(A, Y, rcond=None)[0]

# Number of test cases
T = int(next(it))

# Predict each test case
for _ in range(T):
    test = np.array([[float(next(it)) for _ in range(F)]])

    test_features = polynomial_features(test)

    prediction = test_features @ coefficients

    print(f"{prediction[0]:.2f}")
