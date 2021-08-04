"""
https://www.hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/problem?

"""

from collections import namedtuple


def diagonalDifference(arr):
    d1 = d2 = 0
    # get left-right diagonal
    i = j = 0
    while i < len(arr):
        d1 += arr[i][j]
        i += 1
        j += 1

    # get right-left diagonal
    i = len(arr) - 1
    j = 0
    while i >= 0:
        d2 += arr[i][j]
        i -= 1
        j += 1

    return abs(d1 - d2)


Case = namedtuple("Case", ["arr", "expected"])


def test():
    cases = [
        Case([[1, 2, 3], [4, 5, 6], [9, 8, 9]], 2),
        Case([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15),
    ]
    for c in cases:
        actual = diagonalDifference(c.arr)
        assert actual == c.expected
