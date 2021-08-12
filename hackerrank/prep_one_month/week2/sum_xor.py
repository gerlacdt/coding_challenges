"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-sum-vs-xor/problem

"""

from collections import namedtuple


def sumXor(n):
    exponent = 0
    while n > 0:
        exponent += 1 if n % 2 == 0 else 0
        n //= 2
    return 2 ** exponent


Case = namedtuple("Case", ["n", "expected"])


def test():
    cases = [
        Case(4, 4),
        Case(5, 2),
        Case(10, 4),
        Case(1_000_000_000_000_000, 1073741824),
    ]

    for c in cases:
        actual = sumXor(c.n)
        assert actual == c.expected, "Case: {}".format(c.n)
