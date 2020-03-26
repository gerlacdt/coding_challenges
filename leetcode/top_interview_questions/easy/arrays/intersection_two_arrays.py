"""Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?

What if nums1's size is small compared to nums2's size? Which algorithm is better?

What if elements of nums2 are stored on disk, and the memory is
limited such that you cannot load all elements into the memory at
once?

"""

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1 = sorted(nums1)
        arr2 = sorted(nums2)
        i = j = 0
        result = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                # intersection found
                result.append(arr1[i])
                i += 1
                j += 1
        return result


def test():
    input1a = [1, 2, 2, 1]
    input1b = [2, 2]
    input2a = [4, 9, 5]
    input2b = [9, 4, 9, 8, 4]

    expected1 = [2, 2]
    expected2 = [4, 9]

    sol = Solution()
    result = sol.intersect(input1a, input1b)
    result2 = sol.intersect(input2a, input2b)

    assert result == expected1
    assert result2 == expected2
