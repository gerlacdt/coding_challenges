"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

from random import randint

arr = [10, 15, 3, 7]
k = 17


def solve1(arr, k):
    """Naive solution. Run through the given array in two nested
loops. Sum up the i and j indexes and collect them if sum match the
given k value. Complexity is O(n^2)"""
    return next(((v1, v2) for i, v1 in enumerate(arr) for j, v2 in enumerate(arr)
                 if i != j and v1+v2 == k), None)


def solve2(arr, k):
    """Solution with complexity O(n). Only run through the array
once. Initialize a set. During the loop put k - arr[i] in the set,
i.e. use the difference as hashkey. If current arr[i] is already in
the set return.
    """
    s = set()
    for i, v in enumerate(arr):
        temp = k - v
        if temp in s:
            return (temp, v)
        s.add(v)


def test_random():
    ntests = 100
    sumrange = 100
    for i in range(ntests):
        arr = [randint(-100, 100) for i in range(100)]
        for k in range(sumrange):
            result1, result2 = solve1(arr, k), solve2(arr, k)
            if not result1 and not result2:
                continue
            if sum(result1) != sum(result2):
                print("unequal")
                print((k, arr))
                print((result1, result2))
