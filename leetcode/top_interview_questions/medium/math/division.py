# coding: utf-8

"""Given two integers dividend and divisor, divide two integers
without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing
its fractional part. For example, truncate(8.345) = 8 and
truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.


Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.


Note:

Both dividend and divisor will be 32-bit signed integers.

The divisor will never be 0.

Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−2**31, 2**31 − 1]. For
the purpose of this problem, assume that your function returns 2**31 − 1
when the division result overflows.

"""

from collections import namedtuple


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) ^ (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
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
        return -quotient if sign else min(quotient, (2 ** 31) - 1)


Case = namedtuple("Case", ["x", "y", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(10, 3, 3),
        Case(7, -3, -2),
        Case(8, -3, -2),
        Case(1, 1, 1),
        Case(-1, -1, 1),
        Case(2147483648, 1, 2147483647),
        Case(-2147483648, -1, 2147483647),
    ]
    for c in cases:
        actual = sol.divide(c.x, c.y)
        assert actual == c.expected, "Case: {}".format(c)
