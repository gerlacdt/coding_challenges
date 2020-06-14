"""Given a linked list, swap every two adjacent nodes and return its
head.

You may not modify the values in the list's nodes, only nodes itself
may be changed.


Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

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
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(node):
            if node and node.next:
                node.val, node.next.val = node.next.val, node.val
                helper(node.next.next)

        helper(head)
        return head


def test1():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    sol = Solution()
    actual = sol.swapPairs(head)
    expected = [2, 1, 4, 3, 6, 5]
    assert toList(actual) == expected


def test2():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution()
    actual = sol.swapPairs(head)
    expected = [2, 1, 4, 3, 5]
    assert toList(actual) == expected


def test3():
    head = ListNode(1)
    sol = Solution()
    actual = sol.swapPairs(head)
    expected = [1]
    assert toList(actual) == expected
