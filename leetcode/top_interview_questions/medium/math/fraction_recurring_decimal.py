"""Given two integers representing the numerator and denominator of a
fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"


Example 2:

Input: numerator = 2, denominator = 1
Output: "2"


Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

"""


from collections import namedtuple


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # If the numerator is zero, answer is 0
        if numerator == 0:
            return "0"

        # If any one (out of numerator and denominator)
        # is -ve, sign of resultant answer -ve.
        sign = -1 if (numerator < 0) ^ (denominator < 0) else 1

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Calculate the absolute part
        # (before decimal point).
        initial = numerator // denominator

        # Output string to store the answer
        res = ""

        # Append sign
        if sign == -1:
            res += "-"

        # Append the initial part
        res += str(initial)

        # If completely divisible, return answer.
        if numerator % denominator == 0:
            return res

        res += "."

        # Initialize Remainder
        rem = numerator % denominator
        mp = {}

        # Position at which fraction starts
        # repeating if it exists
        index = 0
        repeating = False
        while rem > 0 and not repeating:

            # If this remainder is already seen,
            # then there exists a repeating fraction.
            if rem in mp:

                # Index to insert parentheses
                index = mp[rem]
                repeating = True
                break

            else:
                mp[rem] = len(res)

            rem = rem * 10

            # Calculate quotient, append it to result
            # and calculate next remainder
            temp = rem // denominator
            res += str(temp)
            rem = rem % denominator

        # If repeating fraction exists,
        # insert parentheses.
        if repeating:
            res += ")"
            x = res[:index]
            x += "("
            x += res[index:]
            res = x

        # Return result.
        return res


Case = namedtuple("Case", ["numerator", "denominator", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(10, 5, "2"),
        Case(12, 5, "2.4"),
        Case(4, 3, "1.(3)"),
        Case(12, 500, "0.024"),
    ]
    for c in cases:
        actual = sol.fractionToDecimal(c.numerator, c.denominator)
        assert actual == c.expected
