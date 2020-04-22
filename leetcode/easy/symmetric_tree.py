"""Given a binary tree, check whether it is a mirror of itself (ie,
symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

"""


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if tree1 and tree2 and tree1.val == tree2.val:
                return helper(tree1.left, tree2.right) and helper(
                    tree1.right, tree2.left
                )
            return False

        return helper(root, root)


def testSymmetric():
    root = TreeNode(
        1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))
    )
    sol = Solution()
    actual = sol.isSymmetric(root)
    expected = True
    assert actual == expected


def testNotSymmetric():
    root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    sol = Solution()
    actual = sol.isSymmetric(root)
    expected = False
    assert actual == expected
