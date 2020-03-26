"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a binary search tree and a range [a, b] (inclusive), return the
sum of the elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10

and the range [4, 9], return 23 (5 + 4 + 6 + 8).

"""

from collections import namedtuple


class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right


def minimum(node):
    if not node:
        raise RuntimeError("Node is null")
    if node.left:
        current = node
        while current.left:
            current = current.left
        return current
    return node


def successor(node):
    if node.right:
        return minimum(node.right)
    parent = node.parent
    current = node
    while parent and current == parent.right:
        current = parent
        parent = parent.parent
    return parent


def search(node, val):
    if not node:
        return None
    if node.val == val:
        return node
    if node.val < val:
        if node.right:
            return search(node.right, val)
        else:
            if node.val > val:
                return node
            else:
                return successor(node)
    else:
        if node.left:
            return search(node.left, val)
        else:
            if node.val > val:
                return node
            else:
                return successor(node)


def rangeSum(rang, root):
    start, end = rang
    current = search(root, start)
    result = []
    while current:
        if current.val > end:
            break
        else:
            result.append(current.val)
        current = successor(current)
    return sum(result)


Case = namedtuple("Case", ["input", "expected", "name"])


def createTree():
    root = Node(5, None)
    three = Node(3, root)
    two = Node(2, three)
    four = Node(4, three)
    three.left = two
    three.right = four
    eight = Node(8, root)
    six = Node(6, eight)
    ten = Node(10, eight)
    eight.left = six
    eight.right = ten
    root.left = three
    root.right = eight
    return root


def testMinimum():
    root = createTree()
    cases = [
        Case(root, 2, "root 2"),
        Case(root.right.right, 10, "ten 10"),
        Case(root.right, 6, "eight 6"),
    ]
    for c in cases:
        actual = minimum(c.input)
        if not c.expected:
            assert not actual
        else:
            assert actual.val == c.expected, c.name


def testSuccessor():
    root = createTree()
    cases = [
        Case(root, 6, "root 6"),
        Case(root.left, 4, "three 4"),
        Case(root.right.right, None, "ten None"),
        Case(root.left.right, 5, "four 5"),
        Case(root.right.left, 8, "six 8"),
    ]
    for c in cases:
        actual = successor(c.input)
        if not c.expected:
            assert not actual
        else:
            assert actual.val == c.expected, c.name


def testSearch():
    root = createTree()
    cases = [Case(4, 4, "4"), Case(6, 6, "6"), Case(7, 8, "7"), Case(1, 2, "1")]
    for c in cases:
        actual = search(root, c.input)
        if not c.expected:
            assert not actual
        else:
            assert actual.val == c.expected, c.name


def testSumRange():
    root = createTree()
    cases = [
        Case((2, 10), 38, "38"),
        Case((4, 9), 23, "23"),
        Case((0, 12), 38, "all 38"),
    ]

    for c in cases:
        actual = rangeSum(c.input, root)
        assert actual == c.expected, c.name
