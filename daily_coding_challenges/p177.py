"""Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a linked list and a positive integer k, rotate the list to the
right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it
should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should
become 3 -> 4 -> 5 -> 1 -> 2.
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "({} -> {})".format(self.val, self.next)

    def length(self):
        count = 0
        current = self
        while current:
            current = current.next
            count += 1
        return count


def rotate(head, k):
    k = k % head.length()
    if k == 0:
        return head
    early = head
    late = head
    for i in range(k):
        early = early.next
    while early.next:
        early = early.next
        late = late.next

    # late stands at new head and early is new tail
    newtail = late
    newhead = late.next
    newtail.next = None
    early.next = head
    return newhead


def test():
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    result = rotate(head, 2)
    expected = Node(4, Node(5, Node(1, Node(2, Node(3)))))
    assert str(result) == str(expected)

    head = Node(7, Node(7, Node(3, Node(5))))
    result = rotate(head, 2)
    expected = Node(3, Node(5, Node(7, Node(7))))
    assert str(result) == str(expected)

    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    result = rotate(head, 0)
    expected = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    assert str(result) == str(expected)

    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    result = rotate(head, 5)
    expected = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    assert str(result) == str(expected)

    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    result = rotate(head, 7)
    expected = Node(4, Node(5, Node(1, Node(2, Node(3)))))
    assert str(result) == str(expected)
