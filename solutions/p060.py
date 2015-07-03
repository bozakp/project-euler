from common import Primes
from itertools import combinations

class CompSets:
    def __init__(self):
        self.comp_sets = dict()
        self.primes = Primes()

    def is_compatible(self, a, b):
        return (self.primes.is_prime(int(str(a) + str(b)))
                and self.primes.is_prime(int(str(b) + str(a))))

    def add_prime(self, n):
        new_set = set()
        for other_prime in self.comp_sets:
            if self.is_compatible(n, other_prime):
                self.comp_sets[other_prime].add(n)
                new_set.add(other_prime)
        self.comp_sets[n] = new_set

    def comp(self, n):
        return self.comp_sets[n]

    def prime_gen(self):
        i = 0 # next prime to be added
        next_prime_mx = 100
        while True:
            while i >= len(self.primes.primes):
                self.primes.generate(next_prime_mx)
                next_prime_mx += 100
            while i < len(self.primes.primes):
                p = self.primes.primes[i]
                self.add_prime(p)
                yield p
                i += 1

def find_five(comp_sets):
    for a in comp_sets.prime_gen():
        ac = comp_sets.comp(a)
        for b in sorted(list(ac)):
            if b >= a:
                break
            bc = comp_sets.comp(b)
            for c in sorted(list(ac.intersection(bc))):
                if c >= b:
                    break
                cc = comp_sets.comp(c)
                for d in sorted(list(ac.intersection(bc).intersection(cc))):
                    if d >= c:
                        break
                    dc = comp_sets.comp(d)
                    for e in sorted(list(ac.intersection(bc).intersection(cc).intersection(dc))):
                        if e >= d:
                            break
                        return [a, b, c, d, e]

def run():
    comp_sets = CompSets()
    result = find_five(comp_sets)
    return sum(result)

from runner import main
main(run)
