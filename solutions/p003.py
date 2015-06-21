import math
from common import prime

def run():
    global c
    c = 600851475143
    mx = math.sqrt(c)
    def callback(p):
        global c
        while c % p == 0:
            c = c / p
        if p*p > c:
            return True
    prime(max_n=mx, callback=callback)
    return c

from runner import main
main(run)
