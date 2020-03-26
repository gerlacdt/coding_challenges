"""You are a product manager and currently leading a team to develop a
new product. Unfortunately, the latest version of your product fails
the quality check. Since each version is developed based on the
previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out
the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return
whether version is bad. Implement a function to find the first bad
version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.

"""


class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            mid = (right + left) // 2
            if isBadVersion(mid):  # leetcode provides this function
                right = mid
            else:
                left = mid + 1
        return left

    def binary_search(self, arr, n):

        def helper(low, high):
            if low > high:
                return None
            mid = (high + low) // 2
            if arr[mid] == n:
                return mid
            elif arr[mid] > n:
                return helper(low, mid-1)
            else:
                return helper(mid+1, high)
        return helper(0, len(arr)-1)


def test():
    arr = [1,2,3,4,5]
    sol = Solution()
    for n in range(len(arr)+1):
        result = sol.binary_search(arr, n)
        if n == 0 or n == 6:
            assert not result
        else:
            assert result == n-1
