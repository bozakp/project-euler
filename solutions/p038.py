from itertools import chain

def run():
    mx = 0
    pan_set = set("123456789")
    for a in chain(xrange(91, 100), xrange(918, 1000), xrange(9182, 10000)):
        d = ""
        i = 1
        while len(d) < 9:
            d += str(a * i)
            i += 1
        if len(d) == 9 and int(d) > mx  and set(d) == pan_set:
            mx = int(d)
    return mx

from runner import main
main(run)
