# coding: utf-8

"""

SEE also Daily Coding Problem #190 [Medium]


Given a circular array C of integers represented by A, find the
maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the
beginning of the array.  (Formally, C[i] = A[i] when 0 <= i <
A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A
at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j],
there does not exist i <= k1, k2 <= j with k1 % A.length = k2 %
A.length.)


Example 1:
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:
Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:
Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:
Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1


Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000

"""

from typing import List
from collections import namedtuple
import os


DEBUG = os.environ.get('DEBUG')


def debug(s):
    if DEBUG:
        print(s)
    return


def kadane2(nums: List[int]) -> int:
    "Original Kadene with dp-table."
    table = [v for v in nums]
    for i in range(1, len(nums)):
        table[i] = max(table[i-1] + nums[i], nums[i])
    return max(table)


def kadane(nums):
    """Optimized Kadene, use constant space. Instead of using dp-table, it
uses only variable for the current maximum value.
    """
    current = 0
    absoluteMax = min(nums)
    for n in nums:
        current = n + max(current, 0)
        absoluteMax = max(current, absoluteMax)
    return absoluteMax


class Solution:
    def maxSubarraySumCircular2(self, A: List[int]) -> int:
        """SEE also Daily Coding Problem #190 [Medium].  This is a fancy
        solution with multiple Kadane's algorighm (find the maximum
        sum in a subarray (without circular))
        """
        sumA = sum(A)
        result1 = kadane(A)
        result2 = sumA + kadane([-A[i] for i in range(1, len(A))])
        result3 = sumA + kadane([-A[i] for i in range(len(A)-1)])
        return max(result1, result2, result3)

    def maxSubarraySumCircular(self, A):
        """
        1. Run Kadene(A), store it
        2. Create rightsums (array with all sums with reverse iteration)
        3. Create maxright
        4. Sum up from 0..N-1 as leftsum and check if leftsum + maxright(i+2) is greater
than current result (result start-value is kadene(A))
        """
        N = len(A)
        ans = kadane(A)

        # rightsums
        rightsums = [None] * N
        rightsums[-1] = A[-1]
        for i in range(N-2, -1, -1):
            rightsums[i] = rightsums[i+1] + A[i]

        # calculate maxright
        maxright = [None] * N
        maxright[-1] = rightsums[-1]
        for i in range(N-2, -1, -1):
            maxright[i] = max(maxright[i+1], rightsums[i])
        debug("array: {} kadane: {} rightsums: {} maxright: {}".format(A, ans, rightsums, maxright))

        # calculate max sum of circular subarray
        leftsum = 0
        for i in range(N-2):
            leftsum += A[i]
            ans = max(ans, leftsum + maxright[i+2])
            debug("leftsum: {}, ans: {}".format(leftsum, ans))
        return ans


Case = namedtuple("Case", ["input", "expected"])


def test():
    s = Solution()
    cases = [
        Case([1, -2, 3, -2], 3),
        Case([5, -3, 5], 10),
        Case([3, -1, 2, -1], 4),
        Case([3, -2, 2, -3], 3),
        Case([-2, -3, -1], -1),
        Case([5, -3, -2, 5], 10)
    ]
    for c in cases:
        actual = s.maxSubarraySumCircular(c.input)
        actual2 = s.maxSubarraySumCircular2(c.input)
        actual3 = max_sum_circular_array(c.input)
        assert actual == c.expected, "Case: {}".format(c)
        assert actual2 == c.expected, "Case: {}".format(c)
        assert actual3 == c.expected, "Case: {}".format(c)


def testKadane():
    cases = [Case([-2, -3, -1], -1), Case([1, 2, 3, -1], 6),
             Case([1, 2, -2, 3, 4], 8), Case([-10, 2, -1, 5], 6),
             Case([-2, 4, -1, 4, -1], 7), Case([5, -3, 5], 7)]
    for c in cases:
        actual = kadane(c.input)
        actual2 = kadane2(c.input)
        assert actual == c.expected, "Case: {}".format(c)
        assert actual2 == c.expected, "Case: {}".format(c)


def max_sum_circular_array(nums):
    "Solution by heart. Just for remembering better."
    def kadene(nums):
        table = nums[:]
        for i in range(1, len(nums)):
            table[i] = max(nums[i], table[i-1]+nums[i])
        return max(table)

    lengthNums = len(nums)
    result = kadene(nums)

    rightsums = nums[:]
    for i in range(lengthNums-2, -1 , -1):
        rightsums[i] = rightsums[i+1] + nums[i]

    rightmax = rightsums[:]
    for i in range(lengthNums-2, -1, -1):
        rightmax[i] = max(rightmax[i], rightmax[i+1])
    debug("array: {} kadane: {} rightsums: {} maxright: {}".format(nums, result, rightsums, rightmax))

    leftsum = 0
    resultCircular = result
    for i in range(lengthNums-2):
        leftsum += nums[i]
        resultCircular = max(resultCircular, leftsum + rightmax[i+2])
        debug("leftsum: {}, ans: {}".format(leftsum, resultCircular))
    return resultCircular
