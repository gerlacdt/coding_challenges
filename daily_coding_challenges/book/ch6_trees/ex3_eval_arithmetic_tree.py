"""Eval a arithmetic expression, given as a binary tree. Each leaf is
an integer and each internal node is one of +, -, *, /.

Given the root to such tree, write a function too evaluate it.

"""

import operator


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def isLeaf(node):
    if not node.left and not node.right:
        return True
    return False


def operation(op, leftval, rightval):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    return ops[op](leftval, rightval)


def evaluate(root):
    if not root:
        return 0
    if isLeaf(root):
        return root.val
    leftval = evaluate(root.left)
    rightval = evaluate(root.right)
    return operation(root.val, leftval, rightval)


def test():
    root = Node("*", Node("+", Node(3), Node(2)), Node("+", Node(4), Node(5)))
    actual = evaluate(root)
    expected = 45
    assert actual == expected

    root = Node("+", Node(1), Node("-", Node(4), Node("+", Node(5), Node(1))))
    actual = evaluate(root)
    expected = -1
    assert actual == expected
