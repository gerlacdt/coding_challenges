"""Sort a stack in ascending order (with biggest items on the
top). You may only use an additional stack to hold items. You may not
copy elements to any other data structure (such as an array). The
stack supports the following operations: push, pop, peek, isEmpty
"""


def sort(stack):
    helperStack = []
    while stack:
        tmp = stack.pop()
        while helperStack and helperStack[-1] > tmp:
            stack.append(helperStack.pop())
        helperStack.append(tmp)
    stack = helperStack


def test():
    stack = [5, 4, 3, 2, 1]
    sort(stack)
    assert stack == sorted(stack)

    stack = [1,3,12,8,5,10,7]
    sort(stack)
    assert stack == sorted(stack)
