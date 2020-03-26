"""Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given an array of integers, return the largest range, inclusive, of
integers that are all included in the array.

For example, given the array [9, 6, 1, 3, 8, 10, 12, 11], return (8,
12) since 8, 9, 10, 11, and 12 are all in the array.

"""


def hashingSolution(nums):
    s = set(nums)

    total = (nums[0], nums[0])
    for i in range(len(nums)):
        if nums[i] - 1 not in s:
            # start a new sequence
            val = nums[i] + 1
            while val in s:
                val += 1
            if total[1] - total[0] < val - 1 - nums[i]:
                total = (nums[i], val - 1)
    return total


def largestRange(nums):
    nums = sorted(nums)
    current = (nums[0], nums[0])
    total = (nums[0], nums[0])

    for i in range(1, len(nums)):
        start, end = current
        new_end = end + 1
        if nums[i] == new_end:
            # extend current range
            current = (start, new_end)
            if new_end - start > total[1] - total[0]:
                total = (start, new_end)
        elif nums[i] == end:
            # handle duplicate numbers
            continue
        else:
            # reset current range
            current = (nums[i], nums[i])
    return total


def test():
    # example from problem description
    nums = [9, 6, 1, 3, 8, 10, 12, 11]
    actual = largestRange(nums)
    actual2 = hashingSolution(nums)
    expected = (8, 12)
    assert actual == expected
    assert actual2 == expected

    # negative numbers
    nums = [9, 6, 1, 3, 8, 10, 12, 11, 2, 0, -1, -2]
    actual = largestRange(nums)
    actual2 = hashingSolution(nums)
    expected = (-2, 3)
    assert actual == expected
    assert actual2 == expected

    # twice the same range (-1,3)and (8, 12)
    nums = [9, 6, 1, 3, 8, 10, 12, 11, 2, 0, -1]
    actual = largestRange(nums)
    actual2 = hashingSolution(nums)
    expected = (-1, 3)
    assert actual == expected
    assert actual2[1] - actual2[0] == expected[1] - expected[0]

    # duplicate 1s
    nums = [9, 6, 1, 3, 8, 10, 12, 11, 1, 2, 0, -1, -2]
    actual = largestRange(nums)
    expected = (-2, 3)
    actual2 = hashingSolution(nums)
    assert actual == expected
    assert actual2 == expected
