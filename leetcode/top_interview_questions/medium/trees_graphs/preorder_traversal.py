"""Implement an iterative version of a preorder traveral of a binary
tree.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
"""

from typing import List
import os


DEBUG = os.environ.get('DEBUG')


def debug(s):
    if DEBUG:
        print(s)
    return


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def helper(node):
            if not node:
                return None
            result.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return result

    def preorderIter(self, root: TreeNode) -> List[int]:
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


def test():
    s = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    actual = s.preorderTraversal(root)
    actual2 = s.preorderIter(root)
    expected = [1, 2, 3]
    assert actual == expected
    assert actual2 == expected

    root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, None, TreeNode(5)))
    actual = s.preorderTraversal(root)
    actual2 = s.preorderIter(root)
    expected = [1, 2, 3, 4, 5]
    assert actual == expected
    assert actual2 == expected
