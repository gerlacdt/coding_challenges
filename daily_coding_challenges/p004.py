"""Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in
linear time and constant space. In other words, find the lowest
positive integer that does not exist in the array. The array can
contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def find(arr):
    """Keep track of lowest positive integer if we encounter this lowest
    integer increase it by 1.
    """
    current = 1
    for v in arr:
        if v == current:
            current += 1
    return current


def test():
    result = find([3, 4, -1, 1])
    expected = 2
    assert result == expected

    result = find([1, 2, 0])
    expected = 3
    assert result == expected
