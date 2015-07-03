import math
from common import Primes

def run():
    global c
    c = 600851475143
    mx = math.sqrt(c)
    def callback(p):
        global c
        while c % p == 0:
            c = c / p
        if p*p > c:
            return True
    primes = Primes(callback)
    primes.generate(mx)
    return c

from runner import main
main(run)
