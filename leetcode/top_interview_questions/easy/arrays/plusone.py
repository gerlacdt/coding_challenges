"""Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the
head of the list, and each element in the array contain a single
digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""

from typing import List
from collections import namedtuple


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rdigits = digits[::-1]
        curry = True
        for i, d in enumerate(rdigits):
            if curry:
                val = d + 1
                if val == 10:
                    rdigits[i] = 0
                    curry = True
                else:
                    rdigits[i] = val
                    curry = False
                    break
        if curry:
            rdigits.append(1)
        return rdigits[::-1]


def test():
    sol = Solution()
    Case = namedtuple('Case', ['input1', 'expected'])
    cases = [Case([1, 2, 3], [1, 2, 4]),
             Case([4, 3, 2, 1], [4, 3, 2, 2]),
             Case([0], [1]),
             Case([9], [1, 0]),
             Case([9, 9, 9], [1, 0, 0, 0])]

    for c in cases:
        result = sol.plusOne(c.input1)
        assert result == c.expected
