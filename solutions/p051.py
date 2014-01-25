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

def wildcard_set():
    digs = [str(x) for x in xrange(10)]
    digs.append("*")
    odds = [str(2*x+1) for x in xrange(5)]
    for a in digs:
        for b in digs:
            for c in digs:
                for d in digs:
                    for e in digs:
                        for f in odds:
                            yield [a, b, c, d, e, f]

def fill_wildcards(w_list):
    if "*" not in w_list:
        return
    for i in xrange(10):
        yield int("".join(str(i) if x=="*" else x for x in w_list))

def smallest_prime(primes, wild_list):
    for i in fill_wildcards(wild_list):
        if primes.is_prime(i):
            return i

def run():
    p = Primes(math.sqrt(1000000))
    for wild in wildcard_set():
        primes = 0
        not_primes = 0
        for n in fill_wildcards(wild):
            if p.is_prime(n):
                primes += 1
            else:
                not_primes += 1
            if not_primes >= 3:
                break
        if primes >= 8:
            print("Answer: %d" % smallest_prime(p, wild))
            break

def main():
    start = time.time()
    run()
    elapse = time.time()-start
    print "Time(ms):", elapse*1000
    
if __name__ == "__main__":
    main()

