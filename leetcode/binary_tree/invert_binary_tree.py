"""Invert a binary tree.

Example:

Input:

     4
   /   \\
  2     7
 / \\   / \\
1   3 6   9


Output:

     4
   /   \\
  7     2
 / \\   / \\
9   6 3   1

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


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
        if not root:
            return root

        def helper(left, right, parentLeft, parentRight):
            if not left and not right:
                return

            if left and right:
                left.val, right.val = right.val, left.val
                helper(left.left, right.right, left, right)
                helper(left.right, right.left, left, right)
            elif left:
                if left == parentLeft.left:
                    parentLeft.left = None
                    parentRight.right = TreeNode(left.val)
                    helper(left.left, None, left, parentRight.right)
                    helper(left.right, None, left, parentRight.right)
                else:
                    parentLeft.right = None
                    parentRight.left = TreeNode(left.val)
                    helper(left.left, None, left, parentRight.left)
                    helper(left.right, None, left, parentRight.left)
            elif right:
                if right == parentRight.right:
                    parentRight.right = None
                    parentLeft.left = TreeNode(right.val)
                    helper(None, right.left, parentLeft.left, right)
                    helper(None, right.right, parentLeft.left, right)
                else:
                    parentRight.left = None
                    parentLeft.right = TreeNode(right.val)
                    helper(None, right.left, parentLeft.right, right)
                    helper(None, right.right, parentLeft.right, right)

        helper(root.left, root.right, root, root)
        return root


def testInvertFullTree():
    root = TreeNode(
        4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
    )

    sol = Solution()
    actual = sol.invertTree(root)
    expected = TreeNode(
        4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1))
    )

    assert inorder(actual) == [9, 7, 6, 4, 3, 2, 1]
    assert preorder(actual) == [4, 7, 9, 6, 2, 3, 1]


def testInvertSimpleTree():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))

    sol = Solution()
    actual = sol.invertTree(root)

    print("actual: {}".format(actual))
    assert inorder(actual) == [1, 2, 3]
    assert preorder(actual) == [1, 2, 3]


def testInvertSimpleTree2():
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)))

    sol = Solution()
    actual = sol.invertTree(root)

    print("actual: {}".format(actual))
    assert inorder(actual) == [3, 2, 1]
    assert preorder(actual) == [3, 1, 2]


def testInvertSimpleTree3():
    root = TreeNode(3, TreeNode(2), TreeNode(4, TreeNode(1)))

    sol = Solution()
    actual = sol.invertTree(root)

    print("actual: {}".format(actual))
    assert inorder(actual) == [4, 1, 3, 2]
    assert preorder(actual) == [3, 4, 1, 2]


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
