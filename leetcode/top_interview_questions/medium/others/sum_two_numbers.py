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


class Solution:
    def getSum(self, a: int, b: int) -> int:
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
        Case(254, 1, 255),
        Case(-1, -1, -2),
        Case(-1, 1, 0),
        Case(-12, -8, -20),
    ]

    for c in cases:
        actual = sol.getSum(c.a, c.b)
        assert actual == c.expected, "Case: {}".format(c)
