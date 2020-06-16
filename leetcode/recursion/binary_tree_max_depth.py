"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \\
  9  20
    /  \\
   15   7
return its depth = 3.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(node, height):
            if not node.left and not node.right:
                return height
            heightLeft = heightRight = 0
            if node.left:
                heightLeft = helper(node.left, height + 1)
            if node.right:
                heightRight = helper(node.right, height + 1)

            return max(heightLeft, heightRight)

        if not root:
            return 0

        return helper(root, 1)


def test1():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    sol = Solution()
    actual = sol.maxDepth(root)
    expected = 3
    assert actual == expected


def test2():
    root = TreeNode(
        1,
        TreeNode(2, None, TreeNode(3, TreeNode(4, TreeNode(8)))),
        TreeNode(5, TreeNode(6), TreeNode(7)),
    )
    sol = Solution()
    actual = sol.maxDepth(root)
    expected = 5
    assert actual == expected


def testSingleNode():
    root = TreeNode(1,)
    sol = Solution()
    actual = sol.maxDepth(root)
    expected = 1
    assert actual == expected


def testEmptyTree():
    root = None
    sol = Solution()
    actual = sol.maxDepth(root)
    expected = 0
    assert actual == expected
