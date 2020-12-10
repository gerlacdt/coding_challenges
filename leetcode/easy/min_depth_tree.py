"""Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from
the root node down to the nearest leaf node.

Note: A leaf is a node with no children.


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

from collections import namedtuple
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isLeaf(node):
    return True if not node.left and not node.right else False


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node):
            if isLeaf(node):
                return 1
            l, r = sys.maxsize, sys.maxsize
            if node.left:
                l = helper(node.left)
            if node.right:
                r = helper(node.right)
            return min(l, r) + 1

        return helper(root)


Case = namedtuple("Case", ["root", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), 2),
        Case(
            TreeNode(
                2,
                None,
                TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))),
            ),
            5,
        ),
        Case(None, 0),
    ]

    for c in cases:
        actual = sol.minDepth(c.root)
        assert actual == c.expected
