# coding: utf-8

"""Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common
ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a
descendant of itself).”

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
"""

from collections import namedtuple


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} ({self.left} {self.right})"


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        def helper(node):
            if node.val > p.val and node.val > q.val:
                return helper(node.left)
            elif node.val < p.val and node.val < q.val:
                return helper(node.right)
            else:
                return node

        return helper(root)


Case = namedtuple("Case", "root p q expected")


def test():
    sol = Solution()
    root1 = TreeNode(2, TreeNode(1))
    root2 = tree()
    root3 = tree()
    cases = [
        Case(root1, root1, root1.left, 2),
        Case(root2, root2.left, root2.right, 6),
        Case(root3, root3.left, root3.left.right, 2),
    ]

    for c in cases:
        actual = sol.lowestCommonAncestor(c.root, c.p, c.q)
        assert actual.val == c.expected


def tree():
    return TreeNode(
        6,
        TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
        TreeNode(8, TreeNode(7), TreeNode(9)),
    )
