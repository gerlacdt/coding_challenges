"""Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.


Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.


Note: Your solution should be in logarithmic time complexity.

"""

from collections import namedtuple
import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        i = 5
        while n / i >= 1:
            count += n // i
            i *= 5
        return count

    def trailingZeroes2(self, n: int) -> int:
        result = math.factorial(n)
        count = 0
        while result > 0:
            if result % 10 == 0:
                count += 1
                result //= 10
            else:
                break
        return count


Case = namedtuple("Case", ["n", "expected"])


def test():
    cases = [Case(5, 1), Case(7, 1), Case(20, 4), Case(100, 24)]
    sol = Solution()
    for c in cases:
        actual = sol.trailingZeroes(c.n)
        assert actual == c.expected
        assert actual == sol.trailingZeroes2(c.n)
