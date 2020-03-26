"""Count unival trees in the given tree.

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def isLeaf(node):
    if not node.left and not node.right:
        return True
    return False


def unival(root):
    def helper(root):
        if not root:
            return (True, 0)

        if isLeaf(root):
            return (True, 1)

        leftunival, leftcount = helper(root.left)
        rightunival, rightcount = helper(root.right)
        if root.left and root.right:
            if leftunival and rightunival and root.left.val == root.right.val and root.left.val == root.val:
                return (True, leftcount + rightcount + 1)
            else:
                return (False, leftcount + rightcount)
        elif root.left:
            if leftunival and root.left.val == root.val:
                return (True, leftcount + 1)
            else:
                return (False, leftcount)
        elif root.right:
            if rightunival and root.right.val == root.val:
                return (True, rightcount + 1)
            else:
                return (False, rightcount)

    isUnival, count = helper(root)
    return count


def test():
    root = Node(2, Node(2, Node(2)), Node(2, Node(2), Node(2)))
    actual = unival(root)
    expected = 6
    assert actual == expected

    root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    actual = unival(root)
    expected = 5
    assert actual == expected

    root = None
    actual = unival(root)
    expected = 0
    assert actual == expected
