import math
from common import Primes
from itertools import permutations

def run():
    prime_max = math.sqrt(987654321)
    primes = Primes()
    primes.generate(prime_max)
    max_pan_prime = 0
    for n_digits in xrange(4,10):
        s = set(xrange(1, n_digits))
        for perm in permutations(s):
            i = 0
            n = 0
            for p in perm:
                n += 10 ** i * p
                i += 1
            if primes.is_prime(n) and n > max_pan_prime:
                max_pan_prime = n
    return max_pan_prime

from runner import main
main(run)
