from common import Primes

def run():
    p = Primes()
    primes = p.generate(70000)
    MIN_PRIME_SUM_LEN = 21
    start = 0
    mx_psum = 0
    while start < len(primes) - 200:
        psum = 0
        offset = 0
        while offset < MIN_PRIME_SUM_LEN:
            psum += primes[start + offset]
            offset += 1
            if psum >= 1000000:
                start = len(primes)
                break
        while psum < 1000000:
            psum += primes[start + offset]
            offset += 1
            if p.is_prime(psum):
                MIN_PRIME_SUM_LEN = offset
                mx_psum = psum
        start += 1
    return mx_psum

from runner import main
main(run)
