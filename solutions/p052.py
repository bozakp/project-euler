def same_digits(n):
    s = str(n)
    if s[0] > "1" or s[1] > "5":
        return False
    l = list(a for a in s)
    l.sort()
    for i in xrange(2, 7):
        ll = list(a for a in str(n * i))
        ll.sort()
        if l != ll:
            return False
    return True

def run():
    n = 2
    while True:
        if same_digits(n):
            return n
        n += 1
        if n > 150000:
            print("wtf")
            return

from runner import main
main(run)
