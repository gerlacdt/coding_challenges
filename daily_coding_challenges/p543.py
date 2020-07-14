"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last
element from the list. k is guaranteed to be smaller than the length
of the list.

The list is very long, so making more than one pass is prohibitively
expensive.

Do this in constant space and in one pass.

"""


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __repr__(self):
        return "{} ({})".format(self.val, self.nxt)


def toList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.nxt
    return result


def removeKthLast(head, k):
    fast = head
    for _ in range(k - 1):
        fast = fast.nxt

    current = head
    prev = None
    while True:
        if not fast.nxt:
            if not prev:
                head = current.nxt
                return head
            prev.nxt = current.nxt
            return head
        fast = fast.nxt
        prev = current
        current = current.nxt


def testRandomElem():
    head = Node(1, Node(2, Node(3, Node(4))))
    actual = removeKthLast(head, 3)
    expected = [1, 3, 4]
    assert toList(actual) == expected


def testFirstElem():
    head = Node(1, Node(2, Node(3)))
    actual = removeKthLast(head, 3)
    expected = [2, 3]
    assert toList(actual) == expected


def testLastElem():
    head = Node(1, Node(2, Node(3, Node(4))))
    actual = removeKthLast(head, 1)
    expected = [1, 2, 3]
    assert toList(actual) == expected
