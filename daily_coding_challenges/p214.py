"""Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run
of 1s in its binary representation.

For example, given 156, you should return 3.

"""


def maxConsecutiveOnes(num):
    n = num
    lst = []
    while n:
        lst.append(n % 2)
        n = n // 2
    lst.reverse()
    counter = 0
    localMax = 0
    for d in lst:
        if d == 1:
            counter += 1
        else:
            if counter > localMax:
                localMax = counter
            counter = 0
    if counter > localMax:
        localMax = counter
    return localMax


def test():
    actual = maxConsecutiveOnes(156)
    expected = 3
    assert actual == expected

    actual = maxConsecutiveOnes(255)
    expected = 8
    assert actual == expected

    actual = maxConsecutiveOnes(47)
    expected = 4
    assert actual == expected

    actual = maxConsecutiveOnes(32)
    expected = 1
    assert actual == expected
