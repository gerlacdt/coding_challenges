"""A robot is located at the top-left corner of a m x n grid (marked
'Start' in the diagram below).

The robot can only move either down or right at any point in time. The
robot is trying to reach the bottom-right corner of the grid (marked
'Finish' in the diagram below).

How many possible unique paths are there?


Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:

From the top-left corner, there are a total of 3 ways to reach the
bottom-right corner:

1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28


Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

"""

from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        start = (0, 0)
        goal = (m - 1, n - 1)
        npaths = 0

        def successors(position):
            row, col = position
            succs = []
            if row + 1 < m:
                succs.append((row + 1, col))
            if col + 1 < n:
                succs.append((row, col + 1))
            return succs

        def helper(position):
            nonlocal npaths
            if position == goal:
                npaths += 1
                return
            for s in successors(position):
                helper(s)

        helper(start)
        return npaths

    def uniquePaths2(self, m: int, n: int) -> int:
        start = (m - 1, n - 1)
        table = [[0 for _ in range(n)] for _ in range(m)]
        table[m - 1][n - 1] = 1
        frontier = deque([start])
        visited = set()

        while frontier:
            i, j = frontier.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if j - 1 >= 0:
                table[i][j - 1] = (
                    table[i][j]
                    if table[i][j - 1] == 0
                    else table[i][j - 1] + table[i][j]
                )
                if (i, j - 1) not in visited:
                    frontier.append((i, j - 1))
            if i - 1 >= 0:
                table[i - 1][j] = (
                    table[i][j]
                    if table[i - 1][j] == 0
                    else table[i][j] + table[i - 1][j]
                )
                if (i - 1, j) not in visited:
                    frontier.append((i - 1, j))
        return table[0][0]


def test():
    sol = Solution()
    m = 7
    n = 3
    actual = sol.uniquePaths(m, n)
    actual2 = sol.uniquePaths2(m, n)
    expected = 28
    assert actual == expected
    assert actual2 == expected

    m = 3
    n = 2
    actual = sol.uniquePaths(m, n)
    actual2 = sol.uniquePaths2(m, n)
    expected = 3
    assert actual == expected
    assert actual2 == expected

    m = 3
    n = 4
    actual = sol.uniquePaths(m, n)
    actual2 = sol.uniquePaths2(m, n)
    expected = 10
    assert actual == expected
    assert actual2 == expected

    m = 7
    n = 7
    actual = sol.uniquePaths(m, n)
    actual2 = sol.uniquePaths2(m, n)
    expected = 924
    assert actual == expected
    assert actual2 == expected

    m = 23
    n = 12
    actual = sol.uniquePaths2(m, n)
    expected = 193536720
    assert actual == expected
