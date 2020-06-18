"""Implement a MergeSort. (Book Excercise)

"""

from collections import deque, namedtuple
from random import randint


class Solution:
    def mergeSort(self, nums):
        if not nums:
            return nums

        def helper(arr):
            if len(arr) == 1:
                return deque(arr)

            mid = len(arr) // 2
            left = helper(arr[:mid])
            right = helper(arr[mid:])
            result = deque()
            while left and right:
                if left[0] < right[0]:
                    result.append(left.popleft())
                else:
                    result.append(right.popleft())
            while left:
                result.append(left.popleft())
            while right:
                result.append(right.popleft())

            return result

        return list(helper(nums))


Case = namedtuple("Case", ["nums", "expected"])


def test():
    randList = [randint(0, 100) for _ in range(100)]
    cases = [
        Case([], []),
        Case([1], [1]),
        Case([2, 1], [1, 2]),
        Case([2, 7, 3, 5, 8, 11, 1], [1, 2, 3, 5, 7, 8, 11]),
        Case(randList, sorted(randList)),
    ]

    sol = Solution()
    for c in cases:
        actual = sol.mergeSort(c.nums)
        assert actual == c.expected, "Case: {}".format(c.nums)
