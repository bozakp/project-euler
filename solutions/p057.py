def run():
    count = 0
    for a in xrange(1001):
        n = 1
        d = 2
        for x in xrange(a):
            n, d = d, (2*d + n)
        n += d
        if len(str(n)) > len(str(d)):
            count += 1
    return count

from runner import main
main(run)
