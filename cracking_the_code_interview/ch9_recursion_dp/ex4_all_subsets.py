"""
Write a method to retun all subsets of a set.
"""

# generate all subsets
# https://www.quora.com/What-is-the-recursive-solution-for-finding-all-subsets-of-a-given-array


def subsets2(lst):

    def helper(index):
        if index == len(lst):
            return [[]]
        else:
            all_subsets = helper(index+1)
            elem = lst[index]
            return extend(all_subsets, elem)

    return helper(0)


def subsets(lst):
    if not lst:
        return [[]]
    head, tail = lst[0], lst[1:]
    return extend(subsets(tail), head)


def extend(lsts, item):
    return [[item] + l for l in lsts] + lsts


def test():
    s = [1, 2, 3]
    actual = subsets(s)
    expected = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    assert len(actual) == len(expected)


def test2():
    s = [1, 2, 3]
    actual = subsets2(s)
    expected = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    assert actual == expected
