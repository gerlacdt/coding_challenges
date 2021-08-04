"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits/problem

"""

from collections import namedtuple


def flippingBits(n):
    bits = "{:032b}".format(n)
    flipBits = ""
    flipTable = {"1": "0", "0": "1"}
    for b in bits:
        flipBits += flipTable[b]
    result = 0
    for i, b in enumerate(list(reversed(flipBits))):
        if b == "1":
            result += 2 ** i
    return result


Case = namedtuple("Case", ["n", "expected"])


def test():
    cases = [Case(9, 4294967286)]

    for c in cases:
        actual = flippingBits(c.n)
        assert actual == c.expected
