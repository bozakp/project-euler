def run():
    nsum = 0
    sqsum = 0
    for a in xrange(1,101):
        nsum += a
        sqsum += a*a
    return nsum*nsum - sqsum

from runner import main
main(run)
