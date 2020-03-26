# coding: utf-8

"""Implement a stack that has the following methods:

push(val) push val onto stack

pop() pop off and return the topmost element of the stack. If there
are no elements in the stack, throw an error.

max() return the maximum element value in the stack currently. If
there are no elements in the stack, throw an error.

"""


import pytest


class MaxStack:
    def __init__(self):
        self.arr = []

    def push(self, val):
        if not self.arr:
            self.arr.append((val, val))
        else:
            _, localmax = self.arr[-1]
            if val > localmax:
                self.arr.append((val, val))
            else:
                self.arr.append((val, localmax))

    def pop(self):
        if not self.arr:
            raise RuntimeError("No elements in stack")
        last, _ = self.arr.pop()
        return last

    def maxvalue(self):
        if not self.arr:
            raise RuntimeError("No elements in stack")
        _, localmax = self.arr[-1]
        return localmax


def test():
    stack = MaxStack()
    stack.push(4)
    stack.push(3)
    stack.push(7)
    stack.push(1)

    assert stack.maxvalue() == 7
    assert stack.pop() == 1
    assert stack.maxvalue() == 7
    stack.push(8)
    assert stack.maxvalue() == 8
    assert stack.pop() == 8
    assert stack.pop() == 7
    assert stack.maxvalue() == 4
    assert stack.pop() == 3
    assert stack.maxvalue() == 4
    assert stack.pop() == 4

    with pytest.raises(RuntimeError) as excinfo:
        stack.maxvalue()

    assert str(excinfo.value) == "No elements in stack"
