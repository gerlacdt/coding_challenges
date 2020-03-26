"""Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

A tree is symmetric if its data and shape remain unchanged when it is
reflected about the root node. The following tree is an example:

        4
      / | \
    3   5   3
  /           \
9              9

Given a k-ary tree, determine whether it is symmetric.


Binary tree:

symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


not symmetric:

    1
   / \
  2   2
   \   \
   3    3

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


class KNode:
    def __init__(self, val, children=None, k=3):
        self.val = val
        if not children:
            children = [None for _ in range(3)]
        assert len(children) == k
        self.children = children
        self.k = k

    def __str__(self):
        return "{} ({})".format(self.val, [c.val for c in self.children])


def symmetricBinary(root):
    """Simple solution for a binary tree. Use two pointers and advance the
pointers mirror-like."""
    if not root:
        return root

    def helper(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return (helper(left.left, right.right) and
                helper(left.right, right.left))

    return helper(root.left, root.right)


def symmetric(root):
    """Approach do preorder traversal and collect nodes in a list. Do
another preorder traversel but use reversed order of the children and
collect it agin into a list. If the given n-ary tree is symmetric both
lists should be equal.
    """
    resultPreorder = []
    resultPreorderInverse = []

    def preorder(root):
        if not root:
            resultPreorder.append(None)
            return
        resultPreorder.append(root.val)
        for c in root.children:
            preorder(c)

    def preorderInverse(root):
        if not root:
            resultPreorderInverse.append(None)
            return
        resultPreorderInverse.append(root.val)
        cs = reversed(root.children)
        for c in cs:
            preorderInverse(c)

    preorder(root)
    preorderInverse(root)
    return resultPreorder == resultPreorderInverse


def testBinary():
    root = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))
    actual = symmetricBinary(root)
    expected = True
    assert actual == expected

    root = Node(1, Node(2, None, Node(3)), Node(2, None, Node(3)))
    actual = symmetricBinary(root)
    expected = False
    assert actual == expected

    root = Node(1, Node(2, None, Node(3)), Node(2, Node(3), None))
    actual = symmetricBinary(root)
    expected = True
    assert actual == expected


def test():
    root = KNode(4, [KNode(3, [KNode(9, [KNode(1), KNode(2), None]), None, None]),
                     KNode(5),
                     KNode(3, [None, None, KNode(9, [None, KNode(2), KNode(1)])])
    ])
    actual = symmetric(root)
    expected = True
    assert actual == expected

    root = KNode(4, [KNode(3, [KNode(9, [KNode(1), KNode(2), None]), None, None]),
                     KNode(5),
                     KNode(3, [None, None, KNode(9, [None, KNode(2), None])])
    ])
    actual = symmetric(root)
    expected = False
    assert actual == expected

    root = KNode(4, [KNode(3, [KNode(9, [KNode(1), KNode(2), None]), None, None]),
                     KNode(5, [None, KNode(7), KNode(8)]),
                     KNode(3, [None, None, KNode(9, [None, KNode(2), KNode(1)])])
    ])
    actual = symmetric(root)
    expected = False
    assert actual == expected

    root = KNode(4, [KNode(3, [KNode(9, [KNode(1), KNode(2), None]), None, None]),
                     KNode(5, [KNode(8), KNode(7), KNode(8)]),
                     KNode(3, [None, None, KNode(9, [None, KNode(2), KNode(1)])])
    ])
    actual = symmetric(root)
    expected = True
    assert actual == expected

    root = KNode(4, [KNode(3, [KNode(9, [KNode(1), KNode(2), None]), None, None]),
                     KNode(5, [KNode(8), None, KNode(8)]),
                     KNode(3, [None, None, KNode(9, [None, KNode(2), KNode(1)])])
    ])
    actual = symmetric(root)
    expected = True
    assert actual == expected
