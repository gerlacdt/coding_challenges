"""Given a string containing digits from 2-9 inclusive, return all
possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is
given below. Note that 1 does not map to any letters.

Phone keyboard:

1()     2(abc) 3(def)
4(ghi)  5(jkl) 6(mno)
7(pqrs) 8(tuv) 9(vwyz)


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer
could be in any order you want.

"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIGITS = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if not digits:
            return []

        def helper(head, tail):
            if not tail:
                return [head]
            results = []
            for c in DIGITS[tail[0]]:
                results.extend(helper(head + c, tail[1:]))
            return results

        return helper("", digits)


def test():
    digits = "23"
    sol = Solution()
    actual = sol.letterCombinations(digits)
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(actual) == sorted(expected)
