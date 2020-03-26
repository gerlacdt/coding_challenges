from collections import namedtuple


def toDecimal(binaryStr):
    result = 0
    s = reversed(binaryStr)
    for i, c in enumerate(s):
        if c == "1":
            result += 2 ** i
    return result


def toBinary(number):
    binary = []
    n = number
    while n > 0:
        binary.append(str(n % 2))
        n = n // 2
    return "".join(reversed(binary))


Case = namedtuple("Case", ["input", "expected"])


def testToDecimal():
    cases = [Case("1", 1), Case("0", 0), Case("111", 7), Case("1001", 9)]
    for c in cases:
        actual = toDecimal(c.input)
        assert actual == c.expected


def testToBinary():
    cases = [Case(1, "1"), Case(0, ""), Case(7, "111"), Case(9, "1001")]
    for c in cases:
        actual = toBinary(c.input)
        assert actual == c.expected
