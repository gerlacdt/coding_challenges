"""Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the
node's key.  The right subtree of a node contains only nodes with keys
greater than the node's key.  Both the left and right subtrees must
also be binary search trees.


Example 1:

    2
   / \\
  1   3

Input: [2,1,3]
Output: true


Example 2:

    5
   / \\
  1   4
     / \\
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""

from collections import namedtuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def isLeaf(node):
    if not node.left and not node.right:
        return True
    return False


def subtreeMax(node):
    if not node.right:
        return node.val
    return subtreeMax(node.right)


def subtreeMin(node):
    if not node.left:
        return node.val
    return subtreeMin(node.left)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def helper(node):
            if isLeaf(node):
                return True
            left = helper(node.left) if node.left else True
            if not left:
                return False
            right = helper(node.right) if node.right else True
            if not right:
                return False
            if (
                left
                and right
                and (not node.left or subtreeMax(node.left) < node.val)
                and (not node.right or subtreeMin(node.right) > node.val)
            ):
                return True
            return False

        return helper(root)


Case = namedtuple("Case", ["root", "expected"])


def test1():
    cases = [
        Case(TreeNode(2, TreeNode(1), TreeNode(3)), True),
        Case(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))), False),
        Case(
            TreeNode(
                4,
                TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(6, TreeNode(5), TreeNode(7)),
            ),
            True,
        ),
        Case(TreeNode(1, TreeNode(1)), False),
        Case(None, True),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.isValidBST(c.root)
        assert actual == c.expected, "Case: {}".format(c.root)
