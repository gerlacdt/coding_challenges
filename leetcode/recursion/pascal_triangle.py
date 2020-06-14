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


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pass


def test():
    sol = Solution()
    actual = sol.getRow(3)
    expected = [1, 3, 3, 1]
    assert actual == expected
