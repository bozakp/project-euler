from itertools import product

def run():
    with open("data/p059_cipher.txt", "r") as f:
        lst = f.read().split(",")
    lst = list(int(a) for a in lst)
    lst2 = range(len(lst))
    for a, b, c in product(xrange(97, 123), repeat=3):
        i = 0
        while i < len(lst):
            lst2[i] = chr(lst[i] ^ a)
            i=i+3
        i=1
        while i < len(lst):
            lst2[i] = chr(lst[i] ^ b)
            i=i+3
        i=2
        while i < len(lst):
            lst2[i] = chr(lst[i] ^ c)
            i=i+3
        if " the " in "".join(lst2):
            return sum(ord(a) for a in lst2)

from runner import main
main(run)
