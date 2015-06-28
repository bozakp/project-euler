import math
from common import prime

def rotations(n):
    s = str(n)
    for i in xrange(len(s)):
        yield int(s[i:]+s[:i])

def run():
    MX = 10**6
    primes = prime(max_n=math.sqrt(MX))
    def is_prime(x):
        i = 0
        sqrt = math.sqrt(x)
        while i < len(primes) and primes[i] <= sqrt:
            if x % primes[i] == 0:
                return False
            i += 1
        return True
    c = 1  # already counting '2'
    for n in xrange(3, MX, 2):
        if all(is_prime(rot) for rot in rotations(n)):
            c += 1
    return c

from runner import main
main(run)
