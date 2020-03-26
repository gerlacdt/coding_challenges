"""Given a list of words, find all pairs of unique indices such that
the concatenation of the two words is a palindome.

For example, given the list ["code", "edoc", "da", "d"], return
[(0,1), (1,0), (2,3)]


see also (trie solution):
https://www.geeksforgeeks.org/palindrome-pair-in-an-array-of-words-or-strings/
"""

from collections import defaultdict


def is_palindrome(w):
    return w == w[::-1]


def palindrome_pairs(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            if is_palindrome(words[i] + words[j]):
                result.append((i, j))
    return result


def sample_solution(words):
    # ERRATA

    # this not works for duplicates in the given list. The second word
    # would override hashmap the existing entry
    # d = {w: i for i, w in  enumerate(words)}
    d = defaultdict(list)
    for i, w in enumerate(words):
        d[w].append(i)

    result = []
    for j, w in enumerate(words):
        for i in range(len(w)):
            prefix, suffix = w[:i], w[i:]
            reversed_prefix, reversed_suffix = prefix[::-1], suffix[::-1]
            if is_palindrome(prefix) and reversed_suffix in d:
                for k in d[reversed_suffix]:
                    if k != j:
                        result.append((k, j))
            if is_palindrome(suffix) and reversed_prefix in d:
                for k in d[reversed_prefix]:
                    if k != j:
                        result.append((j, k))
    return result


def createTrie(words):
    letters = "abcdefghijklmnopqrstuvwxyz"
    trie = dict()
    for j, w in enumerate(words):
        node = trie
        for i in range(len(w)):
            if w[i] not in node:
                node[w[i]] = dict()
            node = node[w[i]]
        node["END"] = j  # end of word
    return trie


def solution(words):
    """
1) Create an empty Trie.
2) Do following for every word:-
    a) Insert reverse of current word.
    b) Also store up to which index it is
       a palindrome.
3) Traverse list of words again and do following
   for every word.
    a) If it is available in Trie then return true
    b) If it is partially available
         Check the remaining word is palindrome or not
         If yes then return true that means a pair
         forms a palindrome.
         Note: Position upto which the word is palindrome
               is stored because of these type of cases.
"""
    reversedWords = [w[::-1] for w in words]
    trie = createTrie(reversedWords)
    results = []

    def search(root, word, index):
        node = root

    for i, w in enumerate(words):
        search(trie, w, i)
    return results


def test():
    words = ["code", "edoc", "da", "d"]
    expected = set([(0,1), (1,0), (2,3)])
    actual = palindrome_pairs(words)
    actual2 = sample_solution(words)
    assert set(actual) == expected
    assert set(actual2) == expected

    words = ["aabc", "aa", "cbaa", "bc", ]
    expected = set([(0, 2), (2, 0), (2, 3)])
    actual = palindrome_pairs(words)
    actual2 = sample_solution(words)
    assert set(actual) == expected
    assert set(actual2) == expected

    words = ["aaa", "aaa"]
    expected = set([(0, 1), (1, 0)])
    actual = palindrome_pairs(words)
    actual2 = sample_solution(words)
    assert set(actual) == expected
    assert set(actual2) == expected


    words = ["aa", "a"]
    expected = set([(0, 1), (1, 0)])
    actual = palindrome_pairs(words)
    actual2 = sample_solution(words)
    print(actual)
    print(actual2)
    assert set(actual) == expected
    assert set(actual2) == expected


def testTrie():
    words = ["code", "edoc", "da", "d"]
    trie = solution(words)
    print(trie)
