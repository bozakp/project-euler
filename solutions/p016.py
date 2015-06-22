def run():
    n = 2**1000
    return sum(int(x) for x in str(n))

from runner import main
main(run)
