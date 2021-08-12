"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-tower-breakers-1/problem

"""

from collections import namedtuple


def towerBreakers(n, m):
    if m == 1:
        return 2
    return 2 if n % 2 == 0 else 1


Case = namedtuple("Case", ["n", "m", "expected"])


def test():
    cases = [Case(2, 2, 2), Case(1, 4, 1)]

    for c in cases:
        actual = towerBreakers(c.n, c.m)
        assert actual == c.expected
