"""Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a complete binary tree, count the number of nodes in faster than
O(n) time. Recall that a complete binary tree has every level filled
except the last, and the nodes in the last level are filled starting
from the left.

"""

from collections import namedtuple


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def countNodes(root: Node) -> int:
    leftHeight = getLeftHeight(root)
    rightHeight = getRightHeight(root)

    if leftHeight == rightHeight:
        return 2**leftHeight - 1

    return countNodes(root.left) + countNodes(root.right) + 1


def getLeftHeight(root: Node) -> int:
    if not root:
        return 0
    height = 0
    current = root
    while current:
        height += 1
        current = current.left
    return height


def getRightHeight(root: Node) -> int:
    if not root:
        return 0
    height = 0
    current = root
    while current:
        height += 1
        current = current.right
    return height


def test():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [Case(None, 0),
             Case(Node(1), 1),
             Case(Node(1, Node(2, Node(3), Node(3)), Node(2, Node(3, Node(3)))), 7),
             Case(Node(1, Node(2, Node(3, Node(4), Node(5)), Node(6, Node(7), Node(8))),
                       Node(9, Node(10), Node(11))), 11),
    ]

    for c in cases:
        actual = countNodes(c.input)
        assert actual == c.expected
