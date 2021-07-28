""""

https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem

"""

from collections import namedtuple, Counter


def lonelyinteger(a):
    counter = Counter(a)
    return next(k for k, v in counter.items() if v == 1)


Case = namedtuple("Case", ["arr", "expected"])


def test():
    cases = [Case([1, 2, 3, 4, 3, 2, 1], 4)]

    for c in cases:
        actual = lonelyinteger(c.arr)
        assert actual == c.expected
