"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the
lists into one sorted singly linked list.

[MEDIUM]
"""

from typing import List
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10000) # needed for big test with 10000 lists


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "({} {})".format(self.val, self.next)

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    # BAD O(n^2) complexity
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     head = None
    #     tail = None
    #     counter = 0
    #     while (any(lists)):
    #         # print("while lists: {}".format([str(v) for v in lists]))
    #         # get next node with minimal value of all k-lists
    #         minimal = None
    #         for i, node in enumerate(lists):
    #             counter += 1
    #             if not node:
    #                 continue
    #             if not minimal:
    #                 minimal = (i, node)
    #                 continue
    #             if node.val < minimal[1].val:
    #                 minimal = (i, node)
    #         minIndex, minNode = minimal
    #         if not head:
    #             head = ListNode(minNode.val)
    #             tail = head
    #         else:
    #             current = ListNode(minNode.val)
    #             tail.next = current
    #             tail = current
    #         lists[minIndex] = minNode.next
    #         if not lists[minIndex]:
    #             del lists[minIndex]
    #         # print("result: {}".format(head))
    #     print("counter: {}".format(counter))
    #     return head

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        "O(N*log(N)) complexity"
        result = []
        for l in lists:
            result.extend(toList(l))
        return toListNode(sorted(result))

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        "min heap approach"
        heap = []
        for l in lists:
            heappush(heap, (l.val, l))
        head = ListNode(-1)  # dummy node, with this if-predicates in loop are reduced
        current = head
        while (heap):
            val, node = heappop(heap)
            current.next = ListNode(val)
            current = current.next
            if (node.next):
                heappush(heap, (node.next.val, node.next))
        return head.next  # first ListNode is dummy node, so skip it

    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:
        "divide-and-conquer approach"
        result = lists[:]
        while (len(result) > 1):
            i = 0
            tmp = []
            while (i+1 < len(result)):
                merged = merge(result[i], result[i+1])
                tmp.append(merged)
                i += 2
            # handle odd length of lists
            if i < len(result):
                tmp.append(result[i])
            result = tmp
        return result[0]


def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val < l2.val:
        node = ListNode(l1.val)
        node.next = merge(l1.next, l2)
        return node
    node = ListNode(l2.val)
    node.next = merge(l1, l2.next)
    return node


def toList(node):
    current = node
    lst = []
    while (current):
        lst.append(current.val)
        current = current.next
    return lst


def toListNode(lst):
    rlst = reversed(lst)
    current = None
    for v in rlst:
        node = ListNode(v)
        node.next = current
        current = node
    return current


## test code

def testmerge():
    l1 = toListNode([1, 4, 5])
    l2 = toListNode([1, 3, 4])
    l3 = toListNode([2, 6])
    l4 = toListNode([])
    result = toList(merge(l2, l3))
    expected = [1, 2, 3, 4, 6]
    assert result == expected

    result = toList(merge(l1, l2))
    expected = [1, 1, 3, 4, 4, 5]
    assert result == expected

    result = toList(merge(l1, l4))
    expected = [1, 4, 5]
    assert result == expected

    result = toList(merge(l4, l1))
    expected = [1, 4, 5]
    assert result == expected


def test1():
    l1 = toListNode([1, 4, 5])
    l2 = toListNode([1, 3, 4])
    l3 = toListNode([2, 6])
    lsts = [l1, l2, l3]
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    solution = Solution()
    result =  toList(solution.mergeKLists(lsts))
    assert result == expected

    result =  toList(solution.mergeKLists2(lsts))
    assert result == expected

    result =  toList(solution.mergeKLists3(lsts))
    assert result == expected

    result =  toList(solution.mergeKLists3(lsts[:2]))
    assert result == [1, 1, 3, 4, 4, 5]

    result =  toList(solution.mergeKLists3([toListNode([1]),
                                            toListNode([2]), toListNode([3])]))
    assert result == [1, 2, 3]


def testlong():
    content = readFile("p78input.txt")
    arr = eval(content)
    input1 = [toListNode(l) for l in arr]
    solution = Solution()

    # with sorting
    result =  toList(solution.mergeKLists(input1))
    assert result == sorted(result)

    # with heap
    result =  toList(solution.mergeKLists2(input1))
    assert result == sorted(result)

    # with divide-and-conquer
    result =  toList(solution.mergeKLists3(input1))
    assert result == sorted(result)


def readFile(filename):
    '''Read whole file with filename into a string and returns it.'''
    with open(filename, 'r') as content_file:
        content = content_file.read().rstrip('\n')
    return content
