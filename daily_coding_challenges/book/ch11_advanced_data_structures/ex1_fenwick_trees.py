"""You are given an array of length 24, where each element represents
the number of new subscribers during a corresponding hour. Implement a
data structure that efficiently support the following:

update(hour, value): Increment the element at index hour by value

query(start, end): Retrieve the number of subscribers that have signed
                   up between start and end (inclusive)

You can assume that all value get cleared at the end of the day, and
that you will not be asked for start and end values that wrap around
midnight.

"""


class FenwickTree:
    def __init__(self, nums):
        self.nums = [0 for _ in range(len(nums))]
        self.tree = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.update(i, nums[i])

    def query(self, index):
        i = index + 1  # needed because of the bit-operation trick
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)  # get least significant set bit
        return total

    def queryRange(self, start, end):
        return self.query(end) - self.query(start - 1)

    def update(self, index, val):
        diff = abs(val - self.nums[index])
        self.nums[index] = val
        i = index + 1
        while i < len(self.tree):
            self.tree[i] += diff
            i += i & (-i)


def test():
    nums = [4, 8, 1, 9, 3, 5, 5, 3]
    tree = FenwickTree(nums)
    actual = tree.tree
    expected = [0, 4, 12, 1, 22, 3, 8, 5, 38]
    assert actual == expected


def testQuery():
    nums = [4, 8, 1, 9, 3, 5, 5, 3]
    tree = FenwickTree(nums)
    actual = tree.query(7)
    expected = 38
    assert actual == expected

    actual = tree.query(6)
    expected = 35
    assert actual == expected


def testQueryRange():
    nums = [4, 8, 1, 9, 3, 5, 5, 3]
    tree = FenwickTree(nums)
    actual = tree.queryRange(2, 6)
    expected = 23
    assert actual == expected


def testUpdate():
    nums = [4, 8, 1, 9, 3, 5, 5, 3]
    tree = FenwickTree(nums)
    tree.update(2, 2)
    actual = tree.tree
    expected = [0, 4, 12, 2, 23, 3, 8, 5, 39]
    assert actual == expected
