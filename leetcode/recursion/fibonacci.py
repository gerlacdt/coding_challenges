"""The Fibonacci numbers, commonly denoted F(n) form a sequence,
called the Fibonacci sequence, such that each number is the sum of the
two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.


Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.


Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""

from collections import namedtuple


class Solution:
    def recFib(self, N: int) -> int:
        if N <= 2:
            return 1
        return self.recFib(N - 1) + self.recFib(N - 2)

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        def helper(n, first, second):
            if n == 0:
                return second
            return helper(n - 1, second, first + second)

        return helper(n - 2, 1, 1)


Case = namedtuple("Case", ["n", "expected"])


def test():
    # fibonacci sequence 0,1,1,2,3,5,8,13,21,34,55,89
    cases = [Case(3, 2), Case(5, 5), Case(10, 55), Case(11, 89)]
    sol = Solution()
    for c in cases:
        actual = sol.recFib(c.n)
        actual2 = sol.fib(c.n)
        assert actual == c.expected, "Case: {} {}".format(c.n, c.expected)
        assert actual2 == c.expected, "Case: {} {}".format(c.n, c.expected)

    fibs = [sol.fib(i) for i in range(0, 30)]
    print(fibs)
