"""Given a linked list, remove the n-th node from the end of list and
return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes
1->2->3->5.  Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

"""


class ListNode:
    "Definition for singly-linked list."
    def __init__(self, x, node):
        self.val = x
        self.next = node

    def __str__(self):
        return "({} {})".format(self.val, self.next)

    def __repr__(self):
        return "({} {})".format(self.val, self.next)


def toList(head):
    if not head:
        return None
    current = head
    lst = []
    while current:
        lst.append(current.val)
        current = current.next

    return lst


def fromList(lst):
    if not lst:
        return None
    head = ListNode(lst[0], None)
    prev = head
    current = None
    for i in range(1, len(lst)):
        current = ListNode(lst[i], None)
        prev.next = current
        prev = current
    return head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        lst = []
        while current:
            lst.append(current)
            current = current.next

        if n+1 > len(lst):
            node = lst[-n]
            return node.next
        prev = lst[-n-1]
        node = lst[-n]
        prev.next = node.next
        return head


def test():
    lst = [1, 2, 3, 4, 5]
    head = fromList(lst)
    sol = Solution()
    head = sol.removeNthFromEnd(head, 2)
    result = toList(head)
    expected = [1, 2, 3, 5]

    assert result == expected

    lst = [1, 2]
    head = fromList(lst)
    sol = Solution()
    head = sol.removeNthFromEnd(head, 2)
    result = toList(head)
    expected = [2]

    assert result == expected

    lst = [1]
    head = fromList(lst)
    sol = Solution()
    head = sol.removeNthFromEnd(head, 1)
    result = toList(head)
    expected = None

    assert result == expected
