"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-drawing-book/problem

"""

from collections import namedtuple


def pageCount(n, p):
    total = n // 2
    forward = p // 2
    backward = total - forward
    return forward if forward <= backward else backward


Case = namedtuple("Case", ["n", "p", "expected"])


def test():
    cases = [Case(5, 3, 1), Case(10, 8, 1), Case(6, 2, 1), Case(5, 4, 0)]

    for c in cases:
        actual = pageCount(c.n, c.p)
        assert actual == c.expected, "n={} p={}".format(c.n, c.p)
