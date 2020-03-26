"""Given an array of integers and a number k, where 1 <= k <=
len(array), compute the maximum values of each subarray of length k.

For example, the array [10,5,2,7,8,7] and k = 3. We should get:
[10,7,8,8]

10 -> max(10,5,3)
7 -> max(5,2,7)
8 -> max(2,7,8)
8 -> max(7,8,7)

"""


from collections import deque


def maximumKSubarray(arr, k):
    q = deque([])
    result = []
    for item in arr:
        q.append(item)
        if len(q) == k:
            result.append(max(q))
            q.popleft()
    return result


def sample_solution(arr, k):
    q = deque([])
    result = []
    # initially fill up queue, max k elements
    for i in range(k):
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k, len(arr)):
        result.append(arr[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
    result.append(arr[q[0]])
    return result


def test():
    arr = [10, 5, 2, 7, 8, 7]
    k = 3
    actual = maximumKSubarray(arr,  k)
    actual2 = sample_solution(arr, k)
    expected = [10, 7, 8, 8]
    assert actual == expected
    assert actual2 == expected
