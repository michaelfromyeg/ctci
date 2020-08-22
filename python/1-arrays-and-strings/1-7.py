# Rotate Matrix: rotate an NxN matrix by 90 deg
# TODO: do this in place

from array import *
import itertools


def rotate_matrix(m: [[]]) -> [[]]:  # Not sure if it's possible to enforce 2D int array
    if len(m) <= 1:
        return m

    # Initialize a new matrix
    temp = itertools.count(1)
    new = [
        [next(temp) for i in range(len(m))] for i in range(len(m))
    ]  # create outer arrays of inner arrays

    for i, r in enumerate(m):  # for each row
        for j, c in enumerate(r):  # for each cell
            new[j][len(m) - 1 - i] = c
    return new


assert rotate_matrix([[]]) == [[]]
assert rotate_matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]]) == [
    [6, 3, 0],
    [7, 4, 1],
    [8, 5, 2],
]
