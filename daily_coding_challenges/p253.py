"""Good morning! Here's your coding interview problem for today.

This problem was asked by PayPal.

Given a string and a number of lines k, print the string in zigzag
form. In zigzag, characters are printed out diagonally from top left
to bottom right until reaching the kth line, then back up to top
right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g

"""


def zigzag(s, k):
    length = len(s)
    table = [[" " for col in range(length)] for row in range(k)]
    col = 0
    row = 0
    direction = "DOWN"
    while col < length:
        # toggle direction if necessary
        if row == 0:
            direction = "DOWN"
        elif row == k-1:
            direction = "UP"
        table[row][col] = s[col]
        if direction == "DOWN":
            col += 1
            row += 1
        else:
            col += 1
            row -= 1

    # print table
    print()
    for row in table:
        print("".join(row))


def test():
    s = "thisisazigzag"
    k = 4
    zigzag(s, k)
