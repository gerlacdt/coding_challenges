"""Given the root of a binary tree, return the preorder traversal of its
nodes' values.


Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [1,2]

Example 5:

Input: root = [1,null,2]
Output: [1,2]


Can you do it iteratively?

https://leetcode.com/problems/binary-tree-preorder-traversal/

"""

from collections import namedtuple
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} ({self.left} {self.right})"


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def helper(node):
            if not node:
                return
            result.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return result

    def iterative(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


Case = namedtuple("Case", ["root", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(TreeNode(1, None, TreeNode(2, TreeNode(3))), [1, 2, 3]),
        Case(None, []),
        Case(TreeNode(1), [1]),
        Case(TreeNode(1, TreeNode(2)), [1, 2]),
        Case(TreeNode(1, None, TreeNode(2)), [1, 2]),
    ]
    for c in cases:
        actual = sol.preorderTraversal(c.root)
        assert actual == c.expected

        actual2 = sol.iterative(c.root)
        assert actual2 == c.expected
