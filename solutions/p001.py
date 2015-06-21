def add_multiples(d, max_n):
    a = 0
    s = 0
    while a < max_n:
        s += a
        a += d
    return s

def run():
    sum3 = add_multiples(3, 1000)
    sum5 = add_multiples(5, 1000)
    sum15 = add_multiples(15, 1000)
    return sum3 + sum5 - sum15

from runner import main
main(run)
