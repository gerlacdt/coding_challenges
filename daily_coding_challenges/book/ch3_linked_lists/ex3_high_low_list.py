"""Given a linked list, rearrange the node values such that they
appear in alternating low -> high -> low -> high -> ...

For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4

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


def highlow(head):
    even = True
    current = head
    while current:
        if not even and current.nxt and current.val < current.nxt.val:
            current.val, current.nxt.val = current.nxt.val, current.val
        if even and current.nxt and current.val > current.nxt.val:
            current.val, current.nxt.val = current.nxt.val, current.val
        even = not even
        current = current.nxt
    return head


def highlow2(head):
    if not head:
        return None
    prev = head
    current = head.nxt
    while current:
        if prev.val > current.val:
            prev.val, current.val = current.val, prev.val
        if not current.nxt:
            break
        if current.val < current.nxt.val:
            current.val, current.nxt.val = current.nxt.val, current.val
        prev = current.nxt
        current = current.nxt.nxt
    return head


def test():
    # odd number of items
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    head2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    actual = highlow(head)
    actual2 = highlow2(head2)
    expected = [1,3,2,5,4]
    assert toList(actual) == expected
    assert toList(actual2) == expected

    # even number of items
    head = Node(1, Node(2, Node(3, Node(4))))
    head2 = Node(1, Node(2, Node(3, Node(4))))
    actual = highlow(head)
    actual2 = highlow2(head2)
    expected = [1,3,2,4]
    assert toList(actual) == expected
    assert toList(actual2) == expected

    # reverse sorted items in list
    head = Node(5, Node(4, Node(3, Node(2, Node(1)))))
    head2 = Node(5, Node(4, Node(3, Node(2, Node(1)))))
    actual = highlow(head)
    actual2 = highlow2(head2)
    expected = [4,5,2,3,1]
    assert toList(actual) == expected
    assert toList(actual2) == expected
