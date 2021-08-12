"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-dynamic-array/problem

"""


def dynamicArray(n, queries):
    seqlist = [[] for i in range(n)]
    lastAnswer = 0
    result = []
    for q in queries:
        if q[0] == 1:
            seq = (q[1] ^ lastAnswer) % n
            seqlist[seq].append(q[2])
        else:
            seq = (q[1] ^ lastAnswer) % n
            lastAnswer = seqlist[seq][q[2] % len(seqlist[seq])]
            result.append(lastAnswer)
    return result


def test():
    n = 2
    queries = [
        [1, 0, 5],
        [
            1,
            1,
            7,
        ],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1],
    ]

    actual = dynamicArray(n, queries)
    expected = [7, 3]
    assert actual == expected
