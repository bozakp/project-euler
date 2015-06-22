norm=[31,28,31,30,31,30,31,31,30,31,30,31]
leap=list(norm)
leap[1] = 29

def run():
    d=2
    n=0
    for y in xrange(1901, 2001):
        if y % 4 == 0 and not y % 400 == 0:
            for x in leap:
                if d%7==0:
                    n=n+1
                d=d+x
        else:
            for x in norm:
                if d%7==0:
                    n=n+1
                d=d+x
    return n

from runner import main
main(run)
