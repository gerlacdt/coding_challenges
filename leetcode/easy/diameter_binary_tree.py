"""Given a binary tree, you need to compute the length of the diameter
of the tree. The diameter of a binary tree is the length of the
longest path between any two nodes in a tree. This path may or may not
pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

"""

from collections import namedtuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} ({self.left} {self.right})"


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        totalMax = 0

        def helper(node):
            nonlocal totalMax
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            totalMax = max(totalMax, l + r)
            return max(l, r) + 1

        helper(root)
        return totalMax


Case = namedtuple("Case", ["root", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)), 3),
        Case(
            TreeNode(
                1,
                TreeNode(
                    2,
                    TreeNode(3, TreeNode(5)),
                    TreeNode(4, None, TreeNode(6, None, TreeNode(7))),
                ),
                None,
            ),
            5,
        ),
    ]
    for c in cases:
        actual = sol.diameterOfBinaryTree(c.root)
        assert actual == c.expected
