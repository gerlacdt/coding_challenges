"""Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        def helper(node):
            if not node:
                return 0
            nleft = helper(node.left)
            nright = helper(node.right)
            return max(nleft, nright) + 1
        return helper(root)


def test():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    result = sol.maxDepth(root)
    expected = 3
    assert result == expected
