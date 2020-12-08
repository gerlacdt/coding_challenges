"""Given a string s consists of some words separated by spaces, return the
length of the last word in the string. If the last word does not
exist, return 0.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5


Example 2:

Input: s = " "
Output: 0
"""

from collections import namedtuple


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        # print(f"words: {words}")
        return len(words[-1]) if words else 0


Case = namedtuple("Case", ["input", "expected"])


def test():
    sol = Solution()
    cases = [Case("Hello World", 5), Case(" ", 0)]
    for c in cases:
        actual = sol.lengthOfLastWord(c.input)
        assert actual == c.expected
