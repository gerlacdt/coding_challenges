"""Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree,
the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?

"""

from math import floor

DEGREE_PER_HOUR = 30
DEGREE_PER_MINUTE = 6


def calcAngle(hour, minute):
    hourFraction = floor((minute / 60) * 30)
    return abs((hour * DEGREE_PER_HOUR + hourFraction) - (minute * DEGREE_PER_MINUTE))


def test():
    actual = calcAngle(3, 0)
    expected = 90
    assert actual == expected

    actual = calcAngle(3, 30)
    expected = 75
    assert actual == expected

    actual = calcAngle(4, 45)
    expected = 128
    assert actual == expected
