"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the
intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8.

In this example, assume nodes with the same value are the exact same
node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists)
and constant space.

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


def length(head):
    return len(toList(head))


class Solution:
    def findIntersection(self, lst1, lst2):
        len1 = length(lst1)
        len2 = length(lst2)
        diff = abs(len1 - len2)
        current1 = lst1
        current2 = lst2
        if len1 >= len2:
            for _ in range(diff):
                current1 = current1.nxt
        else:
            for _ in range(diff):
                current2 = current2.nxt

        while current1 != current2:
            current1 = current1.nxt
            current2 = current2.nxt

        return current1


def testIntersectionSameLength():
    node3 = Node(3)
    node7 = Node(7)
    node8 = Node(8)
    node10 = Node(10)
    node3.nxt = node7
    node7.nxt = node8
    node8.nxt = node10

    node99 = Node(99)
    node1 = Node(1)
    node99.nxt = node1
    node1.nxt = node8

    sol = Solution()
    actual = sol.findIntersection(node3, node99)
    expected = 8
    assert actual.val == expected


def testIntersectionDifferentLength():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)

    # first list
    node1.nxt = node2
    node2.nxt = node3
    node3.nxt = node4
    node4.nxt = node5
    node5.nxt = node6

    # second list, intersects with first list
    node7.nxt = node8
    node8.nxt = node5

    sol = Solution()
    actual = sol.findIntersection(node1, node7)
    expected = 5
    assert actual.val == expected


def testNoIntersection():
    lst1 = Node(1, Node(2))
    lst2 = Node(3, Node(4))
    sol = Solution()
    actual = sol.findIntersection(lst1, lst2)
    expected = None
    assert actual == expected
