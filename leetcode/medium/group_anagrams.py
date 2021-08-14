"""Given an array of strings strs, group the anagrams together. You
can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters
exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]


https://leetcode.com/problems/group-anagrams/

"""

from typing import List, Dict
from collections import namedtuple, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table: Dict[str, List[str]] = defaultdict(list)

        for s in strs:
            anagram = "".join(sorted(s))
            table[anagram].append(s)

        return list(table.values())


Case = namedtuple("Case", ["strs", "expected"])


def test():
    cases = [
        Case(
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        Case(["a"], [["a"]]),
        Case([""], [[""]]),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.groupAnagrams(c.strs)
        for group in actual:
            group.sort()
        for group in c.expected:
            group.sort()
        assert sorted(actual) == sorted(c.expected)
