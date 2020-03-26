"""Implement an autocomplete system.  That is, given a query string s
and a set of all possible query strings, return all strings in the set
that have s as a prefix.

For example, given the query string de and the set of strings [dog,
deer, deal], return [deer, deal]

"""

from collections import deque


END = "#"


class Trie:
    def __init__(self):
        self._trie = {}

    def insert(self, word):
        trie = self._trie
        for c in word:
            if c in trie:
                trie = trie[c]
            else:
                trie[c] = {}
                trie = trie[c]
        trie[END] = True

    def find(self, prefix):
        trie = self._trie
        for c in prefix:
            if c in trie:
                trie = trie[c]
            else:
                return None
        return trie


def autocomplete(prefix, dictionary):
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    prefixTrie = trie.find(prefix)

    if not prefixTrie:
        return None

    # find all words from the found trie node
    # i use BFS here, even if DFS is more space efficient
    # BFS find smaller words first and longer words will be at the end
    frontier = deque([(prefixTrie, prefix)])
    results = []
    while frontier:
        currentTrie, currentPrefix = frontier.popleft()
        if currentPrefix in dictionary:
            results.append(currentPrefix)
        for key, t in currentTrie.items():
            if key == END:
                continue
            frontier.append((t, currentPrefix+key))
    return results


def test():
    s = "de"
    dictionary = ["dog", "deer", "deal"]
    actual = autocomplete(s, dictionary)
    expected = ["deer", "deal"]
    assert actual == expected

    s = "def"
    dictionary = ["dog", "deer", "deal", "defun", "defmetal", "foo"]
    actual = autocomplete(s, dictionary)
    expected = ["defun", "defmetal"]
    assert actual == expected

    s = "fooo"
    dictionary = ["dog", "deer", "deal", "defun", "defmetal", "foo"]
    actual = autocomplete(s, dictionary)
    expected = None
    assert actual == expected


    # check if smallest words come first and long words come last in
    # resultset, expected because of BFS
    s = "aa"
    dictionary = set(["aa", "aaa", "aaaa", "aaaaa"])
    actual = autocomplete(s, dictionary)
    expected = ["aa", "aaa", "aaaa", "aaaaa"]
    assert actual == expected
