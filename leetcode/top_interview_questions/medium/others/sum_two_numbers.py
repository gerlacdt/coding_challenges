"""Calculate the sum of two integers a and b, but you are not allowed to
use the operator + and -.
n
Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

"""

from collections import namedtuple
from time import sleep


class Solution:
    def getSumPositive(self, a: int, b: int) -> int:
        """Does not work with negative integers. Because integer overflow is
in python not like in C or Java."""
        while b != 0:
            # sleep(0.3)
            curry = a & b
            a = a ^ b
            b = curry << 1
        return a

    def getSum(self, a: int, b: int) -> int:
        def add(x, y, curry1):
            if x & y:
                return 1 if curry1 else 0, 1
            if x | y:
                return 0 if curry1 else 1, 1 if curry1 else 0
            return curry1, 0

        aBinaryString = "".join(reversed(toBinaryString(a)))
        bBinaryString = "".join(reversed(toBinaryString(b)))
        result = []
        curry = 0
        for i in range(len(aBinaryString)):
            a1 = int(aBinaryString[i])
            b1 = int(bBinaryString[i])
            r, curry = add(a1, b1, curry)
            result.append(r)

        return toDecimal("".join([str(n) for n in reversed(result)]))


Case = namedtuple("Case", ["a", "b", "expected"])


def testSum():
    sol = Solution()
    cases = [
        Case(1, 2, 3),
        Case(7, 7, 14),
        Case(0, 1, 1),
        Case(0, 0, 0),
        Case(63, 64, 127),
        Case(-1, -1, -2),
        Case(-1, 1, 0),
        Case(-12, -8, -20),
        Case(-128, 0, -128),
        Case(-128, -1, 127),  # overflow with 8-bits
        Case(127, 1, -128),  # overflow with 8-bits
    ]

    for c in cases:
        actual = sol.getSum(c.a, c.b)
        assert actual == c.expected, "Case: {}".format(c)


def toBinaryString(x: int, bits=8) -> str:
    """Return bits-length binary string representation of the given
integer. If x is negative the two-complement is created.
    """
    return "".join(list(reversed([str((x >> i) & 1) for i in range(bits)])))


def toDecimal(s: str) -> int:
    if s[0] == "1":
        # manually convert two complement string in order to get absolute value
        s = "".join(["0" if c == "1" else "1" for c in s])
        return -(int(s[1:], 2) + 1)
    return int(s[1:], 2)


SimpleCase = namedtuple("SimpleCase", ["x", "expected"])


def testBinaryString():
    cases = [
        SimpleCase(6, "00000110"),
        SimpleCase(14, "00001110"),
        SimpleCase(127, "01111111"),
        SimpleCase(1, "00000001"),
        SimpleCase(-1, "11111111"),
        SimpleCase(-2, "11111110"),
        SimpleCase(-3, "11111101"),
        SimpleCase(-4, "11111100"),
    ]
    for c in cases:
        actual = toBinaryString(c.x, 8)
        assert actual == c.expected, "Case: {}".format(c)


def testToDecimal():
    cases = [
        SimpleCase("00000110", 6),
        SimpleCase("00001110", 14),
        SimpleCase("01111111", 127),
        SimpleCase("00000001", 1),
        SimpleCase("11111111", -1),
        SimpleCase("11111110", -2),
        SimpleCase("11111101", -3),
        SimpleCase("11111100", -4),
    ]
    for c in cases:
        actual = toDecimal(c.x)
        assert actual == c.expected, "Case: {}".format(c)
