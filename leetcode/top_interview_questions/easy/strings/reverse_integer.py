# coding: utf-8

"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:

Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−2**31, 2**31 − 1]. For
the purpose of this problem, assume that your function returns 0 when
the reversed integer overflows.

"""


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        s = str(x)
        negative = False
        if s[0] == '-':
            negative = True
            s = s[1:]
        s = s.rstrip('0')
        n = int(s[::-1])  # reverse string
        if n > (2**31) - 1:
            return 0
        if negative:
            if n > 2**31:
                return 0
            return -n
        return n


def test():
    sol = Solution()
    input1 = 123
    expected1 = 321
    result1 = sol.reverse(input1)
    assert result1 == expected1

    input2 = -123
    expected2 = -321
    result2 = sol.reverse(input2)
    assert result2 == expected2

    input3 = 120
    expected3 = 21
    result3 = sol.reverse(input3)
    assert result3 == expected3

    input4 = 1
    expected4 = 1
    result4 = sol.reverse(input4)
    assert result4 == expected4

    input5 = -1
    expected5 = -1
    result5 = sol.reverse(input5)
    assert result5 == expected5

    input6 = 0
    expected6 = 0
    result6 = sol.reverse(input6)
    assert result6 == expected6
