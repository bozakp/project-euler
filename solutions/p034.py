def run():
    dfacts = [0] * 10
    for i in xrange(len(dfacts)):
        dfacts[i] = math.factorial(i)
    MX = dfacts[9] * len(str(dfacts[9]))
    s = 0
    for a in xrange(3, MX):
        if sum(dfacts[int(c)] for c in str(a)) == a:
            s += a
    return s

from runner import main
main(run)
