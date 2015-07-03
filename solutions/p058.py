from common import Primes
import math

def run():
    pr = Primes()
    pr.generate(100000)
    a = 4
    n = 9
    t = 5
    p = 3
    while 100 * p / t >= 10:
        p += sum(1 if b else 0 for b in [pr.is_prime(n+a), pr.is_prime(n+2*a), pr.is_prime(n+3*a)])
        n += 4*a
        t += 4
        a += 2
    return a - 1

from runner import main
main(run)
