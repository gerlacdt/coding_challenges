class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n <= 1:
            return 1
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.cache[n] = result
            return result

    def recClimbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


def test():
    sol = Solution()
    for i in range(16):
        result1 = sol.recClimbStairs(i)
        result2 = sol.climbStairs(i)
        print("climbStairs({}) = {}".format(i, result2))
        assert result1 == result2
