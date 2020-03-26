"""Given a binary tree, return a list with all values of the levels of
the tree.

      1
   2     3
  4 5  6  7

should return:
[
[1],
[2,3],
[4,5,6,7]
]
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def height(root):
    if not root:
        return 0
    return max(height(root.left)+1, height(root.right)+1)


def level_order(root):
    if not root:
        return []
    length = height(root)
    arr = [[] for i in range(length)]
    def helper(node, level):
        if not node:
            return
        arr[level].append(node.val)
        helper(node.left, level+1)
        helper(node.right, level+1)
    helper(root, 0)
    return arr


def test():
    root = Node(1, Node(2, Node(4), Node(5)),
                Node(3, Node(6), Node(7)))
    expected = [[1], [2, 3], [4, 5, 6, 7]]
    result = level_order(root)
    assert result == expected

    root = Node(3, Node(9), Node(20, Node(15), Node(7)))
    expected = [
        [3],
        [9, 20],
        [15, 7]
    ]
    result = level_order(root)
    assert result == expected

    result = level_order(None)
    assert result == []
