"""Implement a SetOfStacks class. It should be composed of several
stacks. If one stacks get to high and exceeds capacity you might
create a new stack.

SetOfStacks.push/pop() should behave like a single stack.


FOLLOW UP:

Implement a function popAt(int stack_index) which performs a stack
operation on a specifc sub-stack.

"""

from collections import deque


class SetOfStacks:
    def __init__(self, limit):
        self.arr = []
        self.limit = limit

    def push(self, val):
        if len(self.arr) == 0:
            self.arr.append(deque([]))
        s = self.arr[-1]
        if len(s) < self.limit:
            s.append(val)
        else:
            self.arr.append(deque([val]))

    def pop(self):
        s = self.arr[-1]
        val = s.pop()
        if len(s) == 0:
            self.arr.pop()
        return val

    def popAt(self, i):
        if i >= len(self.arr):
            raise RuntimeError("No enough stacks in set")
        s = self.arr[i]
        val = s.pop()
        for i in range(i, len(self.arr)-1):
            val = self.arr[i+1].popleft()
            self.arr[i].append(val)
        if len(self.arr[-1]) == 0:
            self.arr.pop()


def test():
    stack = SetOfStacks(3)
    for i in range(8):
        stack.push(i)

    assert stack.arr == [deque([0,1,2]), deque([3,4,5]), deque([6,7])]

    for i in range(8):
        val = stack.pop()
        assert val == 7-i

    assert stack.arr == []

    for i in range(8):
        stack.push(i)

    stack.popAt(1)
    assert stack.arr == [deque([0,1,2]), deque([3,4,6]), deque([7])]
    stack.popAt(2)
    assert stack.arr == [deque([0,1,2]), deque([3,4,6])]
    for i in range(3):
        stack.popAt(0)
    assert stack.arr == [deque([0,1,6])]
