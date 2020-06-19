"""Merge two sorted linked lists and return it as a new sorted
list. The new list should be made by splicing together the nodes of
the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{} {}".format(self.val, self.next)


def toList(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result


def reverse(head):
    prev = None
    current = head
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result: ListNode = None
        current1 = l1
        current2 = l2
        while current1 and current2:
            if current1.val < current2.val:
                result = ListNode(current1.val, result)
                current1 = current1.next
            else:
                result = ListNode(current2.val, result)
                current2 = current2.next

        while current1:
            result = ListNode(current1.val, result)
            current1 = current1.next

        while current2:
            result = ListNode(current2.val, result)
            current2 = current2.next

        return reverse(result)


def test1():
    lst1 = ListNode(1, ListNode(2, ListNode(4)))
    lst2 = ListNode(1, ListNode(3, ListNode(4)))

    sol = Solution()
    actual = sol.mergeTwoLists(lst1, lst2)
    expected = [1, 1, 2, 3, 4, 4]
    assert toList(actual) == expected
