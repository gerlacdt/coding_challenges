"""
Implement 3 stacks with a single array.
"""

import pytest


class TripleStack:
    def __init__(self, stack_size, number_of_stacks=3):
        self.number_of_stacks = number_of_stacks
        self.size = stack_size
        self.tops = [-1 for i in range(3)]
        self.arr = [None for i in range(3*stack_size)]

    def push(self, stack_number, val):
        if stack_number >= self.number_of_stacks:
            raise RuntimeError("Too many stacks")
        top = self.tops[stack_number]
        if top >= self.size:
            raise RuntimeError("Stack {} is full".format(stack_number))
        self.tops[stack_number] += 1
        self.arr[self.size * stack_number + top + 1] = val

    def pop(self, stack_number):
        if stack_number >= self.number_of_stacks:
            raise RuntimeError("Too many stacks")
        top = self.tops[stack_number]
        if top < 0:
            raise RuntimeError("Stack {} is empty".format(stack_number))
        self.tops[stack_number] -= 1
        val = self.arr[self.size * stack_number + top]
        self.arr[self.size * stack_number + top] = None
        return val

    def __str__(self):
        return "tops: {}, arr: {}".format(self.tops, self.arr)


def test():
    s = TripleStack(3)
    assert len(s.arr) == 9

    s.push(0, 1)
    s.push(0, 2)
    s.push(0, 3)

    s.push(1, 1)
    s.push(1, 2)
    s.push(1, 3)

    s.push(2, 1)
    s.push(2, 2)
    s.push(2, 3)

    assert s.tops == [2, 2, 2]
    assert s.arr == [1, 2, 3, 1, 2, 3, 1, 2, 3]

    s.pop(0)
    s.pop(0)
    s.pop(0)

    s.pop(1)
    s.pop(1)
    s.pop(1)

    s.pop(2)
    s.pop(2)
    s.pop(2)

    assert s.tops == [-1, -1, -1]
    assert s.arr == [None for i in range(9)]

    with pytest.raises(RuntimeError) as exinfo:
        s.pop(0)
    assert str(exinfo.value) == "Stack 0 is empty"
