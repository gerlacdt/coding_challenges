"""
Find all possible word combinations aka concatenations.

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
