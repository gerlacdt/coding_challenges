"""Given two binary trees, write a function to check if they are the
same or not.

Two binary trees are considered the same if they are structurally
identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false


Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

"""

from collections import namedtuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


Case = namedtuple("Case", ["root1", "root2", "expected"])


def test1():
    cases = [
        Case(
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(1, TreeNode(2), TreeNode(3)),
            True,
        ),
        Case(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2)), False),
        Case(
            TreeNode(1, TreeNode(2), TreeNode(1)),
            TreeNode(1, TreeNode(1), TreeNode(2)),
            False,
        ),
    ]

    sol = Solution()
    for c in cases:
        actual = sol.isSameTree(c.root1, c.root2)
        assert actual == c.expected
