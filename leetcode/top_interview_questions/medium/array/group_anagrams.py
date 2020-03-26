"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through list
        # create unique key for anagram,
        # i.e. used sorted string as key and the original string as value,
        # whereas the original string is put in a list of strings to capture all grouped anagrams
        grouped = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            grouped[key].append(s)
        # dictionary to list
        result = []
        for anagrams in grouped.values():
            result.append(anagrams)
        return result


def test():
    arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    actual = s.groupAnagrams(arr)
    actual = [set(items) for items in actual]
    expected = [
        set(["ate","eat","tea"]),
        set(["nat","tan"]),
        set(["bat"]),
    ]
    assert actual == expected
