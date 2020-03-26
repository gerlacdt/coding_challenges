# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "({} {})".format(self.val, self.next)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev

    def rreverseList(self, head: ListNode) -> ListNode:
        def helper(curr, prev):
            if not curr.next:
                curr.next = prev
                return curr
            nxt = curr.next
            curr.next = prev
            return helper(nxt, curr)

        if not head:
            return None
        return helper(head, None)


def fromList(lst):
    head = ListNode(lst[0])
    prev = head
    for i in range(1, len(lst)):
        current = ListNode(lst[i])
        prev.next = current
        prev = current

    return head


def toList(head):
    current = head
    lst = []
    while current:
        lst.append(current.val)
        current = current.next
    return lst


def test():
    # Input: 1->2->3->4->5->NULL
    # Output: 5->4->3->2->1->NULL
    lst = [1, 2, 3, 4, 5]
    head = fromList(lst)
    sol = Solution()
    result = sol.reverseList(head)

    # start with new head because reverse() changes list in place
    head = fromList(lst)
    result2 = sol.rreverseList(head)

    expected = list(reversed(lst))
    assert toList(result) == expected
    assert toList(result2) == expected
