"""Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

A permutation can be specified by an array P, where P[i] represents
the location of the element at i in the permutation. For example, [2,
1, 0] represents the permutation where elements at the index 0 and 2
are swapped.

Given an array and a permutation, apply the permutation to the
array. For example, given the array ["a", "b", "c"] and the
permutation [2, 1, 0], return ["c", "b", "a"].

"""


def permutation(arr, indices):
    result = [None for i in range(len(arr))]
    for i, index in enumerate(indices):
        result[i] = arr[index]

    # all values in result must be set if indices were valid, meaning
    # all indices of arr are contained
    assert all([True if v is not None else False for v in result])
    return result


def test():
    arr = ["a", "b", "c"]
    indices = [2,1,0]
    actual = permutation(arr, indices)
    expected = ["c", "b", "a"]
    assert actual == expected

    arr = [0,1,2,3,4,5,6]
    indices = [6,5,4,3,2,1,0]
    actual = permutation(arr, indices)
    expected = [6,5,4,3,2,1,0]
    assert actual == expected
