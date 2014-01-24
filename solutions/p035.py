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
        
def permute_digits(n):
    s = str(n)
    for i in xrange(len(s)):
        yield int(s[i:]+s[:i])

def run():
    N = 1000000
    p = Primes(int(math.sqrt(N)))
    c = 1  # already counting '2'
    i = 3
    while i < N:
        if all(p.is_prime(x) for x in permute_digits(i)):
            c += 1
        i += 2
    print("Answer: %d" % c)    

def main():
    start = time.time()
    run()
    elapse = time.time()-start
    print "Time(ms):", elapse*1000
    raw_input("Press ENTER to exit.")
    
if __name__ == "__main__":
    main()