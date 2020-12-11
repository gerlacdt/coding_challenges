"""Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node
differ in height by no more than 1.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true
"""

from collections import namedtuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def helper(node):
            if not node:
                return 0, True

            lheight, lbalanced = helper(node.left)
            rheight, rbalanced = helper(node.right)
            isBalanced = (
                True
                if (abs(lheight - rheight) < 2) and lbalanced and rbalanced
                else False
            )
            return max(lheight, rheight) + 1, isBalanced

        height, isBalanced = helper(root)
        return isBalanced


Case = namedtuple("Case", ["root", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), True),
        Case(
            TreeNode(
                1,
                TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
                TreeNode(2),
            ),
            False,
        ),
        Case(
            TreeNode(
                1,
                TreeNode(2, TreeNode(3, TreeNode(4))),
                TreeNode(2, None, TreeNode(3, None, TreeNode(4))),
            ),
            False,
        ),
    ]
    for c in cases:
        actual = sol.isBalanced(c.root)
        assert actual == c.expected
