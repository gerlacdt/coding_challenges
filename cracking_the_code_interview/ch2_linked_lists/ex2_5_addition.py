"""You have 2 numbers presented as single linked lists. Each node
contains a single digit. The digits are stored in reversed
order. Write a function that adds the two numbers and returns the sum
as a linked list.

(7 -> 1 -> 6) + (5 -> 9 -> 2) that is 617 + 295 = 912
2 -> 1 -> 9

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


def insert(head, val):
    if not head:
        return Node(val)
    current = head
    while current.next:
        current = current.next
    current.next = Node(val)
    return head


def length(head):
    if not head:
        return 0
    current = head
    length = 0
    while current:
        current = current.next
        length += 1
    return length


def pad(head, n):
    for i in range(n):
        head = insert(head, 0)
    return head


def reverse(head):
    prev = None
    current = head
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev


def addition(lst1, lst2):
    c1 = lst1
    c2 = lst2
    curry = 0
    result = None
    while c1 and c2:
        val = c1.val + c2.val + curry
        if val // 10 > 0:
            curry = 1
            val = val % 10
        else:
            curry = 0
        result = insert(result, val)
        c1 = c1.next
        c2 = c2.next
    while c2:
        result = Node(c2.val+curry, result)
        curry = 0
        c2 = c2.next
    while c1:
        result = Node(c1.val+curry, result)
        curry = 0
        c1 = c1.next
    if curry != 0:
        result = insert(result, curry)
    return result


def test():
    lst1 = Node(7, Node(1, Node(6)))
    lst2 = Node(5, Node(9, Node(2)))
    result = addition(lst1, lst2)
    assert toList(result) == [2, 1, 9]

    lst1 = Node(9, Node(9))
    lst2 = Node(2, Node(2))
    result = addition(lst1, lst2)
    assert toList(result) == [1, 2, 1]

    lst1 = Node(0, Node(0, Node(1)))
    lst2 = Node(1)
    result = addition(lst1, lst2)
    assert toList(result) == [1, 0, 1]


    l = Node(1, Node(2, Node(3)))
    result = reverse(l)
    assert toList(result) == [3, 2, 1]

    result = reverse(None)
    assert not result
