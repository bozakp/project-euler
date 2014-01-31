import math
import time

class Primes:
    def __init__(self, N):
        self.primes=[2,3]
        a=5
        while a < N:
            b=math.sqrt(a)
            for x in self.primes:
                if a%x==0:
                    break
                if x>b:
                    self.primes.append(a)
                    break
            else:
                self.primes.append(a)
            a=a+2
    
    def is_prime(self, n):
        i = 0
        sqrt = math.sqrt(n)
        while i < len(self.primes) and self.primes[i] <= sqrt:
            if n % self.primes[i] == 0:
                return False
            i += 1
        return True

    def is_prime_pair(self, n1, n2):
        return (self.is_prime(concat(n2, n2)) 
                and self.is_prime(n1)
                and self.is_prime(n2))

class FiveSet:
    def __init__(self, primes, nums):
        self.p = primes
        self.nums = set(nums)

    def is_valid(self):
        s = set(self.nums)
        for a in s:
            s2 = set(s)
            s2.remove(a)
            for b in s2:
                n1 = int(str(a)+str(b))
                n2 = int(str(b)+str(a))
                if not (self.p.is_prime(n1) and self.p.is_prime(n2)):
                    return False
        return True

    def sum(self):
        return sum(x for x in self.nums)

class Compatibles:
    def __init__(self):
        self.d = {}

    def add(self, a, b):
        if a > b:
            na = b
            nb = a
        elif b > a:
            na = a
            nb = b
        else:
            return
        if not na in self.d:
            self.d[na] = set()
        self.d[na].add(nb)

    def is_comp(self, a, b):
        if a > b:
            n1 = b
            n2 = a
        elif b > a:
            n1 = a
            n2 = b
        else:
            return
        return n2 in self.d[n1]

    def __getitem__(self, i):
        return self.d[i] if i in self.d else None

def pairs(n):
    s = str(n)
    for i in xrange(len(s)-1):
        yield (int(s[:i+1]), int(s[i+1:]))

def comps(poss, so_far, compatibles, i):
    if len(so_far) == 5:
        yield so_far
    else:
        li = list(compatibles[i])
        li.sort()
        for j in li:
            so_far.add(j)
            for cc in comps(poss & compatibles[j], so_far, compatibles, j):
                yield cc
            so_far.remove(j)

def find_five_set(comp):
    keys = [x for x in comp.d.keys()]
    keys.sort()
    for i in keys:
        for cc in comps(comp[i], set(i), comp, i):
            return cc
        
def concat(n1, n2):
    s1 = str(n1)
    s2 = str(n2)
    return int(s1+s2)

def run():
    primes = Primes(1000000)
    comp = Compatibles()
    for p in primes.primes:
        for ns in pairs(p):
            n1 = ns[0]
            n2 = ns[1]
            if primes.is_prime_pair(n1, n2):
                comp.add(n1, n2)
    print(comp.d.keys())
    print("Answer: %d" % sum(find_five_set(comp)))

def main():
    start = time.time()
    run()
    elapse = time.time()-start
    print "Time(ms):", elapse*1000
    
if __name__ == "__main__":
    main()

