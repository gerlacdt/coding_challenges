"""Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL


Follow up:

A linked list can be reversed either iteratively or recursively. Could
you implement both?

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{} ({})".format(self.val, self.next)


def toList(head):
    if not head:
        return []
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(node):
            if not node or not node.next:
                return node
            rest = helper(node.next)
            node.next.next = node
            node.next = None
            return rest

        return helper(head)


def test():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution()
    actual = sol.reverseList(head)
    print(actual)
    expected = [5, 4, 3, 2, 1]
    assert toList(actual) == expected
