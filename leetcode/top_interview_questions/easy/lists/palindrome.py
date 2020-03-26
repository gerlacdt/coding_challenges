"""Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

"""

from collections import namedtuple


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def toList(node):
    result = []
    current = node
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


def isPalindrome(lst):
    i = 0
    j = len(lst) - 1
    while i < j:
        if lst[i] != lst[j]:
            return False
        i += 1
        j -= 1
    return True


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = toList(head)
        return isPalindrome(arr)


def test():
    Case = namedtuple("Case", ["input1", "expected"])
    cases = [Case(fromList([1, 2]), False),
             Case(fromList([1, 2, 2, 1]), True),
             Case(fromList([]), True),
             Case(fromList([1]), True)]
    sol = Solution()
    for c in cases:
        result = sol.isPalindrome(c.input1)
        assert result == c.expected
