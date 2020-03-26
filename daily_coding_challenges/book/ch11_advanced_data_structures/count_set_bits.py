"""
Count the number of set bits in a given integer.
"""

from collections import namedtuple


def countBits(num):
    n = num
    total = 0
    while n > 0:
        total += n & 1
        n >>= 1
    return total


def test():
    Case = namedtuple("Case", ["param", "expected"])
    table = [Case(7, 3), Case(1, 1), Case(8, 1), Case(6, 2)]
    for c in table:
        actual = countBits(c.param)
        assert actual == c.expected
