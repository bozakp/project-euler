import math
import sys

def run():
    for a in xrange(144, sys.maxsize):
        c = a * (2*a - 1)
        if math.sqrt(24*c + 1) % 3 == 2:
            if math.sqrt(8*c + 1) % 2 == 1:
                return c

from runner import main
main(run)
