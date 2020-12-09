"""Given a sorted linked list, delete all duplicates such that each
element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

"""

from collections import namedtuple
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def toList(head: ListNode) -> List[int]:
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        while current:
            if not prev or (prev.val != current.val):
                prev = current
                current = current.next
            else:
                current = current.next
                prev.next = current
        return head


Case = namedtuple("Case", ["head", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(ListNode(1, ListNode(1, ListNode(2))), [1, 2]),
        Case(
            ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))), [1, 2, 3]
        ),
    ]

    for c in cases:
        actual = sol.deleteDuplicates(c.head)
        assert toList(actual) == c.expected, f"{toList(c.head)}"
