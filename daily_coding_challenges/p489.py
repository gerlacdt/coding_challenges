"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of elements, return the length of the longest subarray
where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the
longest subarray of distinct elements is [5, 2, 3, 4, 1].

"""


from collections import namedtuple


class Solution:
    def longestSubarrayDistinct(self, nums):
        """Quadratic solution"""
        max_distinct = set()
        for i in range(len(nums)):
            current = set()
            for j in range(i, len(nums)):
                if nums[j] in current:
                    max_distinct = max([current, max_distinct], key=len)
                    break
                else:
                    current.add(nums[j])
                max_distinct = max([current, max_distinct], key=len)
        return len(max_distinct)

    def solve(self, nums):
        """Linear time complexity."""
        seen = {}
        maxlen = 0
        starting_index = 0
        for i, n in enumerate(nums):
            if n in seen:
                seen_index = seen[n]
                curlen = i - starting_index
                if seen_index < starting_index:
                    # current subarray does not include number, so add 1

                    # [1,2,3,1] subarray includes 1 twice so length is
                    # 3-0 = 3, no +1 needed

                    # [5, 1, 5, 2, 1], last 1 is not included in
                    # subarray, so 4-2+1 = 3

                    curlen += 1
                starting_index = max(seen_index + 1, starting_index)
                seen[n] = i
                maxlen = max(maxlen, curlen)
            else:
                seen[n] = i
                # always add 1 because we know that n is not included
                # in current subarray
                maxlen = max(maxlen, i - starting_index + 1)
        return maxlen


Case = namedtuple("Case", ["nums", "expected"])


def test():
    cases = [
        Case([5, 1, 3, 5, 2, 3, 4, 1], 5),
        Case([1, 2, 3, 4, 5], 5),
        Case([1, 2, 3, 4, 5, 3], 5),
        Case([1, 2, 1, 2, 3, 4, 1, 2], 4),
        Case([1, 2, 1, 2, 3, 4, 2, 1], 4),
        Case([1, 2, 3, 4, 1, 2], 4),
        Case([1, 2, 1, 2, 3, 4], 4),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.longestSubarrayDistinct(c.nums)
        actual2 = sol.solve(c.nums)
        assert actual == c.expected, "Case: {}".format(c)
        assert actual2 == c.expected, "Case: {}".format(c)
