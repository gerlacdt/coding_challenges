# coding: utf-8

"""

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

"""

from collections import namedtuple


class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1.0
        if n > 0:
            for i in range(n):
                result *= x
            return result
        elif n < 0:
            n = -n
            for i in range(n):
                result *= x
            return 1 / result
        else:
            return result


Case = namedtuple("Case", ["x", "n", "expected"])


def test():
    sol = Solution()

    cases = [
        Case(2.0, 10, 1024.0),
        Case(2.0, 0, 1),
        Case(2.00000, -2, 0.25),
        # Case(0.00001, 2147483647),
    ]
    for c in cases:
        actual = sol.myPow(c.x, c.n)
        assert actual == c.expected
