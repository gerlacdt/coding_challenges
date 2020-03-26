# coding: utf-8

"""The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the
count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"

"""

from collections import namedtuple


class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return "1"
        if n == 2:
            return "11"
        result = self.countAndSay(n-1)
        return say(result)


def say(s):
    assert(s)
    counter = 1
    result = []
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            counter += 1
        else:
            result.append(str(counter))
            result.append(s[i-1])
            counter = 1
    result.append(str(counter))
    result.append(s[len(s)-1])
    return "".join(result)


Case = namedtuple('Case', ['input1', 'expected'])


def test():
    sol = Solution()
    cases = [Case(1, "1"),
             Case(2, "11"),
             Case(3, "21"),
             Case(4, "1211"),
             Case(5, "111221"),
             Case(6, "312211")]
    for c in cases:
        result = sol.countAndSay(c.input1)
        assert result == c.expected


def test_say():
    cases = [
        Case("1", "11"),
        Case("11", "21"),
        Case("21", "1211"),
        Case("1211", "111221"),
        Case("111221", "312211")
    ]
    for c in cases:
        result = say(c.input1)
        assert result == c.expected
