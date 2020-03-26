"""Given a binary tree, return the inorder traversal of its nodes'
values.

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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            result.append(root.val)
            helper(root.right)

        helper(root)
        return result

    def inorderIter(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        current = root
        while current or stack:
            if current:
                while current:
                    stack.append(current)
                    debug("stack.append: {}".format(current.val))
                    current = current.left
            else:
                node = stack.pop()
                result.append(node.val)
                if node.right:
                    current = node.right
        return result


def test():
    s = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    actual = s.inorderTraversal(root)
    actual2 = s.inorderIter(root)
    expected = [1, 3, 2]
    assert actual == expected
    assert actual2 == expected

    root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, None, TreeNode(5)))
    actual = s.inorderTraversal(root)
    actual2 = s.inorderIter(root)
    expected = [3, 2, 1, 4, 5]
    assert actual == expected
    assert actual2 == expected
