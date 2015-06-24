def run():
    pds = set([])
    for a in xrange(2, 100):
        b = a + 1
        sa = str(a)
        while True:
            c = a * b
            sb = str(b)
            sc = str(c)
            s = sa + sb + sc
            if len(s) >= 10:
                break
            if set(s) == set("123456789"):
                pds.add(c)
            b += 1
    return sum(x for x in pds)


from runner import main
main(run)
