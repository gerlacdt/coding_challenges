"""Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid
regular expression and returns whether or not the string matches the
regular expression.

For example, given the expression ra. and the string 'ray', your
function should return True. The same regular expression on the string
'raymond' should return False.

Give the regular expression .*at and the string 'chat', your function
should return True. The same regular on the string 'chats' should
return False.

"""


# TODO wrong solution in book! Book solution breaks with empty s!
def match_first_char(s, r):
    # print("match_first_char({},{})".format(s, r))
    if s and r:
        return (r[0] == "." and len(s) > 0) or (s[0] == r[0])
    elif s and not r:
        return True
    else:
        return False


def matches(s, r):
    # print("matches({},{})".format(s, r))
    # handle base case, r is empty
    if r == "":
        return s == ""

    # case, r is of length 1 or r is longer and has not as second char a *
    # (r must have at least 2 chars because we checked it)
    if len(r) == 1 or r[1] != "*":
        if match_first_char(s, r):
            return matches(s[1:], r[1:])
        else:
            return False

    else:
        # handle case with *

        # check first the case with no suffix
        if matches(s, r[2:]):
            return True

        # glob and check all suffixes
        i = 0
        while match_first_char(s[i:], r):
            if matches(s[i + 1 :], r[2:]):
                return True
            i += 1
        return False


def test():
    regexp = "ra."
    s = "ray"
    actual = matches(s, regexp)
    expected = True
    assert actual == expected

    regexp = "ra."
    s = "raymond"
    actual = matches(s, regexp)
    expected = False
    assert actual == expected

    regexp = ".*at"
    s = "chat"
    actual = matches(s, regexp)
    expected = True
    assert actual == expected

    regexp = ".*at"
    s = "chats"
    actual = matches(s, regexp)
    expected = False
    assert actual == expected


def testMatchFirstChar():
    s = "abc"
    r = ".*"
    actual = match_first_char(s, r)
    expected = True
    assert actual == expected

    s = ""
    r = ".*"
    actual = match_first_char(s, r)
    expected = False
    assert actual == expected
