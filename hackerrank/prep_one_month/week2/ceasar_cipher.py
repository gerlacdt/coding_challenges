"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-caesar-cipher-1/problem

"""

from collections import namedtuple


def caesarCipher(s, k):
    letters = "abcdefghijklmnopqrstuvwxyz"
    table = {c: chr(((ord(c) + k) - 97) % 26 + 97) for c in letters}
    tableUpper = {c: chr(((ord(c) + k) - 65) % 26 + 65) for c in letters.upper()}
    tmp = "".join([table.get(c, c) for c in s])  # replace lower cases
    return "".join([tableUpper.get(c, c) for c in tmp])  # replace upper cases


Case = namedtuple("Case", ["s", "k", "expected"])


def test():
    cases = [Case("abc", 1, "bcd"), Case("abc-", 1, "bcd-"), Case("Outz", 2, "Qwvb")]
    for c in cases:
        actual = caesarCipher(c.s, c.k)
        assert actual == c.expected
