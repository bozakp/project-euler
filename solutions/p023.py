from common import d

MX_N = 28124
def run():
    abn=[]
    for a in xrange(12, MX_N):
        if d(a) > a:
            abn.append(a)

    n = [1] * MX_N
    n[0] = 0

    for a in xrange(len(abn)):
        for b in xrange(a+1):
            c = abn[a] + abn[b]
            if c < len(n):
                n[c] = 0
    return sum(a if n[a] else 0 for a in xrange(len(n)))

from runner import main
main(run)
