"""Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest
sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and
5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def max_sum(arr):
    table = []

    table.append(arr[0])
    table.append(arr[1])
    table.append(arr[2] + arr[0])

    for i in range(3, len(arr)):
        table.append(arr[i] + max([table[i-2], table[i-3]]))

    return max(table)


def max_sum2(arr):
    """geekforgeeks solution"""
    incl = arr[0]
    excl = 0

    for i in range(1, len(arr)):
        new_excl = max((incl, excl))
        incl = max((arr[i]+excl), incl)
        excl = new_excl

    return max(incl, excl)


def test():
    t1 = [2, 4, 6, 2, 5]  # 13
    t2 = [5, 1, 1, 5]  # 10
    t3 = [5, 5, 10, 100, 10, 5]  # 110
    t4 = [1, 2, 3]  # 4
    t5 = [1, 20, 3]  # 20
    t6 = [5,  5, 10, 40, 50, 35]  # 80

    cases = ((t1, 13), (t2, 10), (t3, 110),
             (t4, 4), (t5, 20), (t6, 80))

    for case in cases:
        arr, expected = case

        assert max_sum(arr) == expected
        assert max_sum2(arr) == expected
