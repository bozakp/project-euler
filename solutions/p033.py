from common import gcd
import itertools
def run():
    final_denom = 1
    final_numer = 1
    for d in xrange(12, 100):
        if str(d)[1] == "0":
            continue
        for n in xrange(11, d):
            if any(int(nc)*d==int(dc)*n and int(no)==int(do) for nc, no in itertools.permutations(str(n)) for dc, do in itertools.permutations(str(d))):
                final_denom *= d
                final_numer *= n
    return final_denom / gcd(final_denom, final_numer)

from runner import main
main(run)
