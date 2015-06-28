import math

def run():
    # TODO: Make common.prime() accept an argument for non-prime odd numbers?
    # Seems like very specific behavior, so maybe not
    primes=[2,3]
    a=5
    while True:
        b=math.sqrt(a)
        for x in primes:
            if a%x==0:
                for c in primes:
                    if math.sqrt((a-c)/2)%1==0:
                        break
                else:
                    return a
                break
            if x>b:
                primes.append(a)
                break
        else:
            primes.append(a)
        a=a+2

from runner import main
main(run)
