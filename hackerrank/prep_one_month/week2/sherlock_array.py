"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-sherlock-and-array/problem

"""

from collections import namedtuple


def balancedSums(arr):
    leftSum = 0
    rightSum = sum(arr)
    for i, v in enumerate(arr):
        rightSum = rightSum - v
        if leftSum == rightSum:
            return "YES"
        leftSum += v
    return "NO"


Case = namedtuple(
    "Case",
    ["arr", "expected"],
)


def test():
    cases = [
        Case([1], "YES"),
        Case([5, 6, 8, 11], "YES"),
        Case([1, 2, 3, 3], "YES"),
        Case([1, 2, 3], "NO"),
    ]

    for c in cases:
        actual = balancedSums(c.arr)
        assert actual == c.expected, "Case: {}".format(c.arr)
