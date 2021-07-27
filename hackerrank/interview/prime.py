def isPrime(n):
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False

    for (i, isprime) in enumerate(arr):
        if isprime:
            for j in range(i * i, n + 1, i):
                arr[j] = False

    if arr[n] == True:
        return 1
    else:
        for i in range(2, len(arr)):
            isprime = arr[i]
            if isprime:
                factor = n / i
                if factor.is_integer():
                    return int(i)


def test():
    actual = isPrime(2)
    assert 1 == actual

    actual = isPrime(4)
    assert 2 == actual

    actual = isPrime(15)
    assert 3 == actual

    actual = isPrime(25)
    assert 5 == actual

    actual = isPrime(523619)
    assert 593 == actual

    # actual = isPrime(37961921)
    # assert 4051 == actual
