# coding: utf-8

"""The Hamming distance between two integers is the number of
positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are
different.

"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #  x xor y
        result = x ^ y
        # count 1 bits in result
        return self.hammingWeight(result)

    def hammingWeight(self, n: int) -> int:
        remstack = []
        x = n
        while (x > 0):
            rem = x % 2
            remstack.append(rem)
            x = x // 2
        return len(list(filter(lambda x: x == 1, remstack)))


def test():
    s = Solution()
    actual = s.hammingDistance(1, 4)
    assert actual == 2

    actual = s.hammingDistance(7, 0)
    assert actual == 3
