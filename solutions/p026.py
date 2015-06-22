def non_repeating_len(n):
    a=20
    b=1
    while ((10**(a+b)/n)%(10**b))!=((10**(a+2*b)/n)%(10**b)):
        b=b+1
    return b

def run():
    max=0
    for a in range(5,1000):
        b=non_repeating_len(a)
        if b>max:
            max=b
            c=a
    return c

from runner import main
main(run)
