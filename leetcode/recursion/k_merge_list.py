"""Merge k sorted linked lists and return it as one sorted
list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5-6>

"""

from typing import List


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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pass


def test():
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    lists = [l1, l2, l3]
    sol = Solution()
    actual = sol.mergeKLists(lists)
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    assert toList(actual) == expected
