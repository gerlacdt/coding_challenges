"""Given the mapping a=1, b=2,....,z=26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' should be 3, since it could be decoded
as 'aaa', 'ka', 'ak'.

You can assume that the messages are always decodable. For example,
'001' is not allowed.

"""

from collections import namedtuple


letters = "abcdefghijklmnopqrstuvwxyz"


def decode(s: str):
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return 1
    result = 0
    result += decode(s[1:])
    if int(s[:2]) <= 26:
        result += decode(s[2:])
    return result


def decodeMemo(s: str):
    cache = {c: 1 for c in letters}
    cache[""] = 1

    def helper(s: str):
        if len(s) == 0:
            return 1
        elif len(s) == 1:
            return 1
        elif s in cache:
            return cache[s]
        result = 0
        result += decode(s[1:])
        if int(s[:2]) <= 26:
            result += decode(s[2:])
        cache[s] = result
        return result

    return helper(s)


def decodeTable(s: str):
    table = [0 for _ in range(len(s) + 1)]
    table[0] = 1
    table[1] = 1
    for i in range(len(s) - 1, -1, -1):
        substring = s[i:]
        n = len(substring)
        total = 0
        total += table[n - 1]
        if len(substring) > 1 and int(substring[:2]) <= 26:
            total += table[n - 2]
        table[n] = total
    return table[-1]


Case = namedtuple("Case", ["input", "expected"])


def test():
    cases = [
        Case("111", 3),
        Case("271", 1),
        Case("172", 2),
        Case("1111", 5),
        Case("2101", 1),
    ]
    for c in cases:
        actual = decode(c.input)
        actual1 = decodeMemo(c.input)
        actual2 = decodeTable(c.input)
        assert actual == c.expected, "input: {}".format(c.input)
        assert actual1 == c.expected, "input: {}".format(c.input)
        assert actual2 == c.expected, "input: {}".format(c.input)
