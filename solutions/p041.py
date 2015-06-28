import math
from common import prime
from itertools import permutations

def run():
    prime_max = math.sqrt(987654321)
    primes = prime(max_n=prime_max)
    def is_prime(n):
        a = 0
        while n >= primes[a]**2:
            if n % primes[a]==0:
                return False
            a=a+1
        return True
    max_pan_prime = 0
    for n_digits in xrange(4,10):
        s = set(xrange(1, n_digits))
        for perm in permutations(s):
            i = 0
            n = 0
            for p in perm:
                n += 10 ** i * p
                i += 1
            if is_prime(n) and n > max_pan_prime:
                max_pan_prime = n
    return max_pan_prime

from runner import main
main(run)
