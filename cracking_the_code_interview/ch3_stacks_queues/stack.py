"""A simple stack impelmentation with a single linked list.  """

import pytest


class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt

    def __str__(self):
        return "{} -> {}".format(self.val, self.nxt)


def toList(root):
    if not root:
        return None
    current = root
    result = []
    while current:
        result.append(current.val)
        current = current.nxt
    return result


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        node = Node(val, self.top)
        self.top = node

    def pop(self):
        if not self.top:
            raise RuntimeError("Stack is empty!")
        val = self.top.val
        self.top = self.top.nxt
        return val

    def peek(self):
        if not self.top:
            raise RuntimeError("Stack is empty!")
        return self.top.val


def test():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    expected = [5, 4, 3, 2, 1]
    assert toList(stack.top) == expected
    assert stack.peek() == 5

    stack.pop()
    stack.pop()
    assert toList(stack.top) == [3, 2, 1]
    assert stack.peek() == 3

    stack.pop()
    stack.pop()
    stack.pop()
    assert not toList(stack.top)


def test_error():
    with pytest.raises(RuntimeError) as exinfo:
        stack = Stack()
        stack.pop()
    assert str(exinfo.value) == "Stack is empty!"
