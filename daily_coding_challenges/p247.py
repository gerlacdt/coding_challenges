"""Good morning! Here's your coding interview problem for today.

This problem was asked by PayPal.

Given a binary tree, determine whether or not it is height-balanced. A
height-balanced binary tree can be defined as one in which the heights
of the two subtrees of any node never differ by more than one.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def isBalanced(root):

    def helper(node):
        if not node:
            return -1, True
        else:
            leftHeight, leftBalanced = helper(node.left)
            rightHeight, rightBalanced = helper(node.right)

            currentHeight = 1 + max(leftHeight, rightHeight)
            diff = abs(leftHeight - rightHeight)
            if diff > 1 or not leftBalanced or not rightBalanced:
                return currentHeight, False
            return currentHeight, True

    height, balanced = helper(root)
    return balanced


def test():
    root = Node(1, Node(2, Node(3), Node(4)),
                Node(5, Node(8, Node(9, Node(11),Node(12))), Node(7)))

    actual = isBalanced(root)
    expected = False
    assert actual == expected

    root = Node(1, Node(2, Node(4), Node(5)), Node(3))
    actual = isBalanced(root)
    expected = True
    assert actual == expected

    root = Node(1)
    actual = isBalanced(root)
    expected = True
    assert actual == expected
