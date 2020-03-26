"""Given an unordered lits of flights, each represented as (origin,
destination) pairs, and a starting airport, compute a possible
itinerary. If no such itinerary exists, return null. All fligths must
be used in the itinerary.


For example, given the list of flights:
[("SFO", "HKO"), ("YYZ","SFO"), ("YUL", "YYZ"), ("HKO", "ORD")] and starting point "YUL",

you may return the list ["YUL","YYZ", "SFO", "HKO", "ORD"]

Given the list of flights [("SFO", "COM"), ("COM", "YYZ")] and
starting point "COM", you should return null.

"""


def findRoute(flights, itinerary=[]):
    if not flights:
        return itinerary
    result = None
    last_stop = itinerary[-1]
    for i, flight in enumerate(flights):
        origin, destination = flight
        itinerary.append(destination)
        if isValid(flight, last_stop):
            result = findRoute(flights[:i] + flights[i + 1 :], itinerary)
            if result:
                return result
        itinerary.pop()
    return result


def isValid(flight, last_stop):
    origin, destination = flight
    if origin == last_stop:
        return True
    return False


def sampleSolution(flights, current_itinerary):
    if not flights:
        return current_itinerary
    last_stop = current_itinerary[-1]
    for i, (origin, destination) in enumerate(flights):
        remaining_flights = flights[:i] + flights[i + 1 :]
        current_itinerary.append(destination)
        if origin == last_stop:
            return sampleSolution(remaining_flights, current_itinerary)
        current_itinerary.pop()
    return None


def test():
    flights = [("SFO", "HKO"), ("YYZ", "SFO"), ("YUL", "YYZ"), ("HKO", "ORD")]
    actual = findRoute(flights, ["YUL"])
    actual1 = sampleSolution(flights, ["YUL"])
    expected = ["YUL", "YYZ", "SFO", "HKO", "ORD"]
    assert actual == expected
    assert actual1 == expected


def testNegative():
    flights = [("SFO", "COM"), ("COM", "YYZ")]
    actual = findRoute(flights, ["COM"])
    actual1 = sampleSolution(flights, ["COM"])
    expected = None
    assert actual == expected
    assert actual1 == expected
