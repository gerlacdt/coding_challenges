"""Given a string of round, curly and square opening and closing
brackets, return whether the brackets are balanced(well-formed).

Example:

([])[]({})  return True

([)] or ((()   return False


see also leetcode top_interview_questions/easy/design/valid_parens.py
"""

BRACKETS = {
    "[": "]",
    "(": ")",
    "{": "}",
}

OPEN_BRACKETS = set(["(", "[", "{"])
CLOSE_BRACKETS = set([")", "]", "}"])


def match(openChar, closeChar):
    return BRACKETS[openChar] == closeChar


def isBalanced(s):
    stack = []
    for c in s:
        if c in OPEN_BRACKETS:
            stack.append(c)
        elif c in CLOSE_BRACKETS:
            if not stack:
                return False
            if match(stack[-1], c):
                stack.pop()
    if stack:
        return False
    return True


def test():
    s = "([])[]({})"
    actual = isBalanced(s)
    assert actual

    s = "([)]"
    actual = isBalanced(s)
    assert not actual

    s = "((()"
    actual = isBalanced(s)
    assert not actual

    s = "(("
    actual = isBalanced(s)
    assert not actual

    s = ")"
    actual = isBalanced(s)
    assert not actual

    s = "((([[[{{{}}}]]]{[()]})))"
    actual = isBalanced(s)
    assert actual
