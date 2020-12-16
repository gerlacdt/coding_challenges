"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 -> 3 -> 1 -> 1 -> 1 minimizes the sum.


Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

"""

from collections import namedtuple
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # fill initial table
        table = [[0 for _ in row] for row in grid]
        table[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            table[i][0] = table[i - 1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            table[0][j] = table[0][j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                table[i][j] = min(table[i - 1][j], table[i][j - 1]) + grid[i][j]
        # dynamic programming
        return table[-1][-1]


Case = namedtuple("Case", "grid expected")


def test():
    sol = Solution()
    cases = [
        Case([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        Case([[1, 2, 3], [4, 5, 6]], 12),
    ]
    for c in cases:
        actual = sol.minPathSum(c.grid)
        assert actual == c.expected
