"""Good morning! Here's your coding interview problem for today.

This problem was asked by Pivotal.

A step word is formed by taking a given word, adding a letter, and
anagramming the result. For example, starting with the word "APPLE",
you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word, create a function that
returns all valid step words.

"""

from collections import defaultdict


letters = "abcdefghijklmnopqrstuvwxyz"


def stepWords(word, dictionary):
    """Find all step words for the given word and dictionary. First create
a map of anagrams which holds all anagrams, i.e. key is the sorted
string of a word and the value is a list of matching words which
contains all characters of the key string. Second loop through the
alphabet and add all valid letters to the given word and look for a
match in the anagram map. If there is one add word to the result list.
    """
    anagrams = defaultdict(set)
    for w in dictionary:
        anagrams["".join(sorted(w))].add(w)

    result = []
    for c in letters:
        newWord = "".join(sorted(word+c))
        if newWord in anagrams:
            result.extend(list(anagrams[newWord]))

    return result


def test():
    word = "apple"
    dictionary = set(["apple", "appeal", "appela", "aab", "aba", "baa"])
    actual = stepWords(word, dictionary)
    expected = ["appeal", "appela"]
    assert sorted(actual) == sorted(expected)

    word = "aa"
    actual = stepWords(word, dictionary)
    expected = ["aab", "aba", "baa"]
    assert sorted(actual) == sorted(expected)
