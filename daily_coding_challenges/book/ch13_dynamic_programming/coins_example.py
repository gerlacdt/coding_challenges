from collections import namedtuple


def coin_ways(n):
    """Returns the number of ways how to present a value n with 1 cents
and 5 cents. Order matters.
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0

    return coin_ways(n - 1) + coin_ways(n - 5)


def coin_ways_mem(n):
    """Same as above but use memoization, a top-down dynamic
programming.
    """
    cache = {0: 1}

    def helper(n):
        if n in cache:
            return cache[n]
        if n < 0:
            return 0
        result = helper(n - 1) + helper(n - 5)
        cache[n] = result
        return result

    return helper(n)


def coin_ways_table(n):
    """Same as above but use bottom-up approach with a table and loop."""
    table = {0: 1}
    for i in range(1, n + 1):
        table[i] = table.get(i - 1, 0) + table.get(i - 5, 0)
    return table[n]


def test():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [
        Case(1, 1),
        Case(5, 2),
        Case(6, 3),
        Case(9, 6),
        Case(10, 8),
        Case(30, 2328),
        Case(50, 644761),
        Case(100, 823322219501),
    ]

    for c in cases:
        # actual1 = coin_ways(c.input)
        actual2 = coin_ways_mem(c.input)
        actual3 = coin_ways_table(c.input)
        # assert actual1 == c.expected
        assert actual2 == c.expected
        assert actual3 == c.expected


KIND_OF_COINS = [1, 5, 10, 25, 50]


def counting_change(n, kind_of_coins=KIND_OF_COINS):
    """Returns the number of ways to change n cents. It takes into account
1, 5, 10, 25 and 50 cents coins.

Does not consider ordering of coins.
    """
    if n == 0:
        return 1
    elif n < 0 or not kind_of_coins:
        return 0
    result = counting_change(n, kind_of_coins[:-1]) + counting_change(
        n - kind_of_coins[-1], kind_of_coins
    )

    return result


def test_change():
    actual = counting_change(10)
    expected = 4
    assert actual == expected

    onedollar = 100
    actual = counting_change(onedollar)
    expected = 292
    assert actual == expected
