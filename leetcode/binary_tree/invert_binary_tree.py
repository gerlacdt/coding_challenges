"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9


Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    result = []

    def helper(node):
        if not node:
            return
        helper(node.left)
        result.append(node.val)
        helper(node.right)

    helper(root)
    return result


def preorder(root):
    result = []

    def helper(node):
        if not node:
            return
        result.append(node.val)
        helper(node.left)
        helper(node.right)

    helper(root)
    return result


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        pass


def test():
    root = TreeNode(
        4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
    )

    sol = Solution()
    actual = sol.invertTree(root)
    expected = TreeNode(
        4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1))
    )

    assert inorder(actual) == inorder(expected)
    assert preorder(actual) == preorder(expected)


def testInorder():
    root = TreeNode(
        4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
    )
    actual = inorder(root)
    expected = [1, 2, 3, 4, 6, 7, 9]
    assert actual == expected


def testPreorder():
    root = TreeNode(
        4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
    )
    actual = preorder(root)
    expected = [4, 2, 1, 3, 7, 6, 9]
    assert actual == expected
