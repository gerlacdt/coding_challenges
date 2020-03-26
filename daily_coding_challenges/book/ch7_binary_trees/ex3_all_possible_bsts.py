"""Construct all BSTs with n nodes.

Given an integer n, construct all possible binary search trees with n
nodes where all values from [1, ..., n] are used.

Example:

n = 3

There are 5 possibilities.

Possiblities are the Catalan numbers:
1,2,5,14,42,132,429,1430

Hence time complexity is O(n * 2**n)

"""

from collections import namedtuple


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def allBSTs(n):

    def helper(low, high):
        if low > high:
            return [None]
        trees = []
        for i in range(low, high+1):
            leftTrees = helper(low, i-1)
            rightTrees = helper(i+1, high)
            for l in leftTrees:
                for r in rightTrees:
                    trees.append(Node(i, l, r))
        return trees

    return helper(1, n)


def test():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [Case(1,1), Case(2,2), Case(3,5),
             Case(4,14), Case(5,42),
             Case(6,132), Case(7,429),
             Case(8, 1430),
    ]


    for c in cases:
        actual = allBSTs(c.input)
        assert len(actual) == c.expected
