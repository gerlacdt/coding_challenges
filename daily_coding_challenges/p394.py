"""Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given a binary tree and an integer k, return whether there exists a
root-to-leaf path that sums up to k.

For example, given k = 18 and the following binary tree:

    8
   / \
  4   13
 / \\    \\
2   6   19
Return True since the path 8 -> 4 -> 6 sums to 18.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isLeaf(self):
        return not self.left and not self.right


def findSum(root, k):
    def helper(node, path):
        if not node:
            return None
        p = path[:] + [node.val]
        if node.isLeaf() and sum(p) == k:
            return p
        left = helper(node.left, p.copy())
        if left:
            return left
        right = helper(node.right, p.copy())
        if right:
            return right

    return helper(root, [])


def test():
    root = Node(8, Node(4, Node(2), Node(6)), Node(13, None, Node(19)))
    k = 18
    actual = findSum(root, k)
    expected = [8, 4, 6]
    assert actual == expected

    root = Node(8)
    k = 8
    actual = findSum(root, k)
    expected = [8]
    assert actual == expected

    root = Node(8)
    k = 3
    actual = findSum(root, k)
    expected = None
    assert actual == expected
