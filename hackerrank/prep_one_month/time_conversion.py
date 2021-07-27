""""
https://www.hackerrank.com/challenges/one-month-preparation-kit-time-conversion/problem

"""
from collections import namedtuple


def timeConversion(s):
    tokens = s.split(":")
    hours = int(tokens[0])
    minutes = int(tokens[1])
    seconds = int(tokens[-1][:2])
    ampm = tokens[-1][2:]

    if ampm.lower() == "am":
        hours = hours if hours != 12 else 0
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    hours = hours + 12 if hours != 12 else 12
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


Case = namedtuple("Case", ["s", "expected"])


def test():
    cases = [
        Case("07:05:45PM", "19:05:45"),
        Case("06:40:03AM", "06:40:03"),
        Case("12:40:22AM", "00:40:22"),
        Case("12:45:54PM", "12:45:54"),
    ]

    for c in cases:
        actual = timeConversion(c.s)
        assert actual == c.expected
