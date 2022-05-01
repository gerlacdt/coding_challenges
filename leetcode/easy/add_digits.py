"""Given an integer num, repeatedly add all its digits until the
result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0

"""

from collections import namedtuple


class Solution:
    def addDigits(self, num: int) -> int:
        def helper(n):
            result = 0
            while n > 0:
                result += n % 10
                n //= 10
            return result

        while num >= 10:
            # more than one digit
            num = helper(num)
        return num

    def addDigits2(self, num: int) -> int:
        if num == 0:
            return 0
        elif num == 9:
            return 9
        return num % 9


Case = namedtuple("Case", ["num", "expected"])


def test():
    cases = [Case(38, 2), Case(0, 0), Case(9, 9)]
    sol = Solution()
    for c in cases:
        actual = sol.addDigits(c.num)
        assert actual == c.expected, "Case: {}".format(c)


def test2():
    cases = [Case(38, 2), Case(0, 0), Case(9, 9)]
    sol = Solution()
    for c in cases:
        actual = sol.addDigits2(c.num)
        assert actual == c.expected, "Case: {}".format(c)
