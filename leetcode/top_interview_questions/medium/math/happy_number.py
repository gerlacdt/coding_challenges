"""Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting
with any positive integer, replace the number by the sum of the
squares of its digits, and repeat the process until the number equals
1 (where it will stay), or it loops endlessly in a cycle which does
not include 1. Those numbers for which this process ends in 1 are
happy numbers.


Example:
Input: 19
Output: true

Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

"""


def getDigits(n):
    current = n
    lst = []
    while current:
        lst.append(current % 10)
        current = current // 10
    return list(reversed(lst))


class Solution:
    def isHappy(self, num: int) -> bool:
        current = num
        for i in range(100):
            numbers = getDigits(current)
            print("numbers: {}".format(numbers))
            current = sum([n*n for n in numbers])
            if current == 1:
                return True
        return False


def test():
    s = Solution()
    n = 19
    actual = s.isHappy(n)
    assert actual

    actual = s.isHappy(8708)
    assert not actual
