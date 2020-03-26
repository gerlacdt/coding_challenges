"""Given a string and a number of lines k, print the string in zigzag
form. In zigzag, characters are printed out diagonally from top left
to bottom right until reaching the kth line, then back up to the top
right, and so on.


Example:

thisisazigzag and k = 4

t     a     g
 h   s z   a
  i i   i z
   s     g

"""


def printLines(lines):
    for l in lines:
        print("".join(l))


def zigzag(word, k):
    if k == 1:
        printLines([word.split()])
        return [word.split()]
    lines = [[" " for j in range(len(word))] for i in range(k)]
    line = 0
    descending = True
    for i in range(len(word)):
        lines[line][i] = word[i]
        if line == k-1:
            descending = False
        elif line == 0:
            descending = True
        if descending:
            line += 1
        else:
            line -= 1
    printLines(lines)
    return lines


def sample_solution(word, k):
    """Attention! This solution does not work with k == 1."""

    def get_spaces(row, desc, k):
        max_spaces = (k-1) * 2 - 1
        if desc:
            spaces = max_spaces - row*2
        else:
            spaces = max_spaces - (k-1-row)*2
        return spaces

    def is_descending(index, k):
        return index % (2*(k-1)) < k-1

    n = len(word)
    for row in (range(k)):
        i = row
        line = [" " for _ in range(n)]
        while i < n:
            line[i] = word[i]
            desc = is_descending(i, k)
            spaces = get_spaces(row, desc, k)
            i += spaces + 1
        print("".join(line))


def test():
    s = "thisisazigzag"
    actual = zigzag(s, 4)
    expected = [['t', ' ', ' ', ' ', ' ', ' ', 'a', ' ', ' ', ' ', ' ', ' ', 'g'],
                [' ', 'h', ' ', ' ', ' ', 's', ' ', 'z', ' ', ' ', ' ', 'a', ' '],
                [' ', ' ', 'i', ' ', 'i', ' ', ' ', ' ', 'i', ' ', 'z', ' ', ' '],
                [' ', ' ', ' ', 's', ' ', ' ', ' ', ' ', ' ', 'g', ' ', ' ', ' ']]
    assert actual == expected

    actual = zigzag(s, 1)
    expected = [s.split()]
    assert actual == expected


def testSampleSolution():
    print()
    s = "thisisazigzag"
    k = 4
    sample_solution(s, k)
    print()
    sample_solution(s, 2)
