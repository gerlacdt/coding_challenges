"""You have 2 tree. T1 with millions of nodes and T2 with hundreds of
nodes.

Implement a function to check if T2 is a subtree of T1.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def isEqual(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False  # one node is null
    if t1.val == t2.val:
        return (isEqual(t1.left, t2.left) and
                isEqual(t1.right, t2.right))
    return False


def isSubtree(t1, t2):
    if not t1:
        return False
    if t1.val == t2.val:
        if isEqual(t1, t2):
            return True
    return isSubtree(t1.left, t2) or isSubtree(t2.right, t2)


def containsTree(t1, t2):
    if not t2:
        return True
    return isSubtree(t1, t2)


def test():
    node2 = Node(2, Node(4), Node(5))
    node3 = Node(3, Node(6), Node(7))
    t1 = Node(1, node2, node3)
    t2 = Node(3, Node(6), Node(7))

    assert containsTree(t1, t2)
    t2 = Node(6)
    assert containsTree(t1, t2)
    assert containsTree(node3, t2)
    assert not containsTree(t1, Node(8))
    assert not containsTree(t1, Node(3, Node(6), Node(7)))
