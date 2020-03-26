# coding: utf-8

"""Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary
until the first non-whitespace character is found. Then, starting from
this character, takes an optional initial plus or minus sign followed
by as many numerical digits as possible, and interprets them as a
numerical value.

The string can contain additional characters after those that form the
integral number, which are ignored and have no effect on the behavior
of this function.

If the first sequence of non-whitespace characters in str is not a
valid integral number, or if no such sequence exists because either
str is empty or it contains only whitespace characters, no conversion
is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−231, 231 − 1]. If
the numerical value is out of the range of representable values,
INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:

Input: "42"
Output: 42

Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−2^31) is returned.

"""


from collections import namedtuple


class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = "0123456789"
        if not s:
            return 0
        s1 = s.lstrip()
        if not s1:
            return 0
        withSign = False
        if s1[0] == "+":
            withSign = True
            s1 = s1[1:]
        if not s1:
            return 0
        if withSign and s1[0] not in numbers:
            return 0
        negative = False
        if s1[0] == "-":
            negative = True
            s1 = s1[1:]
        if not s1:
            return 0
        if s1[0] not in numbers:
            return 0
        # collect numbers only from the left side
        s2 = []
        for c in s1:
            if c in numbers:
                s2.append(c)
            else:
                break
        result = 0
        for i, c in enumerate(reversed(s2)):
            if c in numbers:
                result += (10**i * int(c))
            else:
                break
        if negative and result > 2**31:
            return -2**31
        if not negative and result > 2**31 - 1:
            return 2**31 - 1
        return -1 * result if negative else result


def test():
    Case = namedtuple('Case', ['input1', 'expected'])
    cases = [Case("42", 42),
             Case("  -42", -42),
             Case("4193 with words", 4193),
             Case("words and 987", 0),
             Case("-91283472332", -2147483648),
             Case("-", 0),
             Case(" ", 0),
             Case("+1", 1),
             Case("+", 0),
             Case("+-2", 0)
    ]
    sol = Solution()
    for c in cases:
        result = sol.myAtoi(c.input1)
        assert result == c.expected
