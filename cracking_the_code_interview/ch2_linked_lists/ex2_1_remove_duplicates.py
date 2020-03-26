"""
Remove duplicates from an unsorted linked list.

Follow up: Can you do it without additional space.
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


def remove_duplicates(root):
    if not root:
        return None
    seen = set()
    prev = None
    current = root
    while current:
        if current.val in seen:
            # remove current
            if prev:
                prev.next = current.next
            current = current.next
        else:
            seen.add(current.val)
            prev = current
            current = current.next
    return root


def test():
    root = Node(1, Node(2, Node(3, Node(4, Node(2)))))
    root = remove_duplicates(root)
    assert toList(root) == [1, 2, 3, 4]

    root = Node(1, Node(1, Node(1)))
    root = remove_duplicates(root)
    assert toList(root) == [1]
