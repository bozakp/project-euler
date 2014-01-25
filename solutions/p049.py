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
    seen = [False for x in xrange(10001)]
    p = Primes(math.sqrt(10000))
    for i in xrange(1000,10000):
        dig_set = [int(x) for x in str(i)]
        primes = []
        for permute in permute_list(dig_set):
            if permute < 1000 or seen[permute]:
                continue
            if p.is_prime(permute):
                primes.append(permute)
            seen[permute] = True
        if len(primes) >= 3:
            primes.sort()
            for j in xrange(len(primes)):
                for k in xrange(j+1,len(primes)):
                    for l in xrange(k+1, len(primes)):
                        if (primes[l] - primes[k] == primes[k] - primes[j]
                                and primes[j] != 1487):
                            d = primes[j]*10000*10000 + primes[k]*10000 + primes[l]
                            print("Answer: %d" % d)
                            return

def main():
    start = time.time()
    run()
    elapse = time.time()-start
    print "Time(ms):", elapse*1000
    
if __name__ == "__main__":
    main()

