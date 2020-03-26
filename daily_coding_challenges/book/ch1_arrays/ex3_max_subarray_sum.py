"""Given an array of numbers, find the maximum sum on any contiguous
subarray of the array. For example, the array [34,-50, 42,14,-5,86],
the maximum sum woud be 137, since we would take elements 42, 14, -5
and 86. Given the array [-5,-1,-8,-9], the maximum sum is 0, since we
would choose not to take any elements.

Follow-up: What if the elements can wrap around? For example, given
[8,-1,3,4], return 15, as we choose the numbers 3,4 and 8 where 8 is
obtained from wrapping around.

"""


def kadane(arr):
    """Kadane's algorithm to compute the maximum sum of a contiguous
subarray. Here a dynamic programming table is used. So the space
complexity is O(n).
    """
    if not arr:
        return 0
    table = [0 for i in range(len(arr))]
    table[0] = arr[0]
    for i in range(1, len(arr)):
        table[i] = max(table[i-1] + arr[i], arr[i])
    return max(table) if max(table) > 0 else 0


def circular(arr):
    leftsums = []
    for i, v in enumerate(arr):
        if not leftsums:
            leftsums.append(v)
        else:
            leftsums.append(v + leftsums[i-1])

    rightsums = [0 for i in range(len(arr))]
    for i in range(len(arr)-1, -1, -1):
        if i == len(arr)-1:
            rightsums[i] = arr[i]
        else:
            rightsums[i] = arr[i] + rightsums[i+1]

    rightMaxs = [0 for i in range(len(arr))]
    for i in range(len(arr)-1, -1, -1):
        if i == len(arr)-1:
            rightMaxs[i] = rightsums[i]
        else:
            rightMaxs[i] = max(rightsums[i], rightsums[i+1])

    globalMax = kadane(arr)
    for i in range(len(leftsums)-2):
        lsum = leftsums[i]
        for j in range(i+2, len(rightMaxs)):
            if lsum + rightMaxs[j] > globalMax:
                globalMax = lsum + rightMaxs[j]

    return globalMax


def maximum_subarray(arr):
    """Kadane's algorithm, but space complexity is constant. In the above
Kadane's solution i used a dynamic programming lookup table to store
all result, but it's enough to only store the current max.
    """
    max_so_far = max_current = 0
    for v in arr:
        max_current = max(v, v + max_current)
        max_so_far = max(max_current, max_so_far)
    return max_so_far


def minimum_subarray(arr):
    min_so_far = min_current = 0
    for i in range(len(arr)):
        min_current = min(arr[i], min_current + arr[i])
        min_so_far = min(min_so_far, min_current)
    return min_so_far


def circular2(arr):
    """Here we calculate normal kadane and also the inverse kadane,
i.e. find the minimum subarry. With that we can check if the maximum
subarray is bigger than the sum of all elements - minimum subarray. If
not the sum(arr) - minimum_subarray(arr) is the result.

Attention! We need to check this if it works with only negative numbers.
    """
    max_subarray = maximum_subarray(arr)
    max_wrapped_array = sum(arr) - minimum_subarray(arr)
    return max(max_subarray, max_wrapped_array)


def test():
    arr = [34,-50,42,14,-5,86]
    actual = kadane(arr)
    actual2 = circular(arr)
    actual3 = maximum_subarray(arr)
    actual4 = minimum_subarray(arr)
    actual5 = circular2(arr)
    expected = 137
    expected2 = 171
    assert actual == expected
    assert actual2 == expected2
    assert actual3 == expected
    assert actual4 == -50
    assert actual5 == expected2

    arr = [-5, -1, -8, -9]
    actual = kadane(arr)
    actual2 = circular(arr)
    actual3 = maximum_subarray(arr)
    actual4 = circular2(arr)
    expected = 0
    assert actual == expected
    assert actual2 == expected
    assert actual3 == expected
    assert actual4 == expected

    arr = [8, -1, 3, 4]
    actual = circular(arr)
    actual2 = circular2(arr)
    expected = 15
    assert actual == expected
    assert actual2 == expected
