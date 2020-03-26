"""Given a linked list, rotate the list to the right by k places,
where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

"""


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        return "({} {})".format(self.val, self.next)


def length(node):
    count = 0
    current = node
    while current:
        current = current.next
        count += 1
    return count


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


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head:
            return head
        k = k % length(head)
        if k == 0:
            return head
        early = head
        late = head
        for i in range(k):
            early = early.next
        while early.next:
            early = early.next
            late = late.next

        # late stands at new head and early is new tail
        newtail = late
        newhead = late.next
        newtail.next = None
        early.next = head
        return newhead


def test():
    s = Solution()
    head = ListNode(0, ListNode(1, ListNode(2)))
    result = s.rotateRight(head, 4)
    expected = ListNode(2, ListNode(0, ListNode(1)))
    assert toList(result) == toList(expected)

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = s.rotateRight(head, 2)
    expected = ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3)))))
    assert toList(result) == toList(expected)
