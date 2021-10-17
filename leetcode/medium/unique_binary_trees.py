"""Given an integer n, return the number of structurally unique BST's
(binary search trees) which has exactly n nodes of unique values from
1 to n.

Example 1:

Input: n = 3
Output: 5

Example 2:

Input: n = 1
Output: 1


https://leetcode.com/problems/unique-binary-search-trees/

"""

from collections import namedtuple
from functools import lru_cache


class Solution:
    def numTrees(self, n: int) -> int:
        def helper(k):
            if k == 0 or k == 1:
                return 1
            result = 0
            for i in range(k):
                result += helper(i) * helper(k - 1 - i)
            return result

        return helper(n)

    def numTreesDP(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            result = 0
            for j in range(i):
                result += dp[j] * dp[i - 1 - j]
            dp[i] = result

        return dp[-1]

    @lru_cache(maxsize=None)
    def numTreesMemoize(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        result = 0
        for i in range(n):
            result += self.numTreesMemoize(i) * self.numTreesMemoize(n - 1 - i)
        return result


Case = namedtuple("Case", ["n", "expected"])


def test():
    cases = [
        Case(0, 1),
        Case(1, 1),
        Case(2, 2),
        Case(3, 5),
        Case(4, 14),
        Case(5, 42),
        Case(6, 132),
        Case(40, 2622127042276492108820),
    ]
    sol = Solution()
    for c in cases:
        # actual = sol.numTreesMemoize(c.n)
        # assert actual == c.expected

        actual = sol.numTreesDP(c.n)
        assert actual == c.expected
