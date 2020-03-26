"""Give a list, sort it using the helper method reverse(lst, i, j).

This method takes a sublist as indicated by the left and rights bounds
i and j and reverses all its elements.

For example, reverse([10,20,30,40,50], 1, 3) would result in
[10,40,30,20,50].

"""


def reverse(arr, low, high):
    assert low >= 0
    assert high < len(arr)
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1


def findMaxIndex(arr, low, high):
    assert len(arr) > 0
    assert low >= 0
    assert high < len(arr)
    assert low <= high
    maxIndex = 0
    for i in range(low, high + 1):
        if arr[i] > arr[maxIndex]:
            maxIndex = i
    return maxIndex


def pancake_sort(arr):
    nums = arr[:]
    for i in range(len(nums) - 1, 0, -1):
        j = findMaxIndex(nums, 0, i)
        reverse(nums, 0, j)
        reverse(nums, 0, i)
    return nums


def test():
    arr = [10, 4, 3, 2, 1]
    actual = pancake_sort(arr)
    expected = sorted(arr)
    assert actual == expected

    arr = []
    actual = pancake_sort(arr)
    expected = sorted(arr)
    assert actual == expected
