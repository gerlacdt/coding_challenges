"""Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded
as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is
not allowed.
"""


from collections import namedtuple


def my_solution(s):
    def helper(s, n):
        if n < 2:
            return 1
        if s[n - 2] == "1" and s[n - 1] == "0":  # handler special case with '10'
            return helper(s, n - 2)
        if (s[n - 2] == "1" or s[n - 2] == "2") and s[n - 1] < "7":
            return helper(s, n - 1) + helper(s, n - 2)
        else:
            return helper(s, n - 1)

    n = len(s)
    return helper(s, n)


def youtube(digits):
    """https://www.youtube.com/watch?v=qli-JCrSwuk
    """

    def helper(digits, k):
        if k == 0:
            return 1
        s = len(digits) - k  # current index at digits[]
        if digits[s] == "0":  # handle trailing '0'
            return 0
        result = helper(digits, k - 1)
        if k >= 2 and int(digits[s : s + 2]) <= 26:
            result += helper(digits, k - 2)
        return result

    return helper(digits, len(digits))


Case = namedtuple("TestCase", ["input1", "expected"])


def test():
    cases = [
        Case("1", 1),
        Case("11", 2),
        Case("111", 3),
        Case("1111", 5),
        Case("11111", 8),
        Case("121", 3),
        Case("1234", 3),
        Case("314", 2),
        Case("12321", 6),
        Case("10", 1),
        Case("1010", 1),
        Case("1110", 2),
    ]

    for c in cases:
        assert youtube(c.input1) == c.expected
        assert my_solution(c.input1) == c.expected
        assert my_solution(c.input1) == youtube(c.input1)
