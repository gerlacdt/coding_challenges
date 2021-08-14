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


class Solution:
    def numTrees(self, n: int) -> int:
        pass


Case = namedtuple("Case", ["n", "expected"])


def test():
    cases = [Case(3, 5)]
    sol = Solution()
    for c in cases:
        actual = sol.numTrees(c.n)
        assert actual == c.expected
