"""Given a binary tree, return the level of the tree that has the
minimum sum. The level of a node is defined as the number of
connections required to get to the root, with the root having level
zero.

"""

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def height(root):
    "Return the height of the given binary tree."

    def helper(node):
        if not node:
            return -1
        left = helper(node.left)
        right = helper(node.right)
        return max(left, right) + 1

    if not root:
        return 0
    return helper(root)


def findMinimumIndex(arr):
    "Return the array index which holds the minimum value."
    minIndex = 0
    for i, val in enumerate(arr):
        if val < arr[minIndex]:
            minIndex = i
    return minIndex


def minSumLevel(root):
    """Use BFS with a FIFO-queue. Store node and corresponding
level. Increase level by one if you go down the tree. Hold old level
sums in a array, the indices match to the tree levels.

    """
    frontier = deque([(0, root)])
    levelSums = [0 for _ in range(height(root)+1)]
    while frontier:
        level, node = frontier.popleft()
        levelSums[level] += node.val
        for succ in [node.left, node.right]:
            if succ:
                frontier.append((level+1, succ))
    return findMinimumIndex(levelSums)


def test():
    root = Node(1, Node(2), Node(3, Node(4), Node(5)))
    actual = minSumLevel(root)
    expected = 0
    assert actual == expected

    root = Node(10, Node(2), Node(3, Node(4), Node(5)))
    actual = minSumLevel(root)
    expected = 1
    assert actual == expected

    root = Node(10, Node(2), Node(3, Node(4), Node(5, Node(12))))
    actual = minSumLevel(root)
    expected = 1
    assert actual == expected

    root = Node(10, Node(2, Node(2)), Node(3, Node(4), Node(5, Node(1), Node(1))))
    actual = minSumLevel(root)
    expected = 3
    assert actual == expected
