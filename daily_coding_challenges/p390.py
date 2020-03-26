"""Good morning! Here's your coding interview problem for today.

This problem was asked by Two Sigma.

You are given an unsorted list of 999,000 unique integers, each from 1
and 1,000,000. Find the missing 1000 numbers. What is the
computational and space complexity of your solution?

"""


def findMissing(lst, k):
    copy = [0] * k

    for item in lst:
        # mark all numbers which are there
        copy[item] = 1

    copy[0] = 1  # 0 is not in range of 1 to k

    return [i for i, num in enumerate(copy) if not num]  # filter missing numbers


def test():
    lst = [0, 1, 4, 5, 6, 7, 8, 9]
    actual = findMissing(lst, 10)
    expected = [2, 3]
    assert actual == expected

    lst = [1, 4, 5, 6, 7, 8, 9]
    actual = findMissing(lst, 10)
    expected = [2, 3]
    assert actual == expected
