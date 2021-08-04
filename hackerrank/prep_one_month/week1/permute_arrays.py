"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/problem

"""

from collections import namedtuple


def twoArrays(k, A, B):
    assert len(A) == len(B)
    a = sorted(A)
    b = list(reversed(sorted(B)))

    for i in range(len(A)):
        if a[i] + b[i] < k:
            return "NO"

    return "YES"


Case = namedtuple("Case", ["k", "A", "B", "expected"])


def test():
    cases = [
        Case(5, [1, 2, 2, 1], [3, 3, 3, 4], "NO"),
        Case(2, [2, 1, 3], [7, 8, 9], "YES"),
    ]

    for c in cases:
        actual = twoArrays(c.k, c.A, c.B)
        assert actual == c.expected
