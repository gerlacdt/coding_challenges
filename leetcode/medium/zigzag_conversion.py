"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given
number of rows like this: (you may want to display this pattern in a
fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

https://leetcode.com/problems/zigzag-conversion/

"""

from collections import namedtuple
from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        table: List[List[str]] = [[] for _ in range(numRows)]
        goingDown = False
        i = 0
        for c in s:
            table[i].append(c)
            if i == 0 or i == numRows - 1:
                goingDown = not goingDown
            if goingDown:
                i += 1
            else:
                i -= 1
        return "".join(["".join(row) for row in table])


Case = namedtuple("Case", ["s", "numRows", "expected"])


def test():
    sol = Solution()
    cases = [
        Case("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        Case("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        Case("foobar", 1, "foobar"),
    ]

    for c in cases:
        actual = sol.convert(c.s, c.numRows)
        assert actual == c.expected
