"""Given an array of integers that are out of order, determine the
bounds of the smallest window that must be sorted in order for the
entire array to be sorted.

For example:
[3,7,5,6,9]
returns:
(1,3)

"""


def smallestWindow(arr):
    sorted_arr = sorted(arr)
    start = end = 0
    for i in range(len(arr)):
        if arr[i] == sorted_arr[i]:
            continue
        else:
            start = i
            # find end with reverse iteration
            for j in range(len(arr)-1, i, -1):
                if arr[j] == sorted_arr[j]:
                    continue
                else:
                    end = j
                    break
            break
    return (start, end)


def smallest2(arr):
    currentMin = float("inf")
    currentMax = -float("inf")
    left = right = 0

    # find right
    for i in range(len(arr)):
        currentMax = max(currentMax, arr[i])
        if currentMax > arr[i]:
            right = i

    # find left
    for i in range(len(arr) - 1, -1, -1):
        currentMin = min(currentMin, arr[i])
        if currentMin < arr[i]:
            left = i

    return left, right


def test():
    arr = [3,7,5,6,9]
    actual = smallestWindow(arr)
    actual2 = smallest2(arr)
    expected = (1, 3)
    assert actual == expected
    assert actual2 == expected

    arr = [3,7,6,5,9]
    actual = smallestWindow(arr)
    acutal2 = smallest2(arr)
    expected = (1, 3)
    assert actual == expected
    assert actual2 == expected

    arr = [3,7,5,6,9,2]
    actual = smallestWindow(arr)
    actual2 = smallest2(arr)
    expected = (0, 5)
    assert actual == expected
    assert actual2 == expected

    arr = [1,2,3,4,5]
    actual = smallestWindow(arr)
    actual2 = smallest2(arr)
    expected = (0, 0)
    assert actual == expected
    assert actual2 == expected


    arr = []
    actual = smallestWindow(arr)
    actual2 = smallest2(arr)
    expected = (0, 0)
    assert actual == expected
    assert actual2 == expected

    arr = [1]
    actual = smallestWindow(arr)
    actual2 = smallest2(arr)
    expected = (0, 0)
    assert actual == expected
    assert actual2 == expected
