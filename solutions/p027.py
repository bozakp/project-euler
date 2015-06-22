from common import prime

primes = prime(max_n=50000)

def isprime(z):
    return z in primes

def run():
    d = 0
    c = 0
    for a in xrange(-999, 1000):
        bi = 0
        while primes[bi] < 1000:
            b = primes[bi]
            if b > -a and b > (1 - 40*(a + 40)):
                n = 1
                while isprime(n*(n+a)+b):
                    n += 1
                if n > c:
                    d = a * b
                    c = n
            bi += 1
    return d

from runner import main
main(run)
