"""Given an array of number of length n, find both the minimum and
maximimum using less than 2 * (n - 2) comparisons


-> Recursion, divide and conquer

"""


def getMinMax(arr):
    def helper(low, high):
        print("helper({},{})".format(low, high))
        if low >= high:
            assert low == high
            result = arr[low], arr[low]
            print("single result {}".format(result))
            return result
        mid = ((high - low) // 2) + low
        left = helper(low, mid)
        right = helper(mid + 1, high)

        leftMin, leftMax = left
        rightMin, rightMax = right

        result = (min(leftMin, rightMin), max(leftMax, rightMax))
        print("result {}".format(result))
        return result

    return helper(0, len(arr) - 1)


def test():
    arr = [4, 2, 7, 5, -1, 3, 6]
    actual = getMinMax(arr)
    expected = (-1, 7)
    assert actual == expected
