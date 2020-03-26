"""Given an unsorted array of integers, find the length of the
longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

"""

from typing import List
from collections import namedtuple


class Solution:
    def longestConsecutiveWithSorting(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sortedList = sorted(list(set(nums)))
        currentConsecutives = 1
        maxConsecutives = 1
        for i in range(1, len(sortedList)):
            val = sortedList[i]
            if sortedList[i-1] == val - 1:
                currentConsecutives += 1
            else:
                if currentConsecutives > maxConsecutives:
                    maxConsecutives = currentConsecutives
                currentConsecutives = 1
        return max(maxConsecutives, currentConsecutives)

    def longestConsecutive(self, nums: List[int]) -> int:
        # handle empty list
        if not nums:
            return 0

        # handle normal list
        s = set(nums)  # with set, duplicates are not relevant anymore
        seen = set([])
        maxConsecutives = 1
        for v in s:
            if v in seen:
                continue
            seen.add(v)
            currentConsecutives = 1
            counter = 0
            while True:
                counter += 1
                if v + counter in s:
                    seen.add(v+counter)
                    currentConsecutives += 1
                else:
                    break
            maxConsecutives = max(maxConsecutives, currentConsecutives)
        return maxConsecutives


def test():
    Case = namedtuple('Case', ['testinput', 'expected'])
    cases = [Case([100, 4, 200, 1, 3, 2], 4), Case([], 0),
             Case([0, -1], 2), Case([1, 2, 0, 1, 3], 4)]

    sol = Solution()
    for c in cases:
        print("case: {}".format(c))
        result = sol.longestConsecutive(c.testinput)
        result1 = sol.longestConsecutiveWithSorting(c.testinput)
        assert result == c.expected
        assert result == result1
