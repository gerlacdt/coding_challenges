"""Given an array nums of n integers, return an array of all the unique
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

"""

from typing import List, Dict, Tuple, Set
from collections import namedtuple, defaultdict
from bisect import bisect_left


def binary_search(a, x, low):
    "Locate the leftmost value exactly equal to x"
    i = bisect_left(a, x, low)
    if i != len(a) and a[i] == x:
        return i
    return None


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result: Set[Tuple[int]] = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    rest = nums[i] + nums[j] + nums[k]
                    last_index = binary_search(nums, target - rest, k + 1)
                    if last_index or last_index == 0:
                        tmp = [nums[i], nums[j], nums[k], nums[last_index]]
                        tmp.sort()
                        result.add(tuple(tmp))

        return sorted([list(r) for r in result])

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        table: Dict[int, int] = {}
        result = []
        for i, v in enumerate(nums):
            if v in table:
                result.append([nums[table[v]], v])  # capture the values NOT indices
            table[target - v] = i
        return result

    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        table1: Dict[int, int] = {}
        result: Set[Tuple[int]] = set()
        for i, v1 in enumerate(nums):
            table2: Dict[int, List[int]] = defaultdict(list)
            table1[target - v1] = i
            for j, v2 in enumerate(nums):
                if i == j:
                    continue
                if v2 in table2:
                    tmp = [nums[table2[v2][0]], nums[table2[v2][1]], v2]
                    tmp.sort()
                    result.add(tuple(tmp))

                for index in table1.values():
                    if index == j:
                        continue
                    table2[target - nums[index] - v2] = [index, j]
        return sorted([list(r) for r in result])


Case = namedtuple("Case", ["nums", "target", "expected"])


def testFourSum():
    cases = [
        Case(
            [1, 0, -1, 0, -2, 2],
            0,
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
        ),
        Case([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        Case(
            [-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5],
            0,
            [
                [-5, -4, 4, 5],
                [-5, -3, 3, 5],
                [-5, -2, 2, 5],
                [-5, -2, 3, 4],
                [-5, -1, 1, 5],
                [-5, -1, 2, 4],
                [-5, 0, 0, 5],
                [-5, 0, 1, 4],
                [-5, 0, 2, 3],
                [-4, -3, 2, 5],
                [-4, -3, 3, 4],
                [-4, -2, 1, 5],
                [-4, -2, 2, 4],
                [-4, -1, 0, 5],
                [-4, -1, 1, 4],
                [-4, -1, 2, 3],
                [-4, 0, 0, 4],
                [-4, 0, 1, 3],
                [-3, -2, 0, 5],
                [-3, -2, 1, 4],
                [-3, -2, 2, 3],
                [-3, -1, 0, 4],
                [-3, -1, 1, 3],
                [-3, 0, 0, 3],
                [-3, 0, 1, 2],
                [-2, -1, 0, 3],
                [-2, -1, 1, 2],
                [-2, 0, 0, 2],
                [-1, 0, 0, 1],
            ],
        ),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.fourSum(c.nums, c.target)
        assert sorted(actual) == sorted(c.expected), "Case: {}, target: {}".format(
            c.nums, c.target
        )


def testThreeSum():
    cases = [Case([-1, 0, 1, 2, -1, -4], 0, sorted([[-1, -1, 2], [-1, 0, 1]]))]

    sol = Solution()
    for c in cases:
        actual = sol.threeSum(c.nums, c.target)
        assert actual == c.expected


def testTwoSum():
    cases = [
        Case([2, 7, 11, 15], 9, [[2, 7]]),
        Case([3, 2, 4], 6, [[2, 4]]),
        Case([3, 3], 6, [[3, 3]]),
    ]

    sol = Solution()
    for c in cases:
        actual = sol.twoSum(c.nums, c.target)
        assert actual == c.expected
