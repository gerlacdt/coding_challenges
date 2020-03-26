"""Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Given the root of a binary tree, find the most frequent subtree
sum. The subtree sum of a node is the sum of all values under a node,
including the node itself.

For example, given the following tree:

  5
 / \
2  -5

Return 2 as it occurs twice: once as the left leaf, and once as the
sum of 2 + 5 - 5.

"""


from collections import defaultdict


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def subtreeSum(root):
    """Returns the most frequent subtree sum. It is done via a postorder
traversal. For very node the subtree sum is calculated and stored in a
dictionary where every sum is counted. At the end returns the highest
count.
    """
    sums = defaultdict(int)

    def helper(node):
        if not node:
            return 0
        else:
            sumLeft = helper(node.left)
            sumRight = helper(node.right)
            nodeSum = sumLeft + sumRight + node.val
            sums[nodeSum] += 1
            return nodeSum

    helper(root)
    return max(sums.values())


def test():
    root = Node(5, Node(2), Node(-5))
    actual = subtreeSum(root)
    expected = 2 # two times 2
    assert actual == expected

    root = Node(1, Node(2, Node(2), Node(2)), Node(3, Node(2)))
    actual = subtreeSum(root)
    expected = 3  # three times 2
    assert actual == expected
