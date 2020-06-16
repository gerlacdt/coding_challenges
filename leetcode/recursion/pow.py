"""
Implement pow(x, n), which calculates x raised to the power n (x**n).

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

"""
from collections import namedtuple


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if not n:
                return 1
            tmp = helper(x, n // 2)
            if n % 2 == 0:
                return tmp * tmp
            return tmp * tmp * x

        return helper(x, n)


Case = namedtuple("Case", ["x", "n", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(2, 3, 8,),
        Case(2, 2, 4),
        Case(2, 5, 32),
        Case(2, 6, 64),
        Case(2, 10, 1024,),
        Case(2, 11, 2048),
    ]
    for c in cases:
        actual = sol.myPow(c.x, c.n)
        assert actual == c.expected
