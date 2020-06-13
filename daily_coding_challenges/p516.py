"""Good morning! Here's your coding interview problem for today.

This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of
7, or the sum of unique powers of 7. The first few sevenish numbers
are 1, 7, 8, 49, and so on. Create an algorithm to find the nth
sevenish number.

"""


class Solution:
    def sevenish(self, n):
        result = []
        currentPower = 0
        while len(result) <= n:
            val = 7 ** currentPower
            currentPower += 1
            result.append(val)
            for i in range(len(result) - 1):
                result.append(val + result[i])
                if len(result) >= n:
                    return result[n - 1]
        return result[n - 1]


def test():
    sol = Solution()
    expected = [
        1,
        7,
        8,
        49,
        50,
        56,
        57,
        343,
        344,
        350,
        351,
        392,
    ]
    for i, exp in enumerate(expected):
        actual = sol.sevenish(i + 1)
        assert actual == exp
