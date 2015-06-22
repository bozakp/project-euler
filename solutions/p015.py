import math

def run():
    b=20
    n=math.factorial(b*2)
    n=n/math.factorial(b)
    n=n/math.factorial(b)
    return n

from runner import main
main(run)
