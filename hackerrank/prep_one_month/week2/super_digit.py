"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-recursive-digit-sum/problem

"""

from collections import namedtuple


def superDigit(n, k):
    startSuperDigit = sum([int(c) for c in n]) * k
    result = str(startSuperDigit)
    while len(result) > 1:
        result = str(sum([int(c) for c in result]))
    return int(result)


Case = namedtuple("Case", ["n", "k", "expected"])


def test():
    cases = [Case("9875", 4, 8)]

    for c in cases:
        actual = superDigit(c.n, c.k)
        assert actual == c.expected
