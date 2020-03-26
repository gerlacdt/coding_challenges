"""Given an integer array, find the maximum XOR of any two elements.

"""


def toBin(n: int, k: int):
    arr = []
    for i in range(k, -1, -1):
        bit = 1 if n & (1 << i) else 0
        arr.append(bit)
    return arr


END = "#"


class Trie:
    def __init__(self, k: int):
        self.k = k
        self.trie = {}

    def insert(self, n):
        binary = toBin(n, self.k)
        trie = self.trie
        for b in binary:
            if b in trie:
                trie = trie[b]
            else:
                trie[b] = {}
                trie = trie[b]
        trie[END] = True

    def findMaxXor(self, n: int):
        binary = toBin(n, self.k)
        binary.reverse()  # highest bit must be at the end of the array
        trie = self.trie
        xor = 0
        for i in range(self.k, -1, -1):
            b = binary[i]
            if 1-b in trie:
                trie = trie[1-b]
                xor |= (1 << i)
            else:
                trie = trie[b]
        return xor


def maxXorPair(arr):
    k = max(arr).bit_length()
    trie = Trie(k)
    for n in arr:
        trie.insert(n)
    return max([trie.findMaxXor(n) for n in arr])


def test():
    arr = [2, 1]
    actual = maxXorPair(arr)
    expected = 3
    assert actual == expected

    arr = [2, 4, 6, 7]
    actual = maxXorPair(arr)
    expected = 6
    assert actual == expected
