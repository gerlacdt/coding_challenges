"""Calculate the edit distance of 2 given strings aka Leventstein
distance.

"""

from collections import namedtuple


class Solution:
    def editDistance(self, a, b):
        def helper(a, b):
            if not a and not b:
                return 0
            if not a:
                return len(b)
            if not b:
                return len(a)

            val = 1
            if a[0] == b[0]:
                val = 0
            deletion = helper(a[1:], b) + 1
            insertion = helper(a, b[1:]) + 1
            substitution = helper(a[1:], b[1:]) + val

            return min(deletion, insertion, substitution)

        return helper(a, b)

    def editDistanceDynamic(self, a, b):
        n = len(a) + 1
        m = len(b) + 1

        # init dynamic programming table
        table = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            table[i][0] = i

        for j in range(m):
            table[0][j] = j

        for i in range(1, n):
            for j in range(1, m):
                if a[i - 1] == b[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = min(
                        table[i - 1][j] + 1,
                        table[i][j - 1] + 1,
                        table[i - 1][j - 1] + 1,
                    )
        return table[n - 1][m - 1]


Case = namedtuple("Case", ["a", "b", "expected"])


def test():
    cases = [
        Case("sitting", "kitten", 3),
        Case("foo", "", 3),
        Case("Sunday", "Saturday", 3),
        Case("Tier", "Tor", 2),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.editDistance(c.a, c.b)
        actual2 = sol.editDistanceDynamic(c.a, c.b)
        assert actual == c.expected, "Case: {} {}".format(c.a, c.b)
        assert actual2 == c.expected, "Case: {} {}".format(c.a, c.b)
