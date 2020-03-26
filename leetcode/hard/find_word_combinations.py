"""Find all possible word combinations aka concatenations in a given list
of words.  Meaning a word can be a concatenation of multiple words
(NOT only of two words).

See also daily_coding_challenges/techlead


Leetcode problem description:

Given a list of words (without duplicates), please write a program
that returns all concatenated words in the given list of words.  A
concatenated word is defined as a string that is comprised entirely of
at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation:

"catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".


Note:

The number of elements of the given array will not exceed 10,000 The
length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.  The
returned elements order does not matter.

"""

from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordDict = set(words)
        results = set()

        def helper(word):
            for index in range(1, len(word)):
                prefix = word[index:]
                suffix = word[:index]
                if prefix in wordDict:
                    if suffix in wordDict or helper(suffix):
                        return True

        for w in words:
            if helper(w):
                results.add(w)
        return results


def test():
    words = [
        "cat",
        "cats",
        "catsdogcats",
        "dog",
        "dogcatsdog",
        "hippopotamuses",
        "rat",
        "ratcatdogcat",
    ]
    sol = Solution()
    actual = sol.findAllConcatenatedWordsInADict(words)
    expected = set(["catsdogcats", "dogcatsdog", "ratcatdogcat"])
    assert actual == expected
