"""Given a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

https://leetcode.com/problems/partition-list/solution/
"""

from collections import namedtuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.var} ({self.next})"


def toList(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result


def reverse(head):
    current = head
    prev = None
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev


def concat(head, other):
    if not head:
        return other
    current = head
    while current.next:
        current = current.next
    current.next = other
    return head


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lo = hi = None
        current = head
        while current:
            if current.val < x:
                lo = ListNode(current.val, lo)
            else:
                hi = ListNode(current.val, hi)
            current = current.next
        return concat(reverse(lo), reverse(hi))

    def partition2(self, head: ListNode, x: int) -> ListNode:
        before = beforeHead = ListNode(0)
        after = afterHead = ListNode(0)
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None

        before.next = afterHead.next
        return beforeHead.next


Case = namedtuple("Case", ["head", "x", "expected"])


def testSol():
    sol = Solution()
    cases = [
        Case(
            ListNode(
                1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))
            ),
            3,
            [1, 2, 2, 4, 3, 5],
        )
    ]
    for c in cases:
        actual = sol.partition(c.head, c.x)
        assert toList(actual) == c.expected

        actual = sol.partition2(c.head, c.x)
        assert toList(actual) == c.expected


def testReverse():
    head = ListNode(1, ListNode(2, ListNode(3)))
    actual = reverse(head)
    assert toList(actual) == [3, 2, 1]


def testConcat():
    head = ListNode(1, ListNode(2, ListNode(3)))
    other = ListNode(4, ListNode(5))
    actual = concat(head, other)
    assert toList(actual) == [1, 2, 3, 4, 5]
