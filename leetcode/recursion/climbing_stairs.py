"""You are climbing a stair case. It takes n steps to reach to the
top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {0: 1, 1: 1, 2: 2}

        def helper(n):
            if n in cache:
                return cache[n]

            result = helper(n - 1) + helper(n - 2)
            cache[n] = result
            return result

        return helper(n)


def test():
    sol = Solution()
    expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i in range(10):
        actual = sol.climbStairs(i)
        assert actual == expected[i]
