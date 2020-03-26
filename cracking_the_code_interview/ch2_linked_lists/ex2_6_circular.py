"""Given a circular list. Return the node at the beginning of the
loop.

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


def headCircle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast


def test():
    head = Node(1, Node(2, Node(3, Node(4))))
    # circular list Node(3) starts loop
    head.next.next.next.next = head.next.next
    current = head
    result = []
    for i in range(10):
        result.append(current.val)
        current = current.next
    assert result == [1, 2, 3, 4, 3, 4, 3, 4, 3, 4]
    assert headCircle(head).val == 3

    head = Node(1, Node(2, Node(3)))
    head.next.next.next = head.next
    assert headCircle(head).val == 2
