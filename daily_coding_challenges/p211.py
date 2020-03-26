"""Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all
occurrences of the pattern in the string. For example, given the
string "abracadabra" and the pattern "abr", you should return [0, 7].

"""


def startingPatterns(word, pattern):
    result = []
    for i in range(len(word) - len(pattern) + 1):
        matches = 0
        current = 0
        for j in range(i, i + len(pattern)):
            if word[j] != pattern[current]:
                break
            else:
                matches += 1
                current += 1
                if matches == len(pattern):
                    result.append(i)
    return result

# above solution has O(n**2), quadratic time complexity
# better it is the KMP Knuth-Morris-Pratt algorithm


def test():
    word = "abracadabra"
    pattern = "abr"
    actual = startingPatterns(word, pattern)
    expected = [0, 7]
    assert actual == expected
