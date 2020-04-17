"""Given a column title as appear in an Excel sheet, return its
corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1


Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

Explanation: (26 * 26**1) + (25**26**0)

"""

from collections import namedtuple


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
VALUES = {letter: i + 1 for i, letter in enumerate(letters)}


class Solution:
    def titleToNumber(self, s: str) -> int:
        reverseString = reversed(s)
        result = 0
        for i, c in enumerate(reverseString):
            result += 26 ** i * VALUES[c]
        return result


Case = namedtuple("Case", ["s", "expected"])


def test():
    sol = Solution()
    cases = [Case("A", 1), Case("AB", 28), Case("ZY", 701)]
    for c in cases:
        actual = sol.titleToNumber(c.s)
        assert actual == c.expected
