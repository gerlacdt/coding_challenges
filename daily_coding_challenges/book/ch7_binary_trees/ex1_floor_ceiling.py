"""Given a binary tree, the floor and ceiling of a given integer. The
floor is the highest element in the tree less then or equal to an
integer, while the ceiling is the lowest element in the tree greater
than or equal to an integer.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def findFloorCeiling(root, value):

    def helper(node, val, floor=None, ceiling=None):
        print("node: {} floor: {} ceiling: {}".format(node, floor, ceiling))
        if not node:
            return floor, ceiling

        if val == node.val:
            return val, val

        if val < node.val:
            return helper(node.left, val, floor, node.val)

        if val > node.val:
            return helper(node.right, val, node.val, ceiling)

    return helper(root, value)


def test():
    root = Node(10, Node(7, Node(3, Node(2, Node(1)), Node(4)),
                         Node(8)), Node(15, Node(13), Node(17, Node(16))))

    floor, ceiling = findFloorCeiling(root, 9)
    assert (floor, ceiling) == (8, 10)
