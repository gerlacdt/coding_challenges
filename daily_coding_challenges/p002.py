"""Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers in the
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the
expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def solve1(arr):
    """Solves the problem without division but with O(n^2) time
complexity."""
    n = len(arr)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= arr[j]
        result.append(product)
        product = 1
    return result


def solve2(arr):
    """Solve the problem with division but with O(n)"""
    def product(arr):
        result = 1
        for v in arr:
            result *= v
        return result

    product_all = product(arr)
    return [product_all // v for v in arr]


def solve3(arr):
    """Solve the problem without division but in O(n).  See:
https://www.geeksforgeeks.org/a-product-array-puzzle/
    """
    length = len(arr)
    left = [1] * length
    right = [1] * length
    prod = [1] * length

    for i in range(1, length):
        left[i] = arr[i-1] * left[i-1]

    print(left)
    for i in range(length-2, -1, -1):
        right[i] = arr[i+1] * right[i+1]
    print(right)

    for i in range(length):
        prod[i] = left[i] * right[i]

    return prod


def test():
    input1 = [1, 2, 3, 4, 5]
    input2 = [1, 2, 3]

    assert solve1(input1) == solve2(input1)
    assert(solve1(input2) == solve2(input2))
    assert solve1(input1) == solve3(input1)
    assert(solve1(input2) == solve3(input2))
