from itertools import product
def run():
    mx = 0
    for pair in product(xrange(1, 100), repeat=2):
        c = sum(int(x) for x in str(pair[0]**pair[1]))
        if c > mx:
            mx = c
    return mx

from runner import main
main(run)
