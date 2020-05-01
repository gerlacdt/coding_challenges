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

from collections import namedtuple, OrderedDict
from itertools import permutations
import re
import cProfile
import pstats
import io
from pstats import SortKey
from typing import List


leading_zeros = re.compile(r"\b0[0-9]").search


class Solution:
    def solve(self, formula):
        """Given a formula like 'NUM + BER = PLAY', fill in digits to solve
        it.  Generate all valid digit-filled-in strings.
        """
        return next(filter(self._valid, self._letter_replacements(formula)))

    def _letter_replacements(self, formula):
        """All possible replacements of letters with digits in formula."""
        letters = "".join(set(re.findall("[A-Z]", formula)))
        formula = formula.replace(" = ", " == ")
        for p in permutations("1234567890", len(letters)):
            table = str.maketrans(letters, "".join(p))
            yield formula.translate(table)
        return None

    def _valid(self, formula):
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


class CompiledSolution:
    def compile_formula(self, formula):
        """Compile formula into a function. Also return letters found, as a
    str, in same order as params of function. For example, 'YOU == ME**2'
    returns (lambda E,M,O,U,Y: M and Y and ((100*Y+10*O+U) == (10*M+E)**2), 'YMEUO'
        """
        formula = formula.replace(" = ", " == ")
        letters = "".join(sorted(set(re.findall("[A-Z]", formula))))
        firstletters = sorted(set(re.findall(r"\b([A-Z])[A-Z]", formula)))
        body = re.sub("[A-Z]+", self.compile_word, formula)
        body = " and ".join(firstletters + [body])
        fn = "lambda {}: {}".format(",".join(letters), body)
        print(fn)
        assert len(letters) <= 10
        return eval(fn), letters

    def compile_word(self, matchobj):
        """Compile the word 'YOU' as (100*Y + 10*O + U)"""
        word = matchobj.group()
        terms = reversed([self.mult(10 ** i, L) for i, L in enumerate(reversed(word))])
        return "(" + "+".join(terms) + ")"

    def mult(self, factor, var):
        return var if factor == 1 else str(factor) + "*" + var

    def faster_solve(self, formula):
        """Given a formula like 'NUM + BER == PLAY', fill in digits to solve
        it.  This version precompiles the formula and generates all
        digit-filled-in strings.
        """
        formula = formula.replace(" = ", " == ")
        fn, letters = self.compile_formula(formula)
        for digits in permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
            try:
                if fn(*digits):
                    yield formula.translate(
                        str.maketrans(letters, "".join((map(str, digits))))
                    )
            except ArithmeticError:
                pass

    def solve(self, formula):
        return next(self.faster_solve(formula))


class BookSolution:
    def solve(self, problem: List[str]):
        words = list(map(list, problem))
        n = len(words[-1])
        words[0] = self._normalize(words[0], n)
        words[1] = self._normalize(words[1], n)
        letters = self._order_letters(words)
        unassigned = [letter for letter in letters if letter != "#"]
        nums = set(range(0, 10))
        return dict(self._solve(letters, unassigned, nums, words))

    def _solve(self, letters, unassigned, nums, words):
        if not unassigned:
            if self._is_valid(letters, words):
                return letters
            else:
                return None
        char = unassigned[0]
        for num in nums:
            letters[char] = num
            nums.remove(num)
            if self._is_valid(letters, words):
                solution = self._solve(letters, unassigned[1:], nums, words)
                if solution:
                    return solution
            nums.add(num)
            letters[char] = None
        return False

    def _is_valid(self, letters, words):
        a, b, c = words
        n = len(c)
        carry = 0
        for i in range(n - 1, -1, -1):
            if any(letters[word[i]] is None for word in words):
                return True
            elif letters[a[i]] + letters[b[i]] + carry == letters[c[i]]:
                carry = 0
            elif letters[a[i]] + letters[b[i]] + carry == 10 + letters[c[i]]:
                carry = 1
            else:
                return False
        return True

    def _normalize(self, word, n):
        diff = n - len(word)
        return ["#"] * diff + word

    def _order_letters(self, words):
        n = len(words[2])
        letters = OrderedDict()
        for i in range(n - 1, -1, -1):
            for word in words:
                if word[i] not in letters:
                    letters[word[i]] = None
        return letters


Case = namedtuple("Case", ["formula"])


def testSolve():
    sol = Solution()
    cases = [
        Case("AA + CC = BB"),
        Case("A + B = C"),
        # Case("SEND + MORE = MONEY")
    ]
    for c in cases:
        actual = sol.solve(c.formula)
        print("actual {}".format(actual))
        assert eval(actual)


def testFasterSolveWithProfiling():
    sol = CompiledSolution()
    pr = cProfile.Profile()
    pr.enable()
    formula = "SEND + MORE = MONEY"
    actual = next(sol.faster_solve(formula))
    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
    print("actual {}".format(actual))
    assert eval(actual)


def testBookSolution():
    sol = BookSolution()
    problem = ["SEND", "MORE", "MONEY"]
    actual = sol.solve(problem)
    expected = {
        "D": 8,
        "E": 4,
        "Y": 2,
        "N": 3,
        "R": 0,
        "O": 9,
        "S": 7,
        "M": 1,
        "#": None,
    }
    table = str.maketrans(
        "".join([k for k in actual.keys() if k != "#"]),
        "".join(map(str, [k for k in actual.values() if k != None])),
    )
    print([w.translate(table) for w in problem])
    assert actual == expected
