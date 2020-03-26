"""Given an array of numbers. Move all zeros to the end of the array.

see:
https://www.geeksforgeeks.org/move-zeroes-end-array/
"""


def zeros(arr):
    low = 0
    high = len(arr) - 1
    arr2 = arr[:]
    while low < high:
        if arr2[low] == 0:
            arr2[low], arr2[high] = arr2[high], arr2[low]
            high -= 1
        low += 1
    return arr2


def test():
    arr = [1, 0, 2, 3, 0, 0, 5, 6]
    actual = zeros(arr)
    expected = [1, 6, 2, 3, 5, 0, 0, 0]
    assert actual == expected
