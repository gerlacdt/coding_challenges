"""Given a non-empty array of integers, every element appears twice
except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you
implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4

"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = set()
        for n in nums:
            if n in table:
                table.remove(n)
                continue
            table.add(n)
        result = list(table)
        if len(result) != 1:
            raise RuntimeError("Array contains more than single duplicate: {}".format(result))
        return result[0]


def test():
    sol = Solution()
    i1 = [2, 2, 1]
    expected1 = 1
    i2 = [4, 1, 2, 1, 2]
    expected2 = 4

    result1 = sol.singleNumber(i1)
    assert result1 == expected1

    result2 = sol.singleNumber(i2)
    assert result2 == expected2
