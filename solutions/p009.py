import math

def run():
    for a in xrange(1, 500):
        for b in xrange(1, a):
            c = math.sqrt(a*a + b*b)
            if math.floor(c) == c and a + b + c == 1000:
                return a * b * int(c)

from runner import main
main(run)
