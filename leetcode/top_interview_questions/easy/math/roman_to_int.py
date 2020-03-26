"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's
added together. Twelve is written as, XII, which is simply X + II. The
number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to
right. However, the numeral for four is not IIII. Instead, the number
four is written as IV. Because the one is before the five we subtract
it making four. The same principle applies to the number nine, which
is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed
to be within the range from 1 to 3999.


Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

from collections import namedtuple


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0

        while (i < len(s)):
            c1 = s[i]
            if (i == len(s) - 1):
                if c1 == 'I':
                    result += 1
                    i += 1
                elif c1 == 'V':
                    result += 5
                    i += 1
                elif c1 == 'X':
                    result += 10
                    i += 1
                elif c1 == 'L':
                    result += 50
                    i += 1
                elif c1 == 'C':
                    result += 100
                    i += 1
                elif c1 == 'D':
                    result += 500
                    i += 1
                elif c1 == 'M':
                    result += 1000
                    i += 1
                else:
                    raise RuntimeError("Not a valid roman number: {}".format(s))
                return result

            c2 = s[i+1]
            if c1 == 'I' and c2 == 'V':
                result += 4
                i += 2
            elif c1 == 'I' and c2 == 'X':
                result += 9
                i += 2
            elif c1 == 'X' and c2 == 'L':
                result += 40
                i += 2
            elif c1 == 'X' and c2 == 'C':
                result += 90
                i += 2
            elif c1 == 'C' and c2 == 'D':
                result += 400
                i += 2
            elif c1 == 'C' and c2 == 'M':
                result += 900
                i += 2
            elif c1 == 'I':
                result += 1
                i += 1
            elif c1 == 'V':
                result += 5
                i += 1
            elif c1 == 'X':
                result += 10
                i += 1
            elif c1 == 'L':
                result += 50
                i += 1
            elif c1 == 'C':
                result += 100
                i += 1
            elif c1 == 'D':
                result += 500
                i += 1
            elif c1 == 'M':
                result += 1000
                i += 1
            else:
                raise RuntimeError("Not a valid roman number: {}".format(s))
        return result


def test():
    s = Solution()
    Case = namedtuple("Case", ["input", "expected"])
    cases = [Case("III", 3), Case("IV", 4), Case("IX", 9), Case("LVIII", 58),
             Case("MCMXCIV", 1994)]
    for c in cases:
        actual = s.romanToInt(c.input)
        assert actual == c.expected
