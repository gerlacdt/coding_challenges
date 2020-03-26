"""Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice
in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

from typing import List
from collections import namedtuple


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = set()
        for n in nums:
            if n in table:
                return True
            table.add(n)
        return False


def test():
    Case = namedtuple('Case', ['input1', 'expected'])
    cases = [Case([1, 2, 3, 1],  True),
             Case([1, 2, 3, 4],  False),
             Case([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],  True)]

    sol = Solution()
    for c in cases:
        result = sol.containsDuplicate(c.input1)
        assert result == c.expected
