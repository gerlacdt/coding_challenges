"""Given an integer n, return true if it is a power of
two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that
n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 2^0 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 2^4 = 16

Example 3:

Input: n = 3
Output: false

Example 4:

Input: n = 4
Output: true

Example 5:

Input: n = 5
Output: false


https://leetcode.com/problems/power-of-two/

"""

from collections import namedtuple


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        current = n
        while (current % 2) == 0:
            current //= 2

        if current == 1:
            return True
        return False

    def isPowerOfTwo2(self, n: int) -> bool:
        # bin(8) -> "0b1000"
        # bin(8)[2:] -> "1000"
        return bin(n)[2:].count("1") == 1


Case = namedtuple("Case", "n expected")


def test():
    sol = Solution()
    cases = [
        Case(0, False),
        Case(1, True),
        Case(16, True),
        Case(3, False),
        Case(1024, True),
        Case(1600, False),
    ]
    for c in cases:
        actual = sol.isPowerOfTwo(c.n)
        assert actual == c.expected, f"n: {c.n}"

        actual2 = sol.isPowerOfTwo2(c.n)
        assert actual2 == c.expected, f"n: {c.n}"
