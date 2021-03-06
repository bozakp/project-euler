import time

def nxt(n):
    return n/2 if n % 2 == 0 else 3*n+1

class Collatz:
    def __init__(self, N):
        self.ns = [0]*(N+1)
        self.ns[1] = 1

    def dist(self, n):
        if n == 1:
            return 1
        if n >= len(self.ns):
            return self.dist(nxt(n)) + 1
        if self.ns[n] != 0:
            return self.ns[n]
        d = self.dist(nxt(n)) + 1
        self.ns[n] = d
        return d

    def max_dist(self, n):
        max_i = 0
        max_d = 0
        for i in xrange(1, n):
            if self.dist(i) > max_d:
                max_i = i
                max_d = self.dist(i)
        return max_i, max_d

def run():
    N = 1000000
    c = Collatz(N)
    return c.max_dist(N)[0]

from runner import main
main(run)
