"""Get prodcut of all other elements.  Given an array of integers,
return a new array such that each element at index i of the new array
is the product of all other numbers in the original array except the
one at i.

Example 1:
[1,2,3,4,5]
[120, 60, 40, 30, 24]

Example 2:
[3,2,1]
[2,3,6]

"""


def product(arr):
    prefixes = []
    postfixes = []

    prefixes.append(arr[0])
    for i in range(1, len(arr)):
        prefixes.append(prefixes[-1]*arr[i])

    postfixes.append(arr[-1])
    for i in range(len(arr)-2, -1, -1):
        postfixes.append(postfixes[-1]*arr[i])
    postfixes.reverse()

    result = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        if i == 0:
            result[i] = postfixes[1]
            continue
        if i == len(arr) - 1:
            result[i] = prefixes[-2]
            continue
        result[i] = prefixes[i-1] * postfixes[i+1]
    return result


def test():
    actual = product([1, 2, 3, 4, 5])
    expected = [120,  60,  40,  30,  24]
    assert actual == expected

    actual = product([3, 2, 1])
    expected = [2, 3, 6]
    assert actual == expected
