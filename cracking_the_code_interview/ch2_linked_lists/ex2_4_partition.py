"""Partition a linked list around a value x, such thatall nodes less
than x come before all nodes greater than or equal to x.

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


def partition(root, x):
    if not root:
        return None
    lesslst = None
    gtlst = None
    current = root
    while current:
        if current.val < x:
            lesslst = Node(current.val, lesslst)
        else:
            gtlst = Node(current.val, gtlst)
        current = current.next
    if not lesslst:
        return gtlst
    # append gtlst ot last node of lesslst
    current = lesslst
    while current.next:
        current = current.next
    current.next = gtlst
    return lesslst


def test():
    root = Node(7, Node(3, Node(5, Node(10, Node(1, Node(2))))))
    lst = partition(root, 5)
    print(toList(lst))
    assert toList(lst) == [2, 1, 3, 10, 5, 7]

    root = Node(7)
    lst = partition(root, 5)
    assert toList(lst) == [7]

    root = Node(4)
    lst = partition(root, 5)
    assert toList(lst) == [4]
