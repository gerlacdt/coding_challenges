"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which
serializes the tree into a string, and deserialize(s), which
deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""

from collections import deque

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)
        pass

    def serialize(self):
        collector = []

        def helper(node):
            collector.append(str(node.val))
            if node.left:
                helper(node.left)
            else:
                collector.append("NIL")
            if node.right:
                helper(node.right)
            else:
                collector.append("NIL")
        helper(self)
        return " ".join(collector)

    def __str__(self):
        return "Node('{}', {}, {})".format(self.val, self.left, self.right)


def deserialize(s):
    items = deque(s.split())
    def helper(items):
        val = items.popleft()
        if val == 'NIL':
            return None
        root = Node(val)
        root.left = helper(items)
        root.right = helper(items)
        return root
    return helper(items)


def test():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(node.serialize())
    assert deserialize(node.serialize()).left.left.val == 'left.left'
