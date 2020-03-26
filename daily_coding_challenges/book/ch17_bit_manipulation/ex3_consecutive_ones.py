"""Given an integer n, return the length of the longest consecutive
run of ones in its binary form.

For example, given 156, which is 10011100 in binary, you should return
3.

"""

from collections import namedtuple


def ones(n):
    # get bits as array
    bits = []
    power = 32
    for i in range(power):
        bit = (n >> i) & 1
        bits.append(bit)
    bits.reverse()

    # count consecutive ones
    maxOnes = counter = 0
    for b in bits:
        if b == 1:
            counter += 1
            maxOnes = max(counter, maxOnes)
        else:
            counter = 0
    return maxOnes


def onesShifting(n):
    max_length = 0
    while n:
        max_length += 1
        n = n & (n << 1)
    return max_length


Case = namedtuple("Case", ["input", "expected"])


def test():
    cases = [Case(156, 3), Case(31, 5)]
    for c in cases:
        actual = ones(c.input)
        actual2 = onesShifting(c.input)
        assert actual == c.expected, "Case: {}".format(c)
        assert actual2 == c.expected, "Case: {}".format(c)
