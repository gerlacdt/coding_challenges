"""Given an array of integers, return a new array where each element
in the new array is the number of smaller elements to the right of
that element in the original input.

Example:
[3,4,9,6,1]

Result:
[1,1,2,1,0]
"""

import bisect


def smaller(arr):
    """Naive solution. Run over array and count all smaller elements for
current element. Time complexity is O(n**2)
    """
    result = []
    for i, v in enumerate(arr):
        count = 0
        for j in range(i+1, len(arr)):
            if arr[j] < v:
                count += 1
        result.append(count)
    return result


def sample_solution(arr):
    """We keep 'seen' as a sorted array. During reverse array loop we
check at which index the the current value would be inserted. This
index tells us how many smaller elements are in the original array on
the right side.
    """
    seen = []
    result = []
    for v in reversed(arr):
        i = bisect.bisect_left(seen, v)
        result.append(i)
        bisect.insort(seen, v)
    return list(reversed(result))


def test():
    arr = [3,4,9,6,1]
    actual = smaller(arr)
    actual2 = sample_solution(arr)
    expected = [1,1,2,1,0]
    assert actual == expected
    assert actual2 == expected
