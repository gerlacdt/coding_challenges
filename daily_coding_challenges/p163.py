"""Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, write a
program to evaluate it.

The expression is given as a list of numbers and operands. For
example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5,
since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.

"""

import operator


OPERATORS = "+-/*"


def isOperator(s):
    if s in OPERATORS:
        return True
    return False


def getOp(op):
    if op == "+":
        return operator.add
    elif op == "-":
        return operator.sub
    elif op == "*":
        return operator.mul
    elif op == "/":
        return operator.floordiv
    else:
        raise RuntimeError("no valid operator: {}".format(op))


def calc(formula):
    # create stack
    # loop over elements formula
    # if elem is number -> push only
    # if elem is operator -> 2x stack.pop() and call operator -> stack.push(result)
    # check stack must be empty
    stack = []
    for elem in formula:
        if isinstance(elem, int):
            stack.append(elem)
        elif isOperator(elem):
            first, second = stack.pop(), stack.pop()
            op = getOp(elem)
            stack.append(op(second, first))
        print("stack: {}".format(stack))
    assert len(stack) == 1
    return stack[0]


def test():
    formula = [5, 3, '+']
    result = calc(formula)
    expected = 8
    assert result == expected
    print("#########")
    formula = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
    result = calc(formula)
    expected = 5
    assert result == expected
