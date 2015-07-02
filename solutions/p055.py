def run():
    n = 0
    for x in xrange(10000):
        c = x
        for _ in xrange(50):
            c += int(str(c)[::-1])
            if str(c) == str(c)[::-1]:
                break
        else:
            n += 1
    return n

from runner import main
main(run)
