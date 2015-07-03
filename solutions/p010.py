from common import Primes

def run():
    global prime_sum
    prime_sum = 0
    def callback(p):
        global prime_sum
        prime_sum += p
    max_prime = 2 * 10**6
    Primes(callback).generate(max_prime)
    return prime_sum

from runner import main
main(run)
