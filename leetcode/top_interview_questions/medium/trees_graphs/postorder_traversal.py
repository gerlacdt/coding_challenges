"""Implement an iterative version of a postorder traveral of a binary
tree.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3, 2, 1]
"""

from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def helper(node):
            if not node:
                return None
            helper(node.left)
            helper(node.right)
            result.append(node.val)

        helper(root)
        return result

    def postorderIter(self, root: TreeNode) -> List[int]:
        """WE need to know the postorder is the reverse order of a preorder
        done with visiting node.right first and node.left second.

        So the solution is: Do a preorder iterative traversal where
        you put node.left and then node.right on the stack. After that
        just reverse the result-order and you get the postorder.

        """
        result = []
        stack = [root]

        # do preorder traversal
        while stack:
            node = stack.pop()
            result.append(node.val)
            # just toggle node.left and node.right visiting
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # reverse the toggle preorder and you get the postorder
        return list(reversed(result))


def test():
    s = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    actual = s.postorderTraversal(root)
    actual2 = s.postorderIter(root)
    expected = [3, 2, 1]
    assert actual == expected
    assert actual2 == expected

    root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, None, TreeNode(5)))
    actual = s.postorderTraversal(root)
    actual2 = s.postorderIter(root)
    expected = [3, 2, 5, 4, 1]
    assert actual == expected
    assert actual2 == expected
