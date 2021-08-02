"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-sock-merchant/problem

"""

from collections import namedtuple, Counter


def sockMerchant(n, ar):
    counts = Counter(ar)
    return sum([v // 2 for v in counts.values()])


Case = namedtuple("Case", ["n", "arr", "expected"])


def test():
    cases = [Case(9, [10, 20, 20, 10, 10, 30, 50, 10, 20], 3)]

    for c in cases:
        actual = sockMerchant(c.n, c.arr)
        assert actual == c.expected
