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

def permute_list(s):
    if len(s) == 0:
        yield 0
        return
    for i in s:
        s2 = list(s)
        s2.remove(i)
        p = i * (10 ** (len(s) - 1))
        for other in permute_list(s2):
            yield p + other

def run():
    p = Primes(math.sqrt(10000))
    for i in xrange(1000,10000):
        dig_set = [int(x) for x in str(i)]
        primes = []
        for permute in permute_list(dig_set):
            if permute < 1000:
                continue
            if p.is_prime(permute):
                primes.append(permute)
        if len(primes) == 3:
            primes.sort()
            if primes[2] - primes[1] == primes[1] - primes[0]:
                d = primes[0]*10000*10000 + primes[1]*10000 + primes[2]
                print("Answer: %d" % d)
                break

def main():
    start = time.time()
    run()
    elapse = time.time()-start
    print "Time(ms):", elapse*1000
    
if __name__ == "__main__":
    main()

