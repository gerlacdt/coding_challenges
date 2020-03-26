"""The child runs up a stairways with n stairs. The child can do 1, 2
or 3 steps a time.

How many possible ways can the child run up the stairs?

"""

from collections import namedtuple


def stairs(n: int, k: int = 3) -> int:
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    else:
        result = 0
        for i in range(1, k+1):
            result += stairs(n - i, k)
        return result


def test3Steps():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [Case(0, 1), Case(1, 1), Case(2, 2),
             Case(3, 4),
             Case(4, 7), Case(5, 13)]
    for c in cases:
        actual = stairs(c.input)
        assert actual == c.expected


def test2Steps():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [
        Case(0, 1),
        Case(1, 1),
        Case(2, 2),
        Case(3, 3),
        Case(4, 5),
        Case(5, 8)
    ]
    for c in cases:
        actual = stairs(c.input, 2)
        assert actual == c.expected
