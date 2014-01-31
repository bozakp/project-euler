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
        if n == 1:
            return False
        i = 0
        sqrt = math.sqrt(n)
        while i < len(self.primes) and self.primes[i] <= sqrt:
            if n % self.primes[i] == 0:
                return False
            i += 1
        return True

    def is_prime_pair(self, a, b):
        sa = str(a)
        sb = str(b)
        if (a+b) % 3 == 0:
            return False
        return (self.is_prime(int(sa+sb)) 
                and self.is_prime(int(sb+sa)))

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
        if not a in self.d:
            self.d[a] = set()
        self.d[a].add(b)

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
        sa = s[:i+1]
        sb = s[i+1:]
        if sb[0] != "0":
            yield (int(sa), int(sb))

def comps(poss, so_far, compatibles):
    if len(so_far) == 5:
        yield so_far
    else:
        li = list(poss)
        li.sort()
        for j in li:
            if compatibles[j] is not None:
                so_far.add(j)
                for cc in comps(poss & compatibles[j], so_far, compatibles):
                    yield cc
                so_far.remove(j)

def find_five_set(comp):
    keys = [x for x in comp.d.keys()]
    keys.sort()
    for i in keys:
        for cc in comps(comp[i], set([i]), comp):
            yield cc
        
def run():
    primes = Primes(8340)
    comp = Compatibles()
    print(len(primes.primes))
    for i in xrange(len(primes.primes)):
        print(i)
        a = primes.primes[i]
        for j in xrange(i+1, len(primes.primes)):
            b = primes.primes[j]
            if primes.is_prime_pair(a, b):
                comp.add(a, b)
    print("Answer: %d" % min(sum(answer_set) for answer_set in find_five_set(comp)))

def main():
    start = time.time()
    run()
    elapse = time.time()-start
    print "Time(ms):", elapse*1000

if __name__ == "__main__":
    main()

