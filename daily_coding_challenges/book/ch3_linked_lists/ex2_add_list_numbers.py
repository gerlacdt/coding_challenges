"""We can represent an integer in a linked list format by having each
node represent a digit in the number. The node are connected in
reverse order, such that the number 54321 is represented by the
following list:

1 -> 2 -> 3 -> 4 -> 5

Give two lists in this format, return their sum:

99 + 25 = 124

9 -> 9
5 -> 2

returns:

4 -> 2 -> 1
"""


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __str__(self):
        return "{} -> {}".format(self.val, self.nxt)


def toList(head):
    if not head:
        return []
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.nxt
    return result


def reverse(head):
    if not head:
        return None
    current = head
    prev = None
    while current:
        tmpNxt = current.nxt
        tmpPrev = prev
        prev = current
        prev.nxt = tmpPrev
        current = tmpNxt
    return prev


def add(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    current1 = lst1
    current2 = lst2
    head = None
    curry = 0
    while current1 and current2:
        localSum = current1.val + current2.val + curry
        if localSum > 9:
            head = Node(localSum % 10, head)
            curry = 1
        else:
            head = Node(localSum, head)
            curry = 0
        current1 = current1.nxt
        current2 = current2.nxt

    while current1:
        localSum = current1.val + curry
        if localSum > 9:
            head = Node(localSum % 10, head)
            curry = 1
        else:
            head = Node(localSum, head)
            curry = 0
        current1 = current1.nxt

    while current2:
        localSum = current2.val + curry
        if localSum > 9:
            head = Node(localSum % 10, head)
            curry = 1
        else:
            head = Node(localSum, head)
            curry = 0
        current2 = current2.nxt

    if not current1 and not current2 and curry > 0:
        head = Node(curry, head)
        curry = 0

    return reverse(head)


def sample_solution(node1, node2, curry=0):
    if not node1 and not node2 and not curry:
        return None
    val1 = node1.val if node1 else 0
    val2 = node2.val if node2 else 0
    node1Nxt = node1.nxt if node1 else None
    node2Nxt = node2.nxt if node2 else None
    total = val1 + val2 + curry
    if total > 9:
        curry = 1
    else:
        curry = 0
    return Node(total % 10, sample_solution(node1Nxt, node2Nxt, curry))


def test():
    lst1 = Node(9, Node(9))
    lst2 = Node(5, Node(2))
    actual = add(lst1, lst2)
    actual2 = sample_solution(lst1, lst2)
    expected = [4,2,1]
    assert toList(actual) == expected
    assert toList(actual2) == expected

    lst1 = Node(1)
    lst2 = Node(9, Node(9, Node(9)))
    actual = add(lst1, lst2)
    actual2 = sample_solution(lst1, lst2)
    expected = [0,0,0,1]
    assert toList(actual) == expected
    assert toList(actual2) == expected


    lst1 = None
    lst2 = Node(0, Node(1))
    actual = add(lst1, lst2)
    actual2 = sample_solution(lst1, lst2)
    expected = [0,1]
    assert toList(actual) == expected
    assert toList(actual2) == expected
