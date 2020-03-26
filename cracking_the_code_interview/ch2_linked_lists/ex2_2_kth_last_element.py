"""
Find the kth last element of the list.
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


def kth_last(root, k):
    if not root or k < 1:
        return None
    current = runner = root
    # move runner pointer k elements forward
    for i in range(k):
        if not runner:
            raise RuntimeError("List has not {} elements".format(k))
        runner = runner.next
    # run though list, stop when runner pointer hits end of list
    while runner:
        runner = runner.next
        current = current.next
    return current


def test():
    root = Node(1, Node(2, Node(3)))
    node = kth_last(root, 1)
    assert node.val == 3

    node = kth_last(root, 2)
    assert node.val == 2

    node = kth_last(root, 3)
    assert node.val == 1

    node = kth_last(root, 0)
    assert not node
