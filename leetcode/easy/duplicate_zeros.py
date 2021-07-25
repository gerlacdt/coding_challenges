""""Given a fixed length array arr of integers, duplicate each occurrence
of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not
written.

Do the above modifications to the input array in place, do not return
anything from your function.


Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]


Leetcode: https://leetcode.com/problems/duplicate-zeros/

"""

from typing import List, Deque
from collections import namedtuple, deque


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        q: Deque[int] = deque([])
        for i, v in enumerate(arr):
            q.append(v)
            if v == 0:
                q.append(0)

        for i in range(len(arr)):
            arr[i] = q.popleft()


Case = namedtuple("Case", ["arr", "expected"])


def test_queue():
    cases = [
        Case([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
        Case([1, 2, 3], [1, 2, 3]),
    ]

    sol = Solution()
    for c in cases:
        sol.duplicateZeros(c.arr)
        assert c.expected == c.arr
