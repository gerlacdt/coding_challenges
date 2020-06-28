"""Quicksort.

"""

from random import randint


class Solution:
    def quicksort(self, nums):
        def helper(low, high):
            if low < high:
                mid = self._partition(low, high, nums)
                helper(low, mid - 1)
                helper(mid + 1, high)

        return helper(0, len(nums) - 1)

    def _partition(self, low, high, nums):
        pivot = nums[high]
        mid = low
        for i in range(low, high):
            if nums[i] <= pivot:
                nums[mid], nums[i] = nums[i], nums[mid]
                mid += 1
        nums[mid], nums[high] = nums[high], nums[mid]
        return mid


def testRandom():
    nums = [1, 5, 3, 2, 8, 7, 6, 4]
    sol = Solution()
    expected = sorted(nums)
    sol.quicksort(nums)
    assert nums == expected

    nums = [randint(0, 100) for _ in range(100)]
    sol.quicksort(nums)
    assert nums == sorted(nums)


def test():
    arr = [1, 3, 7, 2, 4, 8, 9, 5]
    sol = Solution()
    sol.quicksort(arr)
    assert arr == sorted(arr)


def testSortedArray():
    arr = [1, 2, 3, 4, 5]
    sol = Solution()
    sol.quicksort(arr)
    assert arr == sorted(arr)


def testReversedArray():
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sol = Solution()
    sol.quicksort(arr)
    assert arr == sorted(arr)


def testDuplicatesArray():
    arr = [4, 4, 4, 4, 3, 3, 3, 5, 5, 5]
    sol = Solution()
    sol.quicksort(arr)
    assert arr == sorted(arr)


def testEmptyArray():
    arr = []
    sol = Solution()
    sol.quicksort(arr)
    assert arr == sorted(arr)
