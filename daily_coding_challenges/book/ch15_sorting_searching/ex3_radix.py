"""Given an array of a million integers between zero and a billion,
out of order, how would you efficiently sort it?

Assume that you cannot store an array of a billion elements in memory.
"""


def counting_sort(arr, position):
    counts = [[] for _ in range(10)]  # 0..9 possible digits
    for n in arr:
        digit = (n // 10 ** position) % 10
        counts[digit].append(n)

    # get the counts in order, so we stable-sort the given array by
    # the digit at the given position
    result = []
    for ns in counts:
        result.extend(ns)

    return result


def radix_sort(arr, k=3):
    nums = arr[:]
    for position in range(k):
        # We must use a stable sort here.  We chose counting sort
        # because we know sth. about the elements like the have at max
        # 3 digits. Counting sort has a time complexity of O(n). It is
        # better than the regular sorts like quicksort and heapsort.
        nums = counting_sort(nums, position)
    return nums


def test():
    arr = [100, 2, 4, 54, 537, 89]
    actual = radix_sort(arr)
    expected = sorted(arr)
    assert actual == expected

    arr = [100, 0, 0, 1, 1, 99, 99]
    actual = radix_sort(arr)
    expected = sorted(arr)
    assert actual == expected

    arr = []
    actual = radix_sort(arr)
    expected = sorted(arr)
    assert actual == expected
