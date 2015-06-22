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
                    return primes
                break
        else:
            if new_prime(a):
                return primes
        a += 2
    return primes

def d(x):
    b = math.sqrt(x)
    c = 1
    for a in xrange(2, int(b)):
        if x%a==0:
            c=c+a+x/a
    if b % 1 == 0:
        c = c + int(b)
    return c

