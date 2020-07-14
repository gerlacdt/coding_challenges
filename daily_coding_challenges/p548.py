"""Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree,
the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?

"""

from collections import namedtuple

DEGREE_HOUR = 30
DEGREE_MINUTE = 6


def clockAngle(time):
    # split time into 2 ints
    hour, minute = [int(val) for val in time.split(":")]

    # calculate angle
    hourFraction = DEGREE_HOUR * minute // 60  # hour hands move forward during hour
    return abs(((hour * DEGREE_HOUR) + hourFraction) - (minute * DEGREE_MINUTE))


Case = namedtuple("Case", ["time", "expected"])


def test():
    cases = [
        Case("0:00", 0),
        Case("3:30", 75),
        Case("8:15", 157),
        Case("8:45", 8),
        Case("4:45", 128),
    ]
    for c in cases:
        actual = clockAngle(c.time)
        assert actual == c.expected, "Case: {}".format(c.time)
