"""Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a linked list and an integer k, remove the k-th node from the
end of the list and return the head of the list.

k is guaranteed to be smaller than the length of the list.

Do this in one pass.

"""


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __str__(self):
        return "{} -> {}".format(self.val, self.nxt)


def toLst(head):
    current = head
    lst = []
    while current:
        lst.append(current.val)
        current = current.nxt
    return lst


def fromLst(lst):
    current = None
    for i in range(len(lst) - 1, -1, -1):
        node = Node(lst[i], current)
        current = node
    return current


def remove(head, k):
    if k == 0:
        head = head.nxt
        return head
    current = head
    prev = None
    i = 0
    while current:
        if i == k:
            prev.nxt = current.nxt
            break
        prev = current
        current = current.nxt
        i += 1

    return head


def test():
    head = Node(1, Node(2, Node(4, Node(5))))
    k = 2
    actual = remove(head, k)
    expected = [1, 2, 5]
    assert toLst(actual) == expected

    head = Node(1, Node(2, Node(4, Node(5))))
    k = 3
    actual = remove(head, k)
    expected = [1, 2, 4]
    assert toLst(actual) == expected

    head = Node(1, Node(2, Node(4, Node(5))))
    k = 0
    actual = remove(head, k)
    expected = [2, 4, 5]
    assert toLst(actual) == expected


def testToLst():
    head = Node(1, Node(2, Node(3)))
    actual = toLst(head)
    expected = [1, 2, 3]
    assert actual == expected


def testFromList():
    lst = [1, 2, 3]
    actual = fromLst(lst)
    expected = lst
    assert toLst(actual) == expected
