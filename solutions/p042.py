def run():
    with open("data/p042_words.txt", "r") as f:
        e = f.read().split(",")
    for a in xrange(len(e)):
        e[a] = e[a][1:-1]  # strip quotes
    t = [(a+1) * a/2 for a in xrange(500)]
    n = 0
    for word in e:
        w = 0
        for c in word:
            w += ord(c) - 64
        if t.count(w) > 0:
            n += 1
    return n

from runner import main
main(run)
