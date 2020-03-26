"""Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos
which represents the position (0-indexed) in the linked list where
tail connects to. If pos is -1, then there is no cycle in the linked
list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true

Explanation: There is a cycle in the linked list, where tail connects
to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true

Explanation: There is a cycle in the linked list, where tail connects
to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Follow up:

Can you solve it using O(1) (i.e. constant) memory?

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "({} {})".format(self.val, self.next)


def fromList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next
    return head


def toList(head):
    current = head
    lst = []
    while current:
        lst.append(current.val)
        current = current.next
    return lst


class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


def test():
    sol = Solution()
    input1 = ListNode(3)
    input1.next = ListNode(2)
    input1.next.next = ListNode(0)
    input1.next.next.next = ListNode(-4)
    input1.next.next.next.next = input1.next
    result = sol.hasCycle(input1)
    assert result

    input1 = ListNode(1)
    input1.next = ListNode(2)
    input1.next.next = input1
    result = sol.hasCycle(input1)
    assert result

    input1 = ListNode(1)
    result = sol.hasCycle(input1)
    assert result is False

    input1 = fromList([1, 2, 3])
    result = sol.hasCycle(input1)
    assert result is False
