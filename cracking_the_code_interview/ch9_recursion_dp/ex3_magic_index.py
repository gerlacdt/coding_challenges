"""A magic index in an array [0...n-1] is defined to be an index such
that A[i] = i. Given a sorted array of distinct integers, write a
method to find a magic index, if only on exists, in array A.


FOLLUP UP
What if numbers are not distinct

"""


def magicIndex(arr):

    def helper(low, high):
        if low < 0 or high >= len(arr) or low > high:
            return None
        mid = (low + high) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            return helper(mid+1, high)
        else:
            return helper(low, mid-1)

    return helper(0, len(arr)-1)


def magicIndexDistinct(arr):

    def helper(low, high):
        print("low: {} high: {}".format(low, high))
        if low < 0 or high >= len(arr) or low > high:
            return None
        mid = (low + high) // 2
        if arr[mid] == mid:
            return mid

        # left search
        leftIndex = min(mid-1, arr[mid])
        print("left helper")
        left = helper(low, leftIndex)
        if left:
            return left

        # right search
        rightIndex = max(mid+1, arr[mid])
        print("right helper")
        right = helper(rightIndex, high)

        return right

    return helper(0, len(arr)-1)


def test():
    arr = [-1, 1, 3, 7, 10, 12]
    actual = magicIndex(arr)
    expected = 1
    assert actual == expected

    arr = [-1, 1]
    actual = magicIndex(arr)
    expected = 1
    assert actual == expected

    arr = [-1, 2]
    actual = magicIndex(arr)
    expected = None
    assert actual == expected

    arr = [-3, -2, -1, 0, 4]
    actual = magicIndex(arr)
    expected = 4
    assert actual == expected


def testDistinct():
    arr = [-10, -5, 2, 2, 2, 3, 4, 5, 9, 12, 13]
    arr2 = [-10, -5, -5, 2, 2, 3, 4, 7, 9, 12, 13]
    actual = magicIndexDistinct(arr)
    actual2 = magicIndexDistinct(arr2)
    expected = 2
    expected2 = 7
    assert actual == expected
    assert actual2 == expected2
