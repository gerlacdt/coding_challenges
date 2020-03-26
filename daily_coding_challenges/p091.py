"""Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

What does the below code snippet print out? How can we fix the
anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())

"""


def fns(n):
    functions = []
    for i in range(n):
        def fn(x):
            return lambda: x
        functions.append(fn(i))
    return [f() for f in functions]


def test():
    result = fns(3)
    expected = [0, 1, 2]

    assert result == expected
