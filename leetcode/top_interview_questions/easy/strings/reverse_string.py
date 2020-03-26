"""Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return None


def test():
    sol = Solution()
    input1 = ["h", "e", "l", "l", "o"]
    expected1 = ["o", "l", "l", "e", "h"]
    sol.reverseString(input1)
    assert input1 == expected1

    input2 = ["H", "a", "n", "n", "a", "h"]
    expected2 = ["h", "a", "n", "n", "a", "H"]
    sol.reverseString(input2)
    assert input2 == expected2

    input3 = []
    expected3 = []
    sol.reverseString(input3)
    assert input3 == expected3

    input4 = ["a"]
    expected4 = ["a"]
    sol.reverseString(input4)
    assert input4 == expected4
