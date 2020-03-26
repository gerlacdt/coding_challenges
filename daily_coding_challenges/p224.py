"""Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a sorted array, find the smallest positive integer that is not
the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.


See solution:
https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

"""


def smallestSum(arr):
    result = 1
    for i in range(len(arr)):
        if arr[i] <= result:
            result += arr[i]
        else:
            break
    return result


def test():
    arr = [1, 2, 3, 10]
    actual = smallestSum(arr)
    expected = 7
    assert actual == expected

    arr = [1, 2, 3, 5, 10]
    actual = smallestSum(arr)
    expected = 22
    assert actual == expected
