"""Good morning! Here's your coding interview problem for today.

This problem was asked by IBM.

Given a string with repeated characters, rearrange the string so that
no two adjacent characters are the same. If this is not possible,
return None.

For example, given "aaabbc", you could return "ababac". Given "aaab",
return None.

"""


from collections import Counter


def successors(assignment, visited):
    result = []
    if not assignment:
        for c in visited.keys():
            if visited[c] > 0:
                result.append(c)
        return result
    for c in visited.keys():
        if visited[c] > 0 and c != assignment[-1]:
            result.append(c)
    return result


def rearrange(s):

    visited = Counter(s)

    def helper(assignment, c):
        # make move
        assignment.append(c)
        visited[c] -= 1

        # isGoal()
        if len(assignment) == len(s):
            return "".join(assignment)

        # call recursively
        for succ in successors(assignment, visited):
            # print("assignment: {} succ: {}, visited: {}".format(assignment, succ, visited))
            result = helper(assignment[:], succ)
            if result:
                return result

        # unmake move
        assignment.pop()
        visited[c] += 1

        return None

    return helper([], s[0])


def test():
    s = "aaabbc"
    actual = rearrange(s)
    expected = "ababac"
    assert actual == expected

    s = "aaab"
    actual = rearrange(s)
    expected = None
    assert actual == expected


    s = "aabbbccc"
    actual = rearrange(s)
    expected = "abacbcbc"
    assert actual == expected
