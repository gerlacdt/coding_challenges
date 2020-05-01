"""A cryptoarithmetic puzzle is a mathematical game where the digits
of some numbers are represented by letters, and you must figure out
the correct mapping. Each letter represents a unique digit.

For example, a puzzle of the form:

  SEND
+ MORE
 MONEY

may have a solution:

{"S": 9, "E":5, "N": 6, "D": 7, "M":1, "O": 0, "R": 8, "Y": 2}



Sample solution from Peter Norvig, see:

https://github.com/norvig/pytudes/blob/master/ipynb/Cryptarithmetic.ipynb
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


# We see that about 2/3 of the time is spent in eval. So let's
# eliminate the calls to eval. That should be doable, because the
# expression we are evaluating is basically the same each time, but
# with different permutations of digits filled in. We could save a lot
# of work if we convert the expression into a Python function, compile
# that function just once, and then call the function for each of the
# 3.6 million permutations of digits. We want to take an expression
# such as:

# "NUM + BER == PLAY"

# and transform it into the Python function:

# (lambda A,B,E,L,M,N,P,R,U,Y:
#   (100*N+10*U+M) + (100*B+10*E+R) == (1000*P+100*L+10*A+Y))

# Actually that's not quite right. The rules say that "N", "B", and
# "P" cannot be zero. So the function should be:

# (lambda A,B,E,L,M,N,P,R,U,Y:
#   B and N and P and ((100*N+10*U+M) + (100*B+10*E+R) == (1000*P+100*L+10*A+Y)))


def compile_formula(formula):
    """Compile formula into a function. Also return letters found, as a
str, in same order as params of function. For example, 'YOU == ME**2'
returns (lambda E,M,O,U,Y: M and Y and ((100*Y+10*O+U) == (10*M+E)**2), 'YMEUO'
    """
    formula = formula.replace(" = ", " == ")
    letters = "".join(sorted(set(re.findall("[A-Z]", formula))))
    firstletters = sorted(set(re.findall(r"\b([A-Z])[A-Z]", formula)))
    body = re.sub("[A-Z]+", compile_word, formula)
    body = " and ".join(firstletters + [body])
    fn = "lambda {}: {}".format(",".join(letters), body)
    print(fn)
    assert len(letters) <= 10
    return eval(fn), letters


def compile_word(matchobj):
    """Compile the word 'YOU' as (100*Y + 10*O + U)"""
    word = matchobj.group()
    terms = reversed([mult(10 ** i, L) for i, L in enumerate(reversed(word))])
    return "(" + "+".join(terms) + ")"


def mult(factor, var):
    return var if factor == 1 else str(factor) + "*" + var


def faster_solve(formula):
    """Given a formula like 'NUM + BER == PLAY', fill in digits to solve
    it.  This version precompiles the formula and generates all
    digit-filled-in strings.
    """
    fn, letters = compile_formula(formula)
    for digits in permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if fn(*digits):
                yield formula.translate(
                    str.maketrans(letters, "".join((map(str, digits))))
                )
        except ArithmeticError:
            pass


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


def testFasterProfiling():
    pr = cProfile.Profile()
    pr.enable()
    formula = "SEND + MORE = MONEY"
    actual = next(faster_solve(formula))
    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
    print("actual {}".format(actual))
    assert eval(actual)
