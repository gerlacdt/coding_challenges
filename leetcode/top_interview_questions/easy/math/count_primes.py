"""Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4

Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""

import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        ceiling = math.ceil(math.sqrt(n))
        numbers = [True for i in range(n)]
        numbers[0] = False
        numbers[1] = False
        for i in range(2, ceiling):
            if numbers[i]:
                for j in range(i*i, len(numbers), i):
                    numbers[j] = False
        return len(list(filter(lambda x: x, numbers)))


def test():
    s = Solution()
    result = s.countPrimes(10)
    assert result == 4

    result = s.countPrimes(2)
    assert result == 0

    result  = s.countPrimes(3)
    assert result == 1

    result  = s.countPrimes(100)
    assert result == 25

    result  = s.countPrimes(499979)
    assert result == 41537
