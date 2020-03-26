"""Find the k-th largest number in an unsorted array.


The solution uses a min-heap (aka simulates a max-heap with negating
the values before inserting). Building the heap takes O(n). After the
heap is ready, we pop from the heap k-times in order the get the
result. heappop() takes O(log n) k-times.

Time complexity overall is: O(n) + k*O(log n).

"""

from heapq import heappush, heappop


def kthLargest(nums, k):
    assert len(nums) > k

    # build min-heap
    heap = []
    for n in nums:
        heappush(heap, -n)  # inverse value, so we simulate a max-heap

    # pop k times to get k-th largest element
    result = 0
    for i in range(k):
        result = heappop(heap)
    return -result


def test():
    nums = [5, 7, 2, 3, 4, 1, 6]
    k = 3
    actual = kthLargest(nums, k)
    expected = 5
    assert actual == expected


def test2():
    nums = [5, 7, 2, 3, 4, 1, 6, 9, 10, 1001]
    k = 6
    actual = kthLargest(nums, k)
    expected = 5
    assert actual == expected
