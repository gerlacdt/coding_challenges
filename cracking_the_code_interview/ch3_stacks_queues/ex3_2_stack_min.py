"""Design a stack with an additional min() function which returns the
minimum element. push(), pop(), min() should operate in O(n). """

from random import randint


class Elem:
    def __init__(self, val, min):
        self.val = val
        self.min = min

    def __lt__(self, other):
        return self.val < other.val

    def __repr__(self):
        return "({} {})".format(self.val, self.min)


class Stack:
    def __init__(self):
        self.arr = []

    def push(self, x):
        if len(self.arr) == 0:
            self.arr.append(Elem(x, x))
            return None
        top = self.arr[-1]
        if x < top.min:
            self.arr.append(Elem(x, x))
        else:
            self.arr.append(Elem(x, top.min))

    def pop(self):
        if len(self.arr) == 0:
            raise RuntimeError("No elements in stack")
        return self.arr.pop().val

    def min(self):
        if len(self.arr) == 0:
            raise RuntimeError("No elements in stack")
        return self.arr[-1].min

    def peek(self):
        if len(self.arr) == 0:
            raise RuntimeError("No elements in stack")
        return self.arr[-1].val


def test():
    stack = Stack()
    for i in range(3):
        x = randint(0, 50)
        stack.push(x)
        assert stack.min() == min(stack.arr).val

    for i in range(3):
        assert stack.min() == min(stack.arr).val
        stack.pop()
