"""Write a function to delete a node (except the tail) in a singly
linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]

Explanation: You are given the second node with value 5, the linked
list should become 4 -> 1 -> 9 after calling your function.  Example
2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]

Explanation: You are given the third node with value 1, the linked
list should become 4 -> 5 -> 9 after calling your function.


Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.

"""


class ListNode:
    "Definition for singly-linked list."
    def __init__(self, x, node):
        self.val = x
        self.next = node

    def __str__(self):
        return "({} {})".format(self.val, self.next)


class Solution:
    def deleteNode(self, head: ListNode, node: ListNode) -> None:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current = head
        prev = None
        while current:
            if current == node:
                if not prev:
                    head = current.next
                    break
                prev.next = current.next
                break
            prev = current
            current = current.next
        return head


def toList(head):
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


def test():
    head = ListNode(4, ListNode(5, ListNode(1, ListNode(9, None))))
    sol = Solution()
    sol.deleteNode(head, head.next)

    assert toList(head) == [4, 1, 9]

    head = ListNode(4, ListNode(5, ListNode(1, ListNode(9, None))))
    head = sol.deleteNode(head, head)

    assert toList(head) == [5, 1, 9]
