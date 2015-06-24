def run():
    s = 0
    for a in xrange(10**6):
        b = bin(a)[2:]
        sa = str(a)
        if sa == sa[::-1] and b == b[::-1]:
            s += a
    return s

from runner import main
main(run)
