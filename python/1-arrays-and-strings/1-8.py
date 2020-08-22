# Zero Matrix: if a value in an NxM matrix is 0, it's row/col becomes 0

from array import *


def zero_matrix(m: [[]]) -> [[]]:
    zeros = []  # a list of (x,y) tuples
    # Find all 0s as x,y pairs
    for i, r in enumerate(m):
        for j, c in enumerate(r):
            if c == 0:
                zeros.append((i, j))
    # Handle tuples
    for val in zeros:
        x = val[0]
        y = val[1]
        for i in range(0, len(m)):  # dealing with rows
            m[i][y] = 0
        for j in range(0, len(m[0])):  # dealing with cols
            m[x][j] = 0
    return m


# Empty test
assert zero_matrix([[]]) == [[]]

# Single 0 -- outside
assert zero_matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]]) == [
    [0, 0, 0],
    [0, 4, 5],
    [0, 7, 8],
]

# Single 0 -- middle
assert zero_matrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]]) == [
    [1, 0, 3],
    [0, 0, 0],
    [7, 0, 9],
]

# Two 0
assert zero_matrix([[0, 1, 2], [3, 4, 5], [6, 7, 0]]) == [
    [0, 0, 0],
    [0, 4, 0],
    [0, 0, 0],
]

# Three 0
assert zero_matrix([[0, 1, 2], [3, 0, 5], [6, 7, 0]]) == [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
