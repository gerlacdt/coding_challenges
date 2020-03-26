"""Count all unival trees in a given binary tree.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countUnival(root):
    result = 0

    def isUnival(node):
        nonlocal result
        if node.left and node.right:
            isLeftUnival = isUnival(node.left)
            isRightUnival = isUnival(node.right)
            if isLeftUnival and isRightUnival and node.left.val == node.right.val and node.val == node.left.val:
                result += 1
                return True
        elif node.right:
            isRightUnival = isUnival(node.right)
            if isRightUnival and node.val == node.right.val:
                result += 1
                return True
        elif node.left:
            isLeftUnival = isUnival(node.left)
            if isLeftUnival and node.val == node.left.val:
                result += 1
                return True
        else:
            # no left and right node exist -> must be a leaf, leafs
            # are by definition an unival tree
            result += 1
            return True
        return False

    isUnival(root)
    return result


def test():
    root = Node(1, Node(3), Node(2, Node(2), Node(2, None, Node(2))))
    actual = countUnival(root)
    expected = 5
    assert actual == expected

    root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    actual = countUnival(root)
    expected = 5
    assert actual == expected

    root = Node(1, Node(1), Node(1, Node(1), Node(1, None, Node(2))))
    actual = countUnival(root)
    expected = 3
    assert actual == expected
