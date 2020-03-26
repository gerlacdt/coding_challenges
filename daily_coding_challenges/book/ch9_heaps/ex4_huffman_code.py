"""Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Huffman coding is a method of encoding characters based on their
frequency. Each letter is assigned a variable-length binary string,
such as 0101 or 111110, where shorter lengths correspond to more
common letters. To accomplish this, a binary tree is built such that
the path from the root to any leaf uniquely maps to a character. When
traversing the path, descending to a left child corresponds to a 0 in
the prefix, while descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \\     / \
  *   a   t   *
 /             \
c               s
With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree, and
use it to determine a mapping between characters and their encoded
binary strings.

"""

from heapq import heappush, heappop


class Node:
    def __init__(self, char, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right

    def __str__(self):
        return "char: {}".format(self.char)


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root)
    inorder(root.right)


def createHuffmanTree(dictionary):
    if not dictionary:
        return None
    h = []
    for char, frequency in dictionary.items():
        heappush(h, (frequency, Node(char, None, None)))
    if len(h) == 1:
        f, left = heappop(h)
        return Node("*", left, None)
    while len(h) > 1:
        f1, left = heappop(h)
        f2, right = heappop(h)
        merged = (f1 + f2, Node("*", left, right))
        heappush(h, merged)
    freq, tree = heappop(h)
    return tree


def createEncoding(tree):
    encodings = {}
    path = []

    def dfs(node):
        if not node.left and not node.right:
            encodings[node.char] = "".join(path)
        else:
            if node.left:
                path.append("0")
                dfs(node.left)
                path.pop()
            if node.right:
                path.append("1")
                dfs(node.right)
                path.pop()

    dfs(tree)
    return encodings


def test():
    dictionary = {"a": 3, "c": 6, "e": 8, "f": 2}
    tree = createHuffmanTree(dictionary)
    actual = createEncoding(tree)
    expected = {"f": "100", "a": "101", "c": "11", "e": "0"}
    assert actual == expected
