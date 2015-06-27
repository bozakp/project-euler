import math
import operator

def run():
    n = [0] * 1001
    for c in xrange(5, 501):
        a = c - 1
        while a > 0.707 * c:
            b = math.sqrt(c*c - a*a)
            if b % 1 == 0:
                b = int(b)
                if a + b + c > 1000:
                    break
                else:
                    n[a + b + c] += 1
            a -= 1
    max_i, max_value = max(enumerate(n), key=operator.itemgetter(1))
    return max_i

from runner import main
main(run)
