from math import factorial as fact

def run():
    count = 0
    for n in xrange(23, 101):
        r = 1
        fn = fact(n)
        while fn / fact(r) / fact(n - r) < 10**6:
            r += 1
        o = 2 * (int(n / 2) + 1 - r) - (1 if n % 2 == 0 else 0)
        count += o
    return count

from runner import main
main(run)
