"""Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:

Could you do it without using any loop / recursion?

"""

from collections import namedtuple
from math import log10

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 1
        while i <= n:
            if i == n:
                return True
            i = i * 3
        return False

    def isPowerOfThree2(self, n: int) -> bool:
        """This functions utilizes the math.log10():

        n = 3^^i
        i = log3(n)
        i = log10(n) / log10(3)
        """
        if n == 0:
            return False
        result = log10(n) / log10(3)
        return result.is_integer()


def test():
    Case = namedtuple('Case', ['n', 'expected'])

    cases = [Case(27, True), Case(0, False), Case(9, True), Case(45, False),
             Case(1, True)]
    s = Solution()
    for c in cases:
        result = s.isPowerOfThree(c.n)
        result2 = s.isPowerOfThree2(c.n)
        assert result == c.expected
        assert result2 == c.expected
