"""Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the
node's key.  The right subtree of a node contains only nodes with keys
greater than the node's key.  Both the left and right subtrees must
also be binary search trees.

Example 1:

Input:
    2
   / \
  1   3
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.

"""

import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, minimum, maximum):
            if not node:
                return True
            if node.val <= minimum or node.val >= maximum:
                return False
            return helper(node.left, minimum, node.val) and helper(node.right, node.val, maximum)
        return helper(root, -sys.maxsize, sys.maxsize)

    def inorder(self, root: TreeNode):
        last = -sys.maxsize

        def helper(node):
            nonlocal last
            if not node:
                return True
            if not helper(node.left):
                return False
            if node.val <= last:
                return False
            else:
                last = node.val
            if not helper(node.right):
                return False
            return True
        return helper(root)


def test():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    sol = Solution()
    result = sol.isValidBST(root)
    result2 = sol.inorder(root)
    assert result
    assert result == result2

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    result = sol.isValidBST(root)
    result2 = sol.inorder(root)
    assert not result
    assert result == result2

    root = TreeNode(1)
    root.left = TreeNode(1)
    result = sol.isValidBST(root)
    result2 = sol.inorder(root)
    assert not result
    assert result == result2

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    result = sol.isValidBST(root)
    result2 = sol.inorder(root)
    assert not result
    assert result == result2
