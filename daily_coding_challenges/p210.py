"""Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting
with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the
number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?

"""


def collatz(n):
    if n == 0:
        return 0
    counter = 0
    while n != 1:
        counter += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n+1
    return counter


def collatzMax(N):
    """Returns a tuple pair where first is the length of the sequence and
second is the number with this sequence.
    """
    globalMax = (0, 0)
    for i in range(N+1):
        localMax = collatz(i)
        if localMax > globalMax[0]:
            globalMax = (localMax, i)
    return globalMax


def test():
    n = 1000000
    actual = collatzMax(n)
    expected = (524, 837799)
    assert actual == expected
