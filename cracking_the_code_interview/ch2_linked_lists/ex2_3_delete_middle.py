"""Delete an node from the middle of single linked list. Given only
access to that node.

example:

1 -> 2 -> 3 -> 4
remove 3:
1 -> 2 -> 4
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} -> {}".format(self.val, self.next)


def toList(root):
    if not root:
        return None
    current = root
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result


def delete(node):
    if not node:
        raise RuntimeError("Node must not be nil")
    if not node.next:
        raise RuntimeError("Node must have a successor")
    node.val = node.next.val
    node.next = node.next.next


def test():
    root = Node(1, Node(2, Node(3, Node(4))))
    assert root.next.next.val == 3
    delete(root.next.next)
    assert toList(root) == [1, 2, 4]
    delete(root)
    assert toList(root) == [2, 4]
