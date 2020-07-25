"""Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

"""

from collections import namedtuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{} ({})".format(self.val, self.next)


def toList(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid = self._findMid(head)
        tmp = mid.next
        mid.next = None
        left = self.sortList(head)
        right = self.sortList(tmp)
        return self._merge(left, right)

    def _findMid(self, head):
        if not head:
            return None
        current = head
        fast = head.next
        while current.next and fast and fast.next and fast.next.next:
            current = current.next
            fast = fast.next.next
        return current

    def _merge(self, left, right):
        head = None
        tail = None
        if not left:
            return right
        if not right:
            return left
        while left and right:
            if not head:
                if left.val < right.val:
                    head = left
                    left = left.next
                    head.next = None
                    tail = head
                else:
                    head = right
                    right = right.next
                    head.next = None
                    tail = head
            else:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                    tail = tail.next
                    tail.next = None
                else:
                    tail.next = right
                    right = right.next
                    tail = tail.next
                    tail.next = None

        if left:
            tail.next = left
        if right:
            tail.next = right
        return head


Case = namedtuple("Case", ["head", "expected"])


def testFindMid():
    cases = [
        Case(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 2),
        Case(ListNode(1, ListNode(2, ListNode(3))), 1),
        Case(ListNode(1, ListNode(2)), 1),
        Case(ListNode(1), 1),
    ]
    sol = Solution()
    for c in cases:
        actual = sol._findMid(c.head)
        assert actual.val == c.expected, "Case: {}".format(toList(c.head))


def testMerge():
    cases = [
        Case((ListNode(1, ListNode(3)), ListNode(2, ListNode(4))), [1, 2, 3, 4]),
        Case((ListNode(1), ListNode(2, ListNode(3, ListNode(4)))), [1, 2, 3, 4]),
        Case((ListNode(2, ListNode(3, ListNode(4))), ListNode(1)), [1, 2, 3, 4]),
        Case((None, ListNode(1, ListNode(2))), [1, 2]),
    ]
    sol = Solution()
    for c in cases:
        left, right = c.head
        actual = sol._merge(left, right)
        assert toList(actual) == c.expected, "Case: {} {}".format(
            toList(left), toList(right)
        )


def testSort():
    cases = [
        Case(None, []),
        Case(ListNode(1), [1]),
        Case(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))), [1, 2, 3, 4]),
        Case(ListNode(3, ListNode(2, ListNode(1))), [1, 2, 3]),
    ]

    sol = Solution()
    for c in cases:
        actual = sol.sortList(c.head)
        assert toList(actual) == c.expected
