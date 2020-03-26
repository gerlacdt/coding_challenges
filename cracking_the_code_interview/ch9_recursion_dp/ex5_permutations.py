"""Write a function to generate all permutations of a string or
numbers of unique characters.

"""

import math


def permutations(lst):
    if not lst:
        return [[]]
    else:
        result = []
        for i, v in enumerate(lst):
            lstWithoutElem = lst[:i] + lst[i+1:]
            result += [[v] + p for p in permutations(lstWithoutElem)]
        return result


def permutations2(lst):
    "Book solution"
    if not lst:
        return [[]]
    else:
        head, tail = lst[0], lst[1:]
        perms = permutations2(tail)
        newPerms = []
        for p in perms:
            # add head in every possible position
            for i in range(len(p)+1):
                newPermutation = p[:]
                newPermutation.insert(i, head)
                newPerms.append(newPermutation)
        return newPerms


def test():
    lst = [1, 2, 3]
    actual = permutations(lst)
    # print(actual)
    assert len(actual) == math.factorial(len(lst))


def test2():
    lst = [1, 2, 3]
    actual = permutations2(lst)
    # print(actual)
    assert len(actual) == math.factorial(len(lst))
