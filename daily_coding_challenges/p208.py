"""Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Given a linked list of numbers and a pivot k, partition the linked
list so that all nodes less than k come before nodes greater than or
equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3,
the solution could be 1 -> 0 -> 5 -> 8 -> 3.

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
    prev = None
    while current:
        tmp = current.nxt
        current.nxt = prev
        prev = current
        current = tmp
    return prev


# def reverse(head):
#     if not head:
#         return None
#     current = head
#     lst = None
#     while current:
#         lst = Node(current.val, lst)
#         current = current.nxt
#     return lst


def partition(head, k):
    lower = None
    bigger = None
    current = reverse(head)
    while current:
        if current.val < k:
            lower = Node(current.val, lower)
        else:
            bigger = Node(current.val, bigger)
        current = current.nxt
    # get lower tail
    current = lower
    if not current:
        return bigger
    while current.nxt:
        current = current.nxt
    tail = current
    tail.nxt = bigger
    return lower


def test():
    l = Node(5, Node(1, Node(8, Node(0, Node(3)))))
    actual = partition(l, k=3)
    print(actual)
    expected = [1, 0, 5, 8, 3]
    assert toList(actual) == expected
