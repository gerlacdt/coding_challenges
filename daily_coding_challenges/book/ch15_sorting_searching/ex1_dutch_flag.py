"""Given an array of strictly the characters R,G,B, segregate the
values of the array so that all the Rs come first, the Gs come second,
and the Bs come last. You can only swap elements of the array.

Do this in linear time and space.

For example, given the array ["G", "B", "R", "R", "B", "R", "G"], you
should transform it to ["R", "R", "R", "G", "G", "B", "B"].

"""

from collections import namedtuple


def dutchFlag(arr):
    splitter = 0
    for i in range(len(arr)):
        if arr[i] == "R":
            arr[i], arr[splitter] = arr[splitter], arr[i]
            splitter += 1

    for i in range(splitter, len(arr)):
        if arr[i] == "G":
            arr[i], arr[splitter] = arr[splitter], arr[i]
            splitter += 1

    return arr


def sampleSolution(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == "R":
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == "G":
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[low]
            high -= 1
    return arr


Case = namedtuple("Case", ["input", "expected"])


def test():
    cases = [
        Case(["G", "B", "R", "R", "B", "R", "G"], ["R", "R", "R", "G", "G", "B", "B"]),
        Case(["G", "G"], ["G", "G"]),
        Case([], []),
    ]
    for c in cases:
        actual = dutchFlag(c.input)
        assert actual == c.expected


def testSample():
    cases = [
        Case(["G", "B", "R", "R", "B", "R", "G"], ["R", "R", "R", "G", "G", "B", "B"]),
        Case(["G", "G"], ["G", "G"]),
        Case([], []),
    ]
    for c in cases:
        actual = dutchFlag(c.input)
        assert actual == c.expected
