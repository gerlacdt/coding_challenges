"""Given a boolean expression consisting of symbols 0, 1, &, |, ^ and
a desired boolean result. Implement a function to count the number of
ways of parenthesizing the expression such that it evalutates to
result.

Example:

1^0|0|1  -> desired result False or 0

2 ways:
1^((0|0)|1)
1^(0|(0|1))


"""


def eval(exp: str, desired: bool) -> int:

    def helper(exp, desired, start, end):
        if start == end:
            if exp[start] == "1" and desired:
                return 1
            elif exp[start] == "0" and not desired:
                return 1
            else:
                return 0

        result = 0
        if desired:
            for i in range(start+1, end+1, 2):
                op = exp[i]
                if op == "&":
                    result += helper(exp, True, start, i-1) * helper(exp, True, i+1, end)
                elif op == "|":
                    result += helper(exp, True, start, i-1) * helper(exp, False, i+1, end)
                    result += helper(exp, False, start, i-1) * helper(exp, True, i+1, end)
                    result += helper(exp, True, start, i-1) * helper(exp, True, i+1, end)
                elif op == "^":
                    result += helper(exp, True, start, i-1) * helper(exp, False, i+1, end)
                    result += helper(exp, False, start, i-1) * helper(exp, True, i+1, end)
                else:
                    raise RuntimeError("operator not valid: {}".format(op))
        else:
            for j in range(start+1, end+1, 2):
                op = exp[j]
                if op == "&":
                    result += helper(exp, True, start, j-1) * helper(exp, False, j+1, end)
                    result += helper(exp, False, start, j-1) * helper(exp, True, j+1, end)
                    result += helper(exp, False, start, j-1) * helper(exp, False, j+1, end)
                elif op == "|":
                    result += helper(exp, False, start, j-1) * helper(exp, False, j+1, end)
                elif op == "^":
                    result += helper(exp, False, start, j-1) * helper(exp, False, j+1, end)
                    result += helper(exp, True, start, j-1) * helper(exp, True, j+1, end)
                else:
                    raise RuntimeError("operator not valid: {}".format(op))
        return result

    return helper(exp, desired, 0, len(exp)-1)


def test():
    exp = "1^0|0|1"
    actual = eval(exp, False)
    expected = 2
    assert actual == expected
