"""The sequence [0,1,2,3,4, ... N] has been jumbled, and the only clue
you have for its order is an array representing whether each number is
larger or smaller than the last. Given this information, reconstruct
an array that is consistent with it. For example, given [None, +,
+,-,+], you could return [1,2,3,0,4].

"""


def reconstruct(signs):
    result = []
    n = len(signs) - 1
    stack = []
    for i in range(n):
        if signs[i+1] == "-":
            stack.append(i)
        else:
            result.append(i)
            while stack:
                result.append(stack.pop())
    stack.append(n)
    while stack:
        result.append(stack.pop())
    return result


def test():
    signs = [None, "+", "+", "-", "+"]
    actual = reconstruct(signs)
    expected = [0,1,3,2,4]
    assert actual == expected

    signs = [None, "-", "-", "+", "-"]
    actual = reconstruct(signs)
    expected = [2,1,0,4,3]
    assert actual == expected
