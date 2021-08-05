"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-tower-breakers-1/problem

"""

from collections import namedtuple


def towerBreakers(n, m):
    pass


Case = namedtuple("Case", ["n", "m", "expected"])


def test():
    cases = [Case()]

    for c in cases:
        actual = towerBreakers(c.n, c.m)
        assert actual == c.expected
