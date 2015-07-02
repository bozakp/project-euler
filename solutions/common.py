import math
import sys

def dummy_fn(*args):
    pass

class Primes:
    def __init__(self, callback=dummy_fn):
        self.primes = [2, 3]
        self.a = 5  # the next number to check
        self.callback = callback

    def _new_prime(self, n):
        """Register a new prime number n"""
        self.primes.append(n)
        self.callback(n)

    def generate(self, max_n=sys.maxsize):
        """Find primes up to max_n. Returns the list of primes
        when complete"""
        while self.a < max_n:
            b = math.sqrt(self.a)
            for x in self.primes:
                if self.a % x == 0:
                    break
                if x > b:
                    if self._new_prime(self.a):
                        return self.primes
                    break
            else:
                if self._new_prime(self.a):
                    return self.primes
            self.a += 2
        return self.primes

    def is_prime(self, n):
        i = 0
        sqrt = math.sqrt(n)
        while i < len(self.primes) and self.primes[i] <= sqrt:
            if n % self.primes[i] == 0:
                return False
            i += 1
        return True

# TODO: Migrate all code off this function
def prime(max_n=sys.maxsize, callback=dummy_fn):
    primes = [2, 3]
    a = 5
    def new_prime(p):
        primes.append(p)
        return callback(p)
    new_prime(2)
    new_prime(3)
    while a < max_n:
        b = math.sqrt(a)
        for x in primes:
            if a % x == 0:
                break
            if x > b:
                if new_prime(a):
                    return primes
                break
        else:
            if new_prime(a):
                return primes
        a += 2
    return primes

def d(x):
    b = math.sqrt(x)
    c = 1
    for a in xrange(2, int(b)):
        if x%a==0:
            c=c+a+x/a
    if b % 1 == 0:
        c = c + int(b)
    return c

def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)

def lcm(*numbers):
    """Return lowest common multiple."""
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)
