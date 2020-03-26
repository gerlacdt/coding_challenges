"""Given two singly linked lists that intersect at some point, find
the intersecting node. Assume the list are non-cyclic.

Example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8. In this example, assume nodes with the
same value are the exact same node objects.

Do this in O(n + m) time. (where m and n are the lengths of the linked
lists) and constant space.
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


def length(head):
    current = head
    counter = 0
    while current:
        counter += 1
        current = current.nxt
    return counter


def intersection(lst1, lst2):
    if not lst1:
        return None
    if not lst2:
        return None
    current1 = lst1
    current2 = lst2
    len1 = length(lst1)
    len2 = length(lst2)
    diff = abs(len1 - len2)
    if len1 > len2:
        # advance lst1 pointer diff-times
        for _ in range(diff):
            current1 = current1.nxt
    else:
        # advance lst2 pointer diff-times
        for _ in range(diff):
            current2 = current2.nxt
    # now advance c1 and c2 together till the intersection node is found
    while current1 and current2:
        print("c1 {} c2 {}".format(current1, current2))
        if current1 == current2:
            return current1
        current1 = current1.nxt
        current2 = current2.nxt
    return None  # no intersection


def test():
    tail = Node(4, Node(5))
    lst1 = Node(6, Node(7, tail))
    lst2 = Node(1, Node(2, Node(3, tail)))
    actual = intersection(lst1, lst2)
    expected = [4, 5]
    assert toList(actual) == expected

    lst1 = Node(1, tail)
    lst2 = tail
    actual = intersection(lst1, lst2)
    expected = [4, 5]
    assert toList(actual) == expected

    lst1 = None
    lst2 = tail
    actual = intersection(lst1, lst2)
    expected = None
    assert actual == expected
