"""Given two binary trees. Return True if they are equal, otherwise
return False.

https://www.geeksforgeeks.org/check-whether-the-two-binary-search-trees-are-identical-or-not
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{}".format(self.val)

    def __repr__(self):
        return self.__str__()


def inorder(tree):
    traversal = []

    def helper(node):
        if not node:
            return
        helper(node.left)
        traversal.append(node.val)
        helper(node.right)

    helper(tree)
    return traversal


def preorder(tree):
    traversal = []

    def helper(node):
        if not node:
            return
        traversal.append(node.val)
        helper(node.left)
        helper(node.right)

    helper(tree)
    return traversal


def isEqual(root1, root2):
    inorderTraversal1 = inorder(root1)
    inorderTraversal2 = inorder(root2)
    preorderTraversal1 = preorder(root1)
    preorderTraversal2 = preorder(root2)

    return (
        inorderTraversal1 == inorderTraversal2
        and preorderTraversal1 == preorderTraversal2
    )


def test():
    tree1 = Node(1, Node(2, Node(4), Node(5)), Node(3))
    tree2 = Node(1, Node(2, Node(4), Node(5)), Node(3))
    actual = isEqual(tree1, tree2)
    expected = True
    assert actual == expected


def testMirrorTree():
    tree1 = Node(1, Node(2, Node(3)))
    tree2 = Node(1, None, Node(2, None, Node(3)))
    actual = isEqual(tree1, tree2)
    expected = False
    assert actual == expected


def testUnequalTrees():
    tree1 = Node(1, Node(2, Node(4), Node(5)), Node(3))
    tree2 = Node(1, Node(2, Node(6), Node(5)), Node(3))
    actual = isEqual(tree1, tree2)
    expected = False
    assert actual == expected
