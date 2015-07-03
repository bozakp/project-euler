def run():
    d = []
    for k in xrange(33, 0, -1):
        d.append(1)
        d.append(2*k)
        d.append(1)
    d.remove(1)
    num = 1
    den = 1
    for x in d:
        num, den = den, (den*x + num)
    return sum(int(c) for c in str(num + 2*den))

from runner import main
main(run)
