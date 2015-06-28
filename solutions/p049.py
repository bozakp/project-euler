import math
from common import prime
from itertools import combinations, permutations

def run():
    seen = [False] * 10000
    primes = prime(math.sqrt(10000))
    def is_prime(n):
        a = 0
        while a < len(primes) and n >= primes[a]**2:
            if n % primes[a]==0:
                return False
            a=a+1
        return True
    for digits in xrange(1000,10000):
        d_primes = []
        for perm in permutations(int(d) for d in str(digits)):
            n = int("".join(str(p) for p in perm))
            if n < 1000 or seen[n]:
                continue
            if is_prime(n):
                d_primes.append(n)
            seen[n] = True
        if len(d_primes) >= 3:
            d_primes.sort()
            for dps in combinations(d_primes, 3):
                a = dps[0]
                b = dps[1]
                c = dps[2]
                if (c - b == b - a) and a != 1487:
                    return a * 10000**2 + b * 10000 + c

from runner import main
main(run)
