"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?

"""

from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result: List[int] = []
        stack: deque = deque([])
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result

    def inorderTraversalRec(self, root: TreeNode) -> List[int]:
        result = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            result.append(node.val)
            helper(node.right)

        helper(root)
        return result


def test():
    sol = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    actual = sol.inorderTraversalRec(root)
    actual2 = sol.inorderTraversal(root)
    expected = [1, 3, 2]
    assert actual == expected
    assert actual2 == expected
