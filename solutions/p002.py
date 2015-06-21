def run():
    a=0
    b=1
    c=0
    sum=0
    while c < (4 * 10**6):
        c = a + b
        if c % 2 == 0:
            sum += c
        a = b
        b = c
    return sum

from runner import main
main(run)
