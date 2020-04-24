"""Ghost is a two-person word game where players alternate appending
letters to a word. The first person who spells out a dictionary word,
or creates a prefix for which there is no possible continutation,
loses. Here is a sample game:

Turn    Letter

P1      g
P2      h
P1      o
P2      s
P1      t

Player 1 loses since they spelled "ghost".

Given a dictionary of words, determine the letters the first player
should start with, such that with optimal play they cannot lose.

For example, if the dictionary is ["cat", "calf", "dog", "bear"], the
only winning start letter would be b.
"""

IS_WORD = "#"


class Trie:
    def __init__(self, words):
        self.root = {}
        self._build(words)

    def _build(self, words):
        for w in words:
            self._insert(w)

    def _insert(self, word):
        current = self.root
        for c in word:
            if c in current:
                current = current[c]
            else:
                current[c] = {}
                current = current[c]
        current[IS_WORD] = True

    def find(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current:
                return None
            current = current[c]
        return current

    def __repr__(self):
        return "{}".format(self.root)


def is_winning(trie, prefix):
    node = trie.find(prefix)
    if IS_WORD in node:
        return False
    else:
        moves = [prefix + c for c in node.keys()]
        if any(is_winning(trie, move) for move in moves):
            return False
        else:
            return True


def play_ghost(words):
    winner_chars = []
    trie = Trie(words)
    for letter in trie.root.keys():
        if is_winning(trie, letter):
            winner_chars.append(letter)
    return winner_chars


def testBuildTrie():
    words = ["cat", "cadaver"]
    actual = Trie(words)
    expected = {
        "c": {"a": {"t": {"#": True}, "d": {"a": {"v": {"e": {"r": {"#": True}}}}}}}
    }
    assert actual.root == expected


def testFindTrie():
    words = ["cat", "cadaver"]
    trie = Trie(words)
    actual = trie.find("ca")
    expected = {"d": {"a": {"v": {"e": {"r": {"#": True}}}}}, "t": {"#": True}}
    assert actual == expected

    actual = trie.find("cat")
    expected = {"#": True}
    assert actual == expected


def testGhost():
    words = ["cat", "calf", "dog", "bear"]
    actual = play_ghost(words)
    expected = ["c", "b"]
    assert actual == expected
