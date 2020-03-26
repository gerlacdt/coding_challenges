"""Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the
array, rotate the array to the right k elements in-place.

"""


def rotate(arr, k):
    n = len(arr)
    part1 = list(reversed(arr[:-k]))
    part2 = list(reversed(arr[n-k:]))
    print("part1: {} part2: {}".format(part1, part2))
    return list(reversed(part1 + part2))


def test():
    arr = [1, 2, 3, 4, 5]
    k = 3
    actual = rotate(arr, k)
    expected = [3, 4, 5, 1, 2]
    assert actual == expected

    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    actual = rotate(arr, k)
    expected = [6, 7, 1, 2, 3, 4, 5]
    assert actual == expected


def rotateLeft(arr, k):
    r = list(reversed(arr))
    n = len(arr)
    part1 = list(reversed(r[:n-k]))
    part2 = list(reversed(r[n-k:]))
    print("part1: {} part2: {}".format(part1, part2))
    return part1 + part2


def testLeft():
    arr = [1, 2, 3, 4, 5]
    k = 3
    actual = rotateLeft(arr, k)
    expected = [4, 5, 1, 2, 3]
    assert actual == expected

    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    actual = rotateLeft(arr, k)
    expected = [3, 4, 5, 6, 7, 1, 2]
    assert actual == expected
