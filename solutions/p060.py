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

def run():
    p = Primes(30000)
    for i in xrange(len(p.primes)):
        for j in xrange(i+1, len(p.primes)):
            for k in xrange(j+1, len(p.primes)):
                for l in xrange(k+1, len(p.primes)):
                    for m in xrange(l+1, len(p.primes)):
                        five_set = FiveSet(p, [p.primes[x] for x in [i, j, k, l, m]])
                        if five_set.is_valid():
                            print("Answer: %d" % five_set.sum())
                            return

def main():
    start = time.time()
    run()
    elapse = time.time()-start
    print "Time(ms):", elapse*1000
    
if __name__ == "__main__":
    main()

