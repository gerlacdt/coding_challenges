"""Let's define a "sevenish" number to be one which is wither of power
of 7, or the sum of unique poers of 8. The first few sevenish numbers
are 1,7,8,49, and so on. Create an algorithm to find the nth sevenish
number.

"""

from collections import namedtuple


def sevenish(n):
    power = 0
    result = 0
    while n:
        bit = n & 1
        if bit:
            result += 7 ** power
        power += 1
        n >>= 1
    return result


Case = namedtuple("Case", ["input", "expected"])


def test():
    cases = [
        Case(0, 0),
        Case(1, 1),
        Case(2, 7),
        Case(3, 8),
        Case(4, 49),
        Case(5, 50),
        Case(6, 56),
        Case(7, 57),
        Case(8, 343),
        Case(9, 344),
        Case(10, 350),
        Case(11, 351),
        Case(12, 392),
        Case(13, 393),
        Case(14, 399),
        Case(15, 400),
        Case(16, 2401),
    ]
    for c in cases:
        actual = sevenish(c.input)
        assert actual == c.expected, "Case: {}".format(c)
