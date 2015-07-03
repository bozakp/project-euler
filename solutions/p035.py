import math
from common import Primes

def rotations(n):
    s = str(n)
    for i in xrange(len(s)):
        yield int(s[i:]+s[:i])

def run():
    MX = 10**6
    p = Primes()
    p.generate(math.sqrt(MX))
    c = 1  # already counting '2'
    for n in xrange(3, MX, 2):
        if all(p.is_prime(rot) for rot in rotations(n)):
            c += 1
    return c

from runner import main
main(run)
