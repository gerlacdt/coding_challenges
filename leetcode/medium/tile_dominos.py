"""We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

XX  <- domino

XX  <- "L" tromino
X
Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.

(In a tiling, every square must be covered by a tile. Two tilings are
different if and only if there are two 4-directionally adjacent cells
on the board such that exactly one of the tilings has both squares
occupied by a tile.)

Example:
Input: 3
Output: 5
Explanation:
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
Note:

N  will be in range [1, 1000].

"""

from collections import namedtuple


class Solution:
    def numTilings(self, N: int) -> int:
        if N < 4:
            dp = [0, 1, 2, 5]
            return dp[N]
        dp = [0 for i in range(N + 1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        MOD = 10 ** 9 + 7
        for i in range(4, N + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]
            dp[i] %= MOD
        return dp[-1]


Case = namedtuple("Case", ["n", "expected"])


def test():
    cases = [Case(0, 0), Case(1, 1), Case(2, 2), Case(3, 5), Case(4, 11), Case(5, 24)]
    sol = Solution()
    for c in cases:
        actual = sol.numTilings(c.n)
        assert actual == c.expected, "Case: {}".format(c.n)
