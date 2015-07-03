from itertools import product

def trig(n):
    return n * (n + 1) / 2
def squa(n):
    return n * n
def peng(n):
    return n * (3*n - 1) / 2
def hexg(n):
    return n * (2*n - 1)
def hepg(n):
    return n * (5*n - 3) / 2
def octg(n):
    return n * (3*n - 2)

def generate_poly(fn, mx):
    n = 1
    s = set()
    while fn(n) < mx:
        s.add(fn(n))
        n += 1
    return s

def is_cyclic(group):
    starts = [int(str(x)[:2]) for x in group]
    ends = [int(str(x)[2:]) for x in group]
    for s in starts:
        if s not in ends:
            return False
    for e in ends:
        if e not in starts:
            return False
    return True

class Buddies:
    def __init__(self, whole_set):
        strs = [str(x) for x in whole_set]
        s_strs = set(strs)
        starts = [s[:2] for s in strs]
        ends = [s[2:] for s in strs]
        for i in xrange(len(strs)):
            if starts[i] not in ends or ends[i] not in starts:
                s_strs.remove(strs[i])
        ss = []
        starts = []
        ends = []
        for s in s_strs:
            ss.append(s)
            starts.append(s[:2])
            ends.append(s[2:])
        self.buds = dict()
        for i in xrange(len(ss)):
            s = set()
            for j in xrange(len(ends)):
                if starts[i] == ends[j]:
                    s.add(int(ss[j]))
            self.buds[int(ss[i])] = s

def cycles(buds):
    yielded_sets = set()
    for a in buds.buds:
        for b in buds.buds[a]:
            for c in buds.buds[b]:
                for d in buds.buds[c]:
                    for e in buds.buds[d]:
                        for f in buds.buds[e]:
                            l = [a, b, c, d, e, f]
                            if len(set(l)) == 6 and a in buds.buds[f] and frozenset(l) not in yielded_sets:
                                yield l
                                # to not yield duplicates
                                yielded_sets.add(frozenset(l))

def is_pair(i, j):
    return str(i)[:2] == str(j)[2:]

def is_spanning_set(match_lists):
    lsts = [list(x for x in s) for s in match_lists]
    for combo in product(*lsts):
        if len(set(combo)) == 6:
            return True
    return False

def run():
    se = set()
    set_list = []
    for fn in [trig, squa, peng, hexg, hepg, octg]:
        s = generate_poly(fn, 10000)
        set_list.append(s)
        s = set(x for x in s if x > 1000)
        se = se.union(s)
    b = Buddies(se)
    # find all cycles given the buddy list
    for cyc in cycles(b):
        match_lists = []
        for c in cyc:
            matches = set()
            for i in xrange(len(set_list)):
                if c in set_list[i]:
                    matches.add(i)
            match_lists.append(matches)
        if is_spanning_set(match_lists):
            return sum(cyc)

from runner import main
main(run)
