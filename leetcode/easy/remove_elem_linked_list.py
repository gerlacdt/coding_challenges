"""Remove all elements from a linked list of integers that have value
val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""

from collections import namedtuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"self.val (self.next)"


def toList(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        current = head

        while current:
            if current.val == val and not prev:
                current = current.next
                head = current
            elif current.val == val and prev:
                current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next

        return head


Case = namedtuple("Case", ["head", "val", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(
            ListNode(
                1,
                ListNode(
                    2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
                ),
            ),
            6,
            [1, 2, 3, 4, 5],
        ),
        Case(ListNode(1, ListNode(1, ListNode(2, ListNode(1)))), 1, [2]),
        Case(ListNode(1, ListNode(1, ListNode(1))), 1, []),
    ]
    for c in cases:
        actual = sol.removeElements(c.head, c.val)
        assert toList(actual) == c.expected, f"{c.head}, {c.val}"
