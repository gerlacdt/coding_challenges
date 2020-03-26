"""Implement a function to check i a binary tree is balanced. Heights
of the two subtrees never differ more than one."""


class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def getHeight(node):
    if not node:
        return 0
    height_left = getHeight(node.left)
    if height_left == -1:
        return -1

    height_right = getHeight(node.right)
    if height_right == -1:
        return -1

    if abs(height_left - height_right) > 1:
        return -1
    else:
        return max(height_left, height_right) + 1


def isBalanced(root):
    if getHeight(root) == -1:
        return False
    return True


def test():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    result = isBalanced(root)
    assert result

    root = TreeNode(1)
    result = isBalanced(root)
    assert result

    root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
    result = isBalanced(root)
    assert not result
