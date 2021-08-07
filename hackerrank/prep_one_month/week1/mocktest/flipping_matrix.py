"""Flip the matrix rows and columns so that the sum of the upper left nxn
sub-matrix is maximal.


https://www.hackerrank.com/challenges/flipping-the-matrix/problem

"""

from collections import namedtuple


def flippingMatrix(matrix):
    n = len(matrix)
    s = 0
    for i in range(n // 2):
        for j in range(n // 2):
            # search the maximum value for element: matrix[i][j]
            s += max(
                matrix[i][j],  # current
                matrix[i][n - j - 1],  # same row, flipped column
                matrix[n - i - 1][j],  # flipped row, same column
                matrix[n - i - 1][n - j - 1],  # flipped row, flipped column
            )
    return s


Case = namedtuple("Case", ["matrix", "expected"])


def test():
    cases = [
        Case(
            [
                [112, 42, 83, 119],
                [56, 125, 56, 49],
                [15, 78, 101, 45],
                [62, 98, 114, 108],
            ],
            414,
        )
    ]

    for c in cases:
        actual = flippingMatrix(c.matrix)
        assert actual == c.expected
