from common import Primes

def run():
    primes = Primes()
    primes.generate(10000)
    n_found = 0
    s = 0
    a = 11
    while n_found < 11:
        starts_prime = int(str(a)[0]) in [2, 3, 5, 7]
        ends_prime = int(str(a)[-1]) in [3, 5, 7]
        middle_even = any(True for y in str(a)[1:-1] if int(y) in [0, 2, 4, 6, 8])
        if starts_prime and ends_prime and not middle_even:
            for b in range(len(str(a))):
                if b==0:
                    if not primes.is_prime(a):
                        break
                else:
                    if (not primes.is_prime(int(str(a)[b:]))) or (not primes.is_prime(int(str(a)[:-b]))):
                        break
            else:
                s += a
                n_found += 1
        a=a+2
    return s

from runner import main
main(run)
