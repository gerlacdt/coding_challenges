# coding: utf-8

"""

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

xample:

Input: 3
Output: [1,3,3,1]


Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

from typing import List
from collections import namedtuple


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        def helper(k, row):
            if k == 0:
                return row
            nextRow = [1]
            for i in range(len(row) - 1):
                nextRow.append(row[i] + row[i + 1])
            nextRow.append(1)
            return helper(k - 1, nextRow)

        return helper(rowIndex - 1, [1, 1])


Case = namedtuple("Case", ["k", "expected"])


def test():
    cases = [
        Case(1, [1, 1]),
        Case(2, [1, 2, 1]),
        Case(3, [1, 3, 3, 1]),
        Case(4, [1, 4, 6, 4, 1]),
        Case(5, [1, 5, 10, 10, 5, 1]),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.getRow(c.k)
        assert actual == c.expected, "Case: {} {}".format(c.k, c.expected)
