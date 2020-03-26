"""Write a program to find the node at which the intersection of two
singly linked lists begins.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8

Input Explanation: The intersected node's value is 8 (note that this
must not be 0 if the two lists intersect). From the head of A, it
reads as [4,1,8,4,5]. From the head of B, it reads as
[5,0,1,8,4,5]. There are 2 nodes before the intersected node in A;
There are 3 nodes before the intersected node in B.


Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2

Input Explanation: The intersected node's value is 2 (note that this
must not be 0 if the two lists intersect). From the head of A, it
reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There
are 3 nodes before the intersected node in A; There are 1 node before
the intersected node in B.


Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null

Input Explanation: From the head of A, it reads as [2,6,4]. From the
head of B, it reads as [1,5]. Since the two lists do not intersect,
intersectVal must be 0, while skipA and skipB can be arbitrary values.

Explanation: The two lists do not intersect, so return null.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def length(head):
    current = head
    counter = 0
    while current:
        counter += 1
        current = current.next
    return counter


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        lengthA = length(headA)
        lengthB = length(headB)
        diff = abs(lengthA - lengthB)
        currentA = headA
        currentB = headB
        if lengthA > lengthB:
            # move headA pointer
            for i in range(diff):
                currentA = currentA.next
        elif lengthA < lengthB:
            # move headB pointer
            for i in range(diff):
                currentB = currentB.next

        while currentA and currentB:
            if currentA == currentB:
                return currentA
            currentA = currentA.next
            currentB = currentB.next
        return None


def test():
    #       a1 -> a2 -> c1 -> c2 -> c3
    # b1 -> b2 -> b3 ---^
    a1 = ListNode(4)
    a2 = ListNode(1)
    b1 = ListNode(5)
    b2 = ListNode(0)
    b3 = ListNode(1)
    c1 = ListNode(8)
    c2 = ListNode(4)
    c3 = ListNode(5)

    a1.next = a2
    a2.next = c1
    b1.next = b2
    b2.next = b3
    b3.next = c1
    c1.next = c2
    c2.next = c3

    sol = Solution()
    actual = sol.getIntersectionNode(a1, b1)
    expected = c1
    assert actual == expected


def test2():
    # a1 -> a2 -> a3 -> c1 -> c2
    #             b1 ---^
    a1 = ListNode(0)
    a2 = ListNode(9)
    a3 = ListNode(1)
    b1 = ListNode(3)
    c1 = ListNode(2)
    c2 = ListNode(4)

    a1.next = a2
    a2.next = a3
    a3.next = c1
    b1.next = c1
    c1.next = c2

    sol = Solution()
    actual = sol.getIntersectionNode(a1, b1)
    expected = c1
    assert actual == expected


def test3():
    # a1 -> a2 -> a3
    # b1 -> b2
    a1 = ListNode(2)
    a2 = ListNode(6)
    a3 = ListNode(4)
    b1 = ListNode(1)
    b2 = ListNode(5)

    a1.next = a2
    a2.next = a3
    b1.next = b2

    sol = Solution()
    actual = sol.getIntersectionNode(a1, b1)
    expected = None
    assert actual == expected
