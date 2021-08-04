"""
https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem

"""

from collections import namedtuple
from typing import List

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr: List[int]):
    n = len(arr)
    pos = zero = neg = 0

    for v in arr:
        if v < 0:
            neg += 1
        elif v > 0:
            pos += 1
        else:
            zero += 1

    print("{:.6f}".format(pos / n))
    print("{:.6f}".format(neg / n))
    print("{:.6f}".format(zero / n))

    return [
        "{:.6f}".format(pos / n),
        "{:.6f}".format(neg / n),
        "{:.6f}".format(zero / n),
    ]


Case = namedtuple("Case", ["arr", "expected"])


def test():
    cases = [Case([1, 1, 0, -1, -1], ["0.400000", "0.400000", "0.200000"])]

    for c in cases:
        actual = plusMinus(c.arr)
        assert actual == c.expected
