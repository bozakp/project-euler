def run():
    a=1
    c=2
    d=1
    while len(str(d)) < 1000:
        d, a = a+d, d
        c=c+1
    return c

from runner import main
main(run)
