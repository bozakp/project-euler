import math
import sys

def dummy_fn(*args):
    pass

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
                    return
                break
        else:
            if new_prime(a):
                return
        a += 2
    pass
