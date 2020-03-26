"""Reverse a given linked list.

"""


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __str__(self):
        return "{} -> {}".format(self.val, self.nxt)


def toList(head):
    if not head:
        return []
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.nxt
    return result


def reverse(head):
    if not head:
        return None
    current = head
    node = None
    while current:
        node = Node(current.val, node)
        current = current.nxt
    return node


def reverse2(head):
    if not head:
        return None
    current = head
    prev = None
    while current:
        tmp = current.nxt
        current.nxt = prev
        prev = current
        current = tmp
    return prev


def test():
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    actual = reverse(head)
    actual2 = reverse2(head)
    expected = [5,4,3,2,1]
    print(actual)
    assert toList(actual) == expected
    assert toList(actual2) == expected
