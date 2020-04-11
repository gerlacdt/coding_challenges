"""Calculate the sum of two integers a and b, but you are not allowed to
use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

"""

from collections import namedtuple
from typing import List


def toBytesReversed(x: int) -> List[int]:
    result = []
    for _ in range(8):
        result.append(x & 1)
        x >>= 1
    return result


def toDecimal(lst: List[int]) -> int:
    result = 0
    for i, n in enumerate(lst):
        result += (2 ** i) * n
    return result


class Solution:
    def getSum(self, a: int, b: int) -> int:
        def add(x, y, curry1):
            # print("x {} y {} curry1 {}".format(x, y, curry1))
            if x & y:
                return 1 if curry1 else 0, 1
            if x | y:
                return 0 if curry1 else 1, 1 if curry1 else 0
            return curry1, 0

        aBinary = toBytesReversed(a)
        bBinary = toBytesReversed(b)
        # print("a {}".format(aBinary))
        # print("b {}".format(bBinary))
        result = []
        curry = 0
        for i in range(len(aBinary)):
            a1 = aBinary[i]
            b1 = bBinary[i]
            r, curry = add(a1, b1, curry)
            # print("r  {} curry {}".format(r, curry))
            result.append(r)

        if curry:
            result.append(curry)

        # print("result: {}".format(result))
        return toDecimal(result)

    def getSum2(self, a: int, b: int) -> int:
        if not b:
            return a
        if not a:
            return b
        while b != 0:
            carry = a & b
            a ^= b
            b = carry << 1
        return a

    def getSum3(self, a: int, b: int) -> int:
        while a > 0:
            b += 1
            a -= 1

        while a < 0:
            b -= 1
            a += 1

        return b


Case = namedtuple("Case", ["a", "b", "expected"])


def testSum():
    sol = Solution()
    cases = [
        Case(1, 2, 3),
        Case(7, 7, 14),
        Case(0, 1, 1),
        Case(0, 0, 0),
        Case(63, 64, 127),
        Case(254, 1, 255),  # maximum 8 bits
    ]

    for c in cases:
        actual = sol.getSum(c.a, c.b)
        actual2 = sol.getSum2(c.a, c.b)
        actual3 = sol.getSum3(c.a, c.b)
        assert actual == c.expected, "Case: {}".format(c)
        assert actual2 == c.expected, "Case: {}".format(c)
        assert actual3 == c.expected, "Case: {}".format(c)


def testToBytes():
    CaseBytes = namedtuple("CaseBytes", ["x", "expected"])
    cases = [
        CaseBytes(7, [1, 1, 1, 0, 0, 0, 0, 0]),
        CaseBytes(0, [0, 0, 0, 0, 0, 0, 0, 0]),
        CaseBytes(1, [1, 0, 0, 0, 0, 0, 0, 0]),
        CaseBytes(2, [0, 1, 0, 0, 0, 0, 0, 0]),
        CaseBytes(6, [0, 1, 1, 0, 0, 0, 0, 0]),
    ]

    for c in cases:
        actual = toBytesReversed(c.x)
        assert actual == c.expected, "Case: {}".format(c)


def testToDecimal():
    CaseDecimal = namedtuple("CaseDecimal", ["x", "expected"])
    cases = [
        CaseDecimal([1, 1, 1, 0, 0, 0, 0, 0], 7),
        CaseDecimal([0, 0, 0, 0, 0, 0, 0, 0], 0),
        CaseDecimal([1, 0, 0, 0, 0, 0, 0, 0], 1),
        CaseDecimal([0, 1, 0, 0, 0, 0, 0, 0], 2),
        CaseDecimal([0, 1, 1, 0, 0, 0, 0, 0], 6),
    ]

    for c in cases:
        actual = toDecimal(c.x)
        assert actual == c.expected, "Case: {}".format(c)
