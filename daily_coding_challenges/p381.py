"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Paypal.

Read this Wikipedia article on Base64 encoding.

Implement a function that converts a hex string to base64.

For example, the string:

deadbeef

should produce:

3q2+7w==

"""

from collections import namedtuple

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = LETTERS.upper()
NUMBERS = "0123456789+/"
INDEX_TABLE = UPPERCASE_LETTERS + LETTERS + NUMBERS
PADDING = "="


def getIndex(block, table=INDEX_TABLE):
    i = int(block, 2)
    return table[i]


def getBlocks(word):
    blocks = []
    current = ""
    for i, c in enumerate(word):
        if i % 3 == 0 and i != 0:
            blocks.append(current)
            current = ""
        current += format(ord(c), "b").zfill(8)

    if current:
        blocks.append(current)

    return blocks


def getBlocksHex(word):
    hex_string = format(int(word, 16), "b")
    current = 0
    blocks = []
    for i in range(24, len(hex_string) + 1, 24):
        blocks.append(hex_string[current:i])
        current = i

    if current < len(hex_string):
        s = hex_string[current : len(hex_string)]
        n = len(s)
        if n % 8 and n < 8:
            s += "0" * (8 - n)
        elif n % 8 and n < 16:
            s += "0" * (16 - n)
        elif n % 8 and n < 24:
            s += "0" * (24 - n)
        blocks.append(s)

    return blocks


def b64(blocks):
    result = []
    for b in blocks:
        n = len(b)
        if n == 8:
            b += "0000"
        elif n == 16:
            b += "00"
        assert len(b) % 6 == 0
        current = 0
        for i in range(6, len(b) + 1, 6):
            elem = b[current:i]
            result.append(getIndex(elem))
            current = i
        if len(b) // 6 == 3:
            result.append("=")
        elif len(b) // 6 == 2:
            result.append("==")

    return "".join(result)


def encode(word):
    blocks = getBlocks(word)
    return b64(blocks)


def encodeHex(word):
    blocks = getBlocksHex(word)
    return b64(blocks)


Case = namedtuple("Case", ["input", "expected"])


def testDaily():
    word = "deadbeef"
    actual = encodeHex(word)
    expected = "3q2+7w=="
    assert actual == expected

    word = "f"
    actual = encodeHex(word)
    expected = "8A=="
    assert actual == expected


def testSimple():
    cases = [
        Case("Man", "TWFu"),
        Case("Ma", "TWE="),
        Case("M", "TQ=="),
        Case("any carnal pleasure.", "YW55IGNhcm5hbCBwbGVhc3VyZS4="),
        Case("any carnal pleasure", "YW55IGNhcm5hbCBwbGVhc3VyZQ=="),
        Case("any carnal pleas", "YW55IGNhcm5hbCBwbGVhcw=="),
        Case("asure.", "YXN1cmUu"),
    ]
    for c in cases:
        actual = encode(c.input)
        assert actual == c.expected


def testBlocks():
    word = "aaaa"
    actual = getBlocks(word)
    expected = ["011000010110000101100001", "01100001"]
    assert actual == expected

    word = "aaaaa"
    actual = getBlocks(word)
    expected = ["011000010110000101100001", "0110000101100001"]
    assert actual == expected

    word = "aaaaaa"
    actual = getBlocks(word)
    expected = ["011000010110000101100001", "011000010110000101100001"]
    assert actual == expected
