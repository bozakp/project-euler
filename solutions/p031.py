class CoinGen:
    def __init__(self, val):
        self.val = val

    def gen(self, other_gen, max, last):
        for other in other_gen:
            if last and self.val == 1:
                # When only the 1s piece remains, there's guaranteed to be one
                # solution to make 200, even if it's 0 pieces.
                yield 1
            else:
                for i in xrange((max - other) / self.val + 1):
                    yield other + self.val * i

def run():
    gens = list(reversed([CoinGen(x) for x in [1, 2, 5, 10, 20, 50, 100, 200]]))
    gg = (0 for x in xrange(1))  # initial seed
    MX = 200
    for i in xrange(len(gens)):
        if i == len(gens) - 1:
            gg = gens[i].gen(gg, MX, True)
        else:
            gg = gens[i].gen(gg, MX, False)
    return sum(c for c in gg)

from runner import main
main(run)
