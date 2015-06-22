def run():
    s=1
    b=1
    for a in xrange(1, 501):
        s += 4*b+20*a
        b=b+8*a
    return s

from runner import main
main(run)
