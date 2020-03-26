"""Simple implementation of quicksort. By heart without help or
documentation.

"""


def quicksort(arr, low, high):
    if low < high:
        mid = partition(arr, low, high)
        quicksort(arr, low, mid - 1)
        quicksort(arr, mid + 1, high)


def partition(arr, low, high):
    mid = low - 1
    pivot = arr[high]
    for i in range(low, high + 1):
        if arr[i] < pivot:
            mid += 1
            arr[i], arr[mid] = arr[mid], arr[i]
    # put current pivot into the ordered position of array
    mid += 1
    arr[mid], arr[high] = arr[high], arr[mid]
    return mid


def test():
    arr = [1, 3, 7, 2, 4, 8, 9, 5]
    quicksort(arr, 0, len(arr) - 1)
    assert arr == sorted(arr)


def testSortedArray():
    arr = [1, 2, 3, 4, 5]
    quicksort(arr, 0, len(arr) - 1)
    assert arr == sorted(arr)


def testReversedArray():
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    quicksort(arr, 0, len(arr) - 1)
    assert arr == sorted(arr)


def testDuplicatesArray():
    arr = [4, 4, 4, 4, 3, 3, 3, 5, 5, 5]
    quicksort(arr, 0, len(arr) - 1)
    assert arr == sorted(arr)


def testEmptyArray():
    arr = []
    quicksort(arr, 0, len(arr) - 1)
    assert arr == sorted(arr)
