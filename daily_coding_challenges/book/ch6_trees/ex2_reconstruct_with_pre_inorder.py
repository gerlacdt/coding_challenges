"""Reconstructs a tree from a given preoder and inorder order
traversals.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def getHeight(root):
    def helper(node, level):
        if not node:
            return level
        left_height = helper(node.left, level+1)
        right_height = helper(node.right, level+1)
        return max(left_height, right_height)
    return helper(root, -1)


def reconstruct(preorder, inorder):
    assert len(preorder) == len(inorder)
    if not preorder and not inorder:
        return None
    if len(preorder) == len(inorder) == 1:
        return Node(preorder[0])

    current = preorder[0]
    mid = inorder.index(current)
    root = Node(inorder[mid])
    root.left = reconstruct(preorder[1:mid+1], inorder[0:mid])
    root.right = reconstruct(preorder[mid+1:], inorder[mid+1:])
    return root


def inorder(root):
    arr = []

    def helper(node):
        if not node:
            return
        helper(node.left)
        arr.append(node.val)
        helper(node.right)
    helper(root)
    return arr


def preorder(root):
    arr = []

    def helper(node):
        if not node:
            return
        arr.append(node.val)
        helper(node.left)
        helper(node.right)
    helper(root)
    return arr


def test():
    preorder1 = ["a", "b", "d", "e", "c", "f", "g"]
    inorder1 = ["d", "b", "e", "a", "f", "c", "g"]

    root = reconstruct(preorder1, inorder1)

    assert preorder(root) == preorder1
    assert inorder(root) == inorder1

    height = getHeight(root)
    assert height == 2

    root = Node(1, Node(2, Node(3, Node(4))))
    height = getHeight(root)
    assert height == 3

    root = Node(1, Node(2, Node(3, Node(4, None, Node(6)))))
    height = getHeight(root)
    assert height == 4
