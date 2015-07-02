import math
from common import Primes
from itertools import product

def wild_set(length):
    digits = [str(x) for x in xrange(10)] + ["*"]
    odds = [str(x) for x in xrange(1, 10, 2)]
    for combs in product(digits, repeat=(length - 1)):
        for odd in odds:
            yield list(combs) + [odd]

def subst_wildcards(wild_list):
    if "*" not in wild_list:
        return
    for i in xrange(10):
        yield int("".join(str(i) if x=="*" else x for x in wild_list))

def find_eight_primes(primes, length):
    primes.generate(math.sqrt(10**length))
    for wild_list in wild_set(length):
        if wild_list[0] == "0":
            continue
        not_primes = 0
        prime_subs = []
        for n in subst_wildcards(wild_list):
            if primes.is_prime(n):
                prime_subs += [n]
            else:
                not_primes += 1
                if not_primes >= 3:
                    break
        if len(prime_subs) >= 8:
            return min(prime_subs)
    return None

def run():
    primes = Primes()
    n_length = 2
    while True:
        a = find_eight_primes(primes, n_length)
        if a:
            return a
        n_length += 1

from runner import main
main(run)
