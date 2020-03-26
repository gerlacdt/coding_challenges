"""Design a stack that supports push, pop, top, and retrieving the
minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""

from collections import namedtuple
import pytest


StackElem = namedtuple("StackElem", ["value", "min"])


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def push(self, x: int) -> None:
        if not self.arr:
            self.arr.append(StackElem(x, x))
        else:
            self.arr.append(StackElem(x, min(x, self.arr[-1].min)))

    def pop(self) -> None:
        if not self.arr:
            raise RuntimeError("No elements in stack.")
        return self.arr.pop().value

    def top(self) -> int:
        if not self.arr:
            raise RuntimeError("No elements in stack.")
        return self.arr[-1].value

    def getMin(self) -> int:
        if not self.arr:
            raise RuntimeError("No elements in stack.")
        return self.arr[-1].min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
def test():
    s = MinStack()
    s.push(1)
    s.push(2)
    s.push(-1)
    s.push(4)

    assert s.getMin() == -1
    assert s.pop() == 4
    assert s.pop() == -1
    assert s.getMin() == 1
    assert s.pop() == 2
    assert s.getMin() == 1
    assert s.pop() == 1
    with pytest.raises(RuntimeError, match=r"No elements in stack.") as ex:
        s.top()
    print("exception message: {}".format(ex.value))
