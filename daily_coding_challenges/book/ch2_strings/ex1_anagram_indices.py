"""Given a word w and a string s, find all indices in s which are the
starting locations of anagrams of w. For example, given w is ab and s
is abxaba return [0,3,4].
"""

from collections import Counter, namedtuple


def isAnagram(s1, s2):
    return Counter(s1) == Counter(s2)


def anagram_indices(s, word):
    result = []
    lenWord = len(word)
    for i in range(len(s) - lenWord + 1):
        if isAnagram(s[i:i+lenWord], word):
            result.append(i)
    return result


def sample_solution(s, w):
    M = len(w)
    N = len(s)
    window = Counter(s[:M])
    pattern = Counter(w)
    result = []
    for i in range(M, N):
        if window == pattern:
            result.append(i-M)
        del window[s[i-M]]
        window[s[i]] += 1
    if window == pattern:
        result.append(N-M)
    return result


def test():
    Case = namedtuple("Case", ["args", "expected"])
    cases = [
        Case(["abxaba", "ab"], [0,3,4]),
        Case(["", "ab"], [])
    ]
    for c in cases:
        actual = anagram_indices(*c.args)
        actual2 = sample_solution(*c.args)
        assert actual == c.expected
        assert actual2 == c.expected
