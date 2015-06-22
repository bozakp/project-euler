from itertools import permutations

def run():
    c = 1
    for p in permutations(xrange(10)):
        if c == 10**6:
            return "".join(str(x) for x in p)
        c += 1

from runner import main
main(run)
