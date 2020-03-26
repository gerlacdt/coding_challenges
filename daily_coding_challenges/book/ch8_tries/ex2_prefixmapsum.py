"""Implement a PrefixMapSum class with the following methods:

- insert(key: str, value: int): Set a given key's value in the map. If
  the key already exists, overwrite the value.

- sum(prefix: str): Return the sum of all values of keys that begin
  with a given prefix.

Example:

see test()

"""

VAL = "val"
END = "#"


class PrefixMapSum:
    def __init__(self):
        self._trie = {}
        self.seen = {}

    def insert(self, key, val):
        if key in self.seen:
            val -= self.seen[key]
        self.seen[key] = val
        trie = self._trie
        for c in key:
            if c not in trie:
                trie[c] = {}
                trie[c][VAL] = val
                trie = trie[c]
            else:
                trie[c][VAL] += val
                trie = trie[c]
        trie[END] = True

    def sum(self, key):
        trie = self._trie
        current = 0
        for c in key:
            if c in trie:
                trie = trie[c]
                current = trie[VAL]
            else:
                # no match
                return current
        return current


def test():
    mapsum = PrefixMapSum()
    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3

    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5

    # existing key should override vals and not add additionally
    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5
