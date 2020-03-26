"""Check if a given binary tree is a binary search tree.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def is_bst(root):
    prev = -1000000

    def inorder(node):
        if not node:
            return True
        p = inorder(node.left)
        if not p:
            return False
        nonlocal prev
        if prev > node.val:
            return False
        else:
            prev = node.val
        p = inorder(node.right)
        if not p:
            return False
        return True
    return inorder(root)


def is_bst2(root):

    def helper(node, low, high):
        if not node:
            return True
        if (low and node.val <= low) or (high and node.val > high):
            return False
        if (not helper(node.left, low, node.val)
            or not helper(node.right, node.val, high)):
            return False
        return True
    return helper(root, None, None)


def test():
    root = Node(5, Node(4, Node(2, Node(1), Node(3))),
                Node(7, Node(6), Node(8)))
    result = is_bst(root)
    assert result
    assert result == is_bst2(root)

    root = Node(1)
    result = is_bst(root)
    assert result == is_bst2(root)

    root = Node(5, Node(3), Node(4))
    result = is_bst(root)
    assert not result
    assert result == is_bst2(root)
