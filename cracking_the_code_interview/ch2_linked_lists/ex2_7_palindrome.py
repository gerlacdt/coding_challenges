"""
Check if a linked list is a palindrome.
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{} -> {}".format(self.val, self.next)


def toList(root):
    if not root:
        return None
    current = root
    result = []
    while current:
        result.append(current.val)
        current = current.next
    return result


def reverse(head):
    prev = None
    current = head
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev


def isPalindrome(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    root = reverse(head)
    current = root
    for i in range(len(arr)):
        if arr[i] != current.val:
            return False
        current = current.next
    return True


def length(head):
    size = 0
    current = head
    while current:
        current = current.next
        size += 1
    return size


def recusiveSolution(head):
    def helper(head, length):
        print(head, length)
        if not head or length == 0:
            return None, True
        if length == 1:
            return head.next, True
        if length == 2:
            return head.next.next, head.val == head.next.val
        node, result = helper(head.next, length-2)
        if not node or not result:
            return node, result
        else:
            print("return: {}, {}".format(node.next, node.val == head.val))
            return node.next, node.val == head.val
    print("length list: {}".format(length(head)))
    node, result = helper(head, length(head))
    return result


def test():
    head = Node(1, Node(2, Node(3)))
    assert toList(reverse(head)) == [3, 2, 1]

    head = Node(1, Node(2, Node(3)))
    # assert not isPalindrome(head)
    # assert not recusiveSolution(head)

    head = Node(1, Node(2, Node(2, Node(1))))
    # assert isPalindrome(head)
    # assert recusiveSolution(head)

    head = Node(0, Node(1, Node(2, Node(3, Node(4, Node(3, Node(2, Node(1, Node(0)))))))))
    assert recusiveSolution(head)
