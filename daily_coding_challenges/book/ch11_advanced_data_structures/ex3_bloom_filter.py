"""Implement a data structure which carries out the following
operations without resizing the underlying array.

add(value): add value to the set of values
check(value):check whether a value is in the set

The check method may return occasional false positives(in other words,
incorrectly identifying an element as part of the set), but should
always correctly identify a true element.

"""

from hashlib import md5, sha1, sha256, sha384, sha512


class Bloom:
    def __init__(self, N=1000):
        self.N = N
        self.data = [False] * N
        self.hash_algorithms = [md5, sha1, sha256, sha384, sha512]

    def _hash(self, f, value):
        h = f(str(value).encode("utf-8")).hexdigest()
        return int(h, 16) % self.N

    def add(self, value):
        hashes = [self._hash(f, value) for f in self.hash_algorithms]
        for h in hashes:
            self.data[h] = True

    def check(self, value):
        hashes = [self._hash(f, value) for f in self.hash_algorithms]
        for h in hashes:
            if not self.data[h]:
                return False
        return True


def test():
    inputs = [4, 7, 42, 56, 96]
    bloom = Bloom(50)
    for i in inputs:
        bloom.add(i)

    for i in inputs:
        actual = bloom.check(i)
        assert actual

    actual = bloom.check(12)
    assert not actual
