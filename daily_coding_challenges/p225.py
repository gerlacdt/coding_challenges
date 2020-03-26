"""Good morning! Here's your coding interview problem for today.

This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be
executed. The executions are carried out starting with the kth person,
and removing every successive kth person going clockwise until there
is no one left.

Given N and k, write an algorithm to determine where a prisoner should
stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2,
4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.


See solution:
https://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/
"""


def josephusZero(n, k):
    "zero index based array"
    if n == 1:
        return 0
    else:
        return (josephusZero(n-1, k) + k) % n


def josephus(N, k):
    "one-indexed based array"
    if N == 1:
        return 1
    else:
        return ((josephus(N-1, k) + k-1) % N) + 1


def josephus2(n):
    "Optimized version for k=2"
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * josephus2(n//2) - 1
    else:
        return 2 * josephus2((n-1)//2) + 1


def test():
    actual = josephusZero(5,2)
    actual2 = josephus(5,2)
    expected = 3
    assert actual+1 == expected
    assert actual2 == expected

    actual = josephusZero(7,3)
    actual2 = josephus(7,3)
    expected = 4
    assert actual+1 == expected
    assert actual2 == expected

    actual = josephusZero(9,2)
    actual2 = josephus(9,2)
    expected = 3
    assert actual+1 == expected
    assert actual2 == expected

    actual = josephusZero(14,2)
    actual2 = josephus(14,2)
    expected = 13
    assert actual+1 == expected
    assert actual2 == expected

    for i in range(1, 50):
        assert josephus(i, 2) == josephus2(i), "n = {}".format(i)
        assert josephusZero(i, 2) + 1 == josephus(i,2)

    for i in range(1,50):
        for k in range(2,10):
            assert josephus(i,k) == josephusZero(i,k) + 1
