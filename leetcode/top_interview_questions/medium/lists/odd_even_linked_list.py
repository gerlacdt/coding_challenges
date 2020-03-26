"""Given a singly linked list, group all odd nodes together followed
by the even nodes. Please note here we are talking about the node
number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL


Note:

The relative order inside both the even and odd groups should remain
as it was in the input.  The first node is considered odd, the second
node even and so on ...

"""


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        return "({} {})".format(self.val, self.next)


def toList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """Solution approach: Run through the given list with an even and an
        odd pointer. Collect all odds and evens in different single
        linked lists like oddHead and evenHead. After iteration stick
        them together.

        """
        if not head:
            return None
        if not head.next:
            return head
        currentOdd = head
        currentEven = head.next
        odd = None
        even = None
        oddHead = None
        evenHead = None
        while currentOdd and currentEven:
            if odd:
                odd.next = currentOdd
                odd = odd.next
            else:
                odd = currentOdd
                oddHead = odd
            if even:
                even.next = currentEven
                even = even.next
            else:
                even = currentEven
                evenHead = even
            currentOdd = currentOdd.next.next
            if currentOdd:
                currentEven = currentEven.next.next
            else:
                currentEven = None
        if currentOdd:
            odd.next = currentOdd
            odd = odd.next
            even.next = None

        odd.next = evenHead
        return oddHead


def testEvenLength():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    s = Solution()
    actual = s.oddEvenList(head)
    expected = [1, 3, 5, 2, 4, 6]
    assert toList(actual) == expected


def testOddLength():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = Solution()
    actual = s.oddEvenList(head)
    expected = [1, 3, 5, 2, 4]
    assert toList(actual) == expected


def testEdgeCases():
    head = ListNode(1, ListNode(2))
    s = Solution()
    actual = s.oddEvenList(head)
    expected = [1, 2]
    assert toList(actual) == expected

    head = ListNode(1)
    s = Solution()
    actual = s.oddEvenList(head)
    expected = [1]
    assert toList(actual) == expected

    head = None
    s = Solution()
    actual = s.oddEvenList(head)
    expected = []
    assert toList(actual) == expected
