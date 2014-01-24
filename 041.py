import time
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

def permute_set(s):
    if len(s) == 0:
        yield 0
        return
    for i in s:
        s2 = set(s)
        s2.remove(i)
        p = i * (10 ** (len(s) - 1))
        for other in permute_set(s2):
            yield p + other
        
def pandigitals(n):
    s = set(i for i in xrange(1,n+1))
    for i in permute_set(s):
        yield i

def run():
    p = Primes(math.sqrt(987654321))
    max_p = 0
    for n in xrange(4,10):
        for i in pandigitals(n):
            if p.is_prime(i) and i > max_p:
                max_p = i
    print("Answer: %d" % max_p)
        
def main():
    start = time.time()
    run()
    elapse = time.time()-start
    print "Time(ms):", elapse*1000
    raw_input("Press ENTER to exit.")
    
if __name__ == "__main__":
    main()