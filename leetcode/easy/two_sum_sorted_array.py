"""Given an array of integers that is already sorted in ascending
order, find two numbers such that they add up to a specific target
number.

The function twoSum should return indices of the two numbers such that
they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.


Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]

"""

from typing import List
from collections import namedtuple


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = {}
        for i, n in enumerate(numbers):
            table[n] = i

        for i, n in enumerate(numbers):
            x = target - n
            if x in table and table[x] != i:
                return sorted([i + 1, table[x] + 1])
        return []

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        while lo < hi:
            current = numbers[lo] + numbers[hi]
            if current < target:
                lo += 1
            elif current > target:
                hi -= 1
            else:
                return [lo + 1, hi + 1]
        return []


Case = namedtuple("Case", ["numbers", "target", "expected"])


def test():
    sol = Solution()
    cases = [
        Case([2, 7, 11, 15], 9, [1, 2]),
        Case([2, 3, 4], 6, [1, 3]),
        Case([-1, 0], -1, [1, 2]),
    ]

    for c in cases:
        actual = sol.twoSum(c.numbers, c.target)
        assert actual == c.expected

        actual = sol.twoSum2(c.numbers, c.target)
        assert actual == c.expected, f"{c.numbers}, {c.target}"
