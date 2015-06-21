from common import prime

def run():
    global prime_sum
    prime_sum = 0
    def callback(p):
        global prime_sum
        prime_sum += p
    max_prime = 2 * 10**6
    prime(max_n=max_prime, callback=callback)
    return prime_sum

from runner import main
main(run)
