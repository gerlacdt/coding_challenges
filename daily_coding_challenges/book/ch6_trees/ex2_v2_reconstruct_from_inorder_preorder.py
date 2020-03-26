"""Reconstruct a binary tree from a given inorder and preorder
traversal."""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def inorder(root):
    result = []

    def helper(node):
        if not node:
            return None
        helper(node.left)
        result.append(node.val)
        helper(node.right)
    helper(root)
    return result


def preorder(root):
    result = []

    def helper(node):
        if not node:
            return None
        result.append(node.val)
        helper(node.left)
        helper(node.right)
    helper(root)
    return result


def reconstruct(inorder, preorder):
    def helper(inorder, preorder):
        if not inorder or not preorder:
            return None
        assert len(inorder) == len(preorder)
        node = Node(preorder[0])
        mid = inorder.index(node.val)
        node.left = helper(inorder[:mid], preorder[1:mid+1])
        node.right = helper(inorder[mid+1:], preorder[mid+1:])
        return node
    return helper(inorder, preorder)


def test():
    preorderTraversal = ["a", "b", "d", "e", "c", "f", "g"]
    inorderTraversal = ["d", "b", "e", "a", "f", "c", "g"]
    actual = reconstruct(inorderTraversal, preorderTraversal)
    expected = Node("a", Node("b", Node("d"), Node("e")),
                    Node("c", Node("f"), Node("g")))
    assert inorder(actual) == inorder(expected)
    assert preorder(actual) == preorder(expected)

    preorderTraversal = ["a"]
    inorderTraversal = ["a"]
    actual = reconstruct(inorderTraversal, preorderTraversal)
    assert inorder(actual) == inorderTraversal
    assert preorder(actual) == preorderTraversal
