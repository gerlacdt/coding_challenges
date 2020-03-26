"""Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a linked list, remove all consecutive nodes that sum to
zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6-> 6.
In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.

"""


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __str__(self):
        return "{} ({})".format(self.val, self.nxt)


def toList(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.nxt
    return lst


def removeZeroSums(head):
    current = head
    prev = None

    while current:
        currentSum = 0
        runner = current
        foundZero = False
        while runner:
            currentSum += runner.val
            if currentSum == 0:
                foundZero = True
                if not prev:
                    # found Zero at the beginning of the list, change original head
                    head = runner.nxt
                    current = runner.nxt
                    break
                else:
                    # skip zero sum
                    prev.nxt = runner.nxt
                    current = runner.nxt
                    break
            else:
                runner = runner.nxt
        if foundZero:
            continue
        else:
            prev = current
            current = current.nxt

    return head


def test():
    head = Node(3, Node(4, Node(-7, Node(5, Node(-6, Node(6))))))
    actual = removeZeroSums(head)
    expected = [5]
    assert toList(actual) == expected


def testNoZeros():
    head = Node(3, Node(5))
    actual = removeZeroSums(head)
    expected = [3, 5]
    assert toList(actual) == expected


def testInnerZeros():
    head = Node(3, Node(4, Node(-4, Node(5))))
    actual = removeZeroSums(head)
    expected = [3, 5]
    assert toList(actual) == expected


def testHeadZeros():
    head = Node(3, Node(4, Node(-7, Node(5))))
    actual = removeZeroSums(head)
    expected = [5]
    assert toList(actual) == expected


def testEndZeros():
    head = Node(3, Node(4, Node(-4)))
    actual = removeZeroSums(head)
    expected = [3]
    assert toList(actual) == expected
