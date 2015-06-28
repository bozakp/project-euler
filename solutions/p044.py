import math

def pent(n):
    return n * (3*n - 1) / 2

def run():
    for a in xrange(1, 3000):
        for b in xrange(a, 3000):
            pa = pent(a)
            pb = pent(b)
            if math.sqrt(24 * (pa + pb) + 1) % 3 == 2 and math.sqrt(24 * (pb - pa) + 1) % 3 == 2:
                return pb - pa

from runner import main
main(run)
