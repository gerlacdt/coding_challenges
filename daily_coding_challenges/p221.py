"""Good morning! Here's your coding interview problem for today.

This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of
7, or the sum of unique powers of 7. The first few sevenish numbers
are 1, 7, 8, 49, and so on. Create an algorithm to find the nth
sevenish number.

"""

from collections import namedtuple


def sevenish(n):
    result = []
    cpow = 0
    sevenpows = [0]
    while len(result) < n:
        current = 7 ** cpow
        for v in sevenpows:
            result.append(current + v)
        sevenpows.append(current)
        cpow += 1
    return result[n-1]


def test():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [
        Case(1, 1),
        Case(2, 7),
        Case(3, 8),
        Case(4, 49),
        Case(5, 50),
        Case(6, 56),
        Case(7, 7**3),
        Case(8, 7**3+1),
        Case(9, 7**3+7),
        Case(10, 7**3+49),
    ]

    for c in cases:
        actual = sevenish(c.input)
        assert actual == c.expected, "Case: {}".format(c)
