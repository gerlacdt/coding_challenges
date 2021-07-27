"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/problem

"""

from collections import namedtuple
import sys


def miniMaxSum(arr):
    globalMin = sys.float_info.max
    globalMax = -99999

    for i in range(len(arr)):
        total = sum(arr[0:i]) + sum(arr[i + 1 :])
        if total < globalMin:
            globalMin = total
        if total > globalMax:
            globalMax = total

    print("{} {}".format(globalMin, globalMax))

    return (globalMin, globalMax)


Case = namedtuple("Case", ["arr", "expected"])


def test():
    cases = [Case([1, 3, 5, 7, 9], (16, 24))]

    for c in cases:
        actual = miniMaxSum(c.arr)
        assert actual == c.expected
