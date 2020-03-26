"""Merge two sorted linked lists and return it as a new list. The new
list should be made by splicing together the nodes of the first two
lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "({} {})".format(self.val, self.next)


def toList(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result


def fromList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next
    return head


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        current = head
        while l1 and l2:
            if l1.val < l2.val:
                current.next = ListNode(l1.val)
                current = current.next
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                current = current.next
                l2 = l2.next

        # lists have not the same length
        while l1:
            current.next = ListNode(l1.val)
            current = current.next
            l1 = l1.next
        while l2:
            current.next = ListNode(l2.val)
            current = current.next
            l2 = l2.next
        return head.next


def test():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    sol = Solution()
    result = sol.mergeTwoLists(l1,l2)
    expected = [1, 1, 2, 3, 4, 4]
    assert toList(result) == expected
    assert toList(fromList(expected)) == expected
