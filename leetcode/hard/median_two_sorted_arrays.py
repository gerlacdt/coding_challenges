from collections import namedtuple, deque
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = self._merge( nums1, nums2)
        length = len(arr)
        if length % 2 == 0:
            index = length // 2
            return (arr[index] + arr[index-1]) / 2
        else:
            index = (length // 2)
            return arr[index]

    def _merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = deque(nums1)
        d2 = deque(nums2)
        result = []
        while d1 and d2:
            if d1[0] < d2[0]:
                result.append(d1[0])
                d1.popleft()
            else:
                result.append(d2[0])
                d2.popleft()
        if d1:
            result.extend(d1)
        else:
            result.extend(d2)
        return result


def test():
    Case = namedtuple('Case', ['input1', 'expected'])
    cases = [Case([[1, 3], [2]], 2.0),
             Case([[1, 2], [3, 4]], 2.5)]

    solution = Solution()
    for c in cases:
        result = solution.findMedianSortedArrays(*c.input1)
        assert result == c.expected


def test_merge():
    Case = namedtuple('Case', ['input1', 'expected'])
    cases = [Case([[], []], []),
             Case([[1], []], [1]),
             Case([[], [1]], [1]),
             Case([[5, 6, 7], [1, 2, 3]], [1, 2, 3, 5, 6, 7]),
             Case([[5, 6, 7], [2]], [2, 5, 6, 7]),
             Case([[1, 3], [2]], [1, 2, 3]),
             Case([[1, 2], [3, 4]], [1, 2, 3, 4])]
    solution = Solution()
    for c in cases:
        result = solution._merge(c.input1[0], c.input1[1])
        assert result == c.expected
