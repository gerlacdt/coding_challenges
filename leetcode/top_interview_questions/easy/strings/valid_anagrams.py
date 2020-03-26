"""Given two strings s and t , write a function to determine if t is
an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:

What if the inputs contain unicode characters? How would you adapt
your solution to such case?

"""

from collections import namedtuple, defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = defaultdict(int)
        for i in range(len(s)):
            counts[s[i]] += 1
            counts[t[i]] -= 1
        return not any(counts.values())


def test():
    Case = namedtuple('Case', ['input1', 'expected'])
    cases = [Case(("anagram", "nagaram"), True),
             Case(("rat", "car"), False)]

    sol = Solution()

    for c in cases:
        result = sol.isAnagram(c.input1[0], c.input1[1])
        result2 = sol.isAnagram2(c.input1[0], c.input1[1])
        assert result == c.expected
        assert result2 == c.expected
