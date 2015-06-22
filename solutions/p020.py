import math

def run():
    ss = str(math.factorial(100))
    return sum(int(c) for c in ss)

from runner import main
main(run)
