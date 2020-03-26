"""A sorted array of integers has been rotated an unkown number of
times.

Given this array, find the index of an element in the array in faster
than linear time. If the element does not exist return None.



For example, given the array [13, 18, 25, 2, 8, 10] and the element 8
return 4 (the index of 8 in the array).

You can assume the integers in the array are unique.

"""

from collections import namedtuple


def rotation_index(arr):
    """Returns the index of the lowest element in a sorted rotated
array."""
    if not arr:
        return None
    low = 0
    high = len(arr) - 1
    while True:
        mid = (low + high) // 2
        # only 2 or 1 elements left, return the smallest one
        if mid == low or mid == high:
            if arr[low] < arr[high]:
                return low
            elif arr[low] > arr[high]:
                return high
            else:
                # can happen if low and high are the same, 1 element left
                return low
        if arr[low] < arr[high]:
            # array range is completely sorted, return lowest element
            return low
        if arr[mid] < arr[low]:
            high = mid
        if arr[mid] > arr[low]:
            low = mid
    return None


def binary_search(arr, elem, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == elem:
            return mid
        if arr[mid] > elem:
            high = mid - 1
        if arr[mid] < elem:
            low = mid + 1
    return None


def find(arr, elem):
    if not arr:
        return None
    elif len(arr) == 1:
        return 0 if arr[0] == elem else None
    index = rotation_index(arr)
    result = binary_search(arr, elem, index, len(arr) - 1)
    if result:
        return result
    if index > 0:
        return binary_search(arr, elem, 0, index - 1)
    return None


Case = namedtuple("Case", ["input", "expected"])


def testFind():
    cases = [
        Case(([13, 18, 25, 2, 8, 10], 8), 4),
        Case(([1, 2, 3, 4, 5], 3), 2),
        Case(([5, 1, 2, 3, 4], 3), 3),
        Case(([4, 5, 1, 2, 3], 3), 4),
        Case(([3, 4, 5, 1, 2], 3), 0),
        Case(([2, 3, 4, 5, 1], 3), 1),
        Case(([2, 1], 1), 1),
        Case(([2, 1], 2), 0),
        Case(([2, 1], 3), None),
        Case(([1], 2), None),
        Case(([1], 1), 0),
        Case(([1], 2), None),
        Case(([], 1), None),
        Case(([5, 6, 7, 8, 9, 10, 1, 2, 3], 3), 8),
    ]
    for c in cases:
        arr, elem = c.input
        actual = find(arr, elem)
        assert actual == c.expected, "{}".format(c)


def testIndex():
    cases = [
        Case([1, 2, 3, 4, 5], 0),
        Case([5, 1, 2, 3, 4], 1),
        Case([4, 5, 1, 2, 3], 2),
        Case([3, 4, 5, 1, 2], 3),
        Case([2, 3, 4, 5, 1], 4),
        Case([1, 2], 0),
        Case([1], 0),
        Case([], None),
    ]
    for c in cases:
        actual = rotation_index(c.input)
        assert actual == c.expected, "{}".format(c)


def testBinarySearch():
    cases = [
        Case(([1, 2, 3, 4, 5], 1), 0),
        Case(([1, 2, 3, 4, 5], 2), 1),
        Case(([1, 2, 3, 4, 5], 3), 2),
        Case(([1, 2, 3, 4, 5], 4), 3),
        Case(([1, 2, 3, 4, 5], 5), 4),
        Case(([1, 2, 3, 4, 5], 6), None),
        Case(([1, 2], 3), None),
        Case(([1, 2], 1), 0),
        Case(([1, 2], 2), 1),
        Case(([1], 1), 0),
        Case(([], 1), None),
    ]
    for c in cases:
        arr, elem = c.input
        actual = binary_search(arr, elem, 0, len(arr) - 1)
        assert actual == c.expected, "{}".format(c)
