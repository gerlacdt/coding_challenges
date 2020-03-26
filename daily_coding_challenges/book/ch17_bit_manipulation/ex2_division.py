"""Implement division of two positive integers without using the
division, multiplication, or module operators. Return the quotient as
an integer, ignoring the remainder.  """

from collections import namedtuple


def divNaive(a, b):
    "Calculates a/b. Checks how many times b fits in a."
    current = a
    count = 0
    while current > 0:
        current -= b
        count += 1
    return count


def div(a, b):
    "Calculates a/b"
    remainder = a
    power = 32
    b_power = b << 32
    quotient = 0

    while remainder >= b:
        while b_power > remainder:
            b_power >>= 1
            power -= 1
        remainder -= b_power
        quotient += 1 << power

    return quotient


Case = namedtuple("Case", ["input", "expected"])


def test():
    cases = [
        Case((10, 5), 2),
        Case((31, 3), 10),
        Case((31, 2), 15),
        Case((301, 20), 15),
    ]
    for c in cases:
        a, b = c.input
        actual = div(a, b)
        actual2 = divNaive(a, b)
        assert actual == c.expected
