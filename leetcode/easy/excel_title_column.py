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

"""


from collections import namedtuple
from typing import Dict


class Solution:
    def titleToNumber(self, s: str) -> int:
        letters: Dict[str, int] = {
            c: i for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        }

        result = 0
        while s:
            poww = len(s) - 1
            c = s[0]
            s = s[1:]
            result += (26 ** poww) * (letters[c] + 1)

        return result


Case = namedtuple("Case", ["s", "expected"])


def test():
    sol = Solution()
    cases = [
        Case("A", 1),
        Case("AB", 28),
        Case("AZ", 52),
        Case("BA", 53),
        Case("ZY", 701),
    ]
    for c in cases:
        actual = sol.titleToNumber(c.s)
        assert actual == c.expected, f"{c.s}"
