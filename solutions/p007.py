from common import Primes

def run():
    global n_primes, last_prime
    n_primes = 0
    last_prime = None
    def callback(p):
        global n_primes, last_prime
        n_primes += 1
        last_prime = p
        if n_primes == 10001:
            return True
    primes = Primes(callback)
    p = primes.generate()
    return last_prime

from runner import main
main(run)
