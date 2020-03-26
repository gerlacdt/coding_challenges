"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of elements, return the length of the longest subarray
where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the
longest subarray of distinct elements is [5, 2, 3, 4, 1].

"""


def longest_distinct_subarray(arr):
    numbers = set()
    absoluteMax = 0
    for n in arr:
        if n not in numbers:
            numbers.add(n)
        else:
            absoluteMax = max(absoluteMax, len(numbers)) # choose old max or new max
            numbers = set([n])  # reset set to start again
    return max(absoluteMax, len(numbers))


def test():
    arr = [5, 1, 3, 5, 2, 3, 4, 1]
    result = longest_distinct_subarray(arr)
    expected = 5
    assert result == expected

    arr = [1, 2, 3, 4, 5, 7]
    result = longest_distinct_subarray(arr)
    expected = 6
    assert result == expected

    arr = [9, 1, 2, 9, 9, 9, 9, 9]
    result = longest_distinct_subarray(arr)
    expected = 3
    assert result == expected
