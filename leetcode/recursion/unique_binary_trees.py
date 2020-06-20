"""Given an integer n, generate all structurally unique BST's (binary
search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]

Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \\       /     /      / \\      \\
     3     2     1      1   3      2
    /     /       \\                 \\
   2     1         2                 3


Constraints:

0 <= n <= 8

"""

from typing import List
from collections import namedtuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        def helper(rest):
            if not rest:
                return [None]
            result = []
            for i in range(len(rest)):
                val = rest[i]
                leftChildren = helper(rest[:i])
                rightChildren = helper(rest[i + 1 :])
                for leftSubtree in leftChildren:
                    for rightSubtree in rightChildren:
                        result.append(TreeNode(val, leftSubtree, rightSubtree))
            return result

        return helper([i + 1 for i in range(n)])


Case = namedtuple("Case", ["n", "expected"])


def test():
    cases = [
        Case(0, 0),
        Case(1, 1),
        Case(2, 2),
        Case(3, 5),
        Case(4, 14),
        Case(5, 42),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.generateTrees(c.n)
        assert len(actual) == c.expected, "Case: {}".format(c.n)
