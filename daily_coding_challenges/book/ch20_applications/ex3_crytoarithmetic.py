"""A cryptoarithmetic puzzle is a mathematical game where the digits
of some numbers are represented by letters, and you must figure out
the correct mapping. Each letter represents a unique digit.

For example, a puzzle of the form:

  SEND
+ MORE
 MONEY

may have a solution:

{"S": 9, "E":5, "N": 6, "D": 7, "M":1, "O": 0, "R": 8, "Y": 2}



"""

from collections import namedtuple
from itertools import permutations
import re
import cProfile
import pstats
import io
from pstats import SortKey


def solve(formula):
    """Given a formula like 'NUM + BER = PLAY', fill in digits to solve
    it.  Generate all valid digit-filled-in strings.
    """
    return next(filter(valid, letter_replacements(formula)))


def letter_replacements(formula):
    """All possible replacements of letters with digits in formula."""
    letters = "".join(set(re.findall("[A-Z]", formula)))
    formula = formula.replace(" = ", " == ")
    for p in permutations("1234567890", len(letters)):
        table = str.maketrans(letters, "".join(p))
        yield formula.translate(table)
    return None


leading_zeros = re.compile(r"\b0[0-9]").search


def valid(formula):
    """Expression is valid iff it has no leading zero, and evaluates to true."""
    try:
        return not leading_zeros(formula) and eval(formula) is True
    except ArithmeticError:
        return False


Case = namedtuple("Case", ["formula"])


def testSolve():
    cases = [
        Case("AA + CC = BB"),
        Case("A + B = C"),
        # Case("SEND + MORE = MONEY")
    ]
    for c in cases:
        actual = solve(c.formula)
        print("actual {}".format(actual))
        assert eval(actual)


def testProfiling():
    pr = cProfile.Profile()
    pr.enable()
    formula = "SEND + MORE = MONEY"
    actual = solve(formula)
    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
    print("actual {}".format(actual))
    assert eval(actual)
