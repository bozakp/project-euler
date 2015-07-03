# max base = 9. 10^N is always longer than N
# max exponent = 
# b = a**n
# log(b) = n log(a)
# ^ length of b == int(log(b)) + 1
#             ^ [0, 1)
# length(b) = int(n log(a) + 1)
# n = int(n log(a) + 1)
# n >= n log(a) + 1
# 1 >= log(a) + 1/n
# 1 - log(a) >= 1/n
# n >= 1/(1 - log(a))
import math

def run():
    count = 0
    for a in xrange(1, 10):
        max_n = 1.0 / (1.0 - math.log10(a))
        for n in xrange(1, int(max_n+1)):
            if n == int(n*math.log10(a) + 1):
                count += 1
    return count

from runner import main
main(run)
