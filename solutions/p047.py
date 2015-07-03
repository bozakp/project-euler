from common import Primes

def n_prime_factors(primes, n):
    rem = n
    c = 0
    for p in primes:
        if rem % p == 0:
            c += 1
        while rem % p == 0:
            rem = rem / p
        if p * p > rem:
            c += 1
            break
        if rem == 1:
            break
    return c

def run():
    # FLAG: Number needs to be justified
    primes = Primes().generate(200000)
    streak = 0
    i = 2 * 3 * 5 * 7
    while streak != 4:
        if n_prime_factors(primes, i) == 4:
            streak += 1
        else:
            streak = 0
        i += 1
    return i - 4

from runner import main
main(run)
