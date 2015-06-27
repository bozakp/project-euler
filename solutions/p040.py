import operator

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def run():
    a = 1
    s = "0"
    while len(s) < 1000002:
        s += str(a)
        a += 1
    ns = [10**i for i in xrange(7)]
    return prod(int(s[n]) for n in ns)

from runner import main
main(run)
