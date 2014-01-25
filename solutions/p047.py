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

    def n_prime_factors(self, n):
        rem = n
        c = 0
        for prime in self.primes:
            if rem % prime == 0:
                c += 1
            while rem % prime == 0:
                rem = rem / prime
            if prime*prime > rem:
                c += 1
                break
            if rem == 1:
                break
        return c

def run():
    p = Primes(200000)
    streak = 0
    i = 2*3*5*7  # first number with 4 distinct prime factors
    while streak != 4:
        if p.n_prime_factors(i) == 4:
            streak += 1
        else:
            streak = 0
        i += 1
    print("Answer: %d" % (i-4))

def main():
    start = time.time()
    run()
    elapse = time.time()-start
    print "Time(ms):", elapse*1000
    
if __name__ == "__main__":
    main()

