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

    def __repr__(self):
        return "{} ({})".format(self.val, self.nxt)


def toList(head):
    if not head:
        return []
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.nxt
    return result


class Solution:
    def partition(self, head, k):
        if not head:
            return None
        lessHead = None
        bigHead = None
        current = head
        while current:
            if current.val < k:
                node = Node(current.val, lessHead)
                lessHead = node
            else:
                node = Node(current.val, bigHead)
                bigHead = node
            current = current.nxt
        if not lessHead:
            return bigHead
        current = lessHead
        # find last element of lessHead list
        while current.nxt:
            current = current.nxt
        current.nxt = bigHead
        return lessHead


def testMixedElements():
    lst = Node(5, Node(1, Node(8, Node(0, Node(3)))))
    sol = Solution()
    actual = sol.partition(lst, 3)
    expected = [0, 1, 3, 8, 5]
    assert toList(actual) == expected


def testOnlyBiggerElements():
    lst = Node(4, Node(5, Node(6, Node(7))))
    sol = Solution()
    actual = sol.partition(lst, 3)
    expected = [7, 6, 5, 4]
    assert toList(actual) == expected


def testOnlyLesserElements():
    lst = Node(1, Node(2, Node(3, Node(4))))
    sol = Solution()
    actual = sol.partition(lst, 5)
    expected = [4, 3, 2, 1]
    assert toList(actual) == expected


def testNoElements():
    lst = None
    sol = Solution()
    actual = sol.partition(lst, 3)
    expected = []
    assert toList(actual) == expected
