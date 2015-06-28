def run():
    s = 0
    for a in xrange(1, 1001):
        s += pow(a, a, 10**10)
    return str(s)[-10:]

from runner import main
main(run)
