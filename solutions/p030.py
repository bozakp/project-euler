import time
start = time.time()

UPPER_BOUND = (len(str(9**5)) + 1) * 9**5

def run():
    s = 0
    for a in xrange(2, UPPER_BOUND):
        b = 0
        for c in str(a):
            d = int(c)
            b += d**5
        if b == a:
            s += a
    return s

from runner import main
main(run)
