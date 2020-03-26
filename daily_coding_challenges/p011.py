"""Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and
a set of all possible query strings, return all strings in the set
that have s as a prefix.

For example, given the query string de and the set of strings [dog,
deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data
structure to speed up queries.

"""


from collections import namedtuple


END = "#"


class Trie:
    """Implements a prefix-trie."""
    def __init__(self):
        self._trie = {}

    def insert(self, word):
        tree = self._trie  # get root
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree[END] = True

    def find(self, word):
        trie = self._trie
        for c in word:
            if c in trie:
                trie = trie[c]
            else:
                return False
        if END in trie:
            return True
        return False

    def findPrefix(self, prefix):
        trie = self._trie
        for c in prefix:
            if c in trie:
                trie = trie[c]
            else:
                return None
        return trie

    def _elements(self, d):
        results = []
        for c, v in d.items():
            if c == END:
                subresult = ['']
            else:
                subresult = [c + s for s in self._elements(v)]
            results.extend(subresult)
        return results

    def autocomplete(self, prefix):
        trie = self._trie
        for c in prefix:
            if c in trie:
                trie = trie[c]
            else:
                return []
        suffixes = self._elements(trie)
        return [prefix + suffix for suffix in suffixes]

    def __str__(self):
        return str(self._trie)


def autocomplete(prefix, words):
    """Return all possible item with the given prefix."""
    t = Trie()
    for w in words:
        t.insert(w)
    return t.autocomplete(prefix)


def test():
    # initialize trie
    words = ["dog", "done", "doo", "fire"]
    t = Trie()
    for w in words:
        t.insert(w)
    print("Trie: {}".format(t))

    # find testcases
    Case = namedtuple('Case', ['input1', 'expected'])
    cases = [Case("dog", True), Case("dogg", False),
             Case("", False),
             Case("do", False)]
    for c in cases:
        result = t.find(c.input1)
        assert result == c.expected

    # findPrefix testcases
    prefixCases = [Case("dog", {"#": True}),
                   Case("do", {'g': {'#': True}, 'n': {'e': {'#': True}}, 'o': {'#': True}}),
                   Case("foo", None)]
    for c in prefixCases:
        result = t.findPrefix(c.input1)
        assert result == c.expected

    # autocomplete testcases
    autocompleteCases = [Case("dog", ["dog"]),
                         Case("do", ["dog", "done", "doo"]),
                         Case("foo", [])]
    for c in autocompleteCases:
        result = autocomplete(c.input1, words)
        assert result == c.expected
