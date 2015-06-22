from common import d

def run():
    s = 0
    e = 5
    for e in xrange(5,10000):
        dd = d(e)
        if d(dd)==e and dd!=e:
            s += e
    return s

from runner import main
main(run)
