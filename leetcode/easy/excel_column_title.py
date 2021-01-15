"""Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""

from collections import namedtuple


class Solution:
    def convertToTitle(self, n: int) -> str:
        letters = "abcdefghijklmnopqrstuvwxyz".upper()

        result = []
        while n:
            rest = (n - 1) % 26
            result.append(letters[rest])
            n = (n - 1) // 26

        return "".join(reversed(result))


Case = namedtuple("Case", ["n", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(1, "A"),
        Case(27, "AA"),
        Case(28, "AB"),
        Case(701, "ZY"),
    ]
    for c in cases:
        actual = sol.convertToTitle(c.n)
        assert actual == c.expected, f"{c.n}"
