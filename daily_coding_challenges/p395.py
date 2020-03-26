"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Robinhood.

Given an array of strings, group anagrams together.

For example, given the following array:

['eat', 'ate', 'apt', 'pat', 'tea', 'now']
Return:

[['eat', 'ate', 'tea'],
 ['apt', 'pat'],
 ['now']]

"""

from collections import defaultdict


def groupAnagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        s = "".join(sorted(word))
        anagrams[s].append(word)
    return [values for _, values in anagrams.items()]


def test():
    lst = ["eat", "ate", "apt", "pat", "tea", "now"]
    actual = groupAnagrams(lst)
    expected = [["eat", "ate", "tea"], ["apt", "pat"], ["now"]]
    assert actual == expected
