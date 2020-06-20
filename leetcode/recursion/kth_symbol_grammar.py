"""On the first row, we write a 0. Now in every subsequent row, we
look at the previous row and replace each occurrence of 0 with 01, and
each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The
values of K are 1-indexed.) (1 indexed).

Examples:

Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001


Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].

"""

from collections import namedtuple


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def helper(n, k):
            if n == 0 or k == 0:
                return 0

            result = helper(n - 1, k // 2)
            if k % 2 == 0:
                if result == 0:
                    return 0
                else:
                    return 1
            else:
                if result == 0:
                    return 1
                else:
                    return 0

        return helper(N - 1, K - 1)

    def kthGrammarSlow(self, N: int, K: int) -> int:
        def helper(n, row):
            if n == 0:
                return row[K - 1]

            newRow = []
            for val in row:
                if val == 0:
                    newRow.append(0)
                    newRow.append(1)
                else:
                    newRow.append(1)
                    newRow.append(0)
            return helper(n - 1, newRow)

        return helper(N - 1, [0])


Case = namedtuple("Case", ["n", "k", "expected"])


def test():
    cases = [
        Case(1, 1, 0),
        Case(2, 1, 0),
        Case(2, 2, 1),
        Case(4, 5, 1),
        Case(30, 1, 0),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.kthGrammar(c.n, c.k)
        assert actual == c.expected, "Case: n={} k={}".format(c.n, c.k)
