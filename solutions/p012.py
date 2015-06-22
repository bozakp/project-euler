import math

def n_divisors(n):
    nd = 0
    mx = int(math.sqrt(n))
    for i in xrange(1, mx+1):
        if n % i == 0:
            nd += 2
    return nd

def run():
    a = 2
    tri = 1
    while True:
        tri += a
        if n_divisors(tri) > 500:
            return tri
        a += 1

from runner import main
main(run)
