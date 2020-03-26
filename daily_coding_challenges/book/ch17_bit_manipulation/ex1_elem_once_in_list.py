"""Given an array of integers where every integer occurs three times
except for one integer, which only occurs once, find and return the
non-duplicated integer.

Do this in O(N) time and O(1) space.
"""


def findUniq(arr):
    """Given an array with numbers. It contains a single number which
exist only once, all other numbers exist 3 times. Find the unique
number in time complexity O(n) and constant space aka O(1).
    """
    # assume we have 32-bit integer
    bits = [0] * 32
    for n in arr:
        # get all bits one by one of n
        for i in range(32):
            # increase bit counter for the corresponding bit
            bit = (n >> i) & 1
            bits[i] += bit

    # check counted bits,
    # we found unique number if the counter is not fully dividable by 3
    result = 0
    for i, b in enumerate(bits):
        if b % 3 != 0:
            result += 2 ** i
    return result


def test():
    # arr = [6, 1, 3, 3, 3, 6, 6]
    # actual = findUniq(arr)
    # expected = 1
    # assert actual == expected

    arr = [1, 1, 10, 10, 99, 9, 9, 1, 9, 10]
    actual = findUniq(arr)
    expected = 99
    assert actual == expected
