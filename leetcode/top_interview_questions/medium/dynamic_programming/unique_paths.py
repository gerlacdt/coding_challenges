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

from collections import deque, namedtuple


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        start = (0, 0)
        goal = (m - 1, n - 1)

        def helper(position):
            i, j = position
            if i >= m or j >= n:
                return 0
            if position == goal:
                return 1
            return helper((i + 1, j)) + helper((i, j + 1))

        return helper(start)

    def uniquePathsDP(self, m: int, n: int) -> int:
        """Dynamic programming solution. First generate a base case table
like:

        1111
        1000
        1000
        1000

        The 1s indicate there is only one path to this field. The 0s
        need to be calculated bottom-up.

        """
        table = [[1 if i == 0 or j == 0 else 0 for i in range(n)] for j in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if i > 0 and j > 0:
                    table[i][j] = table[i - 1][j] + table[i][j - 1]

        return table[m - 1][n - 1]


Case = namedtuple("Case", ["m", "n", "expected"])


def testSmall():
    sol = Solution()
    cases = [
        Case(7, 3, 28),
        Case(3, 2, 3),
        Case(3, 4, 10),
        Case(7, 7, 924),
        Case(4, 4, 20),
        Case(1, 1, 1),
    ]

    for c in cases:
        actual = sol.uniquePaths(c.m, c.n)
        actual2 = sol.uniquePathsDP(c.m, c.n)
        assert actual == c.expected
        assert actual2 == c.expected


def testBig():
    sol = Solution()
    m = 23
    n = 12
    actual = sol.uniquePathsDP(m, n)
    expected = 193536720
    assert actual == expected
